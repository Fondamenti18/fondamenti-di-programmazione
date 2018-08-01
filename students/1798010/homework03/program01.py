import png
 
w,h = 0,0
 
 
def load(fname,col):
 
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
       
        global w,h
               
        w, h, png_img, _ = reader.asRGB8()
        img = []
       
        #print(w,h)
       
        count = 0;
               
        for line in png_img:
            l = []
           
            for i in range(0, len(line), 3):
                if (line[i], line[i+1], line[i+2]) == col:
                    l+= [1]
                else:
                    l+= [0]
            img += [l]            
        return img
 
       
def quadrato(filename,c):
   
    global w,h
   
    grid = load(filename,c)
   
    size = [[0 for x in range(w)] for y in range(h)]
   
    bigX,bigY = 0,0
    biggest = 0
   
    for y in range(h):
        if grid[y][0] == 1:
            #print(grid[y][0])
            size[y][0] = 1
           
    for x in range(w):
        if grid[0][x] == 1:
            size[0][x % 2] = 1
        else:
            size[0][x % 2] = 0
           
        for y in range(1, h):
            if grid[y][x] == 1:
                size[y][x % 2] = min(size[y - 1][x % 2],size[y][(x - 1) % 2],size[y - 1][(x - 1) % 2]) + 1
                   
                newBiggest = max(biggest, size[y][x % 2])
               
                if newBiggest > biggest:
                    #print('new biggest is ',newBiggest)
                    bigX = x
                    bigY = y
                    biggest = newBiggest
            else:
                size[y][x % 2] = 0
                       
    return biggest,(bigX-biggest + 1,bigY-biggest + 1)