'''
Created on 23-Aug-2015

@author: joyghosh
'''
from models.peer import Peer

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
        self.peers = []
    
    def subscribe(self, peer):
        """
        Add peer to the peer list.
        """
        if(peer in self.peers):
            return False
        else:
            self.peers.append(peer)
            return True
            
    def unsubscribe(self,peer):
        """
        Remove peer from the peer list.
        """
        if(peer in self.peers):
            self.peers.remove(peer)
            return True
        else:
            return False
    
    def broadcast(self):
        """
        Broadcast event to all subscribed peers.
        """
        for peer in self.peers:
            pass