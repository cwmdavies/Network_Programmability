config_filter = """
    <config>    
        <native xmlns="http://cisco.com/ns/yang/ned/ios">
            <snmp-server operation='delete'>
                <community>
                    <name>Secure</name>
                    <RW/>
                </community>
            </snmp-server>
        </native>
    </config>
"""