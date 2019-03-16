import sys
import matplotlib
matplotlib.use("Qt5Agg")

from PyQt5 import QtCore
import matplotlib as mpl

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QSizePolicy, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


class MatplotCanvas(FigureCanvas):
    """形成可选择类型的画布"""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
         # 配置中文显示
        mpl.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一个figure
        self.axes = self.fig.add_subplot(111, projection='3d') 
        
        FigureCanvas.__init__(self, self.fig)
        self.axes.mouse_init()
        self.setParent(parent)
        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
  
  
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()
        
    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MatplotCanvas(self, width=5, height=4, dpi=100)
        self.mpl_ntb = NavigationToolbar(self.mpl, self)  # 添加完整的 toolbar
        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)
        
    def createaxis(self,  scale = 1.0):
        x = Arrow3D([-0.5*scale,0.5*scale],[0,0],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="r")
        y = Arrow3D([0,0],[-0.5*scale,0.5*scale],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="g")
        z = Arrow3D([0,0],[0,0],[-0.5*scale,0.5*scale], mutation_scale=20, lw=1, arrowstyle="-|>", color="b")
        return x, y, z
        
    def drawVector(self, Pt =(1.0, 1.0, 1.0)):
        v = Arrow3D([0,Pt[0]],[0,Pt[1]],[0,Pt[2]], mutation_scale=10, lw=0.5, arrowstyle="-|>", color="y")
        self.mpl.axes.add_artist(v)
        
        
    def drawCoordsystem(self, scale = 1.0):
        x, y, z = self.createaxis(scale)
        self.mpl.axes.add_artist(x)
        self.mpl.axes.add_artist(y)
        self.mpl.axes.add_artist(z)
        
    def SetViewRange(self,  scale = 1.0):
        self.mpl.axes.set(xlim=(-1*scale, 1*scale), ylim=(-1*scale, 1*scale), zlim=(-1*scale, 1*scale))
        
     
     
#        self.mpl.axes.scatter(0.0, 0.0, 0.0)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
#    ui.drawCoordsystem()
    ui.show()
    sys.exit(app.exec_())
