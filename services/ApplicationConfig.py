"""
ApplicationConfig.py
Manage configuration data for an application
This file keeps a class to hold configuration data for the application.
the module also provides methods to load and save configuration data to a
text file
"""

#=====================================================================================================
# Import section
#=====================================================================================================
import os


#=====================================================================================================
# Class Application
#=====================================================================================================
class AppConfig:
    """
    this class is implemented as a storage for configuration data.
    """
    
    # All configuration data are class variables to this class
    # Unchangable configuration data
    _APPLICATION = 'Application Framework'
    _VERSION = '0.0.1'
    _AUTHOR = 'Juergen Baumeister'
    
    # User defined configuration data
    # Configure this information here!!
    _CONFIGFILE = 'config.txt'
    _config_new = 'config.tmp'
    
    # Testparameter
    query_exit = True
    
    
def readConfig(configClass = AppConfig):
    """
    Use the CONFIGFILE setting in AppConfig to read the config file and to set
    the config parameters accordingly
    """
    #print 'Initializing configuration\n'
    #TODO: replace print statement by information at the status line
    try:
        # As the Application Config module is the only source for information about the config file,
        # when the application is started this has to be configured in the module file
        # TODO: Implement a way, that enables a fully flexible way of configuration by the user.
        
        for line in open(configClass._CONFIGFILE).readlines():
            line_el = line.split('#')
            if len(line_el) >= 1 and line_el[0].strip() != '':
                # handle key value pairs of the config file
                key, val = tuple((line_el[0].strip()).split('='))
                # the 'None' value is handled explicitly,
                if val.strip() == 'None':
                    val = None
                elif val.strip() == 'True':
                    val = True
                elif val.strip() == 'False':
                    val = False
                elif type:
                    # for the moment being, only integer values are converted into integer types
                    try:
                        val = int(val)
                    except ValueError:
                        pass
                # attributes of the configClass are set according to the read values
                setattr(configClass, key.strip(), val)
    except IOError:
        # TODO: implement handling of IOError while reading config file
        #print 'Could not read configuration file...\nCreating first time configuration'
        writeFirstConfig()

        
def writeConfig(configClass = AppConfig):
    """
    Write an actual config file from the existing settings in AppConfig.
    We use the existing config file with its comments as a template. This means,
    comments are transfered as they are, key value pairs are updated according
    to the actual settings in the AppConfig class.
    """
    print 'Saving configuration\n'
    #TODO: replace print statement by information at the status line
    
    # Open existing config file and new config file
    configRead = open(AppConfig._CONFIGFILE, 'r')
    configWrite = open(AppConfig._config_new, 'w+')
    # prepare a list of already saved attributes
    saved = []
    
    for line in configRead.readlines():
        #print line
        if line.strip() == '# End predefined' :
            configWrite.write(line + '\n')
            break
        line_el = line.split('#')
        if len(line_el) >= 1 and line_el[0].strip() != '':
            # handle key value pairs of the config file
            key, val = tuple((line_el[0].strip()).split('='))
            if key in dir(configClass):
                # retrieve the value from the AppConfig class
                val = getattr(configClass, key)
                # handle 'None' value
                if ((val == None) or (val == 'None')):
                    line = str(key) + '='
                # handle 'True' and 'False' values
                elif ((val == True) or (val == 'True')):
                    line = str(key) + '=' + 'True'
                elif ((val == False) or (val == 'False')):
                    line = str(key) + '=' + 'False'
                # handle all other values
                else:
                    line = str(key) + '=' + str(val)
                # save information about already saved attributes
                saved.append(key)
                
            if len(line_el) == 2 :
                # line has a comment after the key value pair
                line += '        # ' + line_el[1].strip()
            line += '\n'
        # write config attribute to the new config file
        configWrite.write(line)
    
    # all not yet saved config attributes of the configuration class are appended to the config file here
    configWrite.write('\n\n# Additional attributes not yet saved\n')
    for key in dir(configClass):
        if key in saved:
            pass
        else:
            if key[:2] != '__' and key[:1] != '_': # we don't need to save internal attributes of the class
                val = getattr(configClass, key)
                # handle 'None' value like above
                if ((val == None) or (val == 'None')):
                    line = str(key) + '=\n'
                else:
                    line = str(key) + '=' + str(val) + '\n'
                configWrite.write(line)
    
    configRead.close()
    configWrite.close()
    # replace old config file with the new one
    os.remove(configClass._CONFIGFILE)
    os.rename(configClass._config_new, configClass._CONFIGFILE)

def writeFirstConfig(configClass = AppConfig):
    """
    Write a first config file as a starting point for the application config.
    """
    # Open temporary file to write config
    configWrite = open(AppConfig._config_new, 'w+')
    
    configWrite.write('# automatically created config file for application framework\n\n')

    # additional config data and their explanation goes here
    # TODO: complete list and explanation for config data
    configWrite.write('# for the moment there are no confiuration data to be stored\n\n')    

    configWrite.write('# End predefined\n')
    
    configWrite.close()
    # rename temporary file to be the actual config file
    os.rename(configClass._config_new, configClass._CONFIGFILE)

readConfig()
