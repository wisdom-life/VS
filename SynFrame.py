import sys
from PyQt5.QtCore import pyqtSlot, QStringListModel, QModelIndex
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem
from UI.Ui_basicUI import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, m_Set = set() , parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
#        self.widget.setVisible(True)  # 绘图区域初始化为不可见
        
        self.PtSet = m_Set #引用同一个主集合    
        
        self.PtInputTableWidget.setRowCount(1)
        self.PtInputTableWidget.setColumnCount(3)
        self.PtInputTableWidget.setHorizontalHeaderLabels(['X', 'Y', 'Z'])
        self.PtInputTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.PtInputTableWidget.setItem(0, 0, QTableWidgetItem("0.0"))
        self.PtInputTableWidget.setItem(0, 1, QTableWidgetItem("0.0"))
        self.PtInputTableWidget.setItem(0, 2, QTableWidgetItem("0.0"))
        
        self.VectorShowCheckBox.setChecked(True)
        self.CoordinateRadioButton.setChecked(True)
        self.PtShowWidget.drawCoordsystem(2.0)
        self.PtShowWidget.SetViewRange(3.0)
#        self.PtShowWidget.drawVector()
        self.PtSetListView.clicked.connect(self.ChooseItem)
        self.beChosedItemIndex = None
        self.slm=QStringListModel()
        self.qList = []
        self.ViewToModeldict = {}
        
    def ChooseItem(self, qModelIndex): 
        self.beChosedItemIndex = qModelIndex.row()
        
    @pyqtSlot()
    def on_PtAddButton_clicked(self):
        xx = self.PtInputTableWidget.item(0, 0).text()
        yy = self.PtInputTableWidget.item(0, 1).text()
        zz = self.PtInputTableWidget.item(0, 2).text()
        
        str = '(%s,%s,%s)'%(xx, yy, zz) 
        self.ViewToModeldict[str] = (float(xx), float(yy), float(zz)) #create map view content
        self.PtSet.add(self.ViewToModeldict[str])
        
        self.PtSetListShow()
        
        self.PtShowWidget.mpl.axes.cla()
        
        self.DrawAllVector( Pt = self.PtSet)
      
        
#        self.PtShowWidget.drawVector((float(xx), float(yy), float(zz)))
        
#        self.PtShowWidget.mpl.draw()
#        slm=QStringListModel();
#        self.qList = ["( "+xx+" , "+yy+" , "+ zz+" )"]
#        slm.setStringList(self.qList)
#        self.PtSetListView.setModel(slm)
    
   
    def on_PtDelButton_clicked(self):
#        print(self.qList[self.beChosedItemIndex])

        if self.beChosedItemIndex is None:
            return
#        print((float(num) for num in self.qList[self.beChosedItemIndex]))

        self.PtSet.remove(self.ViewToModeldict[self.qList[self.beChosedItemIndex]])
        self.ViewToModeldict.pop(self.qList[self.beChosedItemIndex])
#        self.PtSet.discard((float(num) for num in self.qList[self.beChosedItemIndex]))
        
        del self.qList[self.beChosedItemIndex]
        
#        slm=QStringListModel()
        self.slm.setStringList(self.qList)
        self.PtSetListView.setModel(self.slm)
        self.beChosedItemIndex = None
    
        self.PtShowWidget.mpl.axes.cla()
        self.DrawAllVector( Pt = self.PtSet)
        self.PtShowWidget.mpl.draw()
        
    def PtSetListShow(self):
        self.qList.clear()
        #self.PtSetListView.
        self.qList = list(self.ViewToModeldict.keys())
#        self.qList = ["( "+str(xx)+" , "+str(yy)+" , "+ str(zz)+" )" for (xx, yy, zz) in self.PtSet]

        self.slm.setStringList(self.qList)
        self.PtSetListView.setModel(self.slm)
    
    def DrawAllVector(self, Pt = set(), has_Coor = True):
        if len(Pt) is 0 :
            return
            
        if has_Coor:
            self.PtShowWidget.drawCoordsystem(2.0)
            self.PtShowWidget.SetViewRange(3.0)
            
        for e in Pt:
            self.PtShowWidget.drawVector(e)
            
        self.PtShowWidget.mpl.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
