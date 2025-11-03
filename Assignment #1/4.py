class Img:
    def __init__(self,data):
        self.data = data
    def clone(self):
        return[r[:] for r in self.data]        
    def apply(self, func):
        return Img(func(self.data))
    def show(self):
        for r in self.data:print(r)
        print()
def flipX(mat):
    return [m[::-1] for m in mat]
def brighten(mat,val):
    return [[p+val for p in m]for m in mat]
def rotate90(mat):
     return [[mat[r][c] for r in range(len(mat)-1,-1,-1)] for c in range(len(mat[0]))]


class Pipe:
    def __init__(self):
        self.funcs = []
    def add(self, f):
        self.funcs.append(f)
    def run (self, img ):
        return [img.apply(f) for f in self.funcs]
    
pixels = [[10,20,30],[40,50,60]]
img = Img(pixels)
smallPipe = Pipe()
smallPipe.add(flipX)
smallPipe.add(rotate90)
smallPipe.add(lambda d: brighten(d,15))

print("the original : ") 

img.show()
for i , n in enumerate (smallPipe.run(img),1):
    print(f"Result {i}:")
    n.show()