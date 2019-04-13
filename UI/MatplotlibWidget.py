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
import matplotlib.animation as animation


class MatplotCanvas(FigureCanvas):
    """形成可选择类型的画布"""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
         # 配置中文显示
        mpl.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一个figure
        self.axes = self.fig.add_subplot(111, projection='3d') 
        
        self.axes.set_aspect('equal')
        
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
#        self._verts3d = [-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5] 

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
        
    def change_verts3d(self, X_diff, Y_diff, Z_diff):
        self._verts3d = X_diff, Y_diff, Z_diff
        self.stale = True


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
        x = Arrow3D([-0.5*scale,0.5*scale],[0,   0],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="r")
        y = Arrow3D([0,0],[-0.5*scale,0.5*scale],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="g")
        z = Arrow3D([0,0],[0,0],[-0.5*scale,0.5*scale], mutation_scale=20, lw=1, arrowstyle="-|>", color="b")
#        x.set_animated(False)
#        x.set_positions((0, 0, 0), (0.5, -0.5, 0.5))
#        x._verts3d =[0, 1], [0, 1], [0, 1]
#        x.stale =True
        return x, y, z
        
    def drawVector(self, Pt =(1.0, 1.0, 1.0)):
        v = Arrow3D([0,Pt[0]],[0,Pt[1]],[0,Pt[2]], mutation_scale=10, lw=0.5, arrowstyle="-|>", color="y")
        self.mpl.axes.add_artist(v)
        
        
    def drawCoordsystem(self, scale = 1.0):
        x, y, z = self.createaxis(scale)
        self.mpl.axes.add_artist(x)
        self.mpl.axes.add_artist(y)
        self.mpl.axes.add_artist(z)
        
    def direct_draw_CS(self, axis_x, axis_y, axis_z):
        self.mpl.axes.add_artist(axis_x)
        self.mpl.axes.add_artist(axis_y)
        self.mpl.axes.add_artist(axis_z)
        
    def drawAnotherCS(self, CS_o,CS_x, CS_y, CS_z):
        a = Arrow3D([CS_o[0], CS_x[0]], [CS_o[1], CS_x[1]], [CS_o[2], CS_x[2]], mutation_scale=20, arrowstyle='-|>', color='k')
        self.mpl.axes.add_artist(a)
        a = Arrow3D([CS_o[0], CS_y[0]], [CS_o[1], CS_y[1]], [CS_o[2], CS_y[2]], mutation_scale=20, arrowstyle='-|>', color='k')
        self.mpl.axes.add_artist(a)
        a = Arrow3D([CS_o[0], CS_z[0]], [CS_o[1], CS_z[1]], [CS_o[2], CS_z[2]], mutation_scale=20, arrowstyle='-|>', color='k')
        self.mpl.axes.add_artist(a)
        text_options = {'horizontalalignment': 'center',
                'verticalalignment': 'center',
                'fontsize': 14}
                
        # add label for origin
        self.mpl.axes.text(CS_o[0],CS_o[1],CS_o[2]-0.05,r'$o$', **text_options)
        self.mpl.axes.text(1.1*CS_x[0],1.1*CS_x[1],1.1*CS_x[2],r'$x_0$', **text_options)
        self.mpl.axes.text(1.1*CS_y[0],1.1*CS_y[1],1.1*CS_y[2],r'$y_0$', **text_options)
        self.mpl.axes.text(1.1*CS_z[0],1.1*CS_z[1],1.1*CS_z[2],r'$z_0$', **text_options)
        
        
    def SetViewRange(self,  scale = 1.0):
        self.mpl.axes.set(xlim=(-1*scale, 1*scale), ylim=(-1*scale, 1*scale), zlim=(-1*scale, 1*scale))
        
     
     
#        self.mpl.axes.scatter(0.0, 0.0, 0.0)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
#    ui.drawCoordsystem()
    ui.show()
    sys.exit(app.exec_())
