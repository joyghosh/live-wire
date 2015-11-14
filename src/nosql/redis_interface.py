'''
Created on 14-Nov-2015

@author: Joy Ghosh
'''
import redis
from helpers import singleton

@singleton
class RedisAdapter(object):
    '''
    RedisAdapter interfaces with a background NO-SQL Redis service. 
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.redis_client = redis.Redis("localhost")
        if(not self.redis_client.exists("lw-user-ids")):
            self.redis_client.incr("lw-user-ids", 0)
    
    def getInstance(self):
        _instance = RedisAdapter.Instance()
        return _instance
    
    def get_lw_id(self):
        return self.redis_client.incrby("lw-user-ids", 1)