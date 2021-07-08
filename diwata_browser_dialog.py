# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DiwataBrowserDialog
                                 A QGIS plugin
 This plugin enables user to browse and load Diwata-2 SMI products.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-07-08
        git sha              : $Format:%H$
        copyright            : (C) 2021 by STAMINA4Space
        email                : cnpante@stamina4space.upd.edu.ph
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt.QtCore import QThread, pyqtSignal
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'diwata_browser_dialog_base.ui'))


class DiwataBrowserDialog(QtWidgets.QDialog, FORM_CLASS):
    closed_signal = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(DiwataBrowserDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def closeEvent(self, event):
        super(DiwataBrowserDialog, self).closeEvent(event)
        self.closed_signal.emit()
