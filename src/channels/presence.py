'''
Created on 26-Sep-2015

@author: joyghosh
'''
from channels.channel import BaseChannel

class Presence(BaseChannel):
    
    """
    Implementation of a specialized presence channel which helps determine availability of peers.
    e.g. online users in a chat application.
    """

    def __init__(self, name):
        '''
        Constructor
        '''
        super(Presence, self).__init__(name)
    
    def notify_peers(self):
        pass
    
    def broadcast_peer_added(self):
        pass
    
    def broadcast_peer_removed(self):
        pass