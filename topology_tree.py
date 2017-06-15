import json

link_list1 = [{
    "source": "com.company.object.kind.type.subtype.family.Feline",
    "target": "com.company.object.kind.type.subtype.family.species.Cat"
}, {
    "source": "com.company.object.kind.type.subtype.Mammal",
    "target": "com.company.object.kind.type.subtype.family.Feline"
}, {
    "source": "com.company.object.Being",
    "target": "com.company.object.kind.LivingBeing"
}, {
    "source": "com.company.object.kind.type.subtype.family.Canine",
    "target": "com.company.object.kind.type.subtype.family.species.Wolf"
}, {
    "source": "com.company.object.kind.type.subtype.Mammal",
    "target": "com.company.object.kind.type.subtype.family.Canine"
}, {
    "source": "com.company.object.kind.type.Animal",
    "target": "com.company.object.kind.type.subtype.Mammal"
}, {
    "source": "com.company.object.kind.LivingBeing",
    "target": "com.company.object.kind.type.Animal"
}, {
    "source": "com.company.object.kind.type.Animal",
    "target": "com.company.object.kind.type.subtype.Fish"
}, {
    "source": "com.company.object.kind.StaticBeing",
    "target": "com.company.object.kind.type.Solid"
}, {
    "source": "com.company.object.Being",
    "target": "com.company.object.kind.StaticBeing"
}, {
    "source": "com.company.object.kind.type.subtype.family.Feline",
    "target": "com.company.object.kind.type.subtype.family.species.Lion"
}, {
    "source": "com.company.object.kind.type.subtype.family.Canine",
    "target": "com.company.object.kind.type.subtype.family.species.Hyena"
}, {
    "source": "com.company.object.kind.StaticBeing",
    "target": "com.company.object.kind.type.Liquid"
}]


input = {}
with open('result_all4.json') as json_data:
    input = json.load(json_data)

node_list = input["network"]["nodes"]
link_list = input["network"]["links"]



def find_top_element():
    source = None
    for item in link_list:
        source = item['source']
        is_parent = True
        for link in link_list:
            if source == link['target']:
                is_parent = False
                break
        if is_parent:
            break
    print 'Parent object %r' % get_node_element(source)
    return get_node_element(source)

def build_output(source):
    output = {}
    output['type'] = source['type']
    output['id'] = source['id']
    output['name'] = source.get('name')
    child_list = build_children(source)
    print 'Child list %r' % child_list
    if child_list is not None or len(child_list) > 0:
        print 'length of child %d' % len(child_list)
        output['children'] = []
        for element in child_list:
            op_tmp = build_output(element)
            print 'element %r' % op_tmp
            print 'Output Temp %r' % output['children']
            output['children'].append(op_tmp)
    return output


def build_children(source):
    child_list = []
    for item in link_list:
        if source['id'] == item['source']:
            child_list.append(get_node_element(item['target']))
    return child_list


def get_node_element(id):
    for item in node_list:
        if item['id'] == id:
            return item
    return None

def build_topology():
    #start = find_top_element()
    start = get_node_element('5cf6c558-e8b8-413c-b745-9ac391cnetfd')
    st_op = build_output(start)
    print st_op

build_topology()