import sys
import SynFrame
from PyQt5.QtWidgets import QApplication
from CoordinateSet import CoordinateSet

def main():
    app = QApplication(sys.argv)
    m_PtSet = CoordinateSet()
    ui = SynFrame.MainWindow(m_PtSet.BasicSet)
    ui.show()
    sys.exit(app.exec_())
 
    
    
if __name__ == "__main__":
    
    main()
   
