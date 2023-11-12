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

        # --------LAYOUT IZQUIERDO-----------

        self.ladoIzquierdo = QFormLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Información del cliente")
        self.letrero1.setFont(QFont("Andale Mono", 20))
        self.letrero1.setStyleSheet("color: #000080;")

        self.ladoIzquierdo.addRow(self.letrero1)

        self.letrero2 = QLabel()
        self.letrero2.setFixedWidth(340)
        self.letrero2.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        self.letrero2.setFont(QFont("Andale Mono", 9))
        self.letrero2.setStyleSheet("color: #000080; margin-bottom: 40px;"
                                    "margin top: 20px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        self.ladoIzquierdo.addRow(self.letrero2)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Ususario*", self.usuario)

        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Password*", self.password)

        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Password*", self.password2)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Documento*", self.documento)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Correo*", self.correo)

        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedWidth(90)
        self.botonRegistrar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(90)
        self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        self.horizontal.addLayout(self.ladoIzquierdo)

        # ---------- FINAL---------
        # el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)

    def accion_botonLimpiar(self):
        pass

    def accion_botonRegistrar(self):
        pass


if __name__ == '__main__':

    # Hacer que la aplicación se genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo Ventana1 con el nombre de ventana1
    ventana1 = Ventana1()
    # Hacer que el objeto ventana 1 se vea
    ventana1.show()

    sys.exit(app.exec_())






