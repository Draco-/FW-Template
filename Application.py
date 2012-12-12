"""
Application.py
The main script for an application.
This file keeps an application class, that defines the basic elements of the application and the
'boilerplate' stuff to start an application.
"""

#=====================================================================================================
# Import section
#=====================================================================================================
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

from services.ApplicationConfig import *
from services.IconManager import IconManager
#from gui.MultiViewManager import MultiViewVSplitter
#from gui.MultiViewManager import MultiViewTabbed
from gui.ViewManager import ViewManager
from model.Model import Model
#from ModelManager import ModelManager

#=====================================================================================================
# Class Application
#=====================================================================================================
class Application(QtGui.QMainWindow):
    """
    This class is used as the MainWindow of the application.
    It sets up the MainWindow and defines other important basics, that are
    needed in the application. See __init__ method for the implementation
    details
    """
    #=================================================================================================
    # initializing the application class
    #=================================================================================================
    def __init__(self,  *args):
        """
        Initialize the MainWindow and the basic elements.
        This method keeps just the boilerplate stuff and calls methods for the
        several initialisation steps.
        Application specific stuff is placed within these methods
        """
        
        # call __init__ method of superclass
        QtGui.QMainWindow.__init__(self,  *args)
        
        self.setGeometry(100, 100, 600, 400)
        #TODO: Make setup of main window and view manager available via user configuration
        
        # initialize basic element of the application gui
        self._initApplicationServices()
        self._initActions()
        self._initMenuBar()
        self._initToolBar()
        self._initStatusBar()
        
        # setup data model or document and view manager
        self._initModelManager()
        self._initViewManager()

    def _initApplicationServices(self):
        """
        initialize an services for the application
        """
        # Service icons, provides icons based on a search path
        self.icons = IconManager()

    def _initActions(self):
        """
        Setup and prepare a list of application actions (to be performed from the top level
        of the application.
        An exit action is already implemented as an example
        """
        # Dictionary of actions
        self.actions = {}
        
        # exitApp - exit the application (end of application programme)
        self.actions['exitApp'] = QtGui.QAction(self.icons.getIcon(['application', 'actions', 'exitApp']), 
                                                'Exit', 
                                                self)
        self.actions['exitApp'].setShortcut('Ctrl+Q')
        self.actions['exitApp'].triggered.connect(self.slotExitApp)
        
        # other actions follow here

    def _initMenuBar(self):
        """
        Define the necessary menues and put them into the menu bar of the main window
        """
        self.fileMenu = QtGui.QMenu('&File',  None)
        self.fileMenu.addAction(self.actions['exitApp'])
        # additional actions in the file menue go here
        self.menuBar().addMenu(self.fileMenu)
        
        # additional menues for the menue bar go here

    def _initToolBar(self):
        """
        Define a tool bar and put required actions in
        """
        self.fileToolBar = self.addToolBar('File')
        self.fileToolBar.addAction(self.actions['exitApp'])
        
        # more actions for the tool bar go here
        
    def _initStatusBar(self):
        """
        Initialize the status bar. Here we just put the string 'Ready ...' to the status bar
        """
        self.statusBar().showMessage('Ready ...')

    #=================================================================================================
    # initializing the data model / document and the view manager
    #=================================================================================================
    def _initModelManager(self):
        """
        Create a model manager or a document from its class and initialize it.
        The application class keeps a reference to the model manager
        """
        # if we need arguments for the model manager, we must provide them here
        self.model = Model()
        
        # other initialisation stuff goes here

    def _initViewManager(self):
        """
        Create a view manager from its class and initialize it.
        The application class keeps a referene to the view manager
        """
        self.view = ViewManager()
        self.setCentralWidget(self.view)

    #=================================================================================================
    # slot implementations for the application
    #=================================================================================================
    # each action, as well as each activity that is triggered from other parts of the application
    # e.g. user demands ...  has to be implemented here
    
    def slotExitApp(self):
        """
        Query the user, if he wants to exit (depending on the query parameter), start the shutdown
        stuff and finally exit the application
        """
        
        query = AppConfig.query_exit
        #query=True
        
        if query:
            self.statusBar().showMessage('Exiting application ...')
            if self.queryExit():
                self.shutdownApplication()
                QtGui.qApp.quit()
            else:
                self.statusBar().showMessage('Ready ...')
        else:
            self.statusBar().showMessage('Exiting application ...')
            self.shutdownApplication()
            QtGui.qApp.quit()

    #=================================================================================================
    # other action methods and hooks
    #=================================================================================================
    def queryExit(self):
        """
        Ask user, if he realy wants to quit the application
        """
        exit = QtGui.QMessageBox.information(self,
                                             'Quit...', 
                                             'Do you really want to quit?', 
                                             '&OK', 
                                             '&Cancel', 
                                             '',  0,  1
                                             )
        if exit == 0:
            return True
        else:
            return False

    def shutdownApplication(self):
        """
        Function hook for the exit application slot.
        This method is intended to clean up the application if necessary before
        final shut down (exit of application)
        """
        writeConfig()
        
    def closeEvent(self, event):
        """
        this event handler catches the close event, that is signalled, when the user tries to close
        the application by the windows close button and sends it to the slotExitApp like all other
        exit / close actions
        """
        event.ignore()
        self.slotExitApp()
        

    #=================================================================================================
    # END OF CLASS Application
    #=================================================================================================

#=====================================================================================================
# main function stuff
#=====================================================================================================
def main(args):
    """
    The main function of the module.
    This function starts up the application
    """
    app = QtGui.QApplication(args)
    appView = Application()
    appView.show()
    
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main(sys.argv)
