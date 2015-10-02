'''
Created on 02-Oct-2015

@author: root
'''
from events.event import BaseEvent

class PresenceEvent(BaseEvent):
    '''
    Event types for presence type channel. Following are the supported event types for a presence channel:
    (i)   peer-subscription-success
    (ii)  peer-subscription-failed
    (iii) peer-removed
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        