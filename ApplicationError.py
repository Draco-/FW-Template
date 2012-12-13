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
 
ApplicationError.py
#=====================================================================================================
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
