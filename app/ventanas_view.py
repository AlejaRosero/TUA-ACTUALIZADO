from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QStackedWidget,
)
from PyQt5.QtGui import QIcon
from app.view import (
    Sildebar_View,
    Usuarios_View,
    Expediente_View,
)


class MainApp(QWidget):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)

        # Configurar la ventana principal
        self.setWindowTitle("Systock")
        self.setWindowIcon(QIcon("assets/logo1.ico"))
        self.resize(800, 600)

        self.setStyleSheet("background-color: white;")

        # Widget central que contiene el diseño principal
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0) 
        layout.setSpacing(0)

        # Crear el Navbar
        self.navbar = Sildebar_View()
        layout.addWidget(self.navbar)  

        self.stacked_widget = QStackedWidget()
        layout.addWidget(
            self.stacked_widget
        ) 

        self.usuarios = Usuarios_View()
        self.expediente = Expediente_View()
        

        self.stacked_widget.addWidget(self.usuarios) 
        self.stacked_widget.addWidget(self.expediente)  
        
        
        self.navbar.pushButton_4.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.expediente)
        )
        
        # este boton es de reportes, pero lo puse a usuarios para ver su funcionalidad
        self.navbar.pushButton_3.clicked.connect( 
            lambda: self.stacked_widget.setCurrentWidget(self.usuarios)
        )


