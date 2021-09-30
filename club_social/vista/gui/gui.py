import sys

from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator, QIntValidator
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox

from club_social.vista.gui.ui_dialogo_afiliar_socio import Ui_DialogAfiliarSocio
from club_social.vista.gui.ui_dialogo_registrar_consumo import Ui_DialogRegistrarConsumo
from club_social.vista.gui.ui_main_window_club_social import Ui_MainWindow


class VentanaClubSocial(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._configurar()
        self.setFixedSize(1028, 600)
        self.show()

    def _configurar(self):
        self.ui.pbutton_afiliar_socio.clicked.connect(self.abrir_dialogo_afiliar_socio)
        self.ui.pbutton_registrar_consumo.clicked.connect(self.abrir_dialogo_registrar_consumo)

    def abrir_dialogo_afiliar_socio(self):
        dialogo = DialogoAfiliarSocio(self)
        resp = dialogo.exec_()
        if resp == QDialog.Accepted:
            cedula = dialogo.ui.lineedit_cedula.text()
            nombre = dialogo.ui.lineedit_nombre.text()

    def abrir_dialogo_registrar_consumo(self):
        dialogo = DialogoRegistrarConsumo(self)
        resp = dialogo.exec_()

class DialogoAfiliarSocio(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_DialogAfiliarSocio()
        self.ui.setupUi(self)

        validador = QRegExpValidator(QRegExp('\\d{12}'))
        self.ui.lineedit_cedula.setValidator(validador)

    def accept(self) -> None:
        if self.ui.lineedit_cedula.text() != "" and self.ui.lineedit_nombre.text() != "":
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()



class DialogoRegistrarConsumo(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_DialogRegistrarConsumo()
        self.ui.setupUi(self)

        validador = QIntValidator(0, 100000000)
        self.ui.lineedit_valor.setValidator(validador)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaClubSocial()
    sys.exit(app.exec_())