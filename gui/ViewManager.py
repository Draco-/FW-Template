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
 
ViewManager.py
#=====================================================================================================
The top level view manager, that implements the basic gui structure for the application
This structure needs to be implementetd manually
"""

# TODO: enhance this module, to enable more generic setup by config parameters

#=====================================================================================================
# Import section
#=====================================================================================================
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

from gui.MultiViewManager import *

#=====================================================================================================
# Class ViewManager
#=====================================================================================================
class ViewManager(QtGui.QSplitter):
    
    #=================================================================================================
    # initialisation of the view manager
    # this stuff needs to be changed, when the framework is adopted to an individual application
    #=================================================================================================
    def __init__(self, *args):

        # call init method of superclass
        QtGui.QSplitter.__init__(self, *args)
        # set datastructure to manage views
        self.view_sets = {}
        self.views = {}
        # define the basic framework of view areas for the
        # application
        self.createViewSets()
        self.setupViewFrames()
        
    def createViewSets(self):
        """
        create single views and multiple views and add them into the framework of
        views for the application
        """
        self.addTopView(QtGui.QTextEdit, 'navigate')
        self.addViewSet(MultiViewTabbed, 'work')
        self.addViewSet(MultiViewTabbed, 'notes')
        
    def setupViewFrames(self):
        """
        setup the framework of views and define various areas, where individual
        views can be placed
        """
        
        # the superclass of ViewManager is a splitter, so we have a left and a right
        # segment for the application gui
        
        # the right segment also is a splitter, but with vertical orientation
        right = QtGui.QSplitter()
        right.setOrientation(QtCore.Qt.Vertical)
        
        # bind the top level views into the framework
        self.view_sets['navigate'].setParent(self)
        right.setParent(self)
        
        self.view_sets['work'].setParent(right)
        self.view_sets['notes'].setParent(right)
        right.setSizes([20, 5])
        self.setSizes([5, 20])
        
    def addViewSet(self, settype, name):
        """
        create a new view set, using one of the multi view managers, by using the given
        type and name
        parameters:
        settype             <class>     the class of the multi view manager
        name                <string>    the name of the view set
        """
        self.view_sets[name] = settype()
        self.views[name] = []
        
    def addTopView(self,  viewtype, name):
        """
        create a new view to become another top level view
        parameters:
        viewtype            <class>     the class of the top level view
        name                <string>    the name of the new view
        """
        self.view_sets[name] = viewtype()

    #=================================================================================================
    # the managing methods of the view manager
    #=================================================================================================
    def getTopView(self, name):
        
        if name in self.view_sets.keys():
            return self.view_sets[name]
        else:
            return none
            
    def addView(self, name, view):
        """
        adds a given view to the top level view set, given by 'name'
        """
        if name in self.view_sets.keys():
            self.view_sets[name].addView(view)
            
    def removeView(self, name, view):
        """
        removes the given view from the top level set 'name'
        """
        if name in self.view_sets.keys():
            self.view_sets[name].removeView(view)
        
    def getActiveView(self, name):
        """
        return the active view of the area given by 'name'
        """
        if name in self.view_sets.keys():
            return self.view_sets[name].activeView()
        else:
            return None
            
    def getActiveViewIndex(self, name):
        """
        return the index for the active view of area given by 'name'
        """
        pass
        
    def setActiveView(self, name):
        """
        return the active view of the area given by 'name'
        """
        pass
            
    
