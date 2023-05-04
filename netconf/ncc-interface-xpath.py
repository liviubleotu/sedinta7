from scrapli_netconf.driver import NetconfDriver

my_device = {
    "host": "192.168.0.47",
    "auth_username": "student",
    "auth_password": "cisco",
    "auth_strict_key": False,
    "port": 830
}

conn = NetconfDriver(**my_device)
conn.open()

ospf_xpath = '/ospf-oper-data/ospf-state/ospf-instance[af="address-family-ipv4" and router-id="2886755332"]/ospf-area[area-id=0]/ospf-interface[name="GigabitEthernet2"]/ospf-neighbor[neighbor-id="172.16.200.5"]/state'


response = conn.get(
    filter_=ospf_xpath, filter_type='xpath')
print(response.result)