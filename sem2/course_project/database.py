#!/usr/bin/env python3
import redis
import redisdl
import json

redis_host = "localhost"
redis_port = 6379
redis_password = ""

class database:
    def __init__(self):
        self.base = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        self.id = 0
        self.DATA_ID = "test"

    def save(self, filename):
        with open(filename, 'w') as f:
            redisdl.dump(f)

    def load(self, filename):
        with open(filename) as f:
            redisdl.load(f)

    def insert(self, el):
        self.base.hset(self.DATA_ID, str(self.id), json.dumps(el))
        self.id = self.id + 1
        print(self.id)
