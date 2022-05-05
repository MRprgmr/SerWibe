import json
from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404, reverse

from utils.data_processing import get_trading_table, food_trading_data, get_dashboard_info, get_sales_graph_data
from utils.date_config import get_start_of_week
from utils.payment_receipt import print_receipt
from utils.request_processing import order_items_add
from .forms import CreateUserForm, CategoryForm, FoodForm, RoomForm, TableForm, ExpenseReasonForm, ExpenseForm, \
    OrderCompletionForm
from .models import Worker, Category, Food, Room, Table, Order, Expense, ExpenseReason


def logoutUser(request):
    logout(request)
    return redirect('signin')


def signin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        waiters = Worker.objects.filter(position="waiter")
        admins = Worker.objects.filter(position="admin")
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('dashboard')
                elif user.worker.position == "waiter":
                    login(request, user)
                    return redirect('room')
            else:
                messages.error(request, "Xato! Parol noto`g`ri")
                return redirect('signin')
        context = {"waiters": waiters, "admins": admins}
        return render(request, 'login.html', context)


@login_required(login_url='/')
def dashboard(request):
    start_date = request.GET.get('fir')
    end_date = request.GET.get('sec')
    dashboard_info = get_dashboard_info()
    xvalues, yvalues, date_string = get_sales_graph_data(start_date, end_date)
    mx = int(max(yvalues) * 1.1)
    mn = min(yvalues) // 2
    print(date_string)
    return render(request, 'dashboard.html',
                  {'dashboard_info': dashboard_info, 'labels': json.dumps(xvalues), 'data': json.dumps(yvalues),
                   'mx': mx, 'mn': mn, 'date_string': json.dumps(date_string)})


@login_required(login_url='/')
def room(request):
    room_models = Room.objects.all()
    return render(request, 'waiter/room.html', {'rooms': room_models})


@login_required(login_url='/')
def table(request, pk):
    room_model = get_object_or_404(Room, pk=pk)
    tables = room_model.table_set.all()
    return render(request, 'waiter/tables.html', {'tables': tables, 'room': room_model})


@login_required(login_url='/')
def add_item(request, pk_room, pk_table):
    room_model = Room.objects.get(pk=pk_room)
    table_model = Table.objects.get(pk=pk_table)
    waiter = Worker.objects.get(user=request.user)
    if request.method == 'POST':
        order_items_add(request.POST, table_model, waiter)
    else:
        food_models = Food.objects.filter(is_available=True, category__is_available=True)
        category_models = Category.objects.filter(is_available=True)
        return render(request, 'waiter/add_item.html',
                      {"foods": food_models, 'categories': category_models, 'table': table_model, 'room': room_model})
    return redirect('table', pk=pk_room)


@login_required(login_url='/')
def waiter_order(request, pk):
    table_model = get_object_or_404(Table, pk=pk)
    order_model = table_model.current_order
    print(order_model)
    return render(request, 'waiter/order_view.html',
                  {'room': table_model.room, 'table': table_model, 'orderitems': order_model.orderitem_set.all(),
                   'order': order_model})


@login_required(login_url='/')
def trading(request):
    category_models = Category.objects.all()
    category_parameter = request.GET.get('category')
    start_date = request.GET.get('fir')
    end_date = request.GET.get('sec')
    food_data, total_sum, date_string = get_trading_table(category_parameter, start_date, end_date)
    p = Paginator(food_data, 10)
    page = p.get_page(request.GET.get('page'))
    return render(request, 'trading/income.html',
                  {'foods': page, 'categories': category_models, 'total': total_sum, 'date_string': date_string,
                   'p_paginator': page})


@login_required(login_url='/')
def trading_detailed_view(request, pk):
    start_date = request.GET.get('fir')
    end_date = request.GET.get('sec')
    dates, xvalues, yvalues, food_model, date_string = food_trading_data(pk, start_date, end_date)
    mn = min(yvalues) // 2
    mx = int(max(yvalues) * 1.1)
    return render(request, 'trading/detailed_view.html',
                  {'dates': dates, 'labels': json.dumps(xvalues), 'data': json.dumps(yvalues), 'mn': mn, 'mx': mx,
                   'food': food_model,
                   'total': sum(yvalues), 'date_string': json.dumps(date_string)})


@login_required(login_url='/')
def worker(request):
    if request.user.is_superuser:
        workers = Worker.objects.all()
        context = {'workers': workers}
        return render(request, 'workers/worker.html', context)
    else:
        return redirect('room')


