from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt

def mach_will ():
    plt.clf()

    plt.savefig( 'mach_will.png' )


app = QApplication( sys.argv )
window = QWidget()

window.setWindowTitle( 'bio3g802r705' )
window.resize( 300, 600 )

btnGenpic = QtWidgets.QPushButton( 'generate pic' )
btnClopic = QtWidgets.QPushButton( 'close pic' )

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget ( btnClopic )
vbox.addWidget ( btnGenpic )

btnGenpic.clicked.connect( mach_will )

window.setLayout( vbox )



window.show()
sys.exit( app.exec_() )
