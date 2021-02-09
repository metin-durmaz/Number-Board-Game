import sys
if len(sys.argv)!=2:
    print("\nPlease run with two arguments!")
else:
    with open(sys.argv[1],"r") as file:
        file1=file.read()
    print("\n"+file1)
    print("\nYour score is: 0")
    file2=open(sys.argv[1],"r").readlines()
    list1=[]
    try:
        for a in file2:
            list1.append(a.strip("\n"))
    except IndexError:
        pass
    list2=[]
    try:
        for b in list1:
            list2.append(b.split(" "))
    except IndexError:
        pass
    fcounter=0
    while True:
        try:
            for i in list2:
                i.insert(0," ")
        except IndexError:
            pass
        try:
            for i in list2:
                i.append(" ")
        except IndexError:
            pass
        a=[]
        try:
            for i in range(len(list2[0])):
                a.append(" ")
        except IndexError:
            pass
        b=[]
        try:
            for i in range(len(list2[0])):
                b.append(" ")
        except IndexError:
            pass
        list2.insert(0,a)
        list2.append(b)
        control1 = 0
        for i in list2: # If there is no cell which has no neighbor with the same value, game is over.
            for j in i:
                if j != " ":
                    control1 += 1
        control2 = 0
        for i in range(len(list2)):
            for j in range(len(list2[i])):
                try:
                    if list2[i+1][j] != list2[i][j] and list2[i-1][j] != list2[i][j] and list2[i][j+1] != list2[i][j] and list2[i][j-1] != list2[i][j]:
                        control2 += 1
                except IndexError:
                    pass
        if control1 == control2:
            print("\nGame Over\n")
            quit()
        while True:
            try:
                r,c=input("\nPlease enter a row and column number: ").split()
                r=int(r)
                c=int(c)
            except ValueError: # If the player enters more or less than 2 numbers or any other data types.
                print("\nYou must enter two \'numbers\'!")
                continue
            if len(list2)<r+2 or len(list2[0])<c+2 or list2[r][c]==" ": # If the chosen cell is out of bounds.
                print("\nPlease enter a correct size!")
                continue
            d = list2[r][c]
            if list2[r + 1][c] != d and list2[r - 1][c] != d and list2[r][c + 1] != d and list2[r][c - 1] != d: # If the cell chosen by the player has no neighbor with the same value.
                print("\nThis cell has no neighbor with the same value")
                continue
            break
        d=list2[r][c] # The cell picked by the player.
        counter=0 # Number of the cells to be destroyed.
        def f(r,c): # The cell picked by the player and the immediate neighbors of the cell disappear from the board.
            if list2[r][c]==d:
                list2[r][c]=" "
                global counter
                counter+=1
                return f(r+1,c),f(r-1,c),f(r,c+1),f(r,c-1)
        f(r,c)
        def fib(counter): # fibonacci(counter) => (Counter is number of the cells to be destroyed.)
            x, y = 0, 1
            for i in range(counter - 1):
                x, y = y, x + y
            return y
        fib(counter)
        fcounter += fib(counter) * int(d) # Calculate score and add to previous score. (Calculate updated score.)
        tzlist=[]
        try:
            for i in range(len(list2[0])): # Turn 90 degrees counterclockwise.
                tz=[j[i] for j in list2]
                tzlist.append(tz)
        except IndexError:
            pass
        [i.reverse() for i in tzlist]
        for i in tzlist: # Columns move down to fill the row blank cells.
            for j in i:
                if j==" ":
                    indexx=i.index(j)
                    i.pop(indexx)
                    i.append(" ")
        tzlist.pop(0)
        tzlist.pop(-1)
        for i in tzlist:
            i.pop(-1)
        for i in tzlist:
            i.pop(-1)
        for j in range(len(tzlist)): # If a column disappears completely, all the cells which are at the right side of that blank column move left to fill the empty space.
            for i in tzlist:
                if i.count(" ") == len(i):
                    indexx1 = tzlist.index(i)
                    tzlist.pop(indexx1)
        tzlist2=[]
        try:
            for i in range(len(tzlist[0])): # Turn 90 degrees clockwise.
                tz2=[j[i] for j in tzlist]
                tzlist2.append(tz2)
        except IndexError:
            pass
        tzlist2.reverse()
        for j in range(len(tzlist2)): # If a row disappears completely, all the cells which are under that blank row move up to fill empty space.
            for i in tzlist2:
                if i.count(" ") == len(i):
                    indexx2 = tzlist2.index(i)
                    tzlist2.pop(indexx2)
        outputlist=[]
        for i in tzlist2: # Convert list to string.
            strr=" ".join(i)
            outputlist.append(strr)
        print()
        for i in outputlist: # Print updated board.
            print(i)
        print("\nYour score is: {}".format(fcounter)) # Print updated score.
        list2 = tzlist2