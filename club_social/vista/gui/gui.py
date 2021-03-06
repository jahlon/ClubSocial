import sys

from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator, QIntValidator, QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QInputDialog

from club_social.mundo.errores import SocioExistenteError, SocioNoExistenteError
from club_social.mundo.mundo import Club
from club_social.vista.gui.ui_dialogo_afiliar_socio import Ui_DialogAfiliarSocio
from club_social.vista.gui.ui_dialogo_registrar_consumo import Ui_DialogRegistrarConsumo
from club_social.vista.gui.ui_main_window_club_social import Ui_MainWindow


class VentanaClubSocial(QMainWindow):

    ARCHIVO = "datos.club"

    def __init__(self, club: Club):
        QMainWindow.__init__(self)
        self.club = club
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.club.cargar(VentanaClubSocial.ARCHIVO)
        self._configurar()
        self.setFixedSize(1028, 600)
        self.show()

    def _configurar(self):
        self.ui.pbutton_afiliar_socio.clicked.connect(self.abrir_dialogo_afiliar_socio)
        self.ui.pbutton_registrar_consumo.clicked.connect(self.abrir_dialogo_registrar_consumo)
        self.ui.pbutton_agregar_autorizado.clicked.connect(self.agregar_autorizado)
        self.ui.pbutton_pagar_factura.clicked.connect(self.pagar_factura)

        self.ui.listview_socios.selectionChanged = self.seleccionar_socio

        self.ui.listview_socios.setModel(QStandardItemModel())
        self.ui.listview_facturas.setModel(QStandardItemModel())
        # sel_model = self.ui.listview_socios.selectionModel()
        # sel_model.selectionChanged.connect(self.seleccionar_socio)

        self.closeEvent = self.cerrar_ventana

        for socio in self.club.socios.values():
            self.actualizar_lista_socios(socio)

    def cerrar_ventana(self, event):
        self.club.guardar(VentanaClubSocial.ARCHIVO)

    def pagar_factura(self):
        indexes_facturas = self.ui.listview_facturas.selectedIndexes()
        if len(indexes_facturas) == 0:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe seleccionar una factura para pagar")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
        else:
            item_factura = self.ui.listview_facturas.model().itemFromIndex(indexes_facturas[0])
            indexes_socios = self.ui.listview_socios.selectedIndexes()
            item_socio = self.ui.listview_socios.model().itemFromIndex(indexes_socios[0])
            factura = item_factura.factura
            cedula_socio = item_socio.socio.cedula

            try:
                self.club.pagar_factura(cedula_socio, factura)
            except SocioNoExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error pagando factura")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                self.actualizar_lista_de_facturas()

    def agregar_autorizado(self):
        indexes = self.ui.listview_socios.selectedIndexes()
        if len(indexes) == 0:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe seleccionar un socio para agregarle un autorizado")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
        else:
            resp = QInputDialog.getText(self, "Agregar autorizado", "Nombre del autorizado:")
            if resp[1]:
                item = self.ui.listview_socios.model().itemFromIndex(indexes[0])
                cedula_socio = item.socio.cedula
                nombre_autorizado = resp[0]

                try:
                    self.club.registrar_autorizado_por_socio(cedula_socio, nombre_autorizado)
                except SocioNoExistenteError as err:
                    msg_box = QMessageBox(self)
                    msg_box.setWindowTitle("Error agregando autorizado")
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setText(err.msg)
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.exec_()
                else:
                    self.actualizar_lista_autorizados()


    def abrir_dialogo_afiliar_socio(self):
        dialogo = DialogoAfiliarSocio(self)
        resp = dialogo.exec_()
        if resp == QDialog.Accepted:
            cedula = dialogo.ui.lineedit_cedula.text()
            nombre = dialogo.ui.lineedit_nombre.text()

            try:
                socio = self.club.afiliar_socio_al_club(cedula, nombre)
            except SocioExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error afiliando socio")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                self.actualizar_lista_socios(socio)

    def actualizar_lista_socios(self, socio):
        item = QStandardItem(str(socio))
        item.setEditable(False)
        item.socio = socio
        self.ui.listview_socios.model().appendRow(item)

    def abrir_dialogo_registrar_consumo(self):
        indexes = self.ui.listview_socios.selectedIndexes()
        if len(indexes) == 0:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe seleccionar un socio para registrarle el consumo")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
        else:
            dialogo = DialogoRegistrarConsumo(self)
            resp = dialogo.exec_()
            if resp == QDialog.Accepted:
                item = self.ui.listview_socios.model().itemFromIndex(indexes[0])

                cedula = item.socio.cedula
                concepto = dialogo.ui.lineedit_detalle.text()
                valor = float(dialogo.ui.lineedit_valor.text())
                autorizado = dialogo.ui.lineedit_autorizado.text()

                try:
                    self.club.registrar_consumo_a_socio(cedula, concepto, valor, autorizado)
                except SocioNoExistenteError as err:
                    msg_box = QMessageBox(self)
                    msg_box.setWindowTitle("Error registrando consumo")
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setText(err.msg)
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.exec_()
                else:
                    self.actualizar_lista_de_facturas()

    def seleccionar_socio(self, selected, deselected):
        indexes = selected.indexes()
        if len(indexes) > 0:
            item = self.ui.listview_socios.model().itemFromIndex(indexes[0])

            self.actualizar_datos_socio(item.socio)
            self.actualizar_lista_de_facturas()
            self.actualizar_lista_autorizados()

    def actualizar_datos_socio(self, socio):
        self.ui.lineedit_cedula.setText(socio.cedula)
        self.ui.lineedit_nombre.setText(socio.nombre)

    def actualizar_lista_de_facturas(self):
        self.ui.listview_facturas.model().clear()
        indexes = self.ui.listview_socios.selectedIndexes()
        item = self.ui.listview_socios.model().itemFromIndex(indexes[0])

        for factura in item.socio.facturas:
            item = QStandardItem(str(factura))
            item.setEditable(False)
            item.factura = factura
            self.ui.listview_facturas.model().appendRow(item)

    def actualizar_lista_autorizados(self):
        self.ui.listwidget_autorizados.clear()
        indexes = self.ui.listview_socios.selectedIndexes()
        item = self.ui.listview_socios.model().itemFromIndex(indexes[0])

        for autorizado in item.socio.autorizados:
            self.ui.listwidget_autorizados.addItem(autorizado)


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
            msg_box.setWindowTitle("Error de validaci??n")
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

    def accept(self) -> None:
        if self.ui.lineedit_detalle.text() != "" and self.ui.lineedit_valor.text() != "":
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validaci??n")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()