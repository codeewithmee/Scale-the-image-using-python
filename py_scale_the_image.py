from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL import Image
import sys
import os 






class py_scale_the_image(QtWidgets.QWidget):
	"""docstring for py_scale_the_image"""
	def __init__(self):
		QMainWindow.__init__(self)
		self.file_path = ""
		self.setWindowTitle("Image Scaler")
		self.ui()
		self.show()


	def ui(self):
 		self.label_1 = QLabel("Select the Image TO Scale")
 		self.text_width = QLabel("Width")
 		self.text_heigth = QLabel("Height")
 		self.select_btn = QPushButton('Browse..',self)
 		self.type_space = QLineEdit('')
 		self.width = QLineEdit()
 		self.height = QLineEdit()
 		self.download_btn = QPushButton('Download',self)

 		hbox = QHBoxLayout()
 		hbox.addWidget(self.type_space)
 		hbox.addWidget(self.select_btn)
 		hbox.addWidget(self.download_btn)

 		vbox = QVBoxLayout()
 		vbox.addWidget(self.text_width)
 		vbox.addWidget(self.width)
 		vbox.addWidget(self.text_heigth)
 		vbox.addWidget(self.height)
 		vbox.addLayout(hbox)

 		self.setLayout(vbox)
 		self.select_btn.clicked.connect(lambda x : self.select_path() )
 		self.download_btn.clicked.connect(lambda x : self.image_scaler())

	def select_path(self):
 		options = QFileDialog.Options()
 		options |= QFileDialog.DontUseNativeDialog
 		self.file_path, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "", options=options)
 		self.type_space.setText(self.file_path)

	def image_scaler(self):
		try:
			im = Image.open(self.file_path)
			image_format = im.format
			width, height = im.size
			newsize = (int(self.width.text()),int(self.width.text()))
			im= im.resize(newsize)
			save_path = self.download_path(image_format)
			im.save(save_path) 
		except Exception as e:
			pass
	 		



	def download_path(self,format):
 		path, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()",f"Untitled.{format}","All Files (*);;Text Files (*.txt)")
 		return path
		
		



if __name__ == '__main__':
	App = QApplication(sys.argv)
	window = py_scale_the_image()
	sys.exit(App.exec())

