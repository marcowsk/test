class Point():
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def get_coord(self):
        print 'x = ', self.x, ' y = ', self.y
        
    def set_coord(self,x1,y2):
        self.x=x1
        self.y=y2
        
class WPoint():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.v = 0
        
    def get_coord(self):
        print 'x = ', self.x, ' y = ', self.y
    
    def get_vel(self):
        print 'v'
        
    def set_coord(self,x1,y2):
        self.x=x1
        self.y=y2
    

if __name__ == "__main__":
    p = Point()
    p.get_coord()
    p.x = 8
    print p.x
    p.set_coord(12,5)
    p.get_coord()
    print p.x