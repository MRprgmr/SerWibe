from datetime import datetime

from utils.img import Receipt
from utils.printer import Document
from utils.system_settings import Settings
from web.models import Order, OrderItem


def print_receipt(order: Order):
    border_string = "-" * 200
    doc = Document(width=int(Settings().get("printer_width", int) * 51), printer=Settings().get("printer", str))
    doc.begin_document()
    page = Receipt(width=Settings().get("printer_width", int) * 80 - 400)
    page.set_font(family="courbd", size=38)
    company_name = Settings().get(key="company_name", tp=str)
    if company_name == "":
        company_name = "SerWibe"
    page.text(text=company_name, space=True)
    page.br(8)
    page.set_font(family="courbd", size=12)
    if Settings().get("address", tp=str):
        page.text("Манзил: " + Settings().get(key="address", tp=str), space=True)
        page.br(5)
    phone_number = Settings().get("phone_number", tp=str)
    if len(phone_number) != 17:
        page.text("Тел: " + Settings().get(key="phone_number", tp=str), space=True)
        page.br(5)
    page.set_font(family="courbd", size=18)
    page.text(border_string, space=True)
    page.br(4)
    page.text("Сана:", align="left")
    page.set_font(family="courbd", size=16)
    page.text(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), align="right", space=True)
    page.set_font(family="courbd", size=18)
    page.br(5)
    page.text("Буюртма рақами:", align="left")
    page.text('#' + str(order.id), align="right", space=True)
    page.br(5)
    if order.order_type == 'table':
        page.text("Хона:", align="left")
        page.text(str(order.table.room.title), align="right", space=True)
        page.br(5)
        page.text("Стол рақами:", align="left")
        page.text(str(order.table.number), align="right", space=True)
        page.br(5)
    page.text("Оффитсант:", align="left")
    page.text(str(order.waiter.full_name), align="right", space=True)
    page.br(8)
    page.text(border_string, space=True)
    page.br(4)
    page.set_font(family="courbd", size=22)
    page.text("Буюртмалар", space=True)
    page.set_font(family="courbd", size=18)
    page.br(4)
    page.text(border_string, space=True)
    page.br(8)
    page.set_font(family="courbd", size=15)
    for order_item in order.orderitem_set.all():
        page.text(f"{order_item.quantity} x {order_item.meal.title}", align="left")
        page.text(f"{order_item.abstract_amount} сўм", align="right", space=True)
        page.br(10)
    page.set_font(family="courbd", size=18)
    page.y -= 4
    page.text(border_string, space=True)
    page.br(4)
    page.set_font(family="courbd", size=18)
    page.text("Умумий сумма:", align="left")
    page.set_font(family="courbd", size=16)
    page.text(f"{order.without_tax} сўм", align="right", space=True)
    page.br(4)
    tax = Settings().get("tax", tp=int)
    if tax != 0 and order.order_type == "table" and order.table.tax_required:
        page.set_font(family="courbd", size=18)
        page.text("Хизмат:", align="left")
        page.set_font(family="courbd", size=16)
        page.text(f"{tax}%,({order.tax_price} сўм)", align="right", space=True)
        page.br(10)
    if order.room_service_cost:
        page.set_font(family="courbd", size=18)
        page.text("Хона хизмати:", align="left")
        page.set_font(family="courbd", size=16)
        page.text(f"{order.room_service_cost} сўм", align="right", space=True)
        page.br(10)
    page.set_font(family="courbd", size=18)
    page.text("Жами:", align="left")
    page.text(f"{order.needed_payment} сўм", align="right", space=True)
    page.set_font(family="courbd", size=18)
    if Settings().get("last_message", tp=str):
        page.br(10)
        page.text(border_string, align="center", space=True)
        page.br(4)
        page.set_font(family="courbd", size=26)
        page.text(Settings().get(key="last_message", tp=str), space=True)
        page.br(4)
        page.set_font(family="courbd", size=18)
        page.text(border_string, space=True)
    page.br(6)
    page.set_font(family="courbd", size=12)
    page.text("created by serwibe.uz", align="right", space=True)
    page.save()
    doc.image(image=page.image, position=(0, 0), size=(page.width, page.height))
    doc.end_document()


def printer_order_item(order_item: OrderItem, quantity: int):
    now = datetime.now()
    doc = Document(printer=order_item.meal.category.printer, width=int(Settings().get("printer_width", int) * 51))
    doc.begin_document()
    page = Receipt(width=Settings().get("printer_width", int) * 80 - 400)
    page.set_font(family="courbd", size=17)
    page.text(now.strftime("%d.%m.%Y %H:%M"), space=True)
    page.br(8)
    page.text(f"Буюртма:   #{order_item.order.id}", space=True)
    page.br(8)
    if order_item.order.order_type == 'table':
        page.text(f"Стол:   {order_item.order.table.room.title}, {order_item.order.table.number}", space=True)
        page.br(8)
    page.text(f"Оффитсант:   {order_item.order.waiter.first_name} {order_item.order.waiter.last_name[0]}", space=True)
    page.br(8)
    page.set_font(family="courbd", size=22)
    page.text(order_item.meal.title, align="left")
    page.text(str(quantity), align="right", space=True)
    page.br(4)
    page.save()
    doc.image(image=page.image, position=(0, 0), size=(page.width, page.height))
    doc.end_document()
