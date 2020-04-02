from netmiko import ConnectHandler

# Define device
cisco_ios = {'device_type': 'cisco_s300', 'ip': '192.168.1.254', 'username': 'cisco', 'password': 'Password1',}

# Connect to device
net_connect = ConnectHandler(**cisco_ios)

# Backup Configuration
showrun = net_connect.send_command('show run')
showvlan = net_connect.send_command('show vlan')
showver = net_connect.send_command('show ver')
log_file = open(r'C:\Users\CDavies\OneDrive - Involve Visual Collaboration Ltd\Projects\Network Programming\Paramiko-Netmiko\Netmiko\Backup.txt', "a")
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")