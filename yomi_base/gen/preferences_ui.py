# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/preferences.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogPreferences(object):
    def setupUi(self, DialogPreferences):
        DialogPreferences.setObjectName(_fromUtf8("DialogPreferences"))
        DialogPreferences.resize(600, 323)
        self.verticalLayout = QtGui.QVBoxLayout(DialogPreferences)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(DialogPreferences)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabGeneral = QtGui.QWidget()
        self.tabGeneral.setObjectName(_fromUtf8("tabGeneral"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabGeneral)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.checkLoadRecentFile = QtGui.QCheckBox(self.tabGeneral)
        self.checkLoadRecentFile.setObjectName(_fromUtf8("checkLoadRecentFile"))
        self.verticalLayout_4.addWidget(self.checkLoadRecentFile)
        self.checkStripReadings = QtGui.QCheckBox(self.tabGeneral)
        self.checkStripReadings.setObjectName(_fromUtf8("checkStripReadings"))
        self.verticalLayout_4.addWidget(self.checkStripReadings)
        self.checkRememberTextContent = QtGui.QCheckBox(self.tabGeneral)
        self.checkRememberTextContent.setObjectName(_fromUtf8("checkRememberTextContent"))
        self.verticalLayout_4.addWidget(self.checkRememberTextContent)
        self.checkCheckForUpdates = QtGui.QCheckBox(self.tabGeneral)
        self.checkCheckForUpdates.setObjectName(_fromUtf8("checkCheckForUpdates"))
        self.verticalLayout_4.addWidget(self.checkCheckForUpdates)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_14 = QtGui.QLabel(self.tabGeneral)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_14)
        self.spinScanLength = QtGui.QSpinBox(self.tabGeneral)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinScanLength.sizePolicy().hasHeightForWidth())
        self.spinScanLength.setSizePolicy(sizePolicy)
        self.spinScanLength.setMinimum(1)
        self.spinScanLength.setObjectName(_fromUtf8("spinScanLength"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinScanLength)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.tabWidget.addTab(self.tabGeneral, _fromUtf8(""))
        self.tabAppearance = QtGui.QWidget()
        self.tabAppearance.setObjectName(_fromUtf8("tabAppearance"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabAppearance)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboFontFamily = QtGui.QFontComboBox(self.tabAppearance)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboFontFamily.sizePolicy().hasHeightForWidth())
        self.comboFontFamily.setSizePolicy(sizePolicy)
        self.comboFontFamily.setObjectName(_fromUtf8("comboFontFamily"))
        self.horizontalLayout.addWidget(self.comboFontFamily)
        self.spinFontSize = QtGui.QSpinBox(self.tabAppearance)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinFontSize.sizePolicy().hasHeightForWidth())
        self.spinFontSize.setSizePolicy(sizePolicy)
        self.spinFontSize.setMinimum(1)
        self.spinFontSize.setMaximum(72)
        self.spinFontSize.setProperty("value", 12)
        self.spinFontSize.setObjectName(_fromUtf8("spinFontSize"))
        self.horizontalLayout.addWidget(self.spinFontSize)
        self.buttonColorFg = QtGui.QPushButton(self.tabAppearance)
        self.buttonColorFg.setObjectName(_fromUtf8("buttonColorFg"))
        self.horizontalLayout.addWidget(self.buttonColorFg)
        self.buttonColorBg = QtGui.QPushButton(self.tabAppearance)
        self.buttonColorBg.setObjectName(_fromUtf8("buttonColorBg"))
        self.horizontalLayout.addWidget(self.buttonColorBg)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.textSample = QtGui.QPlainTextEdit(self.tabAppearance)
        self.textSample.setObjectName(_fromUtf8("textSample"))
        self.verticalLayout_3.addWidget(self.textSample)
        self.checkAllowEditing = QtGui.QCheckBox(self.tabAppearance)
        self.checkAllowEditing.setObjectName(_fromUtf8("checkAllowEditing"))
        self.verticalLayout_3.addWidget(self.checkAllowEditing)
        self.tabWidget.addTab(self.tabAppearance, _fromUtf8(""))
        self.tabAnki = QtGui.QWidget()
        self.tabAnki.setEnabled(False)
        self.tabAnki.setObjectName(_fromUtf8("tabAnki"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabAnki)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.tabAnki)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.radioButtonVocab = QtGui.QRadioButton(self.tabAnki)
        self.radioButtonVocab.setChecked(True)
        self.radioButtonVocab.setObjectName(_fromUtf8("radioButtonVocab"))
        self.horizontalLayout_2.addWidget(self.radioButtonVocab)
        self.radioButtonKanji = QtGui.QRadioButton(self.tabAnki)
        self.radioButtonKanji.setObjectName(_fromUtf8("radioButtonKanji"))
        self.horizontalLayout_2.addWidget(self.radioButtonKanji)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_13 = QtGui.QLabel(self.tabAnki)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_3.addWidget(self.label_13)
        self.comboBoxDeck = QtGui.QComboBox(self.tabAnki)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxDeck.sizePolicy().hasHeightForWidth())
        self.comboBoxDeck.setSizePolicy(sizePolicy)
        self.comboBoxDeck.setObjectName(_fromUtf8("comboBoxDeck"))
        self.horizontalLayout_3.addWidget(self.comboBoxDeck)
        self.label_12 = QtGui.QLabel(self.tabAnki)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_3.addWidget(self.label_12)
        self.comboBoxModel = QtGui.QComboBox(self.tabAnki)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxModel.sizePolicy().hasHeightForWidth())
        self.comboBoxModel.setSizePolicy(sizePolicy)
        self.comboBoxModel.setObjectName(_fromUtf8("comboBoxModel"))
        self.horizontalLayout_3.addWidget(self.comboBoxModel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_11 = QtGui.QLabel(self.tabAnki)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_2.addWidget(self.label_11)
        self.tableFields = QtGui.QTableWidget(self.tabAnki)
        self.tableFields.setObjectName(_fromUtf8("tableFields"))
        self.tableFields.setColumnCount(2)
        self.tableFields.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableFields.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableFields.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.tableFields)
        self.labelTags = QtGui.QLabel(self.tabAnki)
        self.labelTags.setText(_fromUtf8(""))
        self.labelTags.setObjectName(_fromUtf8("labelTags"))
        self.verticalLayout_2.addWidget(self.labelTags)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.checkEnableAnkiConnect = QtGui.QCheckBox(self.tabAnki)
        self.checkEnableAnkiConnect.setObjectName(_fromUtf8("checkEnableAnkiConnect"))
        self.horizontalLayout_4.addWidget(self.checkEnableAnkiConnect)
        self.label_3 = QtGui.QLabel(self.tabAnki)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tabAnki, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(DialogPreferences)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogPreferences)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogPreferences.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogPreferences.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogPreferences)

    def retranslateUi(self, DialogPreferences):
        DialogPreferences.setWindowTitle(_translate("DialogPreferences", "Preferences", None))
        self.checkLoadRecentFile.setText(_translate("DialogPreferences", "Load most recent file", None))
        self.checkStripReadings.setText(_translate("DialogPreferences", "Strip readings from files", None))
        self.checkRememberTextContent.setText(_translate("DialogPreferences", "Remember text content", None))
        self.checkCheckForUpdates.setText(_translate("DialogPreferences", "Check for updates", None))
        self.label_14.setText(_translate("DialogPreferences", "Text scan length", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneral), _translate("DialogPreferences", "General", None))
        self.buttonColorFg.setText(_translate("DialogPreferences", "Foreground...", None))
        self.buttonColorBg.setText(_translate("DialogPreferences", "Background...", None))
        self.textSample.setPlainText(_translate("DialogPreferences", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam accumsan nisi a leo faucibus ut varius velit fringilla. Cras hendrerit eleifend porttitor. Quisque eu elit quis tellus hendrerit ornare et ac tellus. Nunc id felis ut sapien blandit viverra vel ac est. Ut erat lorem, rutrum at scelerisque sollicitudin, lacinia quis diam. Suspendisse potenti. Integer id justo ac ligula aliquet mattis. Etiam malesuada faucibus risus, vel hendrerit elit consectetur quis. Etiam consectetur ipsum ut odio feugiat suscipit. Etiam a tellus metus. ", None))
        self.checkAllowEditing.setText(_translate("DialogPreferences", "Allow editing", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAppearance), _translate("DialogPreferences", "Appearance", None))
        self.label.setText(_translate("DialogPreferences", "Displayed profile", None))
        self.radioButtonVocab.setText(_translate("DialogPreferences", "Vocabulary", None))
        self.radioButtonKanji.setText(_translate("DialogPreferences", "Kanji", None))
        self.label_13.setText(_translate("DialogPreferences", "Deck", None))
        self.label_12.setText(_translate("DialogPreferences", "Model", None))
        self.label_11.setText(_translate("DialogPreferences", "Specify how your model fields are populated when adding facts", None))
        item = self.tableFields.horizontalHeaderItem(0)
        item.setText(_translate("DialogPreferences", "Field", None))
        item = self.tableFields.horizontalHeaderItem(1)
        item.setText(_translate("DialogPreferences", "Value", None))
        self.checkEnableAnkiConnect.setText(_translate("DialogPreferences", "Enable AnkiConnect", None))
        self.label_3.setText(_translate("DialogPreferences", "(see the <a href=\"https://foosoft.net/projects/yomichan-chrome\">extension page</a> for details)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAnki), _translate("DialogPreferences", "Anki", None))

import resources_rc
