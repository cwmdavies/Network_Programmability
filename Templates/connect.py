from ncclient import manager
host = "10.1.1.11"
port = 830
username = "cisco"
password = "cisco"

m = manager.connect(
    host=host,
    port=port,
    username=username,
    password=username,
    hostkey_verify=False
    )
for capability in m.server_capabilities:
        print (capability)
m.close_session()
