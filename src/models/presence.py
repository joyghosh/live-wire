'''
Created on 26-Sep-2015

@author: joyghosh
'''
from models.channel import Channel

class Presence(Channel):
    '''
    Implementation of a specialized presence channel which helps determine availability of peers. 
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        