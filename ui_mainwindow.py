# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'ui_mainwindow.ui'
##
# Created by: Qt User Interface Compiler version 6.7.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(514, 223)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_autoruns = QPushButton(self.centralwidget)
        self.btn_autoruns.setObjectName(u"btn_autoruns")

        self.verticalLayout.addWidget(self.btn_autoruns)

        self.btn_services = QPushButton(self.centralwidget)
        self.btn_services.setObjectName(u"btn_services")

        self.verticalLayout.addWidget(self.btn_services)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"SysToolLauncher", None))
        self.btn_autoruns.setText(QCoreApplication.translate(
            "MainWindow", u"Autoruns", None))
        self.btn_services.setText(QCoreApplication.translate(
            "MainWindow", u"\u0421\u043b\u0443\u0436\u0431\u044b", None))
    # retranslateUi
