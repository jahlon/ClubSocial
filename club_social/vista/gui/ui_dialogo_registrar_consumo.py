# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogo_registrar_consumodOBTJE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogRegistrarConsumo(object):
    def setupUi(self, DialogRegistrarConsumo):
        if not DialogRegistrarConsumo.objectName():
            DialogRegistrarConsumo.setObjectName(u"DialogRegistrarConsumo")
        DialogRegistrarConsumo.resize(400, 139)
        self.verticalLayout = QVBoxLayout(DialogRegistrarConsumo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DialogRegistrarConsumo)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineedit_detalle = QLineEdit(self.frame)
        self.lineedit_detalle.setObjectName(u"lineedit_detalle")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineedit_detalle)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineedit_valor = QLineEdit(self.frame)
        self.lineedit_valor.setObjectName(u"lineedit_valor")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineedit_valor)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineedit_autorizado = QLineEdit(self.frame)
        self.lineedit_autorizado.setObjectName(u"lineedit_autorizado")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineedit_autorizado)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(DialogRegistrarConsumo)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogRegistrarConsumo)
        self.buttonBox.accepted.connect(DialogRegistrarConsumo.accept)
        self.buttonBox.rejected.connect(DialogRegistrarConsumo.reject)

        QMetaObject.connectSlotsByName(DialogRegistrarConsumo)
    # setupUi

    def retranslateUi(self, DialogRegistrarConsumo):
        DialogRegistrarConsumo.setWindowTitle(QCoreApplication.translate("DialogRegistrarConsumo", u"Registrar Consumo", None))
        self.label.setText(QCoreApplication.translate("DialogRegistrarConsumo", u"Detalle consumo:", None))
        self.lineedit_detalle.setPlaceholderText(QCoreApplication.translate("DialogRegistrarConsumo", u"Obligatorio", None))
        self.label_2.setText(QCoreApplication.translate("DialogRegistrarConsumo", u"Valor:", None))
        self.lineedit_valor.setPlaceholderText(QCoreApplication.translate("DialogRegistrarConsumo", u"Obligatorio", None))
        self.label_3.setText(QCoreApplication.translate("DialogRegistrarConsumo", u"Autorizado:", None))
#if QT_CONFIG(whatsthis)
        self.lineedit_autorizado.setWhatsThis(QCoreApplication.translate("DialogRegistrarConsumo", u"<html><head/><body><p><span style=\" font-weight:600;\">Este campo es opcional.</span></p><p>Se refiere al nombre del autorizado que realiz\u00f3 el consumo cuando este no fue hecho por el socio.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineedit_autorizado.setPlaceholderText(QCoreApplication.translate("DialogRegistrarConsumo", u"Opcional", None))
    # retranslateUi

