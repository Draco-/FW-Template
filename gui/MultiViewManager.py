"""
MultiViewManager.py
A collection of classes to manage multiple views for the application.
"""

#=====================================================================================================
# Import section
#=====================================================================================================
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

# import other view managing and handling classes

#=====================================================================================================
# Class MultiViewTabbed
#=====================================================================================================
class MultiViewTabbed(QtGui.QTabWidget):
    """
    This multi view manager class uses a tab widget to handle a list of views, that are shown, when
    the respective tab is clicked
    """
    
    #=================================================================================================
    # initializing the view manager class
    #=================================================================================================
    def __init__(self, *args):
        
        # call __init__ method of superclass
        QtGui.QTabWidget.__init__(self, *args)
        
        # create the list of views
        self.views = []
        #self.setMargin(10)
        # TODO: implement user settable margin here
    
    #=================================================================================================
    # methods for view handling
    #=================================================================================================
    def addView(self, view):
        """
        add a new view to the multi view manager, initialize it and make it visible
        
        The view needs to be a widget (basic or user defined).
        The multi view manager makes sure, that heself becomes the parent of the view
        """
        if view not in self.views:
            view.setParent(self)
            self.views.append(view)
            #self.addTab(view, view.caption())
            self.addTab(view, '')
            #self.showPage(view)
            
    def removeView(self, view):
        """
        remove the view from the list and make shure it is no longer visible
        """
        if view in self.views:
            index = self.indexOf(view)
            self.removeTab(index)
            self.views.remove(view)


    def activeView(self):
        """
        find the active view, handled by the view manager and return it
        """
        return self.currentWidget()
        
    def viewList(self):
        """
        return a list of views, that are handled by the view manager
        """
        return self.views

    def cascade(self):
        """
        cascade the actual existing views, if this is possible
        This method is implemented just to get a common set of methods, every prepared
        view manager provides
        """
        pass

    def tile(self):
        """
        tile the actual existing views, if this is possible
        This method is implemented just to get a common set of methods, every prepared
        view manager provides
        """
        pass

    def canCascade(self):
        """
        Return True, if this view manager is able to cascade its views
        This method is implemented just to get a common set of methods, every prepared
        view manager provides
        """
        return False

    def canTile(self):
        """
        Return True, if this view manager is able to tile its views
        This method is implemented just to get a common set of methods, every prepared
        view manager provides
        """
        return False

          
#=====================================================================================================
# Class MultiViewSplitter
#=====================================================================================================
class MultiViewVSplitter(QtGui.QSplitter):
    """
    This view manager class uses one vertical splitter, to handle a list of separate views 
    (widgets). All views are collected in a list
    """
    
    #=================================================================================================
    # initializing the view manager class
    #=================================================================================================
    def __init__(self, *args):
        """
        Initialize the view manager and its basic elements
        """
        
        # call __init__ method of superclass
        QtGui.QSplitter.__init__(self,  *args)
        
        # create the list of views
        self.views = []

    #=================================================================================================
    # methods for view handling
    #=================================================================================================
    def addView(self, view):
        """
        add a new view to the view manager, initialize it and make it visible
        
        The view needs to be a widget (basic or user defined).
        The view manager makes sure, that heself becomes the parent of the view
        """
        view.setParent(self)
        self.views.append(view)

    def removeView(self, view):
        """
        remove the view from the list and make shure it is no longer visible
        
        With QSplitter, this is quite easy, as the QSplitter cares about his children
        """
        pass

    def activeView(self):
        """
        find the active view, handled by the view manager and return it
        """
        for view in self.view:
            if view.hasFocus():
                return view
        return self.views[0]
        
    def viewList(self):
        """
        return a list of views, that are handled by the view manager
        """
        return self.views

    def cascade(self):
        """
        cascade the actual existing views, if this is possible
        This method is implemented just to get a common set of methods, every prepared
        view manager provides
        """
        pass

    def tile(self):
        """
        tile the actual existing views, if this is possible
        This method is implemented just to get a common set of methods, every prepared
        view manager provides
        """
        pass

    def canCascade(self):
        """
        Return True, if this view manager is able to cascade its views
        This method is implemented just to get a common set of methods, every prepared
        view manager provides
        """
        return False

    def canTile(self):
        """
        Return True, if this view manager is able to tile its views
        This method is implemented just to get a common set of methods, every prepared
        view manager provides
        """
        return False
