import os
import sys
from io import BytesIO

from PyQt5 import QtCore, uic


def resource_path(resFile):
    if getattr(sys, 'frozen', None):
        resFile = QtCore.QFile(
            ':/demo/ui/{}'.format(resFile))
        resFile.open(QtCore.QIODevice.ReadOnly)
        data = resFile.readAll()
        resFile.close()
        return BytesIO(bytes(data))
    path = os.path.join(os.path.dirname(__file__), 'ui', resFile)
    if os.path.isfile(path):
        return path


def load(resFile, widget):
    uic.loadUi(resource_path(resFile), widget)
