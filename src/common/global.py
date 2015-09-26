'''
Created on 26-Sep-2015

@author: joyghosh
'''

class Global(object):
    '''
    Shared data-structure for book keeping.
    '''
    channels = {}
    
    def __init__(self, params):
        '''
        Constructor
        '''
    
    '''Returns the number of channels in-memory.'''
    def get_num_of_channels(self):
        return len(Global.channels)
    
    '''check if the channel name already exists.'''
    def channel_exists(self,channel):
        if(channel in Global.channels):
            return True
        else:
            return False
    
    '''return channel object by name.'''
    def get_channel(self,channel):
        if(channel in Global.channels):
            return Global.channels.get(channel)
        else:
            return None
    
    '''Add a new channel to global data structure.'''
    def put_channel(self,channel,channel_object):
        if(Global.channel_exists(self, channel)):
            return False
        else:
            Global.channels[channel] = channel_object
            return True
            