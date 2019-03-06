from xml.etree import ElementTree as ET
import pprint

#parse method returns the python object people normally store it in variable tree
tree = ET.parse('../../data/chapter3/data-text.xml')
#to traverse the tree we must get its root element 
root = tree.getroot()

data = root.find('Data')

all_data = []

for observations in data:
    record = {}
    for item in observations:
        lookup_key = list(item.attrib.keys())[0]
       
        if(lookup_key == 'Numeric'):
            rec_key = 'NUMERIC'
            rec_value = item.attrib['Numeric']
        else:
            rec_key = item.attrib[lookup_key]
            rec_value = item.attrib['Code']
        record[rec_key] = rec_value
    
    all_data.append(record)

pprint.pprint(all_data)