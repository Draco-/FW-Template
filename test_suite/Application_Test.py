# coding=utf8
"""
 Copyright (C) 2012 Jürgen Baumeister

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Lesser General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Lesser General Public License for more details.

 You should have received a copy of the GNU Lesser General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
Application_Test.py
#=====================================================================================================
A test suite to test the behaviour of class Application
"""

#=====================================================================================================
# Import section
#=====================================================================================================
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

import unittest

# importing the module under Test
from Application import *

#=====================================================================================================
# Class mut_TestCase
#=====================================================================================================
class mut_TestCase(unittest.TestCase):
    """
    The test case class for the module under test (mut)
    """
    
    def setUp(self):
        """
        Implement the sourrounding for the test case
        """
        self.app = QtGui.QApplication([])
        self.mv_manager = stub_ModelViewManager()
        print "setUp called\n"
        
    def tearDown(self):
        """
        Clean environment before exit
        """
        print "tearDown called\n"
        
    def checkInstantiation(self):
        """
        Check, if it is possible to instantiate an object of class
        application
        """
        obj_ut = None
        # check if application object could be instantiated
        obj_ut = Application()
        assert obj_ut != None,  'Object could not be instantiated'
        
        # check initialisation of application services
        #print type(obj_ut.icons).__name__
        assert type(obj_ut.icons).__name__ == 'IconManager',  'No icon manager instantiated'
        
        # check initialisation of actions (at least 'exitApp')
        assert ('exitApp' in obj_ut.actions.keys()) == True, 'Application actions not properly implemented'
        #print type(obj_ut.actions['exitApp']).__name__
        assert type(obj_ut.actions['exitApp']).__name__ == 'QAction',  'Action exitApp not properly implemented'

    def checkSignals(self):
        """
        Check if signal flow between Application class and its sub and helper classes works
        """
        obj_ut = Application()
        obj_ut.sigCreateModelView.connect(self.mv_manager.slot_createModelView)
        obj_ut.createModelViewPair()
        assert self.mv_manager.signal_create == True,  'Signal sigCreateModelView not recieved'
        
    def runTest(self):
        """
        The core of the test suite
        """
        pass
        

#=====================================================================================================
# Helper stub classes
#=====================================================================================================
class stub_ModelViewManager(QtCore.QObject):

    def __init__(self,  *args):
        QtCore.QObject.__init__(self, *args)
        self.signal_create = False
        
    def slot_createModelView(self, modclass,  viewclass):
        self.signal_create = True



#=====================================================================================================
# Test Suite -- The stuff to collect tests in a testsuite
#=====================================================================================================
def suite():
    testSuite=unittest.TestSuite()
    testSuite.addTest(mut_TestCase("checkInstantiation"))
    testSuite.addTest(mut_TestCase("checkSignals"))
    return testSuite
    
def main():
    runner = unittest.TextTestRunner()
    runner.run(suite())

if __name__=="__main__":
    main()
    
