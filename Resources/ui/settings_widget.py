# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/ui/settings_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(518, 655)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Form.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tab = QtWidgets.QTabWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab.setFont(font)
        self.tab.setStyleSheet("\n"
"QLineEdit{\n"
"background-color: white;\n"
"border: 1px solid #59CDF2;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border: 1px solid #29e1ff;\n"
"border-radius: 5px;\n"
"}\n"
"QDateEdit {\n"
"    border: 1px solid #7cd0ef;\n"
"    border-radius: 5px;\n"
"}\n"
"QDateEdit:hover{\n"
"border-color: #5487ee;\n"
"}\n"
"\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
" \n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"QDateEdit::down-arrow {\n"
"  image: url(:/main/drop_down.png);\n"
"height: 18px;\n"
"width: 18px;\n"
"}\n"
"QDateEdit::drop-down:hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d8d7d7, stop: 1 #e9e9e9);\n"
"}\n"
"\n"
"QDateEdit::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"\n"
"QComboBox {\n"
"    border: 1px solid #7cd0ef;\n"
"    border-radius: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"border-color: #5487ee;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
" \n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox::down-arrow {\n"
"  image: url(:/main/drop_down.png);\n"
"height: 18px;\n"
"width: 18px;\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d8d7d7, stop: 1 #e9e9e9);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.tab.setObjectName("tab")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setStyleSheet("")
        self.tab1.setObjectName("tab1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_2 = QtWidgets.QLabel(self.tab1)
        self.title_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        self.title_2.setFont(font)
        self.title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_2.setObjectName("title_2")
        self.verticalLayout_2.addWidget(self.title_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.autostart_title = QtWidgets.QLabel(self.tab1)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.autostart_title.setFont(font)
        self.autostart_title.setObjectName("autostart_title")
        self.horizontalLayout_10.addWidget(self.autostart_title)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.autostart = QtWidgets.QCheckBox(self.tab1)
        self.autostart.setText("")
        self.autostart.setObjectName("autostart")
        self.horizontalLayout_10.addWidget(self.autostart)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.open_from_browser_label = QtWidgets.QLabel(self.tab1)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.open_from_browser_label.setFont(font)
        self.open_from_browser_label.setObjectName("open_from_browser_label")
        self.horizontalLayout_15.addWidget(self.open_from_browser_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.open_from_browser = QtWidgets.QCheckBox(self.tab1)
        self.open_from_browser.setText("")
        self.open_from_browser.setObjectName("open_from_browser")
        self.horizontalLayout_15.addWidget(self.open_from_browser)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.language_title = QtWidgets.QLabel(self.tab1)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.language_title.setFont(font)
        self.language_title.setObjectName("language_title")
        self.horizontalLayout_14.addWidget(self.language_title)
        self.language_box = QtWidgets.QComboBox(self.tab1)
        self.language_box.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.language_box.setFont(font)
        self.language_box.setStyleSheet("")
        self.language_box.setIconSize(QtCore.QSize(30, 30))
        self.language_box.setObjectName("language_box")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/main/uzbek_flag.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.language_box.addItem(icon1, "")
        self.language_box.addItem(icon1, "")
        self.horizontalLayout_14.addWidget(self.language_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.id_bot = QtWidgets.QPushButton(self.tab1)
        self.id_bot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.id_bot.setStyleSheet("QPushButton {\n"
"background-color: None;\n"
"border: None;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(85, 170, 255, 0.2);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(85, 170, 255, 0.4);\n"
"}")
        self.id_bot.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/main/telegram.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.id_bot.setIcon(icon2)
        self.id_bot.setIconSize(QtCore.QSize(45, 45))
        self.id_bot.setObjectName("id_bot")
        self.horizontalLayout_11.addWidget(self.id_bot)
        self.label = QtWidgets.QLabel(self.tab1)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_11)
        self.admin_id_edit = QtWidgets.QLineEdit(self.tab1)
        self.admin_id_edit.setMinimumSize(QtCore.QSize(0, 40))
        self.admin_id_edit.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.admin_id_edit.setFont(font)
        self.admin_id_edit.setStyleSheet("")
        self.admin_id_edit.setObjectName("admin_id_edit")
        self.horizontalLayout_13.addWidget(self.admin_id_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.admin_report = QtWidgets.QPushButton(self.tab1)
        self.admin_report.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.admin_report.setFont(font)
        self.admin_report.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.admin_report.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"border: 2px solid #6AF2F0;\n"
"}\n"
"QPushButton:hover {\n"
"color: white;\n"
"background-color: #6AF2F0;\n"
"}\n"
"QPushButton:pressed {\n"
"color: white;\n"
"background-color: rgb(47, 231, 247);\n"
"border: 2px solid rgb(47, 231, 247);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/main/submit_document.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap(":/main/submit_document.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.admin_report.setIcon(icon3)
        self.admin_report.setIconSize(QtCore.QSize(40, 40))
        self.admin_report.setObjectName("admin_report")
        self.verticalLayout_2.addWidget(self.admin_report)
        self.send_logs = QtWidgets.QPushButton(self.tab1)
        self.send_logs.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.send_logs.setFont(font)
        self.send_logs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send_logs.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"border: 2px solid #6AF2F0;\n"
"}\n"
"QPushButton:hover {\n"
"color: white;\n"
"background-color: #6AF2F0;\n"
"}\n"
"QPushButton:pressed {\n"
"color: white;\n"
"background-color: rgb(47, 231, 247);\n"
"border: 2px solid rgb(47, 231, 247);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/main/send_logs.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap(":/main/send_logs.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.send_logs.setIcon(icon4)
        self.send_logs.setIconSize(QtCore.QSize(40, 40))
        self.send_logs.setObjectName("send_logs")
        self.verticalLayout_2.addWidget(self.send_logs)
        self.clear_database_btn = QtWidgets.QPushButton(self.tab1)
        self.clear_database_btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.clear_database_btn.setFont(font)
        self.clear_database_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_database_btn.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"border: 2px solid #ff1f1f;\n"
"}\n"
"QPushButton:hover {\n"
"color: white;\n"
"background-color: #ff3333;\n"
"}\n"
"QPushButton:pressed {\n"
"color: white;\n"
"background-color: #ff0a0a;\n"
"border: 2px solid #ff0a0a;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/main/delete_database.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon5.addPixmap(QtGui.QPixmap(":/main/send_logs.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.clear_database_btn.setIcon(icon5)
        self.clear_database_btn.setIconSize(QtCore.QSize(40, 40))
        self.clear_database_btn.setObjectName("clear_database_btn")
        self.verticalLayout_2.addWidget(self.clear_database_btn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/main/main_settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tab.addTab(self.tab1, icon6, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab2)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.tab2)
        self.title.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.company_name = QtWidgets.QLabel(self.tab2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.company_name.setFont(font)
        self.company_name.setObjectName("company_name")
        self.horizontalLayout.addWidget(self.company_name)
        self.company_name_edit = QtWidgets.QLineEdit(self.tab2)
        self.company_name_edit.setMinimumSize(QtCore.QSize(240, 40))
        self.company_name_edit.setMaximumSize(QtCore.QSize(220, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.company_name_edit.setFont(font)
        self.company_name_edit.setObjectName("company_name_edit")
        self.horizontalLayout.addWidget(self.company_name_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.address_label = QtWidgets.QLabel(self.tab2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.address_label.setFont(font)
        self.address_label.setObjectName("address_label")
        self.horizontalLayout_2.addWidget(self.address_label)
        self.address_edit = QtWidgets.QLineEdit(self.tab2)
        self.address_edit.setMinimumSize(QtCore.QSize(280, 40))
        self.address_edit.setMaximumSize(QtCore.QSize(280, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.address_edit.setFont(font)
        self.address_edit.setObjectName("address_edit")
        self.horizontalLayout_2.addWidget(self.address_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.number_label = QtWidgets.QLabel(self.tab2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.number_label.setFont(font)
        self.number_label.setObjectName("number_label")
        self.horizontalLayout_3.addWidget(self.number_label)
        self.number_edit = QtWidgets.QLineEdit(self.tab2)
        self.number_edit.setMinimumSize(QtCore.QSize(280, 40))
        self.number_edit.setMaximumSize(QtCore.QSize(280, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.number_edit.setFont(font)
        self.number_edit.setPlaceholderText("")
        self.number_edit.setObjectName("number_edit")
        self.horizontalLayout_3.addWidget(self.number_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tax_label = QtWidgets.QLabel(self.tab2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.tax_label.setFont(font)
        self.tax_label.setObjectName("tax_label")
        self.horizontalLayout_7.addWidget(self.tax_label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tax_edit = QtWidgets.QSpinBox(self.tab2)
        self.tax_edit.setMinimumSize(QtCore.QSize(40, 40))
        self.tax_edit.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.tax_edit.setFont(font)
        self.tax_edit.setObjectName("tax_edit")
        self.horizontalLayout_6.addWidget(self.tax_edit)
        self.tax_label_2 = QtWidgets.QLabel(self.tab2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.tax_label_2.setFont(font)
        self.tax_label_2.setObjectName("tax_label_2")
        self.horizontalLayout_6.addWidget(self.tax_label_2)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.last_message_label = QtWidgets.QLabel(self.tab2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.last_message_label.setFont(font)
        self.last_message_label.setObjectName("last_message_label")
        self.horizontalLayout_4.addWidget(self.last_message_label)
        self.last_message_edit = QtWidgets.QLineEdit(self.tab2)
        self.last_message_edit.setMinimumSize(QtCore.QSize(280, 40))
        self.last_message_edit.setMaximumSize(QtCore.QSize(280, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.last_message_edit.setFont(font)
        self.last_message_edit.setObjectName("last_message_edit")
        self.horizontalLayout_4.addWidget(self.last_message_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.cash_register = QtWidgets.QLabel(self.tab2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.cash_register.setFont(font)
        self.cash_register.setObjectName("cash_register")
        self.horizontalLayout_12.addWidget(self.cash_register)
        self.printer = QtWidgets.QComboBox(self.tab2)
        self.printer.setMinimumSize(QtCore.QSize(250, 35))
        self.printer.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(12)
        self.printer.setFont(font)
        self.printer.setObjectName("printer")
        self.horizontalLayout_12.addWidget(self.printer)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.printer_size_label = QtWidgets.QLabel(self.tab2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.printer_size_label.setFont(font)
        self.printer_size_label.setObjectName("printer_size_label")
        self.horizontalLayout_8.addWidget(self.printer_size_label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.printer_width_edit = QtWidgets.QSpinBox(self.tab2)
        self.printer_width_edit.setMinimumSize(QtCore.QSize(40, 40))
        self.printer_width_edit.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.printer_width_edit.setFont(font)
        self.printer_width_edit.setMaximum(210)
        self.printer_width_edit.setProperty("value", 80)
        self.printer_width_edit.setObjectName("printer_width_edit")
        self.horizontalLayout_9.addWidget(self.printer_width_edit)
        self.tax_label_4 = QtWidgets.QLabel(self.tab2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.tax_label_4.setFont(font)
        self.tax_label_4.setObjectName("tax_label_4")
        self.horizontalLayout_9.addWidget(self.tax_label_4)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cancel_button = QtWidgets.QPushButton(self.tab2)
        self.cancel_button.setMinimumSize(QtCore.QSize(130, 50))
        self.cancel_button.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_5.addWidget(self.cancel_button)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.accept_button = QtWidgets.QPushButton(self.tab2)
        self.accept_button.setMinimumSize(QtCore.QSize(130, 50))
        self.accept_button.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.accept_button.setFont(font)
        self.accept_button.setObjectName("accept_button")
        self.horizontalLayout_5.addWidget(self.accept_button)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/main/receipt.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tab.addTab(self.tab2, icon7, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.current_status_msg = QtWidgets.QLabel(self.tab3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.current_status_msg.setFont(font)
        self.current_status_msg.setObjectName("current_status_msg")
        self.horizontalLayout_32.addWidget(self.current_status_msg)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem7)
        self.license_status_icon = QtWidgets.QPushButton(self.tab3)
        self.license_status_icon.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.license_status_icon.setStyleSheet("background: None;\n"
"border: None;")
        self.license_status_icon.setText("")
        self.license_status_icon.setIcon(icon2)
        self.license_status_icon.setIconSize(QtCore.QSize(30, 30))
        self.license_status_icon.setObjectName("license_status_icon")
        self.horizontalLayout_32.addWidget(self.license_status_icon)
        self.license_status = QtWidgets.QLabel(self.tab3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.license_status.setFont(font)
        self.license_status.setObjectName("license_status")
        self.horizontalLayout_32.addWidget(self.license_status)
        self.verticalLayout_6.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem8)
        self.remaining_days = QtWidgets.QLabel(self.tab3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.remaining_days.setFont(font)
        self.remaining_days.setObjectName("remaining_days")
        self.horizontalLayout_33.addWidget(self.remaining_days)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_33)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem10)
        self.license_info = QtWidgets.QFrame(self.tab3)
        self.license_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.license_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.license_info.setObjectName("license_info")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.license_info)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.line = QtWidgets.QFrame(self.license_info)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem11)
        self.label_4 = QtWidgets.QLabel(self.license_info)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_30.addWidget(self.label_4)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem12)
        self.verticalLayout_5.addLayout(self.horizontalLayout_30)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem13)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.start_date = QtWidgets.QDateEdit(self.license_info)
        self.start_date.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.start_date.setFont(font)
        self.start_date.setStyleSheet("")
        self.start_date.setCalendarPopup(True)
        self.start_date.setObjectName("start_date")
        self.horizontalLayout_29.addWidget(self.start_date)
        self.label_5 = QtWidgets.QLabel(self.license_info)
        self.label_5.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_29.addWidget(self.label_5)
        self.end_date = QtWidgets.QDateEdit(self.license_info)
        self.end_date.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.end_date.setFont(font)
        self.end_date.setCalendarPopup(True)
        self.end_date.setObjectName("end_date")
        self.horizontalLayout_29.addWidget(self.end_date)
        self.verticalLayout_5.addLayout(self.horizontalLayout_29)
        self.verticalLayout_6.addWidget(self.license_info)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem14)
        self.new_license_btn = QtWidgets.QPushButton(self.tab3)
        self.new_license_btn.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.new_license_btn.setFont(font)
        self.new_license_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.new_license_btn.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"border: 2px solid #6AF2F0;\n"
"}\n"
"QPushButton:hover {\n"
"color: white;\n"
"background-color: #6AF2F0;\n"
"}\n"
"QPushButton:pressed {\n"
"color: white;\n"
"background-color: rgb(47, 231, 247);\n"
"border: 2px solid rgb(47, 231, 247);\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/main/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon8.addPixmap(QtGui.QPixmap(":/main/submit_document.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.new_license_btn.setIcon(icon8)
        self.new_license_btn.setIconSize(QtCore.QSize(40, 40))
        self.new_license_btn.setObjectName("new_license_btn")
        self.horizontalLayout_31.addWidget(self.new_license_btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_31)
        self.gridLayout_6.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 246, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem15, 1, 0, 1, 1)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/main/license.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tab.addTab(self.tab3, icon9, "")
        self.gridLayout_2.addWidget(self.tab, 0, 1, 1, 1)

        self.retranslateUi(Form)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Созламалар"))
        self.title_2.setText(_translate("Form", "Asosiy sozlamalar"))
        self.autostart_title.setText(_translate("Form", "Avto boshlash:"))
        self.open_from_browser_label.setText(_translate("Form", "Brauzerda ochish:"))
        self.language_title.setText(_translate("Form", "Til:"))
        self.language_box.setItemText(0, _translate("Form", "O\'zbek (Lotin)"))
        self.language_box.setItemText(1, _translate("Form", "Ўзбек (крилл)"))
        self.id_bot.setShortcut(_translate("Form", "Ctrl+Z, Ctrl+Z"))
        self.label.setText(_translate("Form", "Admin ID:"))
        self.admin_report.setText(_translate("Form", "Adminga xisobot"))
        self.send_logs.setText(_translate("Form", "Xatolik xaqida ma\'lumot"))
        self.clear_database_btn.setText(_translate("Form", "Bazani tozalash"))
        self.tab.setTabText(self.tab.indexOf(self.tab1), _translate("Form", "Asosiy"))
        self.title.setText(_translate("Form", "Chek ma\'lumotlari"))
        self.company_name.setText(_translate("Form", "Tashkilot nomi:"))
        self.company_name_edit.setPlaceholderText(_translate("Form", "SerWibe"))
        self.address_label.setText(_translate("Form", "Manzil:"))
        self.number_label.setText(_translate("Form", "Telefon:"))
        self.number_edit.setInputMask(_translate("Form", "\\+\\9\\9\\8\\(99)-999-99-99"))
        self.tax_label.setText(_translate("Form", "Offitsant uchun:"))
        self.tax_label_2.setText(_translate("Form", "%"))
        self.last_message_label.setText(_translate("Form", "Oxirgi satr:"))
        self.last_message_edit.setText(_translate("Form", "РАХМАТ"))
        self.last_message_edit.setPlaceholderText(_translate("Form", "РАХМАТ"))
        self.cash_register.setText(_translate("Form", "Kassa printer:"))
        self.printer_size_label.setText(_translate("Form", "Printer o\'lchami:"))
        self.tax_label_4.setText(_translate("Form", "мм"))
        self.cancel_button.setText(_translate("Form", "Bekor qilish"))
        self.accept_button.setText(_translate("Form", "Saqlash"))
        self.tab.setTabText(self.tab.indexOf(self.tab2), _translate("Form", "Chek"))
        self.current_status_msg.setText(_translate("Form", "Hozirgi xolat:"))
        self.license_status_icon.setShortcut(_translate("Form", "Ctrl+Z, Ctrl+Z"))
        self.license_status.setText(_translate("Form", "Faol"))
        self.remaining_days.setText(_translate("Form", "4 days remaining"))
        self.label_4.setText(_translate("Form", "Litsenziya muddati:"))
        self.start_date.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.label_5.setText(_translate("Form", "-"))
        self.end_date.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.new_license_btn.setText(_translate("Form", "Yangi litsenziya"))
        self.tab.setTabText(self.tab.indexOf(self.tab3), _translate("Form", "Litsenziya"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
