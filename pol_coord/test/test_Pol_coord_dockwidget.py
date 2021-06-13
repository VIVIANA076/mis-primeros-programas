# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'vivianaandrea26@hotmail.com'
__date__ = '2021-06-05'
__copyright__ = 'Copyright 2021, viviana'

import unittest

from qgis.PyQt.QtGui import QDockWidget

from Pol_coord_dockwidget import poligono_coordenadasDockWidget

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class poligono_coordenadasDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = poligono_coordenadasDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass

if __name__ == "__main__":
    suite = unittest.makeSuite(poligono_coordenadasDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

