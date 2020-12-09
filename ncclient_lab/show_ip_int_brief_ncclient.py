from ncclient import manager

device = {
    'host': 'ios-xe-mgmt.cisco.com',
    'port': 10000,
    'username': 'developer',
    'password': 'C1sco12345',
    'hostkey_verify': False,
    'device_params': {'name': 'iosxe'}
}

with manager.connect(**device) as m:

    # ietf-interfaces:interfaces-state YANG data model
    netconf_filter = '''         
                  <filter>
                    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                      <interface>
                      </interface>
                    </interfaces>
                  </filter>
                '''
    response = m.get(netconf_filter)
    
    print(response)
    print()

    # ietf-interfaces:interfaces YANG data model
    netconf_filter = '''         
                      <filter>
                        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                          <interface>
                          </interface>
                        </interfaces-state>
                      </filter>
                    '''
    response = m.get(netconf_filter)
    
    print(response)
    print()

    # Cisco-IOS-XE-interfaces-oper YANG data model    
    netconf_filter = '''         
                      <filter>
                        <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
                          <interface>
                          </interface>
                        </interfaces>
                      </filter>
                    '''
    
    response = m.get(netconf_filter)
    
    print(response)
    print()

    # openconfig-interfaces YANG data model
    netconf_filter = '''         
                      <filter>
                        <interfaces xmlns="http://openconfig.net/yang/interfaces">
                          <interface>
                          </interface>
                        </interfaces>
                      </filter>
                    '''
    
    response = m.get(netconf_filter)

    print(response)
    print()