"""
ApplicationError.py
Provides the top hierarchy of errors, that can be used within the application
"""

#=====================================================================================================
# Import section
#=====================================================================================================

# There is no import needed up to now

#=====================================================================================================
# Class ApplicationError
#=====================================================================================================
class ApplicationError(Exception):
    
    def __init__(self, object=None):
        self.errorMessage = 'There is an error within your application, concerning object %s' % str(object)
    
    def __repr__(self):
        return self.errorMessage
        
    def __str__(self):
        return self.errorMessage
        
#=====================================================================================================
# Class ModelManagerError
#=====================================================================================================
class ModelError(ApplicationError):
    
    def __init__(self, object=None):
        self.errorMessage = 'There is an error within your model, concerning object %s' % str(object)
        
#=====================================================================================================
# Other error classes, concerning the model manager go here
#=====================================================================================================
        
#=====================================================================================================
# Class ViewManagerError
#=====================================================================================================
class ViewManagerError(ApplicationError):
    
    def __init__(self, object=None):
        self.errorMessage = 'There is an error within your view manager, concerning object %s' % str(object)

#=====================================================================================================
# Other error classes, concerning the view manager go here
#=====================================================================================================

#=====================================================================================================
# Class ModelViewManagerError
#=====================================================================================================
class ModelViewManagerError(ApplicationError):

    def __init__(self, object=None):
        self.errorMessage = 'There is an error within your model-view manager, concerning object %s' % str(object)

class NoSuchModelError(ModelViewManagerError):

    def __init__(self, model):
        self.errorMessage = "Model %s with title %s is not managed by this DocumentManager"\
                            % (str(model), model.title(), str())

class ModelRemainingError(ModelViewManagerError):

    def __init__(self, object=None):
        self.errorMessage = 'There are still documents remaining.'
