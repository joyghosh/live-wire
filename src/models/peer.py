'''
Created on 02-Oct-2015

@author: joyghosh
'''


class Peer(object):
    '''
    Peer model representing the end-point object.
    '''
    
    def __init__(self, user_id, socket):
        '''
        Constructor
        '''
        self.user_id = user_id
        self.socket = socket