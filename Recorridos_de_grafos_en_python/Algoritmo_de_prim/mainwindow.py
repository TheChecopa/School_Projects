from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulasad import Particulasad
from particula import Particula
from algoritmos import distancia_euclidiana
from random import randint
from pprint import pformat, pprint
from collections import deque
from queue import PriorityQueue
from algoritmos import prim

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.particulas = Particulasad()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.grafo = dict()
        self.grafo2 = dict()
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
        self.ui.actionPrim.triggered.connect(self.action_prim)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        

        self.ui.ordenar_Id_pushButton.clicked.connect(self.ordenar_Id)
        self.ui.ordenar_Distancia_pushButton.clicked.connect(self.ordenar_distancia)
        self.ui.ordenar_Velocidad_pushButton.clicked.connect(self.ordenar_velocidad)

        self.ui.graphicsView_Grafo.setScene(self.scene)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.mostrar_pushButton.clicked.connect(self.click_grafo)

        self.ui.Profundidad_pushButton.clicked.connect(self.busqueda_profundidad)
        self.ui.Amplitud_pushButton.clicked.connect(self.busqueda_amplitud)


    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula in self.particulas:
            if id == particula.id:
                self.ui.tabla.clear()                
                self.ui.tabla.setRowCount(1)
                headers = ["Id", "Origen en X", "Origen en Y", "Destino en X", "Destino en Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
                self.ui.tabla.setHorizontalHeaderLabels(headers)

                id_widget = QTableWidgetItem(str(particula.id))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.tabla.setItem(0, 0, id_widget)
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
            QMessageBox.warning(self, "Atencion", f'La particula no fue encontrada')


    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["Id", "Origen en X", "Origen en Y", "Destino en X", "Destino en Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.particulas))
        
        row = 0
        for particula in self.particulas:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
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
        ubicacion = QFileDialog.getOpenFileName(self, 'Abrir archivo', '.', 'JSON (*.json)')[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(self, "Exito", "Se abrio el archivo" + ubicacion)
            for particula in self.particulas:
                origen = (particula.origen_x, particula.origen_y)
                destino = (particula.destino_x, particula.destino_y)
                peso = particula.distancia

                arista_o_d = ((particula.destino_x, particula.destino_y), peso)
                arista_d_o = ((particula.origen_x, particula.origen_y), peso)

                if origen in self.grafo:
                    self.grafo[origen].append(arista_o_d)
                else:
                    self.grafo[origen] = [arista_o_d]
                if destino in self.grafo:
                    self.grafo[destino].append(arista_d_o)
                else:
                    self.grafo[destino] = [arista_d_o]

            for particula in self.particulas:
                origen = (particula.origen_x, particula.origen_y)
                destino = (particula.destino_x, particula.destino_y)

                arista_o_d = ((particula.destino_x, particula.destino_y))
                arista_d_o = ((particula.origen_x, particula.origen_y))

                if origen in self.grafo2:
                    self.grafo2[origen].append(arista_o_d)
                else:
                    self.grafo2[origen] = [arista_o_d]
                if destino in self.grafo2:
                    self.grafo2[destino].append(arista_d_o)
                else:
                    self.grafo2[destino] = [arista_d_o]

        else:
            QMessageBox.critical(self, "Error", "Error al abrir el archivo" + ubicacion)


    @Slot()
    def action_guardar_archivo(self):
       ubicacion = QFileDialog.getSaveFileName(self, 'Guardar Archivo', '.', 'JSON (*.json)')[0]
       if self.particulas.guardar(ubicacion):
           QMessageBox.information(self, "Exito", "Se pudo crear el archivo " + ubicacion)
       else:
         QMessageBox.critical(self, "Error", "No se pudo crear el archivo " + ubicacion)


    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        str = pformat(self.grafo, width=50, indent=1)
        self.ui.salida.insertPlainText(str)



    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    
    @Slot()
    def click_grafo(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.particulas:

            color = QColor(particula.red, particula.green, particula.blue)
            pen.setColor(color)

            origen_x = particula.origen_x
            origen_y = particula.origen_y
            destino_x = particula.destino_x
            destino_y = particula.destino_y

            self.scene.addEllipse(origen_x, origen_y, 3, 3, pen)
            self.scene.addEllipse(destino_x, destino_y, 3, 3, pen)
            self.scene.addLine(origen_x, origen_y, destino_x, destino_y, pen)

            
    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.particulas:

            color = QColor(particula.red, particula.green, particula.blue)
            pen.setColor(color)

            origen_x = particula.origen_x
            origen_y = particula.origen_y
            destino_x = particula.destino_x
            destino_y = particula.destino_y

            self.scene.addEllipse(origen_x, origen_y, 3, 3, pen)
            self.scene.addEllipse(destino_x, destino_y, 3, 3, pen)
            self.scene.addLine(origen_x, origen_y, destino_x, destino_y, pen)


    @Slot()
    def limpiar(self):
        self.scene.clear()


    @Slot()
    def ordenar_Id(self):
        self.particulas.ordenar_id()


    @Slot()
    def ordenar_distancia(self):
        self.particulas.ordenar_distancia()

    @Slot()
    def ordenar_velocidad(self):
        self.particulas.ordenar_velocidad()

            
    @Slot()
    def busqueda_amplitud(self):
        visitados = deque() 
        cola = deque()
        origenX = self.ui.origenX_spinBox.value()
        oirgenY = self.ui.origenY_spinBox.value()

        origen = (origenX, oirgenY)
        visitados.append(origen)
        cola.append(origen)

        while len(cola) > 0:
            vertice = cola[0]
            print(vertice)
            cola.popleft()

            adyacentes = self.grafo2[vertice]

            for ady in adyacentes:
                if not ady in visitados:
                    visitados.append(ady)
                    cola.append(ady)


    @Slot()
    def busqueda_profundidad(self):
        visitados = deque() 
        pila = deque()
        recorrido = deque()
        origenX = self.ui.origenX_spinBox.value()
        oirgenY = self.ui.origenY_spinBox.value()

        origen = (origenX, oirgenY)
        visitados.append(origen)
        pila.append(origen)

        while len(pila) > 0:
            vertice = pila[-1]
            recorrido.append(vertice)
            print(vertice)
            pila.pop()

            adyacentes = self.grafo2[vertice]

            for ady in adyacentes:
                if not ady in visitados:
                    visitados.append(ady)
                    pila.append(ady)
    

    @Slot()               
    def action_prim(self):
        grafo = self.generar_grafo()
        x = self.ui.origenX_spinBox.value()
        y = self.ui.origenY_spinBox.value()
        origen = (x, y)
        recorrido = prim(grafo, origen)
        pen = QPen()
        pen.setWidth(2)
        for particula in recorrido:
            color = QColor(255, 0, 216)
            pen.setColor (color)
            distancia = particula[0]
            origen = particula [1]
            destino = particula[2]
            self.scene.addEllipse(origen[0] - 2, origen[1] - 2, 4, 4, pen)
            self.scene.addEllipse(destino[0] - 2, destino[1] - 2, 4, 4, pen)
            self.scene.addLine(origen[0], origen[1], destino[0], destino[1], pen)


    def generar_grafo(self):
        grafo = dict()
        for particula in self.particulas:
            origen = (particula.origen_x, particula.origen_y)
            destino = (particula.destino_x, particula.destino_y)
            peso = particula.distancia

            arista_o = (origen, peso)
            arista_d = (destino, peso)
            if origen in grafo:
                grafo[origen].append(arista_d)
            else:
                grafo[origen] = [arista_d]
            if destino in grafo:
                grafo[destino].append(arista_o)
            else:
                grafo[destino] = [arista_o]

        return grafo  


    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id_spinBox.text()
        origenX = self.ui.origenX_spinBox.value()
        oirgenY = self.ui.origenY_spinBox.value()
        destinoX = self.ui.destinoX_spinBox.value()
        destinoY = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origenX, oirgenY, destinoX, destinoY, velocidad, red, green, blue)
        self.particulas.agregar_inicio(particula)
        
        origen = (particula.origen_x, particula.origen_y)
        destino = (particula.destino_x, particula.destino_y)
        peso = particula.distancia

        arista_o_d = (particula.destino_x, particula.destino_y, peso)
        arista_d_o = (particula.origen_x, particula.origen_y, peso)

        if origen in self.grafo:
            self.grafo[origen].append(arista_o_d)
        else:
            self.grafo[origen] = [arista_o_d]
        if destino in self.grafo:
            self.grafo[destino].append(arista_d_o)
        else:
            self.grafo[destino] = [arista_d_o]

        arista_o_d = (particula.destino_x, particula.destino_y)
        arista_d_o = (particula.origen_x, particula.origen_y)

        if origen in self.grafo2:
            self.grafo2[origen].append(arista_o_d)
        else:
            self.grafo2[origen] = [arista_o_d]
        if destino in self.grafo2:
            self.grafo2[destino].append(arista_d_o)
        else:
            self.grafo2[destino] = [arista_d_o]


    @Slot()
    def click_agregar_final(self):
        id = self.ui.id_spinBox.text()
        origenX = self.ui.origenX_spinBox.value()
        oirgenY = self.ui.origenY_spinBox.value()
        destinoX = self.ui.destinoX_spinBox.value()
        destinoY = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origenX, oirgenY, destinoX, destinoY, velocidad, red, green, blue)

        self.particulas.agregar_final(particula)
        origen = (particula.origen_x, particula.origen_y)
        print(origen)

        destino = (particula.destino_x, particula.destino_y)
        peso = particula.distancia

        arista_o_d = (particula.destino_x, particula.destino_y, peso)
        arista_d_o = (particula.origen_x, particula.origen_y, peso)

        if origen in self.grafo:
            self.grafo[origen].append(arista_o_d)
        else:
            self.grafo[origen] = [arista_o_d]
        if destino in self.grafo:
            self.grafo[destino].append(arista_d_o)
        else:
            self.grafo[destino] = [arista_d_o]
        
        arista_o_d = (particula.destino_x, particula.destino_y)
        arista_d_o = (particula.origen_x, particula.origen_y)

        if origen in self.grafo2:
            self.grafo2[origen].append(arista_o_d)
        else:
            self.grafo2[origen] = [arista_o_d]
        if destino in self.grafo2:
            self.grafo2[destino].append(arista_d_o)
        else:
            self.grafo2[destino] = [arista_d_o]


    
    









