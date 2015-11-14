'''
Created on 23-Aug-2015

@author: joy ghosh
'''
import sys
import json
from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory
from twisted.python import log
from twisted.internet import reactor
from nosql.redis_interface import RedisAdapter
from common.globals import Conguration

class LiveWireServerProtocol(WebSocketServerProtocol):
    '''
    This class channels the web-socket connection end-point on server's end.
    In simple language this is the web-socket end-point for the push server.  
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.redis_instance = RedisAdapter.getInstance(self)
    
    '''client connection handler'''
    def onConnect(self, request):
        print("Client connecting: {}".format(request.peer))
    
    '''web-socket open handler'''
    def onOpen(self):
        print("Web-socket connection open.")
        #get the lw user id. This should be unique across clusters.
        peer_id = RedisAdapter.get_lw_id(self)
        Conguration.put_peer(self, peer_id, self)
    
    '''message handler'''
    def onMessage(self, payload, isBinary):
        payloadObject = json.loads(payload.decode('utf8'))
        
        if(payloadObject['type'] == "subscribe"):
            self.subscribe_to_channel(payloadObject)
        elif(payloadObject['type'] == "event"):
            self.post_event_to_channel(payloadObject)
        else:
            self.sendMessage(json.dumps({"error":"No such type supported."}), False)
            
        if isBinary:
            print("Binary message received: {} bytes".format(len(payload)))
        else:
            print("Text message received: {}".format(payload.decode('utf-8')))
        
        ##echo back message verbatim.
        self.sendMessage(payload, isBinary)
    
    '''connection close handler'''
    def onClose(self, wasClean, code, reason):
        print("Web-socket connection closed {}".format(reason))

    
    def subscribe_to_channel(self, payload):
        if(payload['channel-type'] == "lw-presence"):
            pass
        elif(payload['channel-type'] == "lw-private"):
            pass
        elif(payload['channel-type'] == "lw-public"):
            pass
        else:
            self.sendMessage(json.dump({"error":"channel-type not supported."}), False)
            
    
    def post_event_to_channel(self, payload):
        if(payload['event-type'] == "lw-custom-event"):
            pass
        elif(payload['event-type'] == "lw-presence-event"):
            pass
        else:
            self.sendMessage(json.dump({"error":"event-type not supported."}), False)
        

if __name__ == '__main__':
    
    log.startLogging(sys.stdout)
    
    factory = WebSocketServerFactory("ws://127.0.0.1:9000")
    factory.protocol = LiveWireServerProtocol
    
    reactor.listenTCP(9000, factory) #@UndefinedVariable
    reactor.run() #@UndefinedVariable