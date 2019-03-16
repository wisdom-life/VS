
class CoordinateSet(object):
    """Represent 3D points in Special Frame"""
    def __init__(self, *args):
        self.BasicSet = set()
        pass
        
    def Add_One_Point(self, Pt_Coor):
        self.BasicSet.add(Pt_Coor)
        pass
        
    def Remove_One_Point(self, Pt_Coor):
        self.BasicSet.discard(Pt_Coor)
        pass
    
    
    
    
    
