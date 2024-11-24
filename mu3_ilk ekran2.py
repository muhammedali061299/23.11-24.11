from PyQt6.QtWidgets import *
uyg = QApplication([])

pencere = QWidget()
pencere.show()  

window1 = QWidget()
window1.show()  

xx = QWidget()
xx.show()



uyg.exec()

print("Birinci uygulama bitti, 2.ye geçiliyor.")
uyg1 = QApplication([])
yy = QWidget()
yy.show()
uyg1.exec()