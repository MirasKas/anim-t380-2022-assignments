from re import L
import sys
import csv
from pathlib import Path
# import maya.cmds as cmdc
# import maya.standalone
# from maya import OpenMayaUI as omui 

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit,QVBoxLayout,QGridLayout,QWidget,QPushButton,
)
 

cameraList = Path(__file__).with_name('cameraList.csv')

cameraType = []
resolutionCam =[]
focalLength = []
filmBack = []

with cameraList.open('r') as f:
	file = csv.reader(f)
	heading = next(file)

	for row in file:	
		cameraType.append(row[0])
		resolutionCam.append(row[1])
		focalLength.append(row[2])
		filmBack.append(row[3])
	


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Maya Camera Tool")
        self.setMinimumWidth(600)
        self.cameraType=""

        layout = QGridLayout()
        boxLayout = QVBoxLayout() 
        self.setLayout(layout)

        widget = QWidget()
        widget.setLayout(layout)



        header = QLabel("Camera Settings")
        font = header.font()
        font.setPointSize(20)
        header.setFont(font)
        header.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        layout.addWidget(header, 0, 0)

        
        self.cameraSelect = QComboBox(self)
        layout.addWidget(self.cameraSelect, 1, 0)
        self.cameraSelect.addItems(cameraType)


    
       

        # resolution = QComboBox()
        # layout.addWidget(resolutionCam, 1, 1)
        # resolution.addItems(resolution)

        # fLength = QComboBox()
        # layout.addWidget(fLength, 1, 2)
        # fLength.addItems(focalLength)
        
        # fBack = QComboBox()
        # layout.addWidget(fBack, 1, 3)
        # fBack.addItems(filmBack)

        self.createBtn = QPushButton("Create")
        layout.addWidget(self.createBtn, 2, 3)
        self.createBtn.pressed.connect(self.find)


        # cameraSelect.currentIndexChanged.connect(self.index_changed)
        # cameraSelect.currentTextChanged.connect(self.text_changed)

        
        self.setCentralWidget(widget)
  
   # def index_changed(self, i):

    def setCameraType(self,cameraType):
        self.cameraType = cameraType
    

    def find(self):
        content = self.cameraSelect.currentText()
        index = cameraType.index(content)
        selectedCamera=[]
        #selectedCamera.append(content)
        selectedCamera.append(resolutionCam[index])
        selectedCamera.append(focalLength[index])
        selectedCamera.append(filmBack[index])
        print(selectedCamera)

    def makeCamera():
        newCam = mc.camera()





# Maya Stuff


# Create a window
tool = QApplication(sys.argv)
window = MainWindow()

window.show()
tool.exec_()
# Starts loop

   
    


