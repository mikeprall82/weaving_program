ls
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Weaving Program MVP')
window.setGeometry(100, 100, 400, 300)

label = QLabel('Hello, Weaver!', parent=window)
label.move(150, 130)

window.show()
sys.exit(app.exec_())

