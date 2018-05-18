#!/usr/bin/env python
import connect_info

m = connect_info.manager.connect(
    host=connect_info.host,
    port=connect_info.port,
    username=connect_info.username,
    password=connect_info.username,
    hostkey_verify=False
    )
with open('Git\\Projects\\Project_Connect\\text.txt', 'w') as f:
    for capability in m.server_capabilities:
        f.write(str(capability)+'\n')
m.close_session()