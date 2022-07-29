from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from Algoritmos.particulasad import Particulasad
from Algoritmos.particula import Particula
from Algoritmos.algoritmos import distancia_euclidiana

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.particulasad = Particulasad()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.mostrar_pushButton.clicked.connect(self.dibujar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_ide)


        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView2.setScene(self.scene)

        self.ui.ordenar_ide_pushButton.clicked.connect(self.ordenar_ide)
        self.ui.ordenar_distancia_pushButton.clicked.connect(self.ordenar_distancia)
        self.ui.ordenar_velocidad_pushButton.clicked.connect(self.ordenar_velocidad)

    @Slot()
    def buscar_ide(self):
        ide = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula in self.particulasad:
            if ide == str(particula.ide):
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                ide_widget = QTableWidgetItem(str(particula.ide))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.tabla.setItem(0, 0, ide_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",
                f'La particula con id "{ide}" no fue encontrado'
            )
        

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(9)
        headers = ["Id", "Origen en x", "Origen en y", "Destino en x", "Destino en y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.particulasad))

        row = 0
        for particula in self.particulasad:
            ide_widget = QTableWidgetItem(str(particula.ide))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0, ide_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)
             
            row += 1
            

    @Slot()
    def action_abrir_archivo(self):
        #print('abrir_archivo')
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulasad.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        #print('guardar_archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.particulasad.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )

    @Slot()
    def click_mostrar(self):
        #self.particulasad.mostrar()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulasad))

    @Slot()
    def click_agregar(self):
        ide = self.ui.id_spinBox.value()
        origenx = self.ui.orix_spinBox_3.value()
        origeny = self.ui.oriy_spinBox_6.value()
        destinox = self.ui.desx_spinBox_2.value()
        destinoy = self.ui.desy_spinBox_5.value()
        velocidad = self.ui.velocidad_spinBox_4.value()
        red = self.ui.red_spinBox_7.value()
        green = self.ui.green_spinBox_8.value()
        blue = self.ui.blue_spinBox_9.value()

        particula = Particula(ide, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        self.particulasad.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):
        ide = self.ui.id_spinBox.value()
        origenx = self.ui.orix_spinBox_3.value()
        origeny = self.ui.oriy_spinBox_6.value()
        destinox = self.ui.desx_spinBox_2.value()
        destinoy = self.ui.desy_spinBox_5.value()
        velocidad = self.ui.velocidad_spinBox_4.value()
        red = self.ui.red_spinBox_7.value()
        green = self.ui.green_spinBox_8.value()
        blue = self.ui.blue_spinBox_9.value()

        particula = Particula(ide, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        self.particulasad.agregar_inicio(particula)

        #print(ide, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        #self.ui.salida.insertPlainText(str(ide) + str(origenx) + str(origeny) + str(destinox) + 
        #str(destinoy) + str(velocidad) + str(red) + str(green) + str(blue))
    
    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)
 
        for particula in self.particulasad:
            r = particula.red
            g = particula.green
            b = particula.blue
            
            color = QColor(r, g, b)
            pen.setColor(color)
 
            origen_x = particula.origen_x
            origen_y = particula.origen_y
            destino_x = particula.destino_x
            destino_y = particula.destino_y
 
            self.scene.addEllipse(origen_x, origen_y, 3, 3, pen)
            self.scene.addEllipse(destino_x, destino_y, 3, 3, pen)
            self.scene.addLine(origen_x+3, origen_y+3, destino_x, destino_y, pen)
    
    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot()
    def ordenar_ide(self):
            self.particulasad.sort_by_ide()
 
    @Slot()
    def ordenar_distancia(self):
            self.particulasad.sort_by_distancia()
 
    @Slot()
    def ordenar_velocidad(self):
            self.particulasad.sort_by_velocidad()