@login_required(login_url='/')
def user_new(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('worker')
        else:
            print(form.errors)
    else:
        form = CreateUserForm()
    return render(request, 'workers/user_edit.html', {'form': form})


@login_required(login_url='/')
def user_edit(request, pk):
    post = get_object_or_404(Worker, pk=pk)
    if request.method == "POST":
        form = CreateUserForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('worker')
    else:
        form = CreateUserForm(instance=post)
    return render(request, 'workers/user_edit.html', {'form': form})


@login_required(login_url='/')
def user_delete(request, pk):
    obj = get_object_or_404(Worker, pk=pk)

    if request.method == "POST":
        obj.user.delete()
        obj.delete()
        return redirect('worker')

    return render(request, "workers/user_delete.html", {'user': obj})


@login_required(login_url='/')
def product(request):
    category_id = request.GET.get('category')
    if request.user.is_superuser:
        categories = Category.objects.all()
        if category_id is not None:
            foods = Food.objects.filter(category_id=int(category_id))
        else:
            foods = Food.objects.all()
        p = Paginator(foods, 10)
        page = p.get_page(request.GET.get('page'))
        context = {'categories': categories, 'foods': page, 'p_paginator': page}
        return render(request, 'foods/product.html', context)
    else:
        return redirect('room')


@login_required(login_url='/')
def category_edit(request, pk):
    post = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=post)
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            return redirect(reverse('product') + '#C')
    else:
        form = CategoryForm(instance=post)
    return render(request, 'foods/category_edit.html', {'form': form})


@login_required(login_url='/')
def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            return redirect(reverse('product') + '#C')
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    return render(request, 'foods/category_edit.html', {'form': form})


@login_required(login_url='/')
def category_delete(request, pk):
    obj = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        obj.delete()
        return redirect(reverse('product') + '#C')

    return render(request, "foods/category_delete.html", {'category': obj})


