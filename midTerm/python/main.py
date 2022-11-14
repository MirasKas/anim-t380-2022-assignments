import sys
import csv
from pathlib import Path

from maya import cmds
from maya import mel
from maya import OpenMayaUI as omui 
from shiboken2 import wrapInstance

from PySide2 import QtGui, QtCore
from PySide2.QtCore import Qt
from PySide2 import QtUiTools
from PySide2.QtWidgets import (
	QMainWindow, QApplication,
	QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
	QLineEdit,QVBoxLayout,QGridLayout,QWidget,QPushButton,QInputDialog,QFileDialog
)
 
def maya_main_window():	
	mayaMainWindowPtr = omui.MQtUtil.mainWindow()

	if sys.version_info.major >= 3:
		return wrapInstance(int(mayaMainWindowPtr),QWidget )

	else:  
		return wrapInstance(long(mayaMainWindowPtr), QWidget)

class CreateCameraUI(QWidget):
	
	def __init__(self, *args,**kwargs):
		self.cameraType = []
		self.resolutionCam =[]
		self.focalLength = []
		self.filmBack = []
		self.selectedCamera=[]

		
		super(CreateCameraUI, self).__init__(*args,**kwargs)
		self.setParent(maya_main_window())
		self.setWindowFlags(Qt.Window)

		self.setWindowTitle("Maya Camera Tool")
		self.setMinimumWidth(600)
		
		self.filename=""
		self.file=""

		layout = QGridLayout()
		boxLayout = QVBoxLayout() 
		self.setLayout(layout)

		# widget = QWidget()
		# widget.setLayout(layout)

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
		

		#Creates button
		self.createBtn = QPushButton("Create", self)
		layout.addWidget(self.createBtn, 2, 3)
		self.createBtn.pressed.connect(self.populateCameraSettings)
	
		# self.setCentralWidget(widget)
  
   # def index_changed(self, i):

	def selectCameraFile(self):
		print("Select File")

	def open_dialog_box(self):
		# print(self.filename)
		# print('Here 1')
		self.filename = QFileDialog.getOpenFileName(parent=self, caption='Open file', dir='.', filter='(*.csv)')
		# print(self.filename)
		# print('Here 2')
		self.filename = Path(self.filename[0])
		# print(self.filename)

		with self.filename.open('r') as f:
			self.file = csv.reader(f)
			self.heading = next(self.file)

			for row in self.file:	
				# print('Here 3')
				# print(row)
				self.cameraType.append(row[0])
				self.resolutionCam.append(row[1])
				self.focalLength.append(row[2])
				self.filmBack.append(row[3])
				# print(self.cameraType, self.resolutionCam, self.focalLength, self.filmBack)

		self.cameraSelect.addItems(self.cameraType)

			

	def setCameraType(self,cameraType):
		self.cameraType = cameraType

	def populateCameraSettings(self):
	
		
		content = self.cameraSelect.currentText()
		index = self.cameraType.index(content)
		
		#selectedCamera.append(content)
		self.selectedCamera.append(self.resolutionCam[index])
		self.selectedCamera.append(float(self.focalLength[index]))
		self.selectedCamera.append(self.filmBack[index])
		# print(self.selectedCamera)
		# cameraValues = selectedCamera[index]

		apeture = self.selectedCamera[2]
		apeture = apeture.split(' x ')
		# print(apeture)
		self.selectedCamera.pop()
		self.selectedCamera.append(float(apeture[0]))
		self.selectedCamera.append(float(apeture[1]))
		# print(self.selectedCamera)

	# def makeCamera(self):
		newCam = cmds.camera( displayResolution = True, hfa = self.selectedCamera[2],
		vfa = self.selectedCamera[3], fl= self.selectedCamera[1], name = content)
		
		
		self.selectedCamera = []


if __name__ == "__main__":
	

	cameraUI = CreateCameraUI()
	cameraUI.show()
	

	

	


# Maya Stuff

# Create a window
# tool = QApplication(sys.argv)
# window = CreateCameraUI()

# window.show()
# tool.exec_()
# Starts loop

   
	


