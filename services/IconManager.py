"""
IconManager.py
A class template to manage the icons required by the application.
Icons are defined in a tree of dictionaries, that define the icons for every section and
topic within the application. At every level there can be an default icon for this section
or topic.

When an icon is needed, the caller provides a list of strings, that are used as a search
path to find the required icon. If there is no icon found, the default icon is returned
"""

#=====================================================================================================
# Import section
#=====================================================================================================
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

from ApplicationError import ApplicationError

# import other data model and data handling classes

#=====================================================================================================
# Class Model
#=====================================================================================================
class IconManager(QtCore.QObject):
    """
    Creates and manages icons for the application
    """
    
    def __init__(self):
        """
        Initialize the icon manager
        """
        
        # call __init__ method of superclass
        QtCore.QObject.__init__(self)
        
        self._icons = {}
        self._populateIconDict()
        
    def _populateIconDict(self):
        """
        Define the icons for the application
        """
        
        self._icons = {'application':{'title':'icons/default.png',
                                      'actions':{'exitApp':'icons/exitApp.png'}}, 
                       'view':{}}
        
        
    def getDefaultIcon(self):
        return QtGui.QIcon('icons/default.png')
        
    def getIcon(self, search_path):
        """
        Provide the actual icon
        """
        try:
            iconLoc = self._getIconLocation(search_path, self._icons)
            print iconLoc
            if not iconLoc:
                print 'Default Icon'
                iconLoc = 'icons/default.png'
                #icon = self.getDefaultIcon()
        except ApplicationError, e:
            raise ApplicationError(search_path + e)
            # TODO: implement IconManagerError for this class
        
        return QtGui.QIcon(iconLoc)
        #return icon
            

    def _getIconLocation(self, path, dict):
        """
        recursively search for the required icon, defined by the search path 
        (list of strings).
        if no icon is found, try to use a default icon at the deepest possible level
        """
        iconLoc = None
        
        # check for end of recursion
        if isinstance(path, list) and len(path) == 1:
            if path[0] in dict.keys():
                iconLoc = dict[path[0]]
            elif 'default' in dict.keys():
                iconLoc = dict['default']
            else:
                iconLoc = False
            return iconLoc
            
        # check, if icon exists on given level
        elif isinstance(path, list) and len(path)> 1:
            if path[0] in dict.keys():
                dict_new = dict[path[0]]
                iconLoc = self._getIconLocation(path[1:], dict_new)

            elif 'default' in dict.keys():
                iconLoc = dict['default']
            return iconLoc
        
                
