'''
asset exporter
'''
import maya.cmds as cmds
import os
import json
from maya import OpenMayaUI as omui 
from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance 



# Get a reference to the main Maya application window
def maya_main_window():	
	mayaMainWindowPtr = omui.MQtUtil.mainWindow()

	if sys.version_info.major >= 3:
		return wrapInstance(int(mayaMainWindowPtr),QWidget )

	else:  
		return wrapInstance(long(mayaMainWindowPtr), QWidget)


class MyMayaWidget(QMainWindow):    
	def __init__(self, *args, **kwargs):        
		super(MyMayaWidget, self).__init__(*args, **kwargs)
		
		self.setWindowTitle("polyCreate")
		self.setGeometry(500, 300, 400, 100)
		self.controlUI()
		self.cmd = 'polyCone'
		
		self.combo = QComboBox(self) 
		self.combo.addItem('Cone')        
		self.combo.addItem('Cube')        
		self.combo.addItem('Sphere')        
		self.combo.addItem('Torus')        
		self.combo.setCurrentIndex(1)        
		self.combo.move(20, 20)        
		self.combo.activated[str].connect(self.comboChange)    

		# Parent widget under Maya main window        
	
	
	def controlUI(self):
		

		createButton = QPushButton("Create")
		applyButton = QPushButton("Apply")
		closeButton = QPushButton("Close")

		hBoxLayout = QHBoxLayout()
		hBoxLayout.addWidget(createButton)
		hBoxLayout.addWidget(applyButton)
		hBoxLayout.addWidget(closeButton)

		vBoxLayout = QVBoxLayout()
		vBoxLayout.addStretch(1)
		vBoxLayout.addLayout(hBoxLayout)

		widget = QWidget(self)
		widget.setLayout(vBoxLayout)
		self.setCentralWidget(widget)

		createButton.clicked.connect(self.createBtnClicked)
		applyButton.clicked.connect(self.applyBtnClicked)
		closeButton.clicked.connect(self.closeBtnClicked)


#function for checking UVs
#works by checking the history of the object for anything UV related that has been done - does not work if history has already been deleted
def checkUVs():
    UVHistory = ["polyTweak", "polyMapSewMove", "polyAutoProjection"] #should be a list of all UV related commands

    objHistory = cmds.listHistory()
    print(objHistory)

    uvHist = []

    for ele in UVHistory:
        if any(ele in s for s in objHistory):
            uvHist.append(True)
        else:
            uvHist.append(False)

    if all(item is False for item in uvHist):
        print("no UVS") #replace with pop up - "[obj name] has no UV history. Please check to make sure proper UVs have been applied"
        #Check now -> opens UV window, Continue exporting -> keeps the script going
    else:
        print("Object has UVs") #script continues

#function for reselecting the selected objects after cycling through them
def reselectList():
    for obj in selected:
        cmds.select(obj, add=True)





#get settings from program files - user needs to copy file here
f = open("C:/Program Files/settings.json")

settings = json.load(f)

#asset information for naming - should be inputted by user through UI
assetInfo = {
"asset": "testAsset",
"location": "basement", #location is either basement, groundFloor, or secondFloor
"version": 1,
"projectDirectory": settings.get("projectDirectory")
} #temp values

#file path
filePathFormat = "{projectDirectory}/ShadyCreekLodge/Content/ShadyCreekLodge/Assets/Environment/{location}/{asset}_{location}_V{version}.fbx"

selected = cmds.ls(selection=True)

#check UVs for each object
#this has to be done before history is deleted for any object in case user wants to interrupt
for obj in selected:
    cmds.select(obj)
    checkUVs()

reselectList()

#Freeze transforms
cmds.makeIdentity(a=True)

#delete history
cmds.delete(constructionHistory = True)

#export file
cmds.file(filePathFormat.format(**assetInfo), force=True, exportSelected = True, type = 'FBX export')

#ui confirmation of exported asset


if __name__ == "__main__":	

	my_widget = MyMayaWidget()     
	my_widget.show()
   