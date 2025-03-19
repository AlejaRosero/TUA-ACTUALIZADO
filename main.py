from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QStackedWidget,
    QHBoxLayout,
    QWidget,
)
import sys
from app.ventanas_view import MainApp
from app.view import Login2_View

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        layout = QHBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)  # Sin márgenes
        layout.setSpacing(0)
        
        self.stacked_widget = QStackedWidget()
        layout.addWidget(self.stacked_widget)

        self.MainApp = MainApp()
        # self.Login = Login2_View()

        self.stacked_widget.addWidget(self.Login)
        self.stacked_widget.addWidget(self.MainApp)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())