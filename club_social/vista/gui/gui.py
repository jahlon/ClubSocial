import sys

from PySide2.QtWidgets import QMainWindow, QApplication

from club_social.vista.gui.ui_main_window_club_social import Ui_MainWindow


class VentanaClubSocial(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setFixedSize(1028, 600)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaClubSocial()
    sys.exit(app.exec_())