import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, \
    QApplication


class Ventana1(QMainWindow):

    # Hacer el metodo de construccion de la ventana:
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # poner el titulo
        self.setWindowTitle("Formulario de registro")

        # Poner el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/north face.jpeg'))

        self.ancho = 900
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.imagenfondo = QPixmap('imagenes/punta cana.jpg')
        self.fondo.setPixmap(self.imagenfondo)
        self.fondo.setScaledContents(True)

        # hacemos que se adapte el tamaño de la imagen
        self.resize(self.imagenfondo.width(), self.imagenfondo.height())

        self.setCentralWidget(self.fondo)

        # distribucion layaout horizontal
        self.horizontal = QHBoxLayout()

        # margenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)



if __name__ == '__main__':

    # Hacer que la aplicación se genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo Ventana1 con el nombre de ventana1
    ventana1 = Ventana1()
    # Hacer que el objeto ventana 1 se vea
    ventana1.show()

    sys.exit(app.exec_())






