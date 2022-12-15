import pandas as pd
import numpy as np
import xml.etree.cElementTree as et

tree=et.parse('osm_ptlines.xml')
root=tree.getroot()



# print(root[1])

# root=tree.getroot()
# print(root.attrib)

# root=tree.getroot()
# root=tree.getroot()


# root=tree.getroot()
# print(root.attrib)


lineDetails = []
moredetails=[]
sub = 'bus'

print("--------------------------------")
i = 0
for line in root.iter('route'):
	i+=1
	# print(i)
	# print(poly.attrib.get('type') == sub)
	# print(line.iter('id'))
	# print(line.attrib)

	try: 
		# print(child[0])
		print((line.attrib))
		lineDetails.append((line.attrib))

		if sub in (line.attrib.get('type')):
			# print(line.attrib.get('id'))
			# lineDetails.append(line.attrib.get('id'))
			# lineDetails.append(line.attrib)
			# lineDetails.append(line[0].attrib)

			# moredetails.append(line[0].attrib.get('edges'))
			# print(poly.attrib)
			pass
		# print((poly.attrib.get('id')))

			# np.average()
			# print(average(poly.attrib.get('shape'), axis=0))
		pass

	except: 
		continue 

df = pd.DataFrame.from_dict(lineDetails) 


df.to_csv (r'bus_lines.csv', index = False, header=True)


