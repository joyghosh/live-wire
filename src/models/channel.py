'''
Created on 23-Aug-2015

@author: joy ghosh
'''

class Channel(object):
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
        pass
            
    def unsubscribe(self,peer):
        pass