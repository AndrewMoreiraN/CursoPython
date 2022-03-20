import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from Exercicios.validador_cpf import ValidadorCPF
from untitled import *


class ValidadorGeradorCPF(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.valida = ValidadorCPF()
        self.btnGerarCPF.clicked.connect(self.show_text)
        self.btnValidarCPF.clicked.connect(self.show_result)
        self.btnclear.clicked.connect(self.clear)

    def clear(self):
        self.receberCPF.setText('')
        self.cpfSemEspecial.setText('')
        self.mostrarResultado.setText('')

    def show_text(self):
        self.receberCPF.setText(self.valida.gera_cpf())
        self.cpfSemEspecial.setText(self.valida.recebe_cpf(self.receberCPF.text()))

    def show_result(self):

        if self.receberCPF.text() == '':
            self.mostrarResultado.setText('Nenhum CPF.')
            return
        self.valida.recebe_cpf(self.receberCPF.text())
        self.cpfSemEspecial.setText(self.valida.recebe_cpf(self.receberCPF.text()))
        if self.valida.valida_cpf():
            self.mostrarResultado.setText('CPF válido.')
        else:
            self.mostrarResultado.setText('CPF inválido.')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    valida = ValidadorGeradorCPF()
    valida.show()
    qt.exec_()
