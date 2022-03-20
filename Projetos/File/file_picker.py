import os
import sys

from PyQt5.QtWidgets import QMainWindow

from list_of_files import ListOfFiles
from projetos.file.UI.file_picker_window import *


class FilePicker(QMainWindow, Ui_FilePicker):
    def __init__(self, directory, parent=None):
        try:
            super().__init__(parent)
            super().setupUi(self)
            self.list_of_files = ListOfFiles()
            # self.file = parent
            self.btnExit.clicked.connect(lambda: sys.exit())
            self.btnMenu.clicked.connect(self.back_menu)
            self.btnBack.clicked.connect(lambda: self.back_next(-1))
            self.btnNext.clicked.connect(lambda: self.back_next(1))
            self.btnSearch.clicked.connect(self.file_search)
            self.directory = directory
            self.list_files = self.list_of_files.get_files_only(self.directory)
            self.index = -1
        except Exception as e:
            print(f'Error: {e}, init FILE_PICKER')

    def back_menu(self):
        try:
            self.hide()
            self.parent().show()
        except Exception as e:
            print(f'Error: {e}, back_menu FILE_PICKER')

    def remove_stuff(self, path):
        try:
            temp = path
            temp, ext = os.path.splitext(temp)
            resposta = temp.replace(f'{self.directory}\\', '').strip()
            return resposta
        except Exception as e:
            print(f'Error: {e}, remove_stuff FILE_PICKER')

    def back_next(self, numero):
        try:
            if self.index <= 0 and numero == -1:
                return
            elif self.index == len(self.list_files) - 1 and numero == 1:
                return
            self.index += numero
            self.inputFile.setText(self.remove_stuff(self.list_files[self.index]))
        except Exception as e:
            print(f'Error: {e}, back_next FILE_PICKER')

    def file_search(self, name=False):
        try:
            if not name:
                text = self.inputFile.text()
            else:
                text = name
            new_directory = self.create_directory(text, self.directory)
            self.verify_name_move_file(self.list_files, text,
                                       new_directory)
            self.list_files = self.list_of_files.get_files_only(self.directory)
            self.inputFile.setText(self.remove_stuff(self.list_files[self.index]))
        except Exception as e:
            print(f'Error: {e}, file_search FILE_PICKER')

    def verify_name_move_file(self, lista_aquivos, file_name, new2_directory):
        try:
            for files in lista_aquivos:
                file = files.replace(self.directory, '')
                if file_name.casefold() in file.casefold():
                    self.list_of_files.verify_if_file_exists(files, self.directory, new2_directory)
            return
        except Exception as e:
            print(f'Error: {e}, verify_name_move_file FILE_PICKER')

    @staticmethod
    def create_directory(directory_name, directory_received):
        try:
            directory_received = f'{directory_received}\\{directory_name}'
            if os.path.isdir(directory_received):
                return directory_received
            else:
                os.mkdir(directory_received)
            return directory_received
        except Exception as e:
            print(f'Error: {e}, create_directory FILE_PICKER')
