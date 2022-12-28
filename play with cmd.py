"""
Tic Tac Toe Ai Game
Undefeatable Ai made by Oday
I make sure that there is no way to win
"""
"""""""""""""""""""""
                 Function Area
               
                         """""""""""""""""""""""
#Function clear screen
def clrscr():
    from os import system
    #clear the command window or the terminator
    system('cls')  
#Timer Function
def timer(s):
    import time
    #to do some delay  
    for i in range(1,s+1):
       time.sleep(1)
#Function give a random number in range(a1,a2)
def random(begin,end):
    import random
    #pick a random number by your range
    rand=int(random.randrange(begin,end))
    return rand
#Function to print the board
def printboard(board):
    import sys
    print('   _________________________')
    for i in range(0,3):
        print("")
        for j in range(0,3):
            sys.stdout.write('   |   ')
            sys.stdout.write(str((board[i][j]))) 
        sys.stdout.write("   |   ")
        print('')
        print('   _________________________')
#Check if board has a winner
def checkwin(board):
    def diag1(board):
        """""""""""""""""
           X   -   -      
           -   X   -
           -   -   X     
        """""""""""""""""
        i=0
        j=0
        l=[]
        while i<3:
            l.append(board[i][j])
            i+=1
            j+=1
        if l[0]==l[1]==l[2]:
            return l[0]
        else:
            return False
        
    def diag2(board):
        """""""""""""""""
            -   -   X
            -   X   -
            X   -   -         
        """""""""""""""""
        i=2
        j=0
        l=[]
        while i>=0:
            l.append(board[i][j])
            i-=1
            j+=1
        if l[0]==l[1]==l[2]:
            return l[0]
        else:
            return False
        
    def diag3(board):
        """""""""""""""""
            X   X   X
            -   -   -
            -   -   -              
        """""""""""""""""
        l=[]
        for i in range(0,3):
            l.append(board[0][i])
        if l[0]==l[1]==l[2]:
            return l[0]
        else:
            return False
    
    def diag4(board):
        """""""""""""""""
            -   -   -
            X   X   X
            -   -   -              
        """""""""""""""""
        l=[]
        for i in range(0,3):
            l.append(board[1][i])
        if l[0]==l[1]==l[2]:
            return l[0]
        else:
            return False
    
    def diag5(board):
        """""""""""""""""
            -   -   -
            -   -   -
            X   X   X              
        """""""""""""""""
        l=[]
        for i in range(0,3):
            l.append(board[2][i])
        if l[0]==l[1]==l[2]:
            return l[0]
        else:
            return False
    
    def diag6(board):
        """""""""""""""""
            X   -   -
            X   -   -
            X   -   -              
        """""""""""""""""
        l=[]
        for i in range(0,3):
            l.append(board[i][0])
        if l[0]==l[1]==l[2]:
            return l[0]
        else:
            return False
    
    def diag7(board):
        """""""""""""""""
            -   X   -
            -   X   -
            -   X   -              
        """""""""""""""""
        l=[]
        for i in range(0,3):
            l.append(board[i][1])
        if l[0]==l[1]==l[2]:
            return l[0]
        else:
            return False
    
    def diag8(board):
        """""""""""""""""
            -   -   X
            -   -   X
            -   -   X              
        """""""""""""""""
        l=[]
        for i in range(0,3):
            l.append(board[i][2])
        if l[0]==l[1]==l[2]:
            return l[0]
        else:
            return False
    #Check If there is one of the diags 
    if not not diag1(board):
        return diag1(board)
    elif not not diag2(board):
        return diag2(board)
    elif not not diag3(board):
        return diag3(board)
    elif not not diag4(board):
        return diag4(board)
    elif not not diag5(board):
        return diag5(board)
    elif not not diag6(board):
        return diag6(board)
    elif not not diag7(board):
        return diag7(board)
    elif not not diag8(board):
        return diag8(board)
    else:
        return False
#Function to know where the player positions
def playerposition(board,ai):
      pos=[]
      for i in range(0,3):
          for j in range(0,3):
              if board[i][j]==ai:
                  p=(i,j)
                  pos.append(p)
      return pos            
