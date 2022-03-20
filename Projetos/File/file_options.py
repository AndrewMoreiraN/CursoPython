import concurrent.futures
import os
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from file_picker import FilePicker
from list_of_files import ListOfFiles
from projetos.file.UI.file_choices_menu_window import Ui_FileOption


class FileOption(QMainWindow, Ui_FileOption, ):
    def __init__(self, parent=None, ):
        try:
            self.threads = 10
            super().__init__(parent)
            super().setupUi(self)
            self.list_of_files = ListOfFiles()
            self.btnCreateFolders.clicked.connect(self.second_window)
            self.btnAutomatic.clicked.connect(self.automatic_file_creation)
            self.btnRemoveFile.clicked.connect(self.remove_single_file_from_folder)
            self.btnRemoveAll.clicked.connect(self.remove_all_files_from_folder)
            self.btnExit.clicked.connect(lambda: sys.exit())
            self.directory = ''
            self.file_picker = ''
        except Exception as e:
            print(f'Error: {e}, init FILE_OPTION')

    def automatic_file_creation(self):
        try:
            self.directory = self.inputFileName.text()
            self.file_picker = FilePicker(self.directory, self)
            list_files = self.list_of_files.get_files_only(self.directory)
            list_of_names = list(map(self.file_picker.remove_stuff, list_files))
            with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
                try:
                    executor.map(self.file_picker.file_search, sorted(list_of_names, key=len, reverse=True))
                except Exception as e:
                    print(f'Error: {e} aqui1, automatic_file_creation FILE_OPTION')
        except Exception as e:
            print(f'Error: {e} aqui2, automatic_file_creation FILE_OPTION')

    def showing(self):
        try:
            self.show()
        except Exception as e:
            print(f'Error: {e}, showing FILE_OPTION')

    def second_window(self):
        try:
            self.directory = self.inputFileName.text()
            self.file_picker = FilePicker(self.directory, self)
            self.file_picker = FilePicker(self.directory, self)
            self.hide()
            self.file_picker.show()
            return
        except Exception as e:
            print(f'Error: {e}, second_window FILE_OPTION')

    def remove_single_file_from_folder(self):
        try:
            self.directory = self.inputFileName.text()
            sub_folders = [f.path for f in os.scandir(self.directory) if f.is_dir()]
            for folder in sub_folders:
                if len(self.list_of_files.get_list_of_files(r'{}'.format(folder))) <= 1:
                    if len(self.list_of_files.get_list_of_files(r'{}'.format(folder))) != 0:
                        file = self.list_of_files.get_list_of_files(r'{}'.format(folder))[0]
                        self.list_of_files.verify_if_file_exists(file, folder, self.directory)
                    os.rmdir(folder)
        except Exception as e:
            print(f'Error: {e}, remove_single_file_from_folder FILE_OPTION')

    def remove_all_files_from_folder(self):
        try:
            self.directory = self.inputFileName.text()
            sub_folders = [f.path for f in os.scandir(self.directory) if f.is_dir()]
            for folder in sub_folders:
                sub_folders = [f.path for f in os.scandir(folder) if f.is_dir()]
                for file in self.list_of_files.get_list_of_files(r'{}'.format(folder)):
                    self.list_of_files.verify_if_file_exists(file, folder, self.directory)
                for sub_folder in sub_folders:
                    if len(self.list_of_files.get_list_of_files(sub_folder)) == 0:
                        os.rmdir(sub_folder)
                os.rmdir(folder)
                # shutil.rmtree()
        except Exception as e:
            print(f'Error: {e}, remove_all_files_from_folder FILE_OPTION')
        return


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    file_option = FileOption()
    file_option.show()
    qt.exec_()
