import pandas as pd
import numpy as np
import xml.etree.cElementTree as et

tree=et.parse('osm_stops.add.xml')
root=tree.getroot()
# print(root[2])

root=tree.getroot()
print(root.attrib)

root=tree.getroot()

polyDetails = []
sub = ''

print("--------------------------------")
i = 0
for poly in root:
	i+=1
	# print(i)
	# print(poly.attrib.get('type') == sub)
	try: 
		# if sub in (poly.attrib.get('type')):
			# print(poly.attrib)
		polyDetails.append(poly.attrib)
			# print(poly.attrib)
		# print((poly.attrib.get('id')))

			# np.average()
			# print(average(poly.attrib.get('shape'), axis=0))

	except: 
		continue 

df = pd.DataFrame.from_dict(polyDetails) 
df.to_csv (r'bus_stops.csv', index = False, header=True)


