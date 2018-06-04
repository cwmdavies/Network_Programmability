#!/usr/bin/env python
from connection_info import host, port , username, password, manager

m = manager.connect(
    host=host,
    port=port,
    username=username,
    password=username,
    hostkey_verify=False
    )
with open('Git\\Projects\\Project_Netconf\\Output\\capabilities.txt', 'w') as f:
    for capability in m.server_capabilities:
        f.write(str(capability)+'\n')
m.close_session()