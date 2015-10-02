'''
Created on 02-Oct-2015

@author: joyghosh
'''
from events.event import BaseEvent

class CustomEvent(BaseEvent):
    '''
    Custom event type model. Supports basic event type and message model. No rocket science.
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        