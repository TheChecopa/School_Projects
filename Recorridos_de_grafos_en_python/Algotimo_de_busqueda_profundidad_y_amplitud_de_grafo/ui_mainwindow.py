# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1279, 517)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionDiccionario = QAction(MainWindow)
        self.actionDiccionario.setObjectName(u"actionDiccionario")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget2 = QTabWidget(self.centralwidget)
        self.tabWidget2.setObjectName(u"tabWidget2")
        self.tabWidget2.setGeometry(QRect(20, 10, 991, 461))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")

        self.gridLayout_2.addWidget(self.salida, 0, 2, 1, 1)

        self.graphicsView2 = QGraphicsView(self.tab)
        self.graphicsView2.setObjectName(u"graphicsView2")

        self.gridLayout_2.addWidget(self.graphicsView2, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.desy_spinBox_5 = QSpinBox(self.groupBox)
        self.desy_spinBox_5.setObjectName(u"desy_spinBox_5")
        self.desy_spinBox_5.setMaximum(500)

        self.gridLayout.addWidget(self.desy_spinBox_5, 4, 1, 1, 1)

        self.ordenar_velocidad_pushButton = QPushButton(self.groupBox)
        self.ordenar_velocidad_pushButton.setObjectName(u"ordenar_velocidad_pushButton")

        self.gridLayout.addWidget(self.ordenar_velocidad_pushButton, 10, 2, 1, 1)

        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout.addWidget(self.agregar_final_pushButton, 8, 0, 1, 2)

        self.oriy_spinBox_6 = QSpinBox(self.groupBox)
        self.oriy_spinBox_6.setObjectName(u"oriy_spinBox_6")
        self.oriy_spinBox_6.setMaximum(500)

        self.gridLayout.addWidget(self.oriy_spinBox_6, 2, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.velocidad_spinBox_4 = QSpinBox(self.groupBox)
        self.velocidad_spinBox_4.setObjectName(u"velocidad_spinBox_4")
        self.velocidad_spinBox_4.setMaximum(500)

        self.gridLayout.addWidget(self.velocidad_spinBox_4, 6, 1, 1, 1)

        self.desx_spinBox_2 = QSpinBox(self.groupBox)
        self.desx_spinBox_2.setObjectName(u"desx_spinBox_2")
        self.desx_spinBox_2.setMaximum(500)

        self.gridLayout.addWidget(self.desx_spinBox_2, 3, 1, 1, 1)

        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout.addWidget(self.agregar_inicio_pushButton, 8, 2, 1, 1)

        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setMaximumSize(QSize(117, 20))
        self.id_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.id_spinBox, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.ordenar_ide_pushButton = QPushButton(self.groupBox)
        self.ordenar_ide_pushButton.setObjectName(u"ordenar_ide_pushButton")

        self.gridLayout.addWidget(self.ordenar_ide_pushButton, 9, 2, 1, 1)

        self.ordenar_distancia_pushButton = QPushButton(self.groupBox)
        self.ordenar_distancia_pushButton.setObjectName(u"ordenar_distancia_pushButton")

        self.gridLayout.addWidget(self.ordenar_distancia_pushButton, 10, 0, 1, 2)

        self.profundidad_pushButton = QPushButton(self.groupBox)
        self.profundidad_pushButton.setObjectName(u"profundidad_pushButton")

        self.gridLayout.addWidget(self.profundidad_pushButton, 11, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.red_spinBox_7 = QSpinBox(self.groupBox_2)
        self.red_spinBox_7.setObjectName(u"red_spinBox_7")
        self.red_spinBox_7.setMaximum(255)

        self.gridLayout_3.addWidget(self.red_spinBox_7, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)

        self.green_spinBox_8 = QSpinBox(self.groupBox_2)
        self.green_spinBox_8.setObjectName(u"green_spinBox_8")
        self.green_spinBox_8.setMaximum(255)

        self.gridLayout_3.addWidget(self.green_spinBox_8, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)

        self.blue_spinBox_9 = QSpinBox(self.groupBox_2)
        self.blue_spinBox_9.setObjectName(u"blue_spinBox_9")
        self.blue_spinBox_9.setMaximum(255)

        self.gridLayout_3.addWidget(self.blue_spinBox_9, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 5, 0, 1, 2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.amplitud_pushButton = QPushButton(self.groupBox)
        self.amplitud_pushButton.setObjectName(u"amplitud_pushButton")

        self.gridLayout.addWidget(self.amplitud_pushButton, 11, 2, 1, 1)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 9, 0, 1, 2)

        self.orix_spinBox_3 = QSpinBox(self.groupBox)
        self.orix_spinBox_3.setObjectName(u"orix_spinBox_3")
        self.orix_spinBox_3.setMaximum(500)

        self.gridLayout.addWidget(self.orix_spinBox_3, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget2.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_4.addWidget(self.tabla, 0, 0, 1, 3)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_4.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.tabWidget2.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar = QPushButton(self.tab_3)
        self.dibujar.setObjectName(u"dibujar")

        self.gridLayout_5.addWidget(self.dibujar, 1, 0, 1, 1)

        self.limpiar = QPushButton(self.tab_3)
        self.limpiar.setObjectName(u"limpiar")

        self.gridLayout_5.addWidget(self.limpiar, 1, 1, 1, 1)

        self.tabWidget2.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1279, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionDiccionario)

        self.retranslateUi(MainWindow)

        self.tabWidget2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionDiccionario.setText(QCoreApplication.translate("MainWindow", u"Diccionario", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Captura de particulas", None))
        self.ordenar_velocidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"ORDENAR POR VELOCIDAD", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"AGREGAR FINAL", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen en y", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"AGREGAR INICIO", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino y", None))
        self.ordenar_ide_pushButton.setText(QCoreApplication.translate("MainWindow", u"ORDENAR POR ID", None))
        self.ordenar_distancia_pushButton.setText(QCoreApplication.translate("MainWindow", u"ORDENAR POR DISTANCIA", None))
        self.profundidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"BUSQUEDA EN PROFUNDIDAD", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Color (rgb)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino x", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id (entero)", None))
        self.amplitud_pushButton.setText(QCoreApplication.translate("MainWindow", u"BUSQUEDA EN AMPLITUD", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"MOSTRAR", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en x", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u00edtulo del libro", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