#Function to Know the empty places to play in
def toplay(board):     
    play=[] #Put the empty slots to play
    for i in range (0,3):
        for j in range (0,3):
            if board[i][j]==' ':
                play.append([i,j])
    return play            
#Insert player in board
def playerptp():
   dec=[[],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
   cp=input("Play_In:")
   cp=int(cp)
   while cp==0 or cp>9:
       #If player give a wrong input : enter again 
    cp=int(input("Re-Enter(it must be 1 to 9):"))
   i=dec[cp][0]
   j=dec[cp][1]
   return [i,j]
#Check where want to play the player
def check_p_play(board,pp):
    #if place not emmpty don't play
    if board[pp[0]][pp[1]]!=' ':
        return False
    else:
    #else play    
        return True
#Player turn    
def p_play(board,player,pp):
     #pp--> Player position
     board[pp[0]][pp[1]]=player
#First Ai play
def ai_play2(board,ai,plr,plr_pos1):
    import random
    #Choose random corner to play-------------------
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==ai:
                if i==0 and j==0:
                    play=[[0,2],[2,0],[2,2]]
                    break
                if i==0 and j==2:
                    play=[[0,0],[2,0],[2,2]]
                    break
                if i==2 and j==0:
                    play=[[0,0],[0,2],[2,2]]
                    break
                if i==2 and j==2:
                    play=[[0,0],[0,2],[2,0]]
                    break    
    #--------------------------------------------------
    #If player play at one of centers ai play symitrique to the center              
    if plr_pos1==[1,1] or plr_pos1==[0,1] or plr_pos1==[1,0] or plr_pos1==[2,1] or plr_pos1==[1,2]:
         if board[0][2]==ai:
             board[2][0]=ai
             
         elif board[2][0]==ai:
             board[0][2]=ai
             
         elif board[2][2]==ai:
             board[0][0]=ai
             
         elif board[0][0]==ai:
             board[2][2]=ai
         
    #If player not in the center Ai play in Corners
    elif plr_pos1!=[1,1]:
        if board[0][2]==ai and board[0][2]==' ':
             board[2][0]=ai
             
        elif board[2][0]==ai and board[2][0]==' ':
             board[0][2]=ai
             
        elif board[2][2]==ai and board[2][2]==' ':
             board[0][0]=ai
             
        elif board[0][0]==ai and board[0][0]==' ':
             board[2][2]=ai
        
        #Else play random corner
        else:
            i=random.randrange(0,3)
            while board[play[i][0]][play[i][1]]==plr:
                i=random.randrange(0,3)
            board[play[i][0]][play[i][1]]=ai     
#Ai turn to play
def ai_turn():
    #Ai play delay
    print('Pc Playing...')
    timer(1)
    clrscr()              
#Give the symitrique position 
def sym(pls,symto):
    #symitrique of center---------
    if symto==[1,1]:
       if pls==[0,0]:
           return [2,2]
       if pls==[0,1]:
           return [2,1]
       if pls==[0,2]:
           return [2,0]
       if pls==[1,0]:
           return [1,2]
       if pls==[2,0]:
           return [0,2]
       if pls==[2,1]:
           return [0,1]
       if pls==[2,2]:
           return [0,0]
       if pls==[1,2]:
           return [1,0]
    #------------------------------
    
    #Top center--------------------   
    if symto==[0,1]:
        if pls==[0,0]:
            return [0,2]
        if pls==[0,2]:
            return [0,0]
        
    #Bottom center-----------------
    if symto==[2,1]:    
        if pls==[2,0]:
            return [2,2]
        if pls==[2,2]:
            return [2,0]
        
    #Right center------------------
    if symto==[1,2]: 
        if pls==[2,2]:
            return [0,2]
        if pls==[0,2]:
            return [2,2]
    
    #Left center--------------------    
    if symto==[1,0]:       
       if pls==[0,0]:
            return [2,0]
       if pls==[2,0]:
            return [0,0]      
#give corner left and right
def corner_lr(corner):
    if corner==[0,0]:
        return[[0,1],[1,0]]
    elif corner==[0,2]:
        return[[0,1],[1,2]]
    elif corner==[2,2]:
        return[[2,1],[1,2]]
    elif corner==[2,0]:
        return[[2,1],[1,0]]
#Second Ai play
def ai_play3(board,ai,plr_pos1,plr_pos2):
    #Player win possibles----------------------------------
    if plr_pos1==[1,1]:
        if plr_pos2==[1,0]:
            play1=sym(plr_pos2,plr_pos1)
            board[play1[0]][play1[1]]=ai
        if plr_pos2==[0,1]:
            play1=sym(plr_pos2,plr_pos1)
            board[play1[0]][play1[1]]=ai
        if plr_pos2==[1,2]:
            play1=sym(plr_pos2,plr_pos1)
            board[play1[0]][play1[1]]=ai
        if plr_pos2==[2,1]:
            play1=sym(plr_pos2,plr_pos1)
            board[play1[0]][play1[1]]=ai  
        if plr_pos2==[0,0]:
            play1=sym(plr_pos2,plr_pos1)
            board[play1[0]][play1[1]]=ai
        if plr_pos2==[0,2]:
            play1=sym(plr_pos2,plr_pos1)
            board[play1[0]][play1[1]]=ai
        if plr_pos2==[2,0]:
            play1=sym(plr_pos2,plr_pos1)
            board[play1[0]][play1[1]]=ai
        if plr_pos2==[2,2]:
            play1=sym(plr_pos2,plr_pos1)
            board[play1[0]][play1[1]]=ai              
    #---------------------------------------------------------    
    else:       
        #If player play in the center----------
        if plr_pos2!=[1,1]:
            if board[0][0]==' ':
                board[0][0]=ai
            elif board[2][2]==' ':
                board[2][2]=ai
            elif board[0][2]==' ':
                board[0][2]=ai
            elif board[2][0]==' ':
                board[2][0]=ai
        if plr_pos2==[1,1]:
            play=sym(plr_pos1,plr_pos2)
            board[play[0]][play[1]]=ai                           
#Third and Fourth Ai to play
def ai_play4(board,ai,plr,plr_pos1,plr_pos3,plr_pos2):
    #Bug---------------------------------------------------------------------------------
  if     len(toplay(board))==3 and board[0][0]==plr and board[1][1]==plr and board[2][2]==' ':
      board[2][2]=ai
  elif   len(toplay(board))==3 and board[2][2]==plr and board[1][1]==plr and board[0][0]==' ':
        board[0][0]=ai
  elif   len(toplay(board))==3 and board[0][2]==plr and board[1][1]==plr and board[2][0]==' ':
         board[2][0]=ai
  elif   len(toplay(board))==3 and board[2][0]==plr and board[1][1]==plr and board[0][2]==' ':
          board[0][2]=ai  
    #-------------------------------------------------------------------------------------    
  else:                 
    #win possibels------------------------------------------------------------------------   
    if check_chance(board,ai)!=[]:
        board[check_chance(board,ai)[0]][check_chance(board,ai)[1]]=ai
    #-----------------------------------------------------------------------fixed   
    else:
        #bug--------------------------------
      if plr_pos1==[1,1]:
        play=sym(plr_pos3,plr_pos1)
        board[play[0]][play[1]]=ai
        #-----------------------------------fixed
      else:
        if plr_pos2==[1,1]:
            play1=sym(plr_pos3,plr_pos2)
            board[play1[0]][play1[1]]=ai
        elif plr_pos2==[0,1]:
            play1=sym(plr_pos3,plr_pos2)
            board[play1[0]][play1[1]]=ai
        elif plr_pos2==[1,2]:
            play1=sym(plr_pos3,plr_pos2)
            board[play1[0]][play1[1]]=ai
        elif plr_pos2==[2,1]:
            play1=sym(plr_pos3,plr_pos2)
            board[play1[0]][play1[1]]=ai  
        elif plr_pos2==[0,0]:
            play1=sym(plr_pos3,plr_pos2)
            board[play1[0]][play1[1]]=ai
        elif plr_pos2==[0,2]:
            play1=sym(plr_pos3,plr_pos2)
            board[play1[0]][play1[1]]=ai
        elif plr_pos2==[2,0]:
            play1=sym(plr_pos3,plr_pos2)
            board[play1[0]][play1[1]]=ai
        elif plr_pos2==[2,2]:
            play1=sym(plr_pos3,plr_pos2)
            board[play1[0]][play1[1]]=ai 
        else:    
            #Tie--------------------------
            play=toplay(board)
            i=random(0,3)
            j=random(0,3)
            while [i,j] not in play:
                i=random(0,3)
                j=random(0,3)
            board[i][j]=ai
#--when player play first--#
def ai_play5(board,ai,plr_pos1):
    fp=[[0,0],[0,2],[2,2],[2,0]]
    fp1=[[1,0],[2,1],[1,2],[0,1]]
    if plr_pos1== [1,1]:
        a=random(0,4)
        i=fp[a][0]
        j=fp[a][1]
        while [i,j]==plr_pos1:
            a=random(0,4)
            i=fp[a][0]
            j=fp[a][1]
        board[i][j]=ai
        return [i,j]
    elif plr_pos1 in fp:
        board[1][1]=ai
        return [1,1]                        
    elif plr_pos1 in fp1:
        board[1][1]=ai
        return [1,1]
#second Ai to play
def ai_play6(board,ai,plr,plr_pos1,plr_pos2,ai_pos):
    fp=[[0,0],[0,2],[2,2],[2,0]]
    fp1=[[1,0],[1,2],[2,1],[0,1]]
    if plr_pos1==[1,1]:
        if plr_pos2!=sym(ai_pos,plr_pos1):
            play=sym(plr_pos2,plr_pos1)
            board[play[0]][play[1]]=ai
            return play
        else:
            a=random(0,4)
            i=fp[a][0]
            j=fp[a][1]
            while [i,j]==plr_pos2 or [i,j]==ai_pos:
                a=random(0,4)
                i=fp[a][0]
                j=fp[a][1]
            board[i][j]=ai
            return [i,j]
    elif plr_pos1 in fp:
        if check_chance(board,plr)!=[]:
             board[check_chance(board,plr)[0]][check_chance(board,plr)[1]]=ai
        elif plr_pos2==sym(plr_pos1,ai_pos):
            a=random(0,4)
            i=fp1[a][0]
            j=fp1[a][1]
            while [i,j]==plr_pos1 or [i,j]==plr_pos2:
                a=random(0,4)
                i=fp1[a][0]
                j=fp1[a][1]
            board[i][j]=ai
            return [i,j]
        elif plr_pos2 in fp1:
            if plr_pos2 not in corner_lr(plr_pos1):
                if plr_pos1==[0,0]:
                    play=[[0,1],[1,0]]
                    play.remove(sym(plr_pos2,ai_pos))
                    board[play[0][0]][play[0][1]]=ai
                    return [play[0][0],[play[0][1]]]
                elif plr_pos1==[2,2]:
                    play=[[2,1],[1,2]] 
                    play.remove(sym(plr_pos2,ai_pos))
                    board[play[0][0]][play[0][1]]=ai
                    return [[play[0][0]],[play[0][1]]]
                elif plr_pos1==[2,0]:
                    play=[[2,1],[1,0]]
                    play.remove(sym(plr_pos2,ai_pos))
                    board[play[0][0]][play[0][1]]=ai
                    return [[play[0][0]],[play[0][1]]]
                elif plr_pos1==[0,2]:
                    play=[[0,1],[1,2]]        
                    play.remove(sym(plr_pos2,ai_pos))
                    board[play[0]][play[1]]=ai
                    return [[play[0]],[play[1]]]
            else:
                play=sym(plr_pos1,plr_pos2)
                board[play[0]][play[1]]=ai
                return play       
    elif plr_pos1 in fp1:
        if plr_pos2 in fp1:
            a=random(0,4)
            board[fp[a][0]][fp[a][1]]=ai
            return [[fp[a][0]],[fp[a][1]]]
        elif plr_pos2 in fp:
            if plr_pos1 in corner_lr(plr_pos2):
                play=sym(plr_pos2,plr_pos1)
                board[play[0]][play[1]]=ai
                return play
            else:
                fp2=fp1
                fp2.remove(plr_pos1)
                fp2.remove(sym(plr_pos1,ai_pos))
                for i in fp:
                    if plr_pos1 in corner_lr(i) and i!=sym(plr_pos2,ai_pos):
                        fp2.append(i)
                a=random(0,3)
                board[fp2[a][0]][fp2[a][1]]=ai
                return [[fp2[a][0]],[fp2[a][1]]]
#check if there win chance
def check_chance(board,ai):
    if board[0][2]==ai and board[0][1]==ai and board[0][0]==' ':
        return [0,0]
    elif board[2][0]==ai and board[1][0]==ai and board[0][0]==' ':    
        return [0,0]
    elif board[2][2]==ai and board[1][1]==ai and board[0][0]==' ':    
        return [0,0]
    elif board[2][1]==ai and board[1][1]==ai and board[0][1]==' ':    
        return [0,1]
    elif board[0][0]==ai and board[0][2]==ai and board[0][1]==' ':    
        return [0,1]
    elif board[0][2]==ai and board[0][0]==ai and board[0][1]==' ':    
        return [0,1]
    elif board[2][2]==ai and board[1][2]==ai and board[0][2]==' ':    
        return [0,2]
    elif board[2][0]==ai and board[1][1]==ai and board[0][2]==' ':    
        return [0,2]
    elif board[0][0]==ai and board[0][1]==ai and board[0][2]==' ':    
        return [0,2]
    elif board[1][2]==ai and board[1][1]==ai and board[1][0]==' ':    
        return [1,0]
    elif board[0][0]==ai and board[2][0]==ai and board[1][0]==' ':    
        return [1,0]
    elif board[2][0]==ai and board[0][0]==ai and board[1][0]==' ':    
        return [1,0]
    elif board[0][0]==ai and board[2][2]==ai and board[1][1]==' ':    
        return [1,1]
    elif board[2][2]==ai and board[0][0]==ai and board[1][1]==' ':    
        return [1,1]
    elif board[2][0]==ai and board[0][2]==ai and board[1][1]==' ':    
        return [1,1]
    elif board[0][2]==ai and board[2][0]==ai and board[1][1]==' ':    
        return [1,1]
    elif board[1][0]==ai and board[1][2]==ai and board[1][1]==' ':    
        return [1,1]
    elif board[1][2]==ai and board[1][0]==ai and board[1][1]==' ':    
        return [1,1]
    elif board[0][1]==ai and board[2][1]==ai and board[1][1]==' ':    
        return [1,1]
    elif board[2][1]==ai and board[0][1]==ai and board[1][1]==' ':    
        return [1,1]
    elif board[1][0]==ai and board[1][1]==ai and board[1][2]==' ':    
        return [1,2]
    elif board[0][2]==ai and board[2][2]==ai and board[1][2]==' ':    
        return [1,2]
    elif board[2][2]==ai and board[0][2]==ai and board[1][2]==' ':    
        return [1,2]
    elif board[2][2]==ai and board[2][1]==ai and board[2][0]==' ':    
        return [2,0]
    elif board[0][2]==ai and board[1][1]==ai and board[2][0]==' ':    
        return [2,0]
    elif board[0][0]==ai and board[1][0]==ai and board[2][0]==' ':    
        return [2,0]
    elif board[0][1]==ai and board[1][1]==ai and board[2][1]==' ':    
        return [2,1]
    elif board[2][0]==ai and board[2][2]==ai and board[2][1]==' ':    
        return [2,1]
    elif board[2][2]==ai and board[2][0]==ai and board[2][1]==' ':    
        return [2,1]
    elif board[0][2]==ai and board[1][2]==ai and board[2][2]==' ':    
        return [2,2]
    elif board[0][0]==ai and board[1][1]==ai and board[2][2]==' ':    
        return [2,2]
    elif board[2][0]==ai and board[2][1]==ai and board[2][2]==' ':    
        return [2,2]
    else:
        return []   
#Third and Fourth Ai to play            
def ai_play7(board,ai,plr):
    if check_chance(board,ai)!=[]:
        board[check_chance(board,ai)[0]][check_chance(board,ai)[1]]=ai
    else:
        if check_chance(board,plr)!=[]:
            board[check_chance(board,plr)[0]][check_chance(board,plr)[1]]=ai
        else:
            board_temp=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
            a=random(0,9)
            i=board_temp[a][0]
            j=board_temp[a][1]
            while [i,j] not in toplay(board):
                a=random(0,10)
                i=board_temp[a][0]
                j=board_temp[a][1]
            board[i][j]=ai          
#setup board
def setup_board():
    board=[['1','2','3'],['4','5','6'],['7','8','9']]
    printboard(board)
    print('')
    print('Play with numbers 1 to 9')
    j=3
    clrscr()
    for i in range(0,3):
        board=[['1','2','3'],['4','5','6'],['7','8','9']]
        printboard(board)
        print('')
        print('Play with numbers 1 to 9')
        print('Get ready! will start in:',j)
        j-=1
        timer(1)
        clrscr()      
    clrscr()
    board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    printboard(board)
    print('')        
    return board       
#not important just for fun
def error(text):
    import os
    os.system("")
    class style():
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
        UNDERLINE = '\033[4m'
        g1 = '\033[41m'
        g2 = '\033[42m'
        g3 = '\033[43m'
        g4 = '\033[44m'
        g5 = '\033[45m'
        g6 = '\033[46m'
        g7 = '\033[47m'
        
    import time  
    sec=[1.4,1.3,1.2,1.1,1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0]
    def random(begin,end):
        import random
        rand=int(random.randrange(begin,end))
        return rand
    o=[style.RED,style.YELLOW,style.GREEN,style.CYAN,style.BLUE,style.MAGENTA,style.RED,style.YELLOW,style.GREEN,style.CYAN,style.BLUE,style.MAGENTA]
    for j in range(0,11):
      print(o[j]+text)
      time.sleep(sec[j])
    
    i=[style.g1,style.g3,style.g2,style.g6,style.g4,style.g5]
    m=0
    try:
        while True:
            print(i[m]+text)
            if m<5:
             m=m+1
            else:
                m=0
    except KeyboardInterrupt:
        pass
"""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""
               Game Area
               
                      """""""""""""""""
#Start the game
game_quit=False
while not game_quit:
    #Player choose X or O      
    print('choose X or O')
    x=['x','X']
    o=['o','O']
    xo=['x','X','o','O']
    plr=''
    while plr not in xo:
        plr=input('X/O: ')
        if plr in x:
            ai='O'
            plr='X'
        elif plr in o:
            ai="X" 
            plr='O'          
    print('Would you like to play first?')
    ans=input('Answer(Y/N):')
    while ans not in ['Y','y','N','n']:
        ans=input('Enter again Y or N :')
    if ans in ['N','n']:                  
        clrscr() #clear screen
        #setup the board
        board=setup_board()
        print('')
        #Ai turn
        ai_turn()
        fp=[[0,0],[0,2],[2,2],[2,0]]
        a=random(0,4)
        i=fp[a][0]
        j=fp[a][1]
        board[i][j]=ai
        clrscr()
        printboard(board)
        #Player turn
        print('')
        print("It's your turn now!")
        timer(1)
        plr_pos1=playerptp()
        while not check_p_play(board,plr_pos1):
            plr_pos1=playerptp()
        clrscr()
        p_play(board,plr,plr_pos1)
        printboard(board)
        print('')
        #Ai turn
        ai_turn()
        ai_play2(board,ai,plr,plr_pos1)
        printboard(board)
        print('')
        #Player turn
        print("It's your turn now!")
        timer(1)
        plr_pos2=playerptp()
        while not check_p_play(board,plr_pos2):
            plr_pos2=playerptp()
        clrscr()
        p_play(board,plr,plr_pos2)
        printboard(board)
        print('')
        #Ai turn
        ai_turn()
        ai_play3(board,ai,plr_pos1,plr_pos2)
        printboard(board)
        #Player turn
        print('')
        print("It's your turn now!")
        timer(1)
        plr_pos3=playerptp()
        while not check_p_play(board,plr_pos3):
            plr_pos3=playerptp()
        clrscr()
        p_play(board,plr,plr_pos3)
        printboard(board)
        #Ai turn
        print('')
        ai_turn()
        ai_play4(board,ai,plr,plr_pos1,plr_pos3,plr_pos2)
        printboard(board)
        #Check if there is a winner
        if checkwin(board)==plr:
                clrscr()
                print('You Win')
        elif checkwin(board)==ai:
                timer(1)
                clrscr()
                printboard(board)
                print('')
                print('Game over Loser!!')
        #If there are no winner continue          
        else:
            #Player turn
            print('')
            print("It's your turn now!")
            timer(1)
            plr_pos3=playerptp()
            while not check_p_play(board,plr_pos3):
                plr_pos3=playerptp()
            clrscr()
            p_play(board,plr,plr_pos3)
            printboard(board)
            print('')
            #Ai turn
            ai_turn()
            ai_play4(board,ai,plr,plr_pos1,plr_pos3,plr_pos2)
            printboard(board)
            print('')
            #Check Winner
            if checkwin(board)==plr:
                print('')
                print('You Win!!')
            elif checkwin(board)==ai:
                print('')
                print('Game over Loser!!')
            else:
                print('')
                print('Tie!!')      
    else:
    #setup the board
        ai_p=0
        board=setup_board()
        #player turn
        print('')
        print("It's your turn!")
        timer(1)
        plr_pos1=playerptp()
        while not check_p_play(board,plr_pos1):
            plr_pos1=playerptp()
        clrscr()
        p_play(board,plr,plr_pos1)
        printboard(board)
        print('')
        #Ai turn
        ai_p+=1
        ai_turn()
        ai_pos=ai_play5(board,ai,plr_pos1)
        printboard(board)
        #Player turn
        print("It's your turn now!")
        timer(1)
        plr_pos2=playerptp()
        while not check_p_play(board,plr_pos2):
            plr_pos2=playerptp()
        clrscr()
        p_play(board,plr,plr_pos2)
        printboard(board)
        print('')
        #Ai turn
        ai_p+=1
        ai_turn()
        ai_pos2=ai_play6(board,ai,plr,plr_pos1,plr_pos2,ai_pos)
        printboard(board)
        print('')
        while toplay(board)!=[]:
            #Player turn
            print("It's your turn now!")
            timer(1)
            plr_pos3=playerptp()
            while not check_p_play(board,plr_pos3):
                plr_pos3=playerptp()
            clrscr()
            p_play(board,plr,plr_pos3)
            printboard(board)
            print('')
            #Ai turn
            if ai_p<4:
                ai_p+=1
                ai_turn()
                ai_play7(board,ai,plr)
                printboard(board)
                print('')
            if checkwin(board)==plr or checkwin(board)==ai:
                break
            else:
                continue   
        #Check Winner
        if checkwin(board)==plr:
            print('')
            print('You Win!!')
        elif checkwin(board)==ai:
            print('')
            print('Game over Loser!!')
        else:
            print('')
            print('Tie!!')           
        print('')        

    print('Would you like to play again?')
    ans=input('Answer(Y/N): ')
    while ans not in ['n','N','y','Y']:
        ans=input('answer(Y/N): ')
    if ans in ['n','N']:
        game_quit=True
        clrscr() 
    else:
        game_quit=False
        clrscr()     
error('Thanks for playing!!')          
exit=input('Press Enter to exit:')          
    