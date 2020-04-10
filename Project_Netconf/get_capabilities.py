#!/usr/bin/env python
from connection_info import host, port , username, password
from ncclient import manager
m = manager.connect(host=host,port=port,username=username,password=password,hostkey_verify=False,)

with open('Output\\capabilities.txt', 'w') as f:
    for capability in m.server_capabilities:
        f.write(str(capability)+'\n')
m.close_session()
