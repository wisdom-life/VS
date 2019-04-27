import numpy as np

from UI.MatplotlibWidget  import Arrow3D

class CoordinateSet(object):
    """Represent 3D points in Special Frame"""
    
    BasicSet = set()
    
    # define origin
    o = np.array([0,0,0])
    
         # define ox0y0z0 axes
    x0 = np.array([1,0,0])
    y0 = np.array([0,1,0])
    z0 = np.array([0,0,1])
    
    psi = 0.0
    theta = 0.0
    phi = 0.0
  
#    # define ox1y1z1 axes
#    psi = 20 * np.pi / 180
#    x1 = Rz(psi).dot(x0)
#    y1 = Rz(psi).dot(y0)
#    z1 = Rz(psi).dot(z0)
#    
#    # define ox2y2z2 axes
#    theta = 10 * np.pi / 180
#    x2 = Rz(psi).dot(Ry(theta)).dot(x0)
#    y2 = Rz(psi).dot(Ry(theta)).dot(y0)
#    z2 = Rz(psi).dot(Ry(theta)).dot(z0)
#    
#    # define ox3y3z3 axes
#    phi = 30 * np.pi / 180
#    x3 = Rz(psi).dot(Ry(theta)).dot(Rx(phi)).dot(x0)
#    y3 = Rz(psi).dot(Ry(theta)).dot(Rx(phi)).dot(y0)
#    z3 = Rz(psi).dot(Ry(theta)).dot(Rx(phi)).dot(z0)
  
    
    def __init__(self, *args):
        
        self.Set_BaseCS()
        self.scale = 2.0
        self.axis_x = Arrow3D([-0.5*self.scale,0.5*self.scale],[0,   0],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="r")
        self.axis_y = Arrow3D([0,0],[-0.5*self.scale,0.5*self.scale],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="g")
        self.axis_z = Arrow3D([0,0],[0,0],[-0.5*self.scale,0.5*self.scale], mutation_scale=20, lw=1, arrowstyle="-|>", color="b")
        
        self.PtShow = None #receive Pt mark instance
    
    
    def Set_BaseCS(self, input_psi = 0.0, input_theta = 0.0,  input_phi = 0.0,  input_o = [0, 0, 0]):
        self.psi = input_psi
        self.theta = input_theta
        self.phi = input_phi
        self.o = np.array(input_o)
        
        self.x0 = np.array([1,0,0])
        self.y0 = np.array([0,1,0])
        self.z0 = np.array([0,0,1])
        
        self.x0 = self.Rz(self.psi).dot(self.Ry(self.theta)).dot(self.Rx(self.phi)).dot(self.x0) + self.o
        self.y0 = self.Rz(self.psi).dot(self.Ry(self.theta)).dot(self.Rx(self.phi)).dot(self.y0) + self.o
        self.z0 = self.Rz(self.psi).dot(self.Ry(self.theta)).dot(self.Rx(self.phi)).dot(self.z0) + self.o
    
    def Add_One_Point(self, Pt_Coor):
        self.BasicSet.add(Pt_Coor)
        pass
        
    def Remove_One_Point(self, Pt_Coor):
        self.BasicSet.discard(Pt_Coor)
        pass
    
    def Rx(self, phi):
        return np.array([[1, 0, 0],
                     [0, np.cos(phi), -np.sin(phi)],
                     [0, np.sin(phi), np.cos(phi)]])
    
    def Ry(self, theta):
        return np.array([[np.cos(theta), 0, np.sin(theta)],
                     [0, 1, 0],
                     [-np.sin(theta), 0, np.cos(theta)]])
    
    def Rz(self, psi):
        return np.array([[np.cos(psi), -np.sin(psi), 0],
                     [np.sin(psi), np.cos(psi), 0],
                     [0, 0, 1]])

    def GetCSValue(self):
        if len(self.BasicSet) is 0:
            return np.NaN
        
        PtData = np.array(list(self.BasicSet))
        xs = PtData[:, 0]
        ys = PtData[:, 1]
        zs = PtData[:, 2]
     
        return xs, ys, zs
    
    
