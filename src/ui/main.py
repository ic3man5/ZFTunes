# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QScrollArea, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QToolButton,
    QTreeView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(849, 620)
        self.action_New_Profile = QAction(MainWindow)
        self.action_New_Profile.setObjectName(u"action_New_Profile")
        self.action_Open_Profile = QAction(MainWindow)
        self.action_Open_Profile.setObjectName(u"action_Open_Profile")
        self.action_Save_Profile = QAction(MainWindow)
        self.action_Save_Profile.setObjectName(u"action_Save_Profile")
        self.actionSave_Profile_As = QAction(MainWindow)
        self.actionSave_Profile_As.setObjectName(u"actionSave_Profile_As")
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBoxGears = QGroupBox(self.centralwidget)
        self.groupBoxGears.setObjectName(u"groupBoxGears")
        self.horizontalLayout = QHBoxLayout(self.groupBoxGears)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableWidgetGears = QTableWidget(self.groupBoxGears)
        self.tableWidgetGears.setObjectName(u"tableWidgetGears")

        self.horizontalLayout.addWidget(self.tableWidgetGears)

        self.widgetGearsChart = QWidget(self.groupBoxGears)
        self.widgetGearsChart.setObjectName(u"widgetGearsChart")
        self.widgetGearsChart.setEnabled(False)

        self.horizontalLayout.addWidget(self.widgetGearsChart)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.groupBoxGears, 0, 0, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 849, 21))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_5 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBoxProfile = QGroupBox(self.dockWidgetContents)
        self.groupBoxProfile.setObjectName(u"groupBoxProfile")
        self.gridLayout = QGridLayout(self.groupBoxProfile)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolButtonProfileExplore = QToolButton(self.groupBoxProfile)
        self.toolButtonProfileExplore.setObjectName(u"toolButtonProfileExplore")

        self.gridLayout.addWidget(self.toolButtonProfileExplore, 0, 2, 1, 1)

        self.comboBoxProfile = QComboBox(self.groupBoxProfile)
        self.comboBoxProfile.setObjectName(u"comboBoxProfile")

        self.gridLayout.addWidget(self.comboBoxProfile, 0, 0, 1, 2)

        self.scrollAreaProfile = QScrollArea(self.groupBoxProfile)
        self.scrollAreaProfile.setObjectName(u"scrollAreaProfile")
        self.scrollAreaProfile.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 320, 478))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.treeViewProfile = QTreeView(self.scrollAreaWidgetContents)
        self.treeViewProfile.setObjectName(u"treeViewProfile")

        self.gridLayout_4.addWidget(self.treeViewProfile, 0, 0, 1, 1)

        self.scrollAreaProfile.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollAreaProfile, 1, 0, 1, 3)


        self.gridLayout_5.addWidget(self.groupBoxProfile, 0, 0, 1, 1)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menu_File.addAction(self.action_New_Profile)
        self.menu_File.addAction(self.action_Open_Profile)
        self.menu_File.addAction(self.action_Save_Profile)
        self.menu_File.addAction(self.actionSave_Profile_As)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ZFTunes", None))
        self.action_New_Profile.setText(QCoreApplication.translate("MainWindow", u"&New Profile", None))
        self.action_Open_Profile.setText(QCoreApplication.translate("MainWindow", u"&Open Profile", None))
        self.action_Save_Profile.setText(QCoreApplication.translate("MainWindow", u"&Save Profile", None))
        self.actionSave_Profile_As.setText(QCoreApplication.translate("MainWindow", u"Save Profile &As", None))
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
        self.groupBoxGears.setTitle(QCoreApplication.translate("MainWindow", u"OSS vs MPH/RPM", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.groupBoxProfile.setTitle(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.toolButtonProfileExplore.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

