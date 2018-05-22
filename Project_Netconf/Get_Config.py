#!/usr/bin/env python
from ncclient import manager
from lxml import etree

get_filter = """
    <native xmlns="http://cisco.com/ns/yang/ned/ios">
        <interface>
            <GigabitEthernet>
                <name>1</name>
            </GigabitEthernet>
        </interface>
    </native>
"""

device = manager.connect(host="10.1.1.11", port=830, username="cisco", password="cisco", hostkey_verify=False, device_params={}, allow_agent=False, look_for_keys=False)

nc_get_reply = device.get(("subtree", get_filter))
print(etree.tostring(nc_get_reply.data, pretty_print=True))