import sys
import csv
from pathlib import Path

# import maya.standalone as standalone
# from maya import cmds
# from maya import mel
# from maya import OpenMayaUI as omui 
# from shiboken2 import wrapInstance

from PySide2 import QtGui, QtCore
from PySide2.QtCore import Qt
from PySide2 import QtUiTools
from PySide2.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit,QVBoxLayout,QGridLayout,QWidget,QPushButton,QInputDialog,QFileDialog
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

# def maya_main_window():	
#     mayaMainWindowPtr = omui.MQtUtil.mainWindow()

#     if sys.version_info.major >= 3:
#         return wrapInstance(int(mayaMainWindowPtr),QWidget )

#     else:  
#         return wrapInstance(long(mayaMainWindowPtr), QWidget)

class CreateCameraUI(QMainWindow):
    
    def __init__(self):
        super(CreateCameraUI, self).__init__()

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

        self.selectBtn = QPushButton("Select",self)
        layout.addWidget(self.selectBtn, 1,0)
        self.selectBtn.pressed.connect(self.open_dialog_box)


        self.cameraSelect = QComboBox(self)
        layout.addWidget(self.cameraSelect, 2, 0)
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


#Creates button
        self.createBtn = QPushButton("Create", self)
        layout.addWidget(self.createBtn, 2, 3)
        self.createBtn.pressed.connect(self.populateCameraSettings)


        # cameraSelect.currentIndexChanged.connect(self.index_changed)
        # cameraSelect.currentTextChanged.connect(self.text_changed)

        
        self.setCentralWidget(widget)
  
   # def index_changed(self, i):

    def selectCameraFile(self):
        print("Select File")

    def open_dialog_box(self):
        filename = QtGui.QFileDialog.getOpenFileName(parent=self, caption='Open file', dir='.', filter='(*.csv)')


    def setCameraType(self,cameraType):
        self.cameraType = cameraType
    

    def populateCameraSettings(self):
        content = self.cameraSelect.currentText()
        index = cameraType.index(content)
        selectedCamera=[]
        #selectedCamera.append(content)
        selectedCamera.append(resolutionCam[index])
        selectedCamera.append(focalLength[index])
        selectedCamera.append(filmBack[index])
        print(selectedCamera)

    def makeCamera():
        newCam = cmds.camera()
        cmds.rename(newCam[0],"Shot Cam")





# Maya Stuff


# Create a window
tool = QApplication(sys.argv)
window = CreateCameraUI()

window.show()
tool.exec_()
# Starts loop

   
    


