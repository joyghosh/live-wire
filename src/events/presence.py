'''
Created on 02-Oct-2015

@author: root
'''
from events.event import BaseEvent

class PresenceEvent(BaseEvent):
    '''
    Event types for presence type channel. Following are the supported event types for a presence channel:
    (i)   lw-peer-subscription-success
    (ii)  lw-peer-subscription-failed
    (iii) lw-peer-removed
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        