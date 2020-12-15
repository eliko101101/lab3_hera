class Weight:
    def __init__(self, massa):
        self.massa = massa

    def __mul__(self, a):
        res = self.massa * a
        return res
    def __sub__(self, a):
        res = self.massa - a
        return res
    def __add__(self, a):
         
        if isinstance(a, str):
            raise TypeError
        res = self.massa + a
        return res

    
        
