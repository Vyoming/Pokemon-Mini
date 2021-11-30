################################################################################
#  Basic format of BFS algorithm from                                          #
#    https://www.youtube.com/watch?v=D14YK-0MtcQ                               #
#    https://levelup.gitconnected.com/solve-a-maze-with-python-e9f0580979a1    #
################################################################################

map=[
    [0,0,0,1,0,0,0,1,0,0,0,0,0],
    [0,1,0,1,0,1,1,1,1,1,1,1,0],
    [0,1,0,0,0,1,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,0,1,1,1,1,1,1],
    [0,1,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,1,1,1,0,1,1,1],
    [1,1,1,0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,0,1,1,0,1,1,1,1,0],
    [1,1,1,1,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,1,1,1,1,1,1],
    [0,1,1,1,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,1,1,1,1,0],
    [1,1,1,1,0,0,0,1,0,0,0,1,0],
    [0,0,0,0,0,1,0,0,0,1,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,1,0,0,0,0,0,0,1,1,0],
    [1,1,0,1,0,1,1,1,1,1,1,1,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0],
]

board=[
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0],
]

enter=19,6
exit=0,6

rows,cols=20,13

def next(x,map,board): #does the next move
    for i in range(20):
        for j in range(13):
            if board[i][j] == x:
                if i>0 and board[i-1][j] == 0 and map[i-1][j] == 0:
                    board[i-1][j] = x + 1
                if j>0 and board[i][j-1] == 0 and map[i][j-1] == 0:
                    board[i][j-1] = x + 1
                if i<19 and board[i+1][j] == 0 and map[i+1][j] == 0:
                    board[i+1][j] = x + 1
                if j<12 and board[i][j+1] == 0 and map[i][j+1] == 0:
                    board[i][j+1] = x + 1

def edit(map,board):
    steps=0
    while board[0][6] == 0:
        steps+=1
        next(steps,map,board)

def getPath(map,board):
    edit(map,board)
    i,j=0,6
    curr=board[i][j]
    result=[(512,-800)]
    while curr>1:
        if i > 0 and board[i - 1][j] == curr-1:
            i, j = i-1, j
            result.append((128+j*64,-800+i*64))
            curr-=1
        elif j > 0 and board[i][j - 1] == curr-1:
            i, j = i, j-1
            result.append((128+j*64,-800+i*64))
            curr-=1
        elif i < 19 and board[i + 1][j] == curr-1:
            i, j = i+1, j
            result.append((128+j*64,-800+i*64))
            curr-=1
        elif j < 12 and board[i][j + 1] == curr-1:
            i, j = i, j+1
            result.append((128+j*64,-800+i*64))
            curr-= 1
    return result