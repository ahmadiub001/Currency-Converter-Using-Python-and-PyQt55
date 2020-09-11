from PyQt5 import QtWidgets, uic

def convert():
    dlg.lineEdit_2.setText(str(float(dlg.lineEdit.text())*166.46))

def convert2():
    dlg.lineEdit_4.setText(str(float(dlg.lineEdit_3.text())*197.29))
    

app = QtWidgets.QApplication([])
dlg = uic.loadUi("test.ui")

dlg.lineEdit.setFocus() # to have already cursor in the first line edit

# these lines gives funtionallity to pish button 
dlg.pushButton.clicked.connect(convert)
dlg.pushButton_2.clicked.connect(convert2)

#there lines of code connect puch button to (Enter Button)
dlg.lineEdit.returnPressed.connect(convert)
dlg.lineEdit_3.returnPressed.connect(convert2)
#there two line to make the line edit box that no one can write any value in it 
dlg.lineEdit_2.setReadOnly(True)
dlg.lineEdit_4.setReadOnly(True)




dlg.show()
app.exec()
