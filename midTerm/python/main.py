from PySide2.QtWidgets import QApplication, QWidget
import sys

tool = QApplication(sys.argv)

# Create a window
window = QWidget()
window.show() 

# Starts loop
tool.exec_()