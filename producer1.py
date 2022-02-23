#!/usr/bin/env python
import greenstalk
import json
import sys

beanstalkTube = 'YouTube'
beanstalkHost = 'localhost'
beanstalkPort = 11300

client = greenstalk.Client((beanstalkHost, beanstalkPort))
client.use(beanstalkTube)

client.put('message 5')

