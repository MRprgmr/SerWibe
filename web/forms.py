from django.contrib.auth.models import User
from django.forms import Form, CharField, ChoiceField, PasswordInput, ModelForm, IntegerField, Textarea, BooleanField

from utils.printer import get_printers
from utils.system_settings import get_tax
from .models import Worker, Category, Food, Room, Table, ExpenseReason, Expense, Order, Product


class CreateUserForm(Form):
    first_name = CharField()
    last_name = CharField()
    position = ChoiceField(choices=[("waiter", "Offitsant"), ("admin", "Admin")])
    password = CharField(widget=PasswordInput, required=False)

    def __init__(self, *args, instance=None, **kwargs):
        instance: Worker
        super().__init__(*args, **kwargs)
        if instance is not None:
            self.instance: Worker = instance
            self.initial = {
                'first_name': instance.first_name,
                'last_name': instance.last_name,
                'position': instance.position,
            }
        else:
            self.instance = None

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        position = self.cleaned_data.get("position")
        password = self.cleaned_data.get("password")
        if self.instance is None:
            user = User.objects.create(username=f"{first_name.lower()}_{last_name.lower()}", password=password)
            user.set_password(password)
            user.save()
            worker = Worker.objects.create(user=user, first_name=first_name, last_name=last_name, position=position)
            worker.save()
        else:
            self.instance: Worker
            self.instance.user.username = f"{first_name.lower()}_{last_name.lower()}"
            if password != "":
                self.instance.user.set_password(password)
            self.instance.first_name = first_name
            self.instance.last_name = last_name
            self.instance.position = position
            self.instance.save()
            self.instance.user.save()


class CategoryForm(ModelForm):
    printer = ChoiceField(choices=[(printer, printer) for printer in get_printers()])

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

    class Meta:
        model = Category
        fields = '__all__'


class FoodForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

    class Meta:
        model = Food
        fields = '__all__'


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class TableForm(Form):
    number = IntegerField()
    tax_required = BooleanField(required=False)
    time_required = BooleanField(required=False)
    time_service_cost = IntegerField(required=False, initial=0)
    initial_payment = IntegerField(initial=0)

    def __init__(self, *args, room=None, instance=None, **kwargs):
        instance: Table
        super().__init__(*args, **kwargs)
        self.room = room
        if instance is not None:
            self.instance: Table = instance
            self.initial = {
                'number': instance.number,
                'tax_required': instance.tax_required,
                'time_required': instance.time_required,
                'time_service_cost': instance.time_service_cost,
                'initial_payment': instance.initial_payment,
            }
        else:
            self.instance = None

    def save(self):
        number = self.cleaned_data.get("number")
        tax_required = self.cleaned_data.get("tax_required")
        time_required = self.cleaned_data.get("time_required")
        time_service_cost = self.cleaned_data.get("time_service_cost")
        initial_payment = self.cleaned_data.get("initial_payment")

        if self.instance is None:
            self.instance = Table.objects.create(number=number, room=self.room)
        self.instance.number = number
        self.instance.room = self.room
        self.instance.initial_payment = initial_payment
        self.instance.tax_required = tax_required
        self.instance.time_required = time_required
        if not time_required:
            self.instance.time_service_cost = 0
        self.instance.time_service_cost = time_service_cost
        self.instance.save()


class ExpenseReasonForm(ModelForm):
    class Meta:
        model = ExpenseReason
        fields = '__all__'


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class OrderCompletionForm(Form):
    cash_money = IntegerField(required=False)
    credit_card = IntegerField(required=False)
    debt_money = IntegerField(required=False)
    comment = CharField(widget=Textarea, required=False)

    def __init__(self, *args, instance=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = instance

    def save(self):
        cash_money = self.cleaned_data.get('cash_money')
        credit_card = self.cleaned_data.get('credit_card')
        debt_money = self.cleaned_data.get('debt_money')
        if cash_money is None:
            cash_money = 0
        if credit_card is None:
            credit_card = 0
        if debt_money is None:
            debt_money = 0
        comment = self.cleaned_data.get('comment')
        self.instance: Order
        if comment is not None:
            self.instance.comment = comment
        self.instance.cash_money = cash_money
        self.instance.credit_card = credit_card
        self.instance.debt_money = debt_money
        self.instance.is_completed = True
        if self.instance.order_type == 'table' and self.instance.table.tax_required:
            self.instance.waiter_fee = int((get_tax() / 100) * self.instance.without_tax)
        self.instance.place_fee = self.instance.room_service_cost
        self.instance.paid_money = cash_money + credit_card
        self.instance.save()
        self.instance.update_stock()
        if self.instance.order_type == 'table':
            self.instance.table.is_available = True
            self.instance.table.save()


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class NewProductForm(Form):
    quantity = IntegerField()

    def __init__(self, *args, instance=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance: Product = instance

    def save(self):
        quantity = self.cleaned_data.get('quantity')
        self.instance.quantity += quantity
        self.instance.save()
