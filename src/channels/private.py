'''
Created on 02-Oct-2015

@author: joyghosh
'''
from channels.channel import BaseChannel

class Private(BaseChannel):
    '''
    Private channel type. Requires authentication on peer subscription.
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        