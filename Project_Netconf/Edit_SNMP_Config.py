#!/usr/bin/env python
from ncclient import manager
import snmp_filter

device = manager.connect(host="10.1.1.11", port=830, username="cisco", password="cisco", hostkey_verify=False, device_params={}, allow_agent=False, look_for_keys=False)
response = device.edit_config(target='running', config=snmp_filter.config_filter)