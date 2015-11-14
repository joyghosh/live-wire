'''
Created on 26-Sep-2015

@author: joyghosh
'''

class Conguration(object):
    '''
    Shared data-structure for book keeping.
    '''
    channels={}
    peers={}
    
    def __init__(self, params):
        '''
        Constructor
        '''
    
    '''Returns the number of channels in-memory.'''
    def num_of_channels(self):
        return len(Conguration.channels)
    
    '''check if the channel name already exists.'''
    def channel_exists(self,channel):
        if(channel in Conguration.channels):
            return True
        else:
            return False
    
    '''return channel object by name.'''
    def get_channel(self,channel):
        if(channel in Conguration.channels):
            return Conguration.channels.get(channel)
        else:
            return None
    
    '''Add a new channel to global data structure.'''
    def put_channel(self,channel,channelObject):
        if(Conguration.channel_exists(self, channel)):
            return False
        else:
            Conguration.channels[channel] = channelObject
            return True
    
    '''Put new peer.'''         #Food for thought. Use Redis or MongoDb.
    def put_peer(self, peerId, peerWSObject):
        if(peerId not in Conguration.peers):
            Conguration.peers[peerId] = peerWSObject
            return True
        else:
            return False
        
    '''Remove peer.'''
    def remove_peer(self, peerId):
        if(peerId in Conguration.peers):
            Conguration.peers.pop(peerId)
            return True
        else:
            return False