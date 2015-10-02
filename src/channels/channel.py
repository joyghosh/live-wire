'''
Created on 23-Aug-2015

@author: joyghosh
'''

class BaseChannel(object):
    '''
    Basic channel entity to which peers are subscribed to.
    '''

    def __init__(self, name):
        '''
        basic instance attributes of a channel:
        (1) channel name.
        (2) Peers subscribed to the channel.
        '''
        self.name = name
        self.peers = {}
    
    def subscribe(self, peer):
        """
        Add peer to the peer list.
        """
        pass
            
    def unsubscribe(self,peer):
        """
        Remove peer from the peer list.
        """
        pass
    
    def broadcast(self):
        """
        Broadcast event to all subscribed peers.
        """
        pass