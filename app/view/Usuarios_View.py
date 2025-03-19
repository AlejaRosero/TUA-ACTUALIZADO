from PyQt5.QtWidgets import (
    QWidget
)
from ..ui import Ui_Usuarios


class Sildebar_View(QWidget, Ui_Usuarios):
    def __init__(self, parent=None):
        super(Sildebar_View, self).__init__(parent)