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
 
Model.py
#=====================================================================================================
A class template to manage a data model of the application.
"""

#=====================================================================================================
# Import section
#=====================================================================================================
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

from ApplicationError import ApplicationError, ModelError

# import other data model and data handling classes here

#=====================================================================================================
# Class Model
#=====================================================================================================
class Model(QtCore.QObject):
    """
    This class is a template, that contains the most important elements of a data model (or a document)
    in this application framework
    In most cases it is necessary, to subclass this template (or to enhance it) with specific
    data structures and functionality
    """

    #=================================================================================================
    # defining signals for the model
    #=================================================================================================
    # signal, that the model was changed (completely)
    sigModelModified = QtCore.pyqtSignal()
    # signal, that an element was added to the model (position, element)
    sigModelElementAdded = QtCore.pyqtSignal(object, object)
    # signal, that an element was removed from the model (position, element) the removed
    # element is transmitted, because it might be a key within the recieving object
    sigModelElementRemoved = QtCore.pyqtSignal(object, object)
    # signal, that an element of the model was updated. The part that was updated is 
    # represented by object
    sigModelElementUpdated = QtCore.pyqtSignal(object)
    # signal, that the model was cleared
    sigModelCleared = QtCore.pyqtSignal()
    
    # Further signals, needed by the model go here

    #=================================================================================================
    # initializing the model class
    #=================================================================================================
    def __init__(self, title=''):
        """
        Initialize the model and its basic elements
        """
        # call __init__ method of superclass
        QtCore.QObject.__init__(self)
        
        # define title of the model
        self.title = title
        
        # define some status information about the model
        self._modified = False

        # create and initialize elements of the model here
        self._initializeElements()
        

    def _initializeElements(self):
        """
        Implement initialization stuff here
        """
        pass
    
    def connectToView(self, view):
        """
        Connect the model to the signals of the view. This method is called by the
        ModelViewManager
        """
        # TODO find a way to automatically retrieve information about the signals from the view
        # probably it is possible, to retrieve all attributes of type 'PyQt4.QtCore.pyqtSignal' from
        # self.__class__.__dict__ an then check, if the signal is availabel before trying to connect
        
        # view.<signal>.connect(self.<SignalHandle>)
        
    #=================================================================================================
    # basic functionality
    #=================================================================================================
    def save(self):
        """
        Save the content of the model to a place / device, where it can be retrieved again
        """
        # Implementation of the method goes here
        self._modified = False
        
    def close(self):
        """
        Perform all necessary actions, before the model is closed
        """
        # Task of also informing the view, that the model was closed is to be performed
        # by the ModelViewManager
        pass
        
    def slotModifyModel(self):
        """
        this is a dummy method, that needs to be specified by the actual implementation of
        a model
        """
        self._modified = True
        # Implementation of the method goes here
        self.sigModelModified.emit()
        
    def slotAddElement(self, position, element):
        """
        add an element to the model at the given position
        """
        self._modified = True
        # Implementation of the method goes here
        self.sigModelElementAdded.emit(position, element)
        
    def slotRemoveElement(self, position, element = None):
        """
        remove an element from the given position (or use element to find, what to remove)
        """
        self._modified = True
        # Implementation of the method goes here
        self.sigModelElementRemoved.emit(position, element)
        
    def slotUpdateElement(self, element):
        """
        this is a dummy method, that needs to be specified by the actual implementation of
        a model
        """
        self._modified = True
        # Implementation of the method goes here
        self.sigModelElementUpdated.emit(element)
        
    def slotClearModel(self):
        """
        clear the model by resetting (or removing) all variable elements
        """
        self._modified = False
        # Implementation of the method goes here
        self.sigModelClear.emit()
        
    #=================================================================================================
    # get/information methods for attributes
    #=================================================================================================
    def isModified(self):
        """
        return attribute _modified
        """
        return self._modified
        
    def getTitle(self):
        """
        return the title of the model
        """
        return self.title
    