@login_required(login_url='/')
def food_edit(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            return redirect('product')
    else:
        form = FoodForm(instance=food)
    return render(request, 'foods/food_edit.html', {'form': form})


@login_required(login_url='/')
def food_new(request):
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            return redirect('product')
        else:
            print(form.errors)
    else:
        form = FoodForm()
    return render(request, 'foods/food_edit.html', {'form': form})


@login_required(login_url='/')
def food_delete(request, pk):
    obj = get_object_or_404(Food, pk=pk)

    if request.method == "POST":
        obj.delete()
        return redirect('product')

    return render(request, "foods/food_delete.html", {'food': obj})


@login_required(login_url='/')
def rooms(request):
    if request.user.is_superuser:
        room_models = Room.objects.all()
        p = Paginator(room_models, 10)
        page = p.get_page(request.GET.get('page'))
        context = {'rooms': page, 'p_paginator': page}
        return render(request, 'tables/rooms.html', context)
    else:
        return redirect('room')


@login_required(login_url='/')
def room_new(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            return redirect('rooms')
        else:
            print(form.errors)
    else:
        form = RoomForm()
    return render(request, 'tables/room_edit.html', {'form': form})


@login_required(login_url='/')
def room_tables(request, pk):
    rm = get_object_or_404(Room, pk=pk)
    tables = rm.table_set.all()
    return render(request, 'tables/room_tables.html', {'tables': tables, 'room': rm})


@login_required(login_url='/')
def room_edit(request, pk):
    room_model = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room_model)
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            return redirect('rooms')
    else:
        form = RoomForm(instance=room_model)
    return render(request, 'tables/room_edit.html', {'form': form})


@login_required(login_url='/')
def room_delete(request, pk):
    obj = get_object_or_404(Room, pk=pk)

    if request.method == "POST":
        obj.delete()
        return redirect('rooms')

    return render(request, "tables/room_delete.html", {'food': obj})


@login_required(login_url='/')
def table_new(request, pk):
    room_m = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = TableForm(request.POST, room=room_m)
        if form.is_valid():
            form.save()
            return redirect('room_tables', pk=pk)
        else:
            print(form.errors)
    else:
        form = TableForm()
    return render(request, 'tables/table_add.html', {'form': form, 'room': room_m})


@login_required(login_url='/')
def table_delete(request, pk_room, pk_table):
    room_obj = get_object_or_404(Room, pk=pk_room)
    table_obj = get_object_or_404(Table, pk=pk_table)

    if request.method == "POST":
        table_obj.delete()
        return redirect('room_tables', pk=pk_room)

    return render(request, "tables/table_delete.html", {'room': room_obj, 'table': table_obj})


@login_required(login_url='/')
def orders(request):
    order_models = Order.objects.filter(is_completed=False)
    return render(request, 'orders/orders.html', context={'orders': order_models})


@login_required(login_url='/')
def order_view(request, pk):
    order_model = get_object_or_404(Order, pk=pk)
    order_items = order_model.orderitem_set.all()
    return render(request, 'orders/order_view.html', context={'order': order_model, 'orderitems': order_items})


@login_required(login_url='/')
def print_order(request, order_id):
    order_model = get_object_or_404(Order, id=order_id)
    print_receipt(order=order_model)
    return redirect('orders')


@login_required(login_url='/')
def expenses(request):
    date = request.GET.get('date')
    today = datetime.today()
    if date == 'today':
        expense_models = Expense.objects.filter(created_at__day=today.day)
    elif date == "week":
        expense_models = Expense.objects.filter(created_at__gt=get_start_of_week())
    elif date == "month":
        expense_models = Expense.objects.filter(created_at__month=today.month)
    else:
        expense_models = Expense.objects.all()
    p = Paginator(expense_models, 10)
    page = p.get_page(request.GET.get('page'))
    expense_reason_models = ExpenseReason.objects.all()
    return render(request, 'expenses/expenses.html',
                  context={'expenses': page, 'expense_reasons': expense_reason_models, 'p_paginator': page})


@login_required(login_url='/')
def expense_reason_new(request):
    if request.method == "POST":
        form = ExpenseReasonForm(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            return redirect(reverse('expenses') + '#C')
        else:
            print(form.errors)
    else:
        form = ExpenseReasonForm()
    return render(request, 'expenses/expense_reason_edit.html', {'form': form})


@login_required(login_url='/')
def expense_reason_edit(request, pk):
    expense_reason = get_object_or_404(ExpenseReason, pk=pk)
    if request.method == "POST":
        form = ExpenseReasonForm(request.POST, instance=expense_reason)
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            return redirect(reverse('expenses') + '#C')
    else:
        form = ExpenseReasonForm(instance=expense_reason)
    return render(request, 'expenses/expense_reason_edit.html', {'form': form})


@login_required(login_url='/')
def expense_new(request):
    worker_model = Worker.objects.get(user=request.user)
    if request.method == "POST":
        tempt_dict = request.POST.copy()
        tempt_dict['performer'] = str(worker_model.id)
        form = ExpenseForm(tempt_dict)
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            return redirect(reverse('expenses'))
        else:
            print(form.errors)
    else:
        default_choice = request.GET.get('reason')
        if default_choice is not None:
            form = ExpenseForm(initial={'reason': ExpenseReason.objects.get(id=int(default_choice))})
        else:
            form = ExpenseForm()
    return render(request, 'expenses/expense_new.html', {'form': form})


@login_required(login_url='/')
def expense_delete(request, pk):
    expense_model = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        expense_model.delete()
        return redirect('expenses')

    return render(request, "expenses/expense_delete.html")


@login_required(login_url='/')
def expense_reason_delete(request, pk):
    expense_reason_model = get_object_or_404(ExpenseReason, pk=pk)
    if request.method == "POST":
        expense_reason_model.delete()
        return redirect('expenses')

    return render(request, "expenses/expense_reason_delete.html", {'reason': expense_reason_model})


@login_required(login_url='/')
def complete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order_items = order.orderitem_set.all()
    if request.method == "POST":
        form = OrderCompletionForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = OrderCompletionForm()
    return render(request, "orders/complete_order.html",
                  context={'form': form, 'order': order, 'orderitems': order_items})


@login_required(login_url='/')
def archive(request):
    now = datetime.now()
    waiter_models = Worker.objects.filter(position='waiter')
    order_models = Order.objects.filter(is_completed=True)
    fir = request.GET.get('fir')
    sec = request.GET.get('sec')
    waiter = request.GET.get('waiter')
    date_string = ""
    if fir in ['day', 'week', 'month']:
        if fir == 'day':
            order_models = order_models.filter(created_at__day=now.day)
            date_string = now.strftime("%a, %d/%m/%Y")
        elif fir == 'week':
            order_models = order_models.filter(created_at__gt=get_start_of_week())
            date_string = f"{get_start_of_week().strftime('%d/%m/%Y')} - {now.strftime('%d/%m/%Y')}"
        elif fir == 'month':
            order_models = order_models.filter(created_at__month=now.month)
            date_string = f"{get_start_of_week().strftime('01/%m/%Y')} - {now.strftime('%d/%m/%Y')}"
    else:
        if fir != '' and fir is not None and sec != '' and sec is not None:
            sd = datetime.strptime(fir, "%Y-%m-%d")
            ed = datetime.strptime(sec, "%Y-%m-%d")
            order_models = order_models.filter(order__created_at__gt=sd, order__created_at__lt=ed)
            date_string = f"{sd.strftime('01/%m/%Y')} - {ed.strftime('%d/%m/%Y')}"
    if waiter not in [None, '']:
        order_models = order_models.filter(waiter_id=int(waiter))
    total_sum = order_models.aggregate(Sum('paid_money'))['paid_money__sum']
    if total_sum is None:
        total_sum = 0
    p = Paginator(order_models, 10)
    page = p.get_page(request.GET.get('page'))
    return render(request, "archive/archive.html",
                  context={'waiters': waiter_models, 'orders': page, 'date_string': date_string, 'total_sum': total_sum,
                           'p_paginator': page})


@login_required(login_url='/')
def archive_order_view(request, pk):
    order_model = get_object_or_404(Order, pk=pk)
    order_items = order_model.orderitem_set.all()
    return render(request, 'archive/order_view.html', context={'order': order_model, 'orderitems': order_items})
