import sys
def _findmin(matrix,i):
    print("sum")
def _print(matrix):
    i =0
    while i <len(matrix):
        print(matrix[i])
        i+=1
def main():
    #command = input("Enter File Name: ")
    _file = open("test.txt", "r")
    max = 0
    #make array n * n size meaning max will shrink later
    matrix =[[16]* 6 for i in range(6)]
    i = 0
    while i < len(matrix):
        matrix[i][i] = 0
        i+=1
    #parse first line indexes are
    #0 node
    #1 node
    #2 cost from node 0  to 1
    _farray = _file.readline().split()
    #while theres stuff to read on the file and store to the matrix
    while _farray:
        #this stores it bidirectional
        matrix[int(_farray[0]) -1][int(_farray[1]) - 1] = int(_farray[2])
        matrix[int(_farray[1]) -1][int(_farray[0]) - 1] = int(_farray[2])
        #this will be used for finding max size
        if(int(_farray[0]) > max):
            max = int(_farray[0])
        if(int(_farray[1]) > max):
            max = int(_farray[1])
        _farray = _file.readline().split()
    print("og information")
    _print(matrix)
    print(" ")
    i = len(matrix)
    #trims the rows
    while (i > max):
        matrix.pop()
        i = i -1
    i = 0
    j = len(matrix[0])
    #this algorithim just trims the columns
    while i < len(matrix):
        j = len(matrix[i])
        while j  > max:
            matrix[i].pop()
            j-=1
        i+=1
    #algorithim happens here assume that the matrix is unstable
    stable = False
    #variable used for equation 
    x = 0
    y = 0
    #stores coordinates and where to modify since I used one table 
    coordinates = []
    coordinates_tracker = 0
    target = -11
    a = 0
    iteration = 1
    #keep fixing the table until no updates...
    while not stable:
        x = 0
        #go through each row and apply bellman ford
        #Dx(y) = C(x,z) + dz(y)
        while x < len(matrix):
            y = 0
            while y < len(matrix):
                _min = matrix[x][y]
                #if Dx(y) pointing to itself we know were at optimal
                if(x == y):
                    y+=1
                    continue
                z = 0
                while z < len(matrix):
                    #if C(x,x) skip to get something else
                    #if c(x,y) has no link skip find another neighbor that satisfies it
                    # #if dz(y) has no link skip because c(x,z) can get messed up
                    if((x == z) or (matrix[x][z] >= 16) or (matrix[z][y] >= 16)):
                        z+=1
                        continue
                    #we passed validation now do we replace?
                    if(_min > (matrix[x][z] + matrix[z][y])):
                        _min = (matrix[x][z] + matrix[z][y])
                        if(len(coordinates) == 0):
                            coordinates.append([])
                            coordinates[len(coordinates) -1].append(x)
                            coordinates[len(coordinates) -1].append(y)
                            coordinates[len(coordinates) -1].append(_min)
                        elif((len(coordinates) >  0) and((coordinates[(len(coordinates) -1)][0] == x)and (coordinates[len(coordinates) -1][1] == y))):
                            coordinates[len(coordinates) -1][2] = _min
                        else:
                            coordinates.append([])
                            coordinates[len(coordinates) -1].append(x)
                            coordinates[len(coordinates) -1].append(y)
                            coordinates[len(coordinates) -1].append(_min)
                    z+=1
                y+=1
            x+=1
        if(len(coordinates) == 0):
            break
        print(coordinates)
        print(iteration)
        while(len(coordinates) > 0):
            matrix[coordinates[0][0]][coordinates[0][1]] = coordinates[0][2]
            coordinates.pop(0)
        print("after",coordinates)
        print("iteration ",iteration)
        _print(matrix)
        iteration+=1
        #either update or and reapeat or were finish

if __name__ == "__main__":
    main()


