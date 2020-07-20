import encodings
import sys

from PyQt5 import QtWidgets

import widgets


class DemoWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        widgets.load('demo.ui', self)


class DemoWindow(QtWidgets.QMainWindow):
    def setupUi(self):
        widget = DemoWidget(self)
        self.setCentralWidget(widget)
        self.setMinimumSize(350, 350)


def main():
    app = QtWidgets.QApplication(sys.argv)
    Window = DemoWindow()
    Window.setupUi()
    Window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
