from PyQt5 import QtWidgets

class Modal(QtWidgets.QWidget):
    def __init__(self, name: str)->None:
        super().__init__()
        """
        name содержит текст ошибки
        """
        self.name=name
        self.modal=QtWidgets.QLabel(self)
        self.modal.resize(400, 200)
        self.modal.raise_()
        self.modal.setText(str(self.name))