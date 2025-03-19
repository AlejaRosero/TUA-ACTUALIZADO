from PyQt5.QtWidgets import (
    QWidget
)
from ..ui import Ui_Login2


class Sildebar_View(QWidget, Ui_Login2):
    def __init__(self, parent=None):
        super(Sildebar_View, self).__init__(parent)