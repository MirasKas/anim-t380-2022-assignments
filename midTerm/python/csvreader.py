import sys
import csv
from pathlib import Path

cameraList = Path(__file__).with_name('cameraList.csv')

cameraType = []
resolution =[]
focalLength = []
filmBack = []

with cameraList.open('r') as f:
	file = csv.reader(f)
	heading = next(file)

	for row in file:	
		cameraType.append(row[0])
		resolution.append(row[1])
		focalLength.append(row[2])
		filmBack.append(row[3])


	print(cameraType)
	print(resolution)
	print(focalLength)
	print(filmBack)	



#    print(f.read())


#cameraList.close()




# Initialize 4 Arrays,
# Start loop
# Read Line
# Put element 0 in cameratype array
# Put element 1,2,3 in rest of the arrays
# Loop completes here