#!/usr/bin/env python
from ncclient import manager

config_filter = """
    <config>    
        <native xmlns="http://cisco.com/ns/yang/ned/ios">
            <snmp-server operation='delete'>
                <community>
                    <name>Testing</name>
                    <RW/>
                </community>
            </snmp-server>
        </native>
    </config>
"""

device = manager.connect(host="10.1.1.11", port=830, username="cisco", password="cisco", hostkey_verify=False, device_params={}, allow_agent=False, look_for_keys=False)
response = device.edit_config(target='running', config=config_filter)