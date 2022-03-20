import sys

from PyQt5.QtWidgets import QApplication

from file_options import FileOption

qt = QApplication(sys.argv)
music_option = FileOption()
music_option.show()
qt.exec_()
