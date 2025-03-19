from PyQt5.QtWidgets import (
    QWidget
)
from ..ui import Ui_Expediente


class Sildebar_View(QWidget, Ui_Expediente):
    def __init__(self, parent=None):
        super(Sildebar_View, self).__init__(parent)