import sys
from PyQt5.QtCore import pyqtSlot, QStringListModel, QModelIndex
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QTreeWidgetItem, QDoubleSpinBox
from UI.Ui_basicUI import Ui_MainWindow
from CoordinateSet import CoordinateSet
import matplotlib.animation as animation


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self,  parent=None): #m_Set = set() 
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
#        self.widget.setVisible(True)  # 绘图区域初始化为不可见
        self.m_PtSet = CoordinateSet()
        self.PtSet = self.m_PtSet.BasicSet #引用同一个主集合    
        
        self.PtInputTableWidget.setRowCount(1)
        self.PtInputTableWidget.setColumnCount(3)
        self.PtInputTableWidget.setHorizontalHeaderLabels(['X', 'Y', 'Z'])
        self.PtInputTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.PtInputTableWidget.setItem(0, 0, QTableWidgetItem("0.0"))
        self.PtInputTableWidget.setItem(0, 1, QTableWidgetItem("0.0"))
        self.PtInputTableWidget.setItem(0, 2, QTableWidgetItem("0.0"))
        
        
        self.CSEulerTableWidget.setRowCount(1)
        self.CSEulerTableWidget.setColumnCount(3)
        self.CSEulerTableWidget.setHorizontalHeaderLabels(['psi', 'theta', 'phi'])
        self.CSEulerTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.CSEulerTableWidget.horizontalHeader().setHighlightSections(True) 
        
        self.psiSpin = QDoubleSpinBox()
        self.psiSpin.setRange(-3.14, 3.14)
        self.psiSpin.setDecimals(2)
        self.psiSpin.setSingleStep(0.01)
        self.psiSpin.valueChanged.connect(self.CSparmChange)
        self.CSEulerTableWidget.setCellWidget(0, 0, self.psiSpin)
      
      
#        self.CSEulerTableWidget.setItem(0, 0, QTableWidgetItem("0.0"))

        self.thetaSpin = QDoubleSpinBox()
        self.thetaSpin.setRange(-3.14, 3.14)
        self.thetaSpin.setDecimals(2)
        self.thetaSpin.setSingleStep(0.01)
        self.thetaSpin.valueChanged.connect(self.CSparmChange)
        self.CSEulerTableWidget.setCellWidget(0, 1, self.thetaSpin)

#        self.CSEulerTableWidget.setItem(0, 1, QTableWidgetItem("0.0"))

        self.phiSpin = QDoubleSpinBox()
        self.phiSpin.setRange(-3.14, 3.14)
        self.phiSpin.setDecimals(2)
        self.phiSpin.setSingleStep(0.01)
        self.phiSpin.valueChanged.connect(self.CSparmChange)
        self.CSEulerTableWidget.setCellWidget(0, 2, self.phiSpin)


#        self.CSEulerTableWidget.setItem(0, 2, QTableWidgetItem("0.0"))
        
      
        self.CSTRTableWidget.setRowCount(1)
        self.CSTRTableWidget.setColumnCount(3)
        self.CSTRTableWidget.setHorizontalHeaderLabels(['X', 'Y', 'Z'])
        self.CSTRTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.TRxSpin = QDoubleSpinBox()
        self.TRxSpin.setRange(-3, 3)
        self.TRxSpin.setDecimals(2)
        self.TRxSpin.setSingleStep(0.01)
        self.TRxSpin.valueChanged.connect(self.CSparmChange)
        self.CSTRTableWidget.setCellWidget(0, 0, self.TRxSpin)
        
        self.TRySpin = QDoubleSpinBox()
        self.TRySpin.setRange(-3, 3)
        self.TRySpin.setDecimals(2)
        self.TRySpin.setSingleStep(0.01)
        self.TRySpin.valueChanged.connect(self.CSparmChange)
        self.CSTRTableWidget.setCellWidget(0, 1, self.TRySpin)
        
        
        self.TRzSpin = QDoubleSpinBox()
        self.TRzSpin.setRange(-3, 3)
        self.TRzSpin.setDecimals(2)
        self.TRzSpin.setSingleStep(0.01)
        self.TRzSpin.valueChanged.connect(self.CSparmChange)
        self.CSTRTableWidget.setCellWidget(0, 2, self.TRzSpin)
        
        
        
        self.VectorShowCheckBox.setChecked(True)
        self.CoordinateRadioButton.setChecked(True)
        
        self.PtShowWidget.direct_draw_CS(self.m_PtSet.axis_x,self.m_PtSet.axis_y, self.m_PtSet.axis_z)
#        self.PtShowWidget.drawCoordsystem(2.0)
        
        
        self.PtShowWidget.SetViewRange(3.0)
#        self.PtShowWidget.drawVector()
        # test code district
        
#        m_PtSet.Set_BaseCS(input_psi = 1.0, input_theta = 1.0,  input_phi = 1.0,  input_o = [0.5, -0.4, 0.2])
#        self.PtShowWidget.drawAnotherCS(m_PtSet.o,m_PtSet.x0, m_PtSet.y0, m_PtSet.z0 )
        



        self.PtSetListView.clicked.connect(self.ChooseItem)
        self.beChosedItemIndex = None
        self.slm=QStringListModel()
        self.qList = []
        self.ViewToModeldict = {}
        
        self.CStreeWidget.setColumnCount(2)
        self.CStreeWidget.setHeaderLabels(['坐标系','点集'])
        self.CSroot = QTreeWidgetItem(self.CStreeWidget)
        self.CSroot.setText(0, 'CS ID')
        self.CStreeWidget.setColumnWidth(0, 80)
        QTreeWidgetItem(self.CSroot).setText(1, '(0.0,0.0,0.0)')
        self.CStreeWidget.expandAll()
        
        self.TFMatrixtableWidget.setRowCount(4)
        self.TFMatrixtableWidget.setColumnCount(4)
        self.TFMatrixtableWidget.setHorizontalHeaderLabels(['R0', 'R1', 'R2','T'])
        self.TFMatrixtableWidget.setVerticalHeaderLabels(['R0', 'R1', 'R2','T'])
        self.TFMatrixtableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.TFMatrixtableWidget.resizeColumnsToContents()
        
        
    def ChooseItem(self, qModelIndex): 
        self.beChosedItemIndex = qModelIndex.row()
        
        
    def CSparmChange(self): 
        #CS change
        
#        m_PtSet = CoordinateSet()
        cur_psi = self.psiSpin.value()
        cur_theta = self.thetaSpin.value()
        cur_phi = self.phiSpin.value()
        cur_o = [self.TRxSpin.value(), self.TRySpin.value(), self.TRzSpin.value()]
        self.m_PtSet.Set_BaseCS(input_psi = cur_psi, input_theta = cur_theta,  input_phi = cur_phi,  input_o = cur_o)
#        self.PtShowWidget.drawAnotherCS(m_PtSet.o,m_PtSet.x0, m_PtSet.y0, m_PtSet.z0 )
#        self.PtShowWidget.mpl.draw()


    # 用于更新绘图数据的函数
    def cs_animate(self, i):
        part = float(i)/100.0
        self.m_PtSet.Set_BaseCS(input_psi = self.animation_cur_psi *part,
            input_theta = self.animation_cur_theta*part, 
            input_phi = self.animation_cur_phi *part, 
            input_o =  [part*x for x in self.animation_cur_o ])
        o=self.m_PtSet.o
        x=self.m_PtSet.x0
        y=self.m_PtSet.y0
        z= self.m_PtSet.z0
        self.m_PtSet.axis_x.change_verts3d([o[0], x[0]], [o[1], x[1]], [o[2], x[2]])
        self.m_PtSet.axis_y.change_verts3d([o[0], y[0]], [o[1], y[1]], [o[2], y[2]])
        self.m_PtSet.axis_z.change_verts3d([o[0], z[0]], [o[1], z[1]], [o[2], z[2]])
        self.PtShowWidget.mpl.draw()
        return self.m_PtSet.axis_x, self.m_PtSet.axis_y, self.m_PtSet.axis_z
        
    def animation_init(self):
        self.animation_cur_psi = self.psiSpin.value()
        self.animation_cur_theta = self.thetaSpin.value()
        self.animation_cur_phi = self.phiSpin.value()
        self.animation_cur_o = [self.TRxSpin.value(), self.TRySpin.value(), self.TRzSpin.value()]

        self.m_PtSet.axis_x.change_verts3d([0, 1], [0, 0], [0, 0])
        self.m_PtSet.axis_y.change_verts3d([0, 0], [0, 1], [0, 0])
        self.m_PtSet.axis_z.change_verts3d([0, 0], [0, 0], [0, 1])
        
        return self.m_PtSet.axis_x, self.m_PtSet.axis_y, self.m_PtSet.axis_z
        
    @pyqtSlot()
    def on_AnimationButton_clicked(self):
        
        x, y, z = self.PtShowWidget.createaxis(1.0)
        
        #FuncAnimation(fig, func, frames=None, init_func=None, fargs=None, save_count=None, **kwargs)
        self.anim = animation.FuncAnimation(self.PtShowWidget.mpl.fig, self.cs_animate,  # 传入之前定义的两个函数
                               init_func=self.animation_init, 
                               frames=100, # 传入更新绘图数据的参数，此处代表animate函数的
                                           # 参数i从1变化到360
                               interval=10,  # 刷新速率
                               blit=False)  # 重叠区域不重绘（可提升效率）
        self.PtShowWidget.mpl.draw()
        pass
        
    def on_CSAddButton_clicked(self):
#        m_PtSet = CoordinateSet()
#        self.PtShowWidget.drawAnotherCS(self.m_PtSet.o,self.m_PtSet.x0, self.m_PtSet.y0, self.m_PtSet.z0 )
        o=self.m_PtSet.o
        x=self.m_PtSet.x0
        y=self.m_PtSet.y0
        z= self.m_PtSet.z0
        self.m_PtSet.axis_x.change_verts3d([o[0], x[0]], [o[1], x[1]], [o[2], x[2]])
        self.m_PtSet.axis_y.change_verts3d([o[0], y[0]], [o[1], y[1]], [o[2], y[2]])
        self.m_PtSet.axis_z.change_verts3d([o[0], z[0]], [o[1], z[1]], [o[2], z[2]])
        self.PtShowWidget.mpl.draw()
    
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
