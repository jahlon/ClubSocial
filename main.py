import sys

from PySide2.QtWidgets import QApplication

from club_social.mundo.mundo import Club
from club_social.vista.gui.gui import VentanaClubSocial

if __name__ == "__main__":
    app = QApplication(sys.argv)
    club = Club()
    window = VentanaClubSocial(club)
    sys.exit(app.exec_())