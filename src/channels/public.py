'''
Created on 02-Oct-2015

@author: root
'''
from channels.channel import BaseChannel

class Public(BaseChannel):
    '''
    Public channel implementation. Requires no peer authentication upon subscription.
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        