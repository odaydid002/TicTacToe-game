# MODULES
import pygame, sys
import numpy as np
# initializes pygame
pygame.init()
# ---------
# CONSTANTS
# ---------
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
# rgb: red green blue
RED = (255, 0, 0)
BG_COLOR = (50, 50, 51)
LINE_COLOR = (40, 40, 41)
CIRCLE_COLOR = (200,200,200,50)
CROSS_COLOR = (30, 30, 31)
# ------
# SCREEN
# ------
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE Ai_impossible' )
screen.fill( BG_COLOR )
# -------------
# CONSOLE BOARD
# -------------
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )
# ---------
# FUNCTIONS
# ---------
def random(begin,end):
    import random
    #pick a random number by your range
    rand=int(random.randrange(begin,end))
    return rand
def draw_lines():
	# 1 horizontal
	pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
	# 2 horizontal
	pygame.draw.line( screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )

	# 1 vertical
	pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )
	# 2 vertical
	pygame.draw.line( screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
def draw_figures():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 1:
				pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
			elif board[row][col] == 2:
				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )	
				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )
def mark_square(row, col, player):
	board[row][col] = player
def available_square(row, col):
	return board[row][col] == 0
def is_board_full():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 0:
				return False

	return True
def check_win(player):
	# vertical win check
	for col in range(BOARD_COLS):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_winning_line(col, player)
			return True

	# horizontal win check
	for row in range(BOARD_ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning_line(row, player)
			return True

	# asc diagonal win check
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_asc_diagonal(player)
		return True

	# desc diagonal win chek
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_desc_diagonal(player)
		return True

	return False
def draw_vertical_winning_line(col, player):
	posX = col * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )
def draw_horizontal_winning_line(row, player):
	posY = row * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH )
def draw_asc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH )
def draw_desc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )
def restart():
	screen.fill( BG_COLOR )
	draw_lines()
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			board[row][col] = 0
def switch_play(player):
    player = player % 2 + 1
    return player	
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
def plr_pos(pos_num):
    return plr_poss[pos_num-1]
def ai_pos(pos_num):
    return ai_poss[pos_num-1]
def check_chance(board,ai):
    if board[0][2]==ai and board[0][1]==ai and board[0][0]==0:
        return [0,0]
    elif board[2][0]==ai and board[1][0]==ai and board[0][0]==0:    
        return [0,0]
    elif board[2][2]==ai and board[1][1]==ai and board[0][0]==0:    
        return [0,0]
    elif board[2][1]==ai and board[1][1]==ai and board[0][1]==0:    
        return [0,1]
    elif board[0][0]==ai and board[0][2]==ai and board[0][1]==0:    
        return [0,1]
    elif board[0][2]==ai and board[0][0]==ai and board[0][1]==0:    
        return [0,1]
    elif board[2][2]==ai and board[1][2]==ai and board[0][2]==0:    
        return [0,2]
    elif board[2][0]==ai and board[1][1]==ai and board[0][2]==0:    
        return [0,2]
    elif board[0][0]==ai and board[0][1]==ai and board[0][2]==0:    
        return [0,2]
    elif board[1][2]==ai and board[1][1]==ai and board[1][0]==0:    
        return [1,0]
    elif board[0][0]==ai and board[2][0]==ai and board[1][0]==0:    
        return [1,0]
    elif board[2][0]==ai and board[0][0]==ai and board[1][0]==0:    
        return [1,0]
    elif board[0][0]==ai and board[2][2]==ai and board[1][1]==0:    
        return [1,1]
    elif board[2][2]==ai and board[0][0]==ai and board[1][1]==0:    
        return [1,1]
    elif board[2][0]==ai and board[0][2]==ai and board[1][1]==0:    
        return [1,1]
    elif board[0][2]==ai and board[2][0]==ai and board[1][1]==0:    
        return [1,1]
    elif board[1][0]==ai and board[1][2]==ai and board[1][1]==0:    
        return [1,1]
    elif board[1][2]==ai and board[1][0]==ai and board[1][1]==0:    
        return [1,1]
    elif board[0][1]==ai and board[2][1]==ai and board[1][1]==0:    
        return [1,1]
    elif board[2][1]==ai and board[0][1]==ai and board[1][1]==0:    
        return [1,1]
    elif board[1][0]==ai and board[1][1]==ai and board[1][2]==0:    
        return [1,2]
    elif board[0][2]==ai and board[2][2]==ai and board[1][2]==0:    
        return [1,2]
    elif board[2][2]==ai and board[0][2]==ai and board[1][2]==0:    
        return [1,2]
    elif board[2][2]==ai and board[2][1]==ai and board[2][0]==0:    
        return [2,0]
    elif board[0][2]==ai and board[1][1]==ai and board[2][0]==0:    
        return [2,0]
    elif board[0][0]==ai and board[1][0]==ai and board[2][0]==0:    
        return [2,0]
    elif board[0][1]==ai and board[1][1]==ai and board[2][1]==0:    
        return [2,1]
    elif board[2][0]==ai and board[2][2]==ai and board[2][1]==0:    
        return [2,1]
    elif board[2][2]==ai and board[2][0]==ai and board[2][1]==0:    
        return [2,1]
    elif board[0][2]==ai and board[1][2]==ai and board[2][2]==0:    
        return [2,2]
    elif board[0][0]==ai and board[1][1]==ai and board[2][2]==0:    
        return [2,2]
    elif board[2][0]==ai and board[2][1]==ai and board[2][2]==0:    
        return [2,2]
    else:
        return []   
def corner_lr(corner):
    if corner==[0,0]:
        return[[0,1],[1,0]]
    elif corner==[0,2]:
        return[[0,1],[1,2]]
    elif corner==[2,2]:
        return[[2,1],[1,2]]
    elif corner==[2,0]:
        return[[2,1],[1,0]]
draw_lines()
# ---------
# VARIABLES
# ---------
ad=random(1,2)
player = ad
plr=ad
ai= player % 2 + 1
game_over = False
plr_poss=[]
ai_poss=[]
fp=[[0,0],[0,2],[2,2],[2,0]]
fp1=[[1,0],[1,2],[2,1],[0,1]]
fp1_temp1=[[1,0],[1,2],[2,1],[0,1]]
fp1_temp2=[[1,0],[1,2],[2,1],[0,1]]
board_temp=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
play00=[[0,1],[1,0]]
play22=[[2,1],[1,2]]
play20=[[2,1],[1,0]]
play02=[[0,1],[1,2]]
counter=0
# --------
# MAINLOOP
# --------
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not game_over and player==ad:

			mouseX = event.pos[0] # x
			mouseY = event.pos[1] # y

			clicked_row = int(mouseY // SQUARE_SIZE)
			clicked_col = int(mouseX // SQUARE_SIZE)
			plr_poss.append([clicked_row,clicked_col])
			if available_square( clicked_row, clicked_col ):
				mark_square( clicked_row, clicked_col, player )
				if check_win( player ):
					game_over = True
				draw_figures()
				player=switch_play(player)
		elif player == ad % 2 + 1 and not is_board_full():
			if counter == 0:
				if plr_pos(1)==[1,1]:
					ai_row = random(0,3)
					ai_col = random(0,3)
					while [ai_row,ai_col] not in fp:
						ai_row = random(0,3)
						ai_col = random(0,3)
					ai_poss.append([ai_row,ai_col])
				else:
					ai_row = 1
					ai_col = 1
			elif counter == 1:
				if plr_pos(1)==[1,1]:
					if plr_pos(2)!=sym(ai_pos(1),plr_pos(1)):
						ai_row = sym(plr_pos(2),[1,1])[0]
						ai_col = sym(plr_pos(2),[1,1])[1]
						ai_poss.append([ai_row,ai_col])
					else:
						ai_row = random(0,3)
						ai_col = random(0,3)
						while [ai_row,ai_col] not in fp and [ai_row,ai_col]!=plr_pos(2):
							ai_row = random(0,3)
							ai_col = random(0,3)
						ai_poss.append([ai_row,ai_col])
				elif plr_pos(1)in fp:
					if check_chance(board,plr)!=[]:
						ai_row=check_chance(board,plr)[0]
						ai_col=check_chance(board,plr)[1]
						ai_poss.append([ai_row,ai_col])
					elif plr_pos(2)==sym(plr_pos(1),[1,1]):
						a=random(0,4)
						ai_row=fp1[a][0]
						ai_col=fp1[a][1]
						while [ai_row,ai_col]==plr_pos(1) or [ai_row,ai_col]==plr_pos(2):
							a=random(0,4)
							ai_row=fp1[a][0]
							ai_col=fp1[a][1]
						ai_poss.append([ai_row,ai_col])
					elif plr_pos(2)in fp1:
						if plr_pos(2) not in corner_lr(plr_pos(1)):
							if plr_pos(1)==[0,0]:
								play00.remove(sym(plr_pos(2),[1,1]))
								ai_row=play00[0][0]
								ai_col=play00[0][1]
								ai_poss.append([ai_row,ai_col])
							elif plr_pos(1)==[2,2]:
								play22.remove(sym(plr_pos(2),[1,1]))
								ai_row=play22[0][0]
								ai_col=play22[0][1]
								ai_poss.append([ai_row,ai_col])
							elif plr_pos(1)==[0,2]:
								play02.remove(sym(plr_pos(2),[1,1]))
								ai_row=play02[0][0]
								ai_col=play02[0][1]
								ai_poss.append([ai_row,ai_col])
							elif plr_pos(1)==[2,0]:
								play20.remove(sym(plr_pos(2),[1,1]))
								ai_row=play20[0][0]
								ai_col=play20[0][1]
								ai_poss.append([ai_row,ai_col])
							else:
								ai_row=sym(plr_pos(1),plr_pos(2))[0]
								ai_col=sym(plr_pos(1),plr_pos(2))[1]
								ai_poss.append([ai_row,ai_col])
				elif plr_pos(1)in fp1:
					if plr_pos(2) in fp1:
						a=random(0,4)
						ai_row=fp[a][0]
						ai_col=fp[a][1]
						ai_poss.append([ai_row,ai_col])
					elif plr_pos(2) in fp:
						if plr_pos(1) in corner_lr(plr_pos(2)):
							ai_row=sym(plr_pos(2),plr_pos(1))[0]
							ai_col=sym(plr_pos(2),plr_pos(1))[1]
							ai_poss.append([ai_row,ai_col])
						else:
							fp1_temp2.remove(plr_pos(1))
							fp1_temp2.remove(sym(plr_pos(1),[1,1]))
							for i in fp:
								if plr_pos(1) in corner_lr(i) and i!=sym(plr_pos(2),[1,1]):
									fp1_temp2.append(i)
								a=random(0,2)
								ai_row=fp1_temp2[a][0]
								ai_col=fp1_temp2[a][1]
								ai_poss.append([ai_row,ai_col])
			elif counter >= 2:
				if check_chance(board,ai)!=[]:
					ai_row=check_chance(board,ai)[0]
					ai_col=check_chance(board,ai)[1]
				else:
					if check_chance(board,plr)!=[]:
						ai_row=check_chance(board,plr)[0]
						ai_col=check_chance(board,plr)[1]
					else:
						if counter==2 and (plr_pos(1)==[0,0] and plr_pos(2)==[1,2] and plr_pos(3)==[2,1]):
							ai_row=sym([0,0],[1,0])[0]
							ai_col=sym([0,0],[1,0])[1]
						elif counter==2 and (plr_pos(1)==[2,0] and plr_pos(2)==[0,1] and plr_pos(3)==[1,2]):
							ai_row=sym([2,0],[2,1])[0]
							ai_col=sym([2,0],[2,1])[1]
						elif counter==2 and (plr_pos(1)==[2,2] and plr_pos(2)==[1,0] and plr_pos(3)==[0,1]):
							ai_row=sym([2,2],[1,2])[0]
							ai_col=sym([2,2],[1,2])[1]
						elif counter==2 and (plr_pos(1)==[0,2] and plr_pos(2)==[1,0] and plr_pos(3)==[2,1]):
							ai_row=sym([0,2],[1,2])[0]
							ai_col=sym([0,2],[1,2])[1]
						else:
							a=random(0,9)
							ai_row=board_temp[a][0]
							ai_col=board_temp[a][1]
							while not available_square( ai_row, ai_col ):
								a=random(0,9)
								ai_row=board_temp[a][0]
								ai_col=board_temp[a][1]
							ai_row=board_temp[a][0]
							ai_col=board_temp[a][1]
			if available_square( ai_row, ai_col ):
				mark_square( ai_row, ai_col, player )
				if check_win( player ):
					game_over = True
				draw_figures()
				counter+=1
				player=switch_play(player)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				restart()
				ad=random(1,3)
				player = ad
				plr=ad
				ai= player % 2 + 1
				game_over = False
				plr_poss=[]
				ai_poss=[]
				fp=[[0,0],[0,2],[2,2],[2,0]]
				fp1=[[1,0],[1,2],[2,1],[0,1]]
				fp1_temp1=[[1,0],[1,2],[2,1],[0,1]]
				fp1_temp2=[[1,0],[1,2],[2,1],[0,1]]
				play00=[[0,1],[1,0]]
				play22=[[2,1],[1,2]]
				play20=[[2,1],[1,0]]
				play02=[[0,1],[1,2]]
				board_temp=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
				counter=0
	pygame.display.update()

