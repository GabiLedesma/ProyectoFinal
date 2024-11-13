import serial
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, QTime


from ui_interfaz_visual import Ui_MainWindow

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.ui = Ui_MainWindow()
        


        self.setWindowTitle("Recordatorio de Pastillas")
        self.setGeometry(100, 100, 400, 300)

        # Crear el layout principal
        layout = QVBoxLayout()

        # Calendario para seleccionar el día
        self.calendar = QCalendarWidget(self)
        layout.addWidget(self.calendar)

        # Selector de hora
        self.timeEdit = QTimeEdit(self)
        self.timeEdit.setTime(QTime.currentTime())  # Valor por defecto
        layout.addWidget(self.timeEdit)

        # ComboBox para elegir el tipo de pastilla
        self.comboPastilla = QComboBox(self)
        self.comboPastilla.addItem("Pastilla A")
        self.comboPastilla.addItem("Pastilla B")
        self.comboPastilla.addItem("Pastilla C")
        layout.addWidget(self.comboPastilla)

        # Botón para enviar los datos
        self.sendButton = QPushButton("Enviar", self)
        self.sendButton.clicked.connect(self.send_data)
        layout.addWidget(self.sendButton)

        # Crear un widget central y asignar el layout
        centralWidget = QWidget(self)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def abrir_nueva_pestana(self):
        # Crear una nueva pestaña (Tab) en un QTabWidget, por ejemplo
        tab_widget = self.findChild(QTabWidget, 'tabWidget')  # Asegúrate de que el QTabWidget tenga este nombre en el UI
        if tab_widget:
            nueva_pestana = QWidget()
            nueva_layout = QVBoxLayout()
            nueva_layout.addWidget(QLabel("Contenido de la nueva pestaña"))
            nueva_pestana.setLayout(nueva_layout)
            tab_widget.addTab(nueva_pestana, "Nueva Pestaña")

    def send_data(self):
        # Obtener los datos seleccionados
        selected_day = self.calendar.selectedDate().toString("yyyy-MM-dd")
        selected_time = self.timeEdit.time().toString("HH:mm")
        selected_pastilla = self.comboPastilla.currentText()

        # Crear el mensaje para enviar
        message = f"{selected_day},{selected_time},{selected_pastilla}\n"

        # Enviar los datos al Arduino
        if self.ser.isOpen():
            self.ser.write(message.encode())  # Enviar el mensaje codificado en bytes
            print(f"Datos enviados: {message}")
        else:
            print("Error: No se puede conectar al puerto serial.")
 


if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show()
    sys.exit(app.exec_())