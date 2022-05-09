from django.urls import path

from web import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('logout', views.logoutUser, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('orders', views.orders, name='orders'),
    path('rooms', views.rooms, name='rooms'),
    path('trading', views.trading, name='trading'),
    path('worker', views.worker, name='worker'),
    path('expenses', views.expenses, name='expenses'),
    path('archive', views.archive, name='archive'),
    path('product', views.product, name='product'),
    path('worker/add', views.user_new, name='user_new'),
    path('worker/<int:pk>/', views.user_edit, name='user_edit'),
    path('worker/<int:pk>/delete', views.user_delete, name='user_delete'),
    path('category/<int:pk>/', views.category_edit, name='category'),
    path('category/new/', views.category_new, name="category_new"),
    path('category/<int:pk>/delete', views.category_delete, name="category_delete"),
    path('product/food/<int:pk>/', views.food_edit, name='food_edit'),
    path('product/food/new/', views.food_new, name="food_new"),
    path('product/<int:pk>/delete', views.food_delete, name="food_delete"),
    path('rooms/new', views.room_new, name='room_new'),
    path('rooms/<int:pk>/tables', views.room_tables, name='room_tables'),
    path('rooms/<int:pk>/', views.room_edit, name='room_edit'),
    path('rooms/<int:pk>/delete', views.room_delete, name='room_delete'),
    path('rooms/<int:pk>/table_new', views.table_new, name='table_add'),
    path('rooms/<int:pk_room>/tables/<int:pk_table>/delete', views.table_delete, name='table_delete'),
    path('orders/<int:pk>/view', views.order_view, name='order_view'),
    path('orders/<int:pk>/complete', views.complete_order, name='order_complete'),
    path('printing/<int:order_id>/order', views.print_order, name='print_order'),
    path('expenses/new_expense_reason/', views.expense_reason_new, name='expense_reason_new'),
    path('expenses/reasons/<int:pk>/', views.expense_reason_edit, name='expense_reason_edit'),
    path('expenses/new_expense/', views.expense_new, name='expense_new'),
    path('expenses/<int:pk>/delete', views.expense_delete, name='expense_delete'),
    path('expenses/reason/<int:pk>/delete', views.expense_reason_delete
         , name='expense_reason_delete'),
    path('trading/<int:pk>/view', views.trading_detailed_view, name='trading_detailed_view'),
    path('archive/<int:pk>/view', views.archive_order_view, name='archive_order_view'),

    path('room', views.room, name='room'),
    path('room/<int:pk>/tables', views.table, name='table'),
    path('room/<int:pk_room>/<int:pk_table>/add_item', views.add_item, name='add_item'),
    path('order_item/<int:pk>/delete', views.order_item_delete, name='delete_order_item'),
    path('order/<int:pk>/view', views.waiter_order, name='waiter_order'),
    path('my_orders', views.my_orders, name='my_orders'),
    path('my_profile', views.my_profile, name='my_profile'),
    path('print_receipt/<int:order_id>/', views.print_order_receipt, name='print_order_receipt'),
    path('pickup', views.pickup, name='pickup'),

]
