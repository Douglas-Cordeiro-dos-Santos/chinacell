from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Estoque(object):
    def setupUi(self, Estoque):
        Estoque.setObjectName("Estoque")
        Estoque.resize(843, 600)
        self.centralwidget = QtWidgets.QWidget(parent=Estoque)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_6 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_6.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"border-radius: 10px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.splitter = QtWidgets.QSplitter(parent=self.frame_6)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.Button_4_sair = QtWidgets.QPushButton(parent=self.splitter)
        self.Button_4_sair.setMinimumSize(QtCore.QSize(0, 25))
        self.Button_4_sair.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_4_sair.setFont(font)
        self.Button_4_sair.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_4_sair.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 127);\n"
"border: 2px solid;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 0, 0);\n"
"border: 2px solid;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.Button_4_sair.setObjectName("Button_4_sair")
        self.horizontalLayout_2.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.frame_6)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_3.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-radius: 10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Button_pesquisa = QtWidgets.QPushButton(parent=self.frame_3)
        self.Button_pesquisa.setMinimumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_pesquisa.setFont(font)
        self.Button_pesquisa.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(0, 255, 0);\n"
"    \n"
"}\n"
"")
        self.Button_pesquisa.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/imagens/lupa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_pesquisa.setIcon(icon)
        self.Button_pesquisa.setIconSize(QtCore.QSize(25, 30))
        self.Button_pesquisa.setObjectName("Button_pesquisa")
        self.horizontalLayout_7.addWidget(self.Button_pesquisa)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit_pesquisa = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_pesquisa.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_pesquisa.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_pesquisa.setCursorPosition(0)
        self.lineEdit_pesquisa.setObjectName("lineEdit_pesquisa")
        self.horizontalLayout_8.addWidget(self.lineEdit_pesquisa)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(139, 29, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.Button_2_novo = QtWidgets.QPushButton(parent=self.frame_3)
        self.Button_2_novo.setMinimumSize(QtCore.QSize(100, 25))
        self.Button_2_novo.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Button_2_novo.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 0, 255);\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"")
        self.Button_2_novo.setObjectName("Button_2_novo")
        self.horizontalLayout_7.addWidget(self.Button_2_novo)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.frame_2)
        self.tabWidget.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.treeWidget = QtWidgets.QTreeWidget(parent=self.tab)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_3.addWidget(self.treeWidget)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-radius: 10px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.Button_3_visualizar = QtWidgets.QPushButton(parent=self.frame_4)
        self.Button_3_visualizar.setMinimumSize(QtCore.QSize(100, 25))
        self.Button_3_visualizar.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Button_3_visualizar.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"")
        self.Button_3_visualizar.setObjectName("Button_3_visualizar")
        self.horizontalLayout_4.addWidget(self.Button_3_visualizar)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame_2)
        Estoque.setCentralWidget(self.centralwidget)

        self.retranslateUi(Estoque)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Estoque)

    def retranslateUi(self, Estoque):
        _translate = QtCore.QCoreApplication.translate
        Estoque.setWindowTitle(_translate("Estoque", "MainWindow"))
        self.label_2.setText(_translate("Estoque", "          ESTOQUE"))
        self.Button_4_sair.setText(_translate("Estoque", "Sair"))
        self.Button_2_novo.setText(_translate("Estoque", "NOVO"))
        self.treeWidget.headerItem().setText(0, _translate("Estoque", "ID"))
        self.treeWidget.headerItem().setText(1, _translate("Estoque", "Produto"))
        self.treeWidget.headerItem().setText(2, _translate("Estoque", "Qtde"))
        self.treeWidget.headerItem().setText(3, _translate("Estoque", "Categoria"))
        self.treeWidget.headerItem().setText(4, _translate("Estoque", "Preço uni"))
        self.treeWidget.headerItem().setText(5, _translate("Estoque", "Preço total"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Estoque", "Tab 1"))
        self.Button_3_visualizar.setText(_translate("Estoque", "VISUALIZAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Estoque = QtWidgets.QMainWindow()
    ui = Ui_Estoque()
    ui.setupUi(Estoque)
    Estoque.show()
    sys.exit(app.exec())
