'''
Created on 02-Oct-2015

@author: joyghosh
'''

class BaseEvent(object):
    '''
    Class representation of an abstract event model.
    '''
    
    def __init__(self, eventType, message):
        '''
        Initialize event type and message.
        '''
        self.eventType = eventType
        self.message = message
    
    def getType(self):
        return self.eventType
    
    def getMessage(self):
        return self.message