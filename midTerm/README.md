# ANIM T380 Mid Term
Problem 4

## Description
This script will create a simple GUI using PySide2 and populate scnes with cameras provided by a CSV list.

## Usage/Arguments


Populates arrays with the tables and rows from CSV list

```
with cameraList.open('r') as f:
	file = csv.reader(f)
	heading = next(file)

	for row in file:	
		cameraType.append(row[0])
		resolutionCam.append(row[1])
		focalLength.append(row[2])
		filmBack.append(row[3])


Creation of the Widget UI Window

```
class CreateCameraUI(QMainWindow):
    
    def __init__(self):
        super(CreateCameraUI, self).__init__()

        self.setWindowTitle("Maya Camera Tool")
        self.setMinimumWidth(600)
        self.cameraType=""
```

## Example
