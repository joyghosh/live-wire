'''
Created on 02-Oct-2015

@author: root
'''
from events.event import BaseEvent

class PresenceEvent(BaseEvent):
    '''
    Event types for presence type channel.
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        