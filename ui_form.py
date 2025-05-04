# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 300)
        MainWindow.setMinimumSize(QSize(550, 300))
        MainWindow.setMaximumSize(QSize(550, 300))
        MainWindow.setWindowTitle(u"hw-info")
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.cpuarch = QLabel(self.widget)
        self.cpuarch.setObjectName(u"cpuarch")
        self.cpuarch.setGeometry(QRect(0, 30, 191, 31))
        font = QFont()
        font.setPointSize(16)
        self.cpuarch.setFont(font)
        self.cpucores = QLabel(self.widget)
        self.cpucores.setObjectName(u"cpucores")
        self.cpucores.setGeometry(QRect(0, 60, 191, 31))
        self.cpucores.setFont(font)
        self.cpubrand = QLabel(self.widget)
        self.cpubrand.setObjectName(u"cpubrand")
        self.cpubrand.setGeometry(QRect(0, 0, 541, 31))
        self.cpubrand.setFont(font)
        MainWindow.setCentralWidget(self.widget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 550, 20))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.cpuarch.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.cpucores.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.cpubrand.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        pass
    # retranslateUi

