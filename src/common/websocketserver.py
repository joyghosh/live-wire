'''
Created on 23-Aug-2015

@author: joy ghosh
'''
from autobahn.twisted.websocket import WebSocketServerProtocol

class LiveWireServerProtocol(WebSocketServerProtocol):
    '''
    This class models the web-socket connection end-point on server's end.
    In simple language this is the web-socket end-point for the push server.  
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    
    '''client connection handler'''
    def onConnect(self, request):
        print("Client connecting: {}".format(request.peer))
    
    '''web-socket open handler'''
    def onOpen(self):
        WebSocketServerProtocol.onOpen(self)
    
    '''message handler'''
    def onMessage(self, payload, isBinary):
        WebSocketServerProtocol.onMessage(self, payload, isBinary)
    
    '''connection close handler'''
    def onClose(self, wasClean, code, reason):
        WebSocketServerProtocol.onClose(self, wasClean, code, reason)