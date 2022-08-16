# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_PruebaRobotilsa(object):
    def setupUi(self, PruebaRobotilsa):
        if not PruebaRobotilsa.objectName():
            PruebaRobotilsa.setObjectName(u"PruebaRobotilsa")
        PruebaRobotilsa.resize(484, 474)
        self.centralwidget = QWidget(PruebaRobotilsa)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Hora = QLabel(self.centralwidget)
        self.Hora.setObjectName(u"Hora")
        self.Hora.setGeometry(QRect(320, 40, 91, 41))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.Hora.setFont(font)
        self.Fecha = QLabel(self.centralwidget)
        self.Fecha.setObjectName(u"Fecha")
        self.Fecha.setGeometry(QRect(290, 80, 151, 31))
        self.Fecha.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 210, 91, 31))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.InfoPersonaje = QListWidget(self.centralwidget)
        QListWidgetItem(self.InfoPersonaje)
        QListWidgetItem(self.InfoPersonaje)
        QListWidgetItem(self.InfoPersonaje)
        QListWidgetItem(self.InfoPersonaje)
        QListWidgetItem(self.InfoPersonaje)
        QListWidgetItem(self.InfoPersonaje)
        QListWidgetItem(self.InfoPersonaje)
        QListWidgetItem(self.InfoPersonaje)
        QListWidgetItem(self.InfoPersonaje)
        QListWidgetItem(self.InfoPersonaje)
        QListWidgetItem(self.InfoPersonaje)
        self.InfoPersonaje.setObjectName(u"InfoPersonaje")
        self.InfoPersonaje.setGeometry(QRect(20, 30, 256, 391))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 250, 83, 29))
        self.pushButton_2.setFont(font)
        PruebaRobotilsa.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PruebaRobotilsa)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 484, 25))
        PruebaRobotilsa.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PruebaRobotilsa)
        self.statusbar.setObjectName(u"statusbar")
        PruebaRobotilsa.setStatusBar(self.statusbar)

        self.retranslateUi(PruebaRobotilsa)
        self.pushButton_2.clicked.connect(PruebaRobotilsa.close)

        QMetaObject.connectSlotsByName(PruebaRobotilsa)
    # setupUi

    def retranslateUi(self, PruebaRobotilsa):
        PruebaRobotilsa.setWindowTitle(QCoreApplication.translate("PruebaRobotilsa", u"Postulante para ROBOTILSA S.A.", None))
        self.Hora.setText(QCoreApplication.translate("PruebaRobotilsa", u"00:00:00", None))
        self.Fecha.setText(QCoreApplication.translate("PruebaRobotilsa", u"00/00/0000", None))
        self.pushButton.setText(QCoreApplication.translate("PruebaRobotilsa", u"REQUEST", None))

        __sortingEnabled = self.InfoPersonaje.isSortingEnabled()
        self.InfoPersonaje.setSortingEnabled(False)
        ___qlistwidgetitem = self.InfoPersonaje.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("PruebaRobotilsa", u"Luke Skywalker", None));
        ___qlistwidgetitem1 = self.InfoPersonaje.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("PruebaRobotilsa", u"New Item", None));
        ___qlistwidgetitem2 = self.InfoPersonaje.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("PruebaRobotilsa", u"C-3P0", None));
        ___qlistwidgetitem3 = self.InfoPersonaje.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("PruebaRobotilsa", u"R2-D2", None));
        ___qlistwidgetitem4 = self.InfoPersonaje.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("PruebaRobotilsa", u"Darth Vader", None));
        ___qlistwidgetitem5 = self.InfoPersonaje.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("PruebaRobotilsa", u"Leia Organa", None));
        ___qlistwidgetitem6 = self.InfoPersonaje.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("PruebaRobotilsa", u"Owen Lars", None));
        ___qlistwidgetitem7 = self.InfoPersonaje.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("PruebaRobotilsa", u"Beru Whitesun Lars", None));
        ___qlistwidgetitem8 = self.InfoPersonaje.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("PruebaRobotilsa", u"R5-D4", None));
        ___qlistwidgetitem9 = self.InfoPersonaje.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("PruebaRobotilsa", u"Biggs Darklighter", None));
        ___qlistwidgetitem10 = self.InfoPersonaje.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("PruebaRobotilsa", u"Obi-Wan Kenobi", None));
        self.InfoPersonaje.setSortingEnabled(__sortingEnabled)

        self.pushButton_2.setText(QCoreApplication.translate("PruebaRobotilsa", u"SALIR", None))
    # retranslateUi

