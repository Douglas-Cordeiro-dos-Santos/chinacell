from PyQt6.QtWidgets import *
from PyQt6 import QtWidgets

from login import Ui_Login
from senha import Ui_Redefinir
from estoque import Ui_Estoque
from verprod import Ui_Ver_produto
from cadastropdt import Ui_Cadastro_pdt

import sys
import mysql.connector

# CONEXÃO SQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="chinacell"
)

# TELA DE LOGIN
class Log(QMainWindow, Ui_Login):
    def __init__(self) -> None:
        super(Log, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("CHINACELL - LOGIN")

        self.Button_login.clicked.connect(self.abrir_sistema)
        self.Button_3_redefinir.clicked.connect(self.abrir_redfsenha)
        self.Button_2_sair.clicked.connect(self.sair_do_programa)
        self.checkBox_mostrasenha.stateChanged.connect(self.mostrar_senha)

    def mostrar_senha(self):
            if self.checkBox_mostrasenha.isChecked():
                self.lineEdit_2_senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            else:
                self.lineEdit_2_senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def sair_do_programa(self):
        self.close()  

    def abrir_sistema(self):
        login = self.lineEdit_usuario.text()
        senha = self.lineEdit_2_senha.text()

        cursor = conexao.cursor()
        cursor.clear_attributes()       
        
        comando = 'SELECT senha FROM usuarios WHERE nome = %s'
        cursor.execute(comando, (login,))
        leitura_banco = cursor.fetchone()
        
        if leitura_banco is not None:
            senha_correta = leitura_banco[0]
            if senha == senha_correta:
                self.w = MainWindow()
                self.w.showMaximized()
                self.close()
            else:
                QMessageBox.warning(self, "Falha no login", "Senha incorreta")
        else:
            QMessageBox.warning(self, "Falha no login", "Usuário não encontrado")
        
    def abrir_redfsenha(self):
        if self.Button_3_redefinir.clicked:
            self.w = RedfMainWindow()
            self.w.showMaximized()
            self.close()

# TELA DE ESTOQUE
class MainWindow(QMainWindow, Ui_Estoque):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Gerenciamento")

        self.Button_pesquisa.clicked.connect(self.pesquisar)
        self.Button_2_novo.clicked.connect(self.cadastrar)
        self.Button_4_sair.clicked.connect(self.sair)
        self.Button_3_visualizar.clicked.connect(self.visualizar)

        self.puxar_tabela()
        
    def visualizar(self):
        item = self.treeWidget.currentItem()
        if item:
            produto_id = item.text(0)
            self.w = VerpdtMainWindow(produto_id)
            self.w.showMaximized()
            self.close()

    def pesquisar(self):
        if self.Button_pesquisa.clicked:
            produto = self.lineEdit_pesquisa.text()

            cursor = conexao.cursor()
            cursor.clear_attributes()   
            comando = 'SELECT * FROM estoque WHERE produto LIKE %s;'
            cursor.execute(comando, (produto,))
            leitura_banco = cursor.fetchall()

            self.treeWidget.clear()
            for row in leitura_banco:
                QTreeWidgetItem(self.treeWidget, [str(item) for item in row])

    def cadastrar(self):
        if self.Button_2_novo.clicked:
            self.w = CadastroMainWindow()
            self.w.showMaximized()
            self.close()    

    def sair(self):
        if self.Button_4_sair.clicked:
            self.w = Log()
            self.w.showMaximized()
            self.close()    

    def puxar_tabela(self):
        cursor = conexao.cursor()
        comando = 'SELECT * FROM estoque'
        cursor.execute(comando)
        leitura_banco = cursor.fetchall()

        self.treeWidget.clear()
        for row in leitura_banco:
            QTreeWidgetItem(self.treeWidget, [str(item) for item in row])


# REDEFINIR SENHA
class RedfMainWindow(QMainWindow, Ui_Redefinir):
    def __init__(self):
        super(RedfMainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Redefinir senha")

        self.Button_2_voltar.clicked.connect(self.voltar_Login)
        self.Button_salvar.clicked.connect(self.redefinir_senha)

    def redefinir_senha(self):
        usuario = self.lineEdit_usuario.text()
        senha_1 = self.lineEdit_2_1senha.text()
        senha_2 = self.lineEdit_3_2senha.text()

        cursor = conexao.cursor()
        cursor.clear_attributes()       
        
        comando = 'SELECT nome FROM usuarios WHERE nome = %s'
        cursor.execute(comando, (usuario,))
        leitura_banco = cursor.fetchone()
        cursor.clear_attributes() 
        
        if leitura_banco is not None and senha_1 == senha_2:
            dados = (str(senha_1), str(usuario))

            comando = 'UPDATE usuarios SET SENHA = %s WHERE nome = %s'
            cursor.execute(comando, dados)
            conexao.commit()  

            QMessageBox.warning(self, "Sucesso!", "Senha alterada.")
            self.voltar_Login()

        elif senha_1 != senha_2:
            QMessageBox.warning(self, "Falha!", "Senhas divergentes")
        else:
            QMessageBox.warning(self, "Falha!", "Usuário não encontrado")


    def voltar_Login(self):
        if self.Button_2_voltar.clicked:
            self.w = Log()
            self.w.showMaximized()
            self.close()

# TELA DE PRODUTO
class VerpdtMainWindow(QMainWindow, Ui_Ver_produto):
    def __init__(self, produto_id) -> None:
        super(VerpdtMainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Visualizar produto")

        self.Button_3_voltar.clicked.connect(self.voltar_Estoque)
        self.Button_sair.clicked.connect(self.voltar_Login)
        
        self.carregar_dados(produto_id)
    
    def voltar_Estoque(self):
        if self.Button_3_voltar.clicked:
            self.w = MainWindow()
            self.w.showMaximized()
            self.close()

    def voltar_Login(self):
        if self.Button_sair.clicked:
            self.w = Log()
            self.w.showMaximized()
            self.close()

    def carregar_dados(self, produto_id):
        cursor = conexao.cursor()
        comando = 'SELECT * FROM estoque WHERE id = %s'
        cursor.execute(comando, (produto_id,))
        produto = cursor.fetchone()

        if produto:
            self.label_12_id.setText(str(produto[0]))
            self.label_produto.setText(produto[1])
            self.lineEdit_5_qtde.setText(str(produto[2]))
            self.lineEdit_6_codbarra.setText(produto[3])
            self.lineEdit_7_prec_uni.setText(str(produto[4]))
            self.lineEdit_8_categoria.setText(produto[5])
            #self.label_14_preco_total.setText(produto[6])
        
# CADASTRO PRODUTO
class CadastroMainWindow(QMainWindow, Ui_Cadastro_pdt):
    def __init__(self) -> None:
        super(CadastroMainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadastrar produto")
        self.showMaximized()

        self.Button_3_voltar.clicked.connect(self.voltar_Estoque)
        self.Button_sair.clicked.connect(self.voltar_Login)
        self.Button_2_salvar.clicked.connect(self.cadastrar_produto)

    def cadastrar_produto(self):
        produto = self.lineEdit_produto.text()
        quantidade = self.lineEdit_5_qtde.text()
        cod_barras = self.lineEdit_6_cod_barra.text()
        preco_unit = self.lineEdit_7_preco_uni.text()
        categoria = self.lineEdit_8_categoria.text()

        cursor = conexao.cursor()
        inserir_dados = "INSERT INTO ESTOQUE (PRODUTO, QUANTIDADE, COD_BARRAS, PRECO_UNIT, CATEGORIA) VALUES (%s, %s, %s, %s, %s)"
        dados = (str(produto), str(quantidade), str(cod_barras),  str(preco_unit), str(categoria))
        cursor.execute(inserir_dados, dados)
        conexao.commit()

        self.lineEdit_produto.clear()
        self.lineEdit_5_qtde.clear()
        self.lineEdit_6_cod_barra.clear()
        self.lineEdit_7_preco_uni.clear()
        self.lineEdit_8_categoria.clear()

        QMessageBox.warning(self, "Sucesso", "Produto cadastrado")
        
    def voltar_Estoque(self):
        if self.Button_3_voltar.clicked:
            self.w = MainWindow()
            self.w.showMaximized()
            self.close()

    def voltar_Login(self):
        if self.Button_sair.clicked:
            self.w = Log()
            self.w.showMaximized()
            self.close()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Log()
    window.showMaximized()
    sys.exit(app.exec())