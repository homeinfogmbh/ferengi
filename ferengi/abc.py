"""
Abstract base classes
"""
__author__ = 'Richard Neumann <r.neumann@homeinfo.de>'
__date__ = '11.09.2014'

#from homie.lib.passwd import User
from homie.api.abc import NamedClass
from homie.lib.config import Configurable
from os.path import join

class UserAware(NamedClass):
    """
    Class that know about its user
    """
    __user = None
    
    def __init__(self, user, name=None):
        """
        Constructor
        """
        super().__init__(name=name)
        self.__user = user
        
    @property
    def user(self):
        """
        Returns the user
        """
        return self.__user
    

class UAC(Configurable, UserAware):
    """
    User aware, configurable class
    """
    def __init__(self, user, name=None, config_suffix='.conf'):
        """
        Constructor
        """
        UserAware.__init__(self, user, name=name)
        Configurable.__init__(self, 
                              {'': join(self.user.home, 
                                        self.name.lower() + config_suffix)})