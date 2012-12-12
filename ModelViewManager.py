"""
ModelViewManager.py
The model view manager of an application maps models and their view(s) and makes sure, that
views and models are kept in sync
"""
"""
Explanation of application:
    the application details go here
  
Revision history:
    03.10.2012  Took the code over from 'GUI Programming with Python' a tutorial book for PyQt programming
"""
#=====================================================================================================
# Import section
#=====================================================================================================
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

#=====================================================================================================
# Class ModelViewManager
#=====================================================================================================
class ModelViewManager(QtCore.QObject):
    """
    The ModelViewManager manages the creation and removal of models
    and views.
    """
    #=================================================================================================
    # defining signals for the model view manager
    #=================================================================================================
    sigNumberOfModelsChanged = QtCore.pyqtSignal()

    #=================================================================================================
    # initializing the application class
    #=================================================================================================
    def __init__(self, parent, ViewManager=None):
        """
        The init method calls the initialisation of the superclass, takes over the given parameters
        of parent and ViewManager to internal attributes and
        creates the viewToModelMap and the modelToViewMap as the central datastructures to manage
        models and views
        """
        
        # call __init__ method of superclass
        QtCore.QObject.__init__(self)
        
        self._viewToModelMap = {}
        self._modelToViewMap = {}
        self._parent = parent
        if ViewManager:
            self._viewManager = ViewManager
        else:
            self._viewManager = parent

    #=================================================================================================
    # get information and objects, handled by the class
    #=================================================================================================
    def get_NumberOfModels(self):
        """
        return the number of models managed by the class instance
        """
        return len(self._modelToViewMap)
    
    def get_NumberOfViews(self):
        """
        return the number of views handled by the class instance
        """
        return len(self._viewToModelMap)

    def get_ViewsByModel(self, model):
        """
        return the views, that are assiciated with a given model
        """
        return self._modelToViewMap[model]
        
    def get_ActiveModel(self):
        """
        return the actually active model (by mapping the actually active view to
        the model)
        """
        if self._viewManager.activeWindow() is not None:
            return self._viewToModelMap[self._viewManager.activeWindow()]
        else:
            return None

    #=================================================================================================
    # manage models
    #=================================================================================================
    def createModel(self, modelClass, viewClass):
        """
        Create a new model and its initial view by using the given model and view classes
        """
        model = modelClass()
        view = self._createView(model, viewClass)
        if model in self._modelToViewMap.keys():
            self._modelToViewMap[model].append(view)
        else:
            self._modelToViewMap[model]= [view]
        self._viewToModelMap[view] = model
        
        self.sigNumberOfModelsChanged.emit()
        return model
        
    def addModel(self, model, viewClass):
        """
        Add a given model to the model view manager and set a view, according to the given
        view class
        """
        view = self._createView(model, viewClass)
        
        if model in self._modelToViewMap.keys():
            self._modelToViewMap[model].append(view)
        else:
            self._modelToViewMap[model] = [view]
            
        self._viewToModelMap[view] = model
        
        self.sigNumberOfModelsChanged.emit()
        return view
        
    #=================================================================================================
    # manage views
    #=================================================================================================
    def addView(self, model, viewClass):
        """
        add a new view of the given viewer class to the model
        """
        if model in self._modelToViewMap.keys():
            view = self._createView(model, viewClass)
            self._modelToViewMap[model].append(view)
            self._viewToModelMap[view] = model
            return view
        else:
            raise NoSuchModelError(model)
        
    #=================================================================================================
    # helper and hook methods
    #=================================================================================================
    def _createView(self, model, viewClass):
        """
        create and return a new view for the model
        """
        view = viewClass(self._viewManager, 
                         model, 
                         None 
                         #QtGui.QWidget.WDestructiveClose
                         )
        #view.installEventFilter(self.parent)
        if self._viewToModelMap == {}:
            view.showMaximized()
        else:
            view.show()
        
        if model in self._modelToViewMap.keys():
            index = len(self._modelToViewMap[model]) + 1
        else:
            index = 1
        
        view.setCaption(model.title() + '%s' % index)
        return view
        
    def _saveModel(self, model):
        try:
            model.save()
        except Exception, e:
            QMessageBox.critical(self, 
                                 'Error', 
                                 'Could not save the model: ' + e)
            raise e
