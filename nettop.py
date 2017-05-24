import json
def test(data):
    """
    Converts a NetJSON 'NetworkGraph' object
    to a NetworkX Graph object,which is then returned.
    Additionally checks for protocol version, revision and metric.
    """
    net = {}
    network = {}
    network1 = []
    network2 = []
    with open(data) as json1:
        data1 = json.load(json1)
        # ensure is NetJSON NetworkGraph object
        d = {}
        l = {}
        a = {}
        b = {}
        c = {}
        type1 = data1['type']
    with open('./result_admin.json', 'w') as json_data:
        net["type"] = type1
        for node in data1["openstack_ports"]:
            for data2 in node["fixed_ips"]:
                b["ip_address"] = (data2['ip_address'])
                b["mac_address"] = (node['mac_address'])
            d["id"] = (node['network_id'])
            d["id"] = (node['device_id'])
            d["type"] = (node['device_owner'])
            d["properties"] = b.copy()
            if d not in network1:
                    network1.append(d.copy())
        for node in data1["openstack_routers"]:
            for data2 in node["external_gateway_info"]["external_fixed_ips"]:
                c["ip_address"] = (data2['ip_address'])
                c["router_name"] = (node['name'])
            d["id"] = (node['external_gateway_info']['network_id'])
            d["type"] = (node['availability_zones'][0])
            d["properties"] = c.copy()
            #print d["id"]
            network1.append(d.copy())
        network["nodes"] = network1
        for link in data1["openstack_ports"]:
            a["status"] = link["status"]
            a["admin_state_up"] = link["admin_state_up"]
            a["lq"] = link["lq"]
            a["nlq"] = link["nlq"]
            a["bitrate"] = link["bitrate"]
            a["latency"] = link["type"]
            l["source"] = link["network_id"]
            l["target"] = link["device_id"]
            l["properties"] = a.copy()
            network2.append(l.copy())
        for link in data1["openstack_routers"]:
            a["status"] = link["status"]
            a["admin_state_up"] = link["admin_state_up"]
            a["lq"] = link["lq"]
            a["nlq"] = link["nlq"]
            a["bitrate"] = link["bitrate"]
            a["latency"] = link["type"]
            l["source"] = link['external_gateway_info']["network_id"]
            l["target"] = link["id"]
            l["properties"] = a.copy()
            network2.append(l.copy())
        network["links"] = network2
        net["network"] = network
        json.dump(net, json_data)
test('admin.json')