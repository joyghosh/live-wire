'''
Created on 02-Oct-2015

@author: Joy Ghosh
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
    
    def getSocket(self):
        '''
        Return underlying socket connection.
        '''
        return self.socket
    
    def getUserId(self):
        '''
        Return user-id.
        '''
        return self.user_id