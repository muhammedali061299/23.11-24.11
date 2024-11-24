from PyQt6.QtWidgets import *
uyg = QApplication([])

pencere = QWidget()
pencere.show()  

window1 = QWidget()
window1.show()  

xx = QWidget()
xx.show()
# print("===>",type(uyg))
uyg.exec() # exec() metodu uygulamayı çalışır durumda tutar
