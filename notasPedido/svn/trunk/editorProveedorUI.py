# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editorProveedor.ui'
#
# Created: Sun Sep 27 21:34:59 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_editorProveedor(object):
    def setupUi(self, editorProveedor):
        editorProveedor.setObjectName("editorProveedor")
        editorProveedor.resize(601, 701)
        self.verticalLayout_2 = QtGui.QVBoxLayout(editorProveedor)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(editorProveedor)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.nombre = QtGui.QLineEdit(editorProveedor)
        self.nombre.setObjectName("nombre")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.nombre)
        self.label_2 = QtGui.QLabel(editorProveedor)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.razonSocial = QtGui.QLineEdit(editorProveedor)
        self.razonSocial.setObjectName("razonSocial")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.razonSocial)
        self.label_3 = QtGui.QLabel(editorProveedor)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.cuit = QtGui.QLineEdit(editorProveedor)
        self.cuit.setObjectName("cuit")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cuit)
        self.telefono = QtGui.QLineEdit(editorProveedor)
        self.telefono.setObjectName("telefono")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.telefono)
        self.label_5 = QtGui.QLabel(editorProveedor)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_10 = QtGui.QLabel(editorProveedor)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_10)
        self.fax = QtGui.QLineEdit(editorProveedor)
        self.fax.setObjectName("fax")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.fax)
        self.horizontalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtGui.QLabel(editorProveedor)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.email = QtGui.QLineEdit(editorProveedor)
        self.email.setObjectName("email")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.email)
        self.direccion = QtGui.QTextEdit(editorProveedor)
        self.direccion.setObjectName("direccion")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.direccion)
        self.label_6 = QtGui.QLabel(editorProveedor)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_11 = QtGui.QLabel(editorProveedor)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_11)
        self.web = QtGui.QLineEdit(editorProveedor)
        self.web.setObjectName("web")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.web)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtGui.QGroupBox(editorProveedor)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listaVend = QtGui.QTreeWidget(self.groupBox_2)
        self.listaVend.setObjectName("listaVend")
        self.listaVend.headerItem().setText(0, "1")
        self.verticalLayout_3.addWidget(self.listaVend)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.telefonoVend = QtGui.QLineEdit(self.groupBox_2)
        self.telefonoVend.setObjectName("telefonoVend")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.telefonoVend)
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_8)
        self.mailVend = QtGui.QLineEdit(self.groupBox_2)
        self.mailVend.setObjectName("mailVend")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.mailVend)
        self.nombreVend = QtGui.QLineEdit(self.groupBox_2)
        self.nombreVend.setObjectName("nombreVend")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.nombreVend)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.quitarVend = QtGui.QPushButton(self.groupBox_2)
        self.quitarVend.setObjectName("quitarVend")
        self.verticalLayout_3.addWidget(self.quitarVend)
        self.agregarVend = QtGui.QPushButton(self.groupBox_2)
        self.agregarVend.setObjectName("agregarVend")
        self.verticalLayout_3.addWidget(self.agregarVend)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(editorProveedor)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listaPago = QtGui.QListWidget(self.groupBox)
        self.listaPago.setObjectName("listaPago")
        self.verticalLayout.addWidget(self.listaPago)
        self.formasPago = QtGui.QComboBox(self.groupBox)
        self.formasPago.setObjectName("formasPago")
        self.verticalLayout.addWidget(self.formasPago)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.agregarForma = QtGui.QPushButton(self.groupBox)
        self.agregarForma.setObjectName("agregarForma")
        self.horizontalLayout_3.addWidget(self.agregarForma)
        self.quitarForma = QtGui.QPushButton(self.groupBox)
        self.quitarForma.setObjectName("quitarForma")
        self.horizontalLayout_3.addWidget(self.quitarForma)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(editorProveedor)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.label.setBuddy(self.nombre)
        self.label_2.setBuddy(self.razonSocial)
        self.label_3.setBuddy(self.cuit)
        self.label_5.setBuddy(self.telefono)
        self.label_10.setBuddy(self.fax)
        self.label_4.setBuddy(self.email)
        self.label_6.setBuddy(self.direccion)
        self.label_11.setBuddy(self.web)
        self.label_9.setBuddy(self.telefonoVend)
        self.label_8.setBuddy(self.mailVend)
        self.label_7.setBuddy(self.nombreVend)

        self.retranslateUi(editorProveedor)
        QtCore.QMetaObject.connectSlotsByName(editorProveedor)

    def retranslateUi(self, editorProveedor):
        editorProveedor.setWindowTitle(QtGui.QApplication.translate("editorProveedor", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("editorProveedor", "&Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("editorProveedor", "&Razón Social", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("editorProveedor", "&CUIT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("editorProveedor", "&Teléfono", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("editorProveedor", "&Fax:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("editorProveedor", "&Email", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("editorProveedor", "&Dirección", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("editorProveedor", "&Web", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("editorProveedor", "Vendedores", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("editorProveedor", "&Teléfono", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("editorProveedor", "&Email", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("editorProveedor", "&Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.quitarVend.setText(QtGui.QApplication.translate("editorProveedor", "&Quitar", None, QtGui.QApplication.UnicodeUTF8))
        self.agregarVend.setText(QtGui.QApplication.translate("editorProveedor", "&Añadir", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("editorProveedor", "Formas de Pago", None, QtGui.QApplication.UnicodeUTF8))
        self.agregarForma.setText(QtGui.QApplication.translate("editorProveedor", "&Añadir", None, QtGui.QApplication.UnicodeUTF8))
        self.quitarForma.setText(QtGui.QApplication.translate("editorProveedor", "&Quitar", None, QtGui.QApplication.UnicodeUTF8))

