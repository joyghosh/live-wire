'''
Created on 23-Aug-2015

@author: joy ghosh
'''
import sys
import json
from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory
from twisted.python import log
from twisted.internet import reactor

class LiveWireServerProtocol(WebSocketServerProtocol):
    '''
    This class models the web-socket connection end-point on server's end.
    In simple language this is the web-socket end-point for the push server.  
    '''

#     def __init__(self, params):
#         '''
#         Constructor
#         '''
    
    '''client connection handler'''
    def onConnect(self, request):
        print("Client connecting: {}".format(request.peer))
    
    '''web-socket open handler'''
    def onOpen(self):
        print("Web-socket connection open.")
    
    '''message handler'''
    def onMessage(self, payload, isBinary):
        
        obj = json.loads(payload.decode('utf8'))
        
        if(obj['type'] == "presence"):
            #TODO
            pass
        elif(obj['type'] == "private"):
            #TODO
            pass
        elif(obj['type'] == "public"):
            #TODO
            pass
        else:
            self.sendMessage(json.dumps({"error":"channel type not supported"}), False)
            
        if isBinary:
            print("Binary message received: {} bytes".format(len(payload)))
        else:
            print("Text message received: {}".format(payload.decode('utf-8')))
        
        ##echo back message verbatim.
        self.sendMessage(payload, isBinary)
    
    '''connection close handler'''
    def onClose(self, wasClean, code, reason):
        print("Web-socket connection closed {}".format(reason))

if __name__ == '__main__':
    
    log.startLogging(sys.stdout)
    
    factory = WebSocketServerFactory("ws://127.0.0.1:9000")
    factory.protocol = LiveWireServerProtocol
    
    reactor.listenTCP(9000, factory) #@UndefinedVariable
    reactor.run() #@UndefinedVariable