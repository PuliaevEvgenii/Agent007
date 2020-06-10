import sys

from PyQt5.QtWidgets import QApplication

from Windows.StartSettingsWindow import StartSettingsWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = StartSettingsWindow()
    sys.exit(app.exec_())
