from maya import OpenMayaUI as omui 
from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance 
import sys
from maya import mel 

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
		
	

	def comboChange(self, text):
		self.cmd = 'poly' + text + '()'

	def createBtnClicked(self):
		mel.eval( self.cmd ) 
	
	def applyBtnClicked(self):
		print("hi")
	
	def closeBtnClicked(self):
		self.close()  
	

if __name__ == "__main__":	

	my_widget = MyMayaWidget()     
	my_widget.show()
   
