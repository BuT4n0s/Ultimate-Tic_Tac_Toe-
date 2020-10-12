import pygame
import os
import sys
import time

pygame.init()

wnWidth = 520
wnHeight = 480
wnColor = (30, 30, 30)
wnTitle = "X-O mega"

wn = pygame.display.set_mode((wnWidth, wnHeight))
pygame.display.set_caption(wnTitle)




blueMouse = pygame.image.load("BlueMouse.png")
redMouse = pygame.image.load("RedMouse.png")
pygame.mouse.set_visible(False)

startBoxColor = (240, 240, 240)
red = (239, 57, 57)
blue = (46, 121, 232)
winr_color=(139,0,0)
winb_color=(0,225,225)
none_play=(155,155,155)

redWon = pygame.image.load("RedWon.png")
blueWon = pygame.image.load("BlueWon.png")
drawImg = pygame.image.load("Draw.png")
endImg = pygame.image.load("ClickToContinue.png")

while True:
    turn = "r"

    bigGrid=[["d", "d", "d"],
             ["d", "d", "d"],
             ["d", "d", "d"]]

    gridData = [[[["d", "d", "d"],
                  ["d", "d", "d"],
                  ["d", "d", "d"]],
                 [["d", "d", "d"],
                  ["d", "d", "d"],
                  ["d", "d", "d"]],
                 [["d", "d", "d"],
                  ["d", "d", "d"],
                  ["d", "d", "d"]]],
                [[["d", "d", "d"],
                  ["d", "d", "d"],
                  ["d", "d", "d"]],
                 [["d", "d", "d"],
                  ["d", "d", "d"],
                  ["d", "d", "d"]],
                 [["d", "d", "d"],
                  ["d", "d", "d"],
                  ["d", "d", "d"]]],
                [[["d", "d", "d"],
                  ["d", "d", "d"],
                  ["d", "d", "d"]],
                 [["d", "d", "d"],
                  ["d", "d", "d"],
                  ["d", "d", "d"]],
                 [["d", "d", "d"],
                  ["d", "d", "d"],
                  ["d", "d", "d"]]]]


    wn = pygame.display.set_mode((wnWidth, wnHeight))
    pygame.display.set_caption(wnTitle)
    grid = []
    run = True

    """
    Red vs Blue
    Tic-Tac-Toe
    """


    class GridBox:
        def __init__(self, pos, expand, color, data, vert, hor):
            self.color = color
            self.rect = (pos[0], pos[1], expand, expand)
            self.data = data
            self.vert = vert
            self.hor = hor

        def draw(self):
            if self.data == "r":
                self.color = red
            elif self.data == "b":
                self.color = blue
            elif self.data=="wr":
                self.color =winr_color
            elif self.data=="wb":
                self.color =winb_color
            elif self.data=="n":
                self.color =none_play
            else:
                self.color = startBoxColor

            pygame.draw.rect(wn, self.color, self.rect)

        def touching_mouse(self):
            mouse_pos = pygame.mouse.get_pos()
            return pygame.Rect(self.rect).collidepoint(mouse_pos[0], mouse_pos[1])


    def add_row(y, color, grid_index):
        global grid

        grid.append(GridBox((50, y), 40, color, "d", grid_index, 0))
        grid.append(GridBox((95, y), 40, color, "d", grid_index, 1))
        grid.append(GridBox((140, y), 40, color, "d", grid_index, 2))
        grid.append(GridBox((195, y), 40, color, "d", grid_index, 3))
        grid.append(GridBox((240, y), 40, color, "d", grid_index, 4))
        grid.append(GridBox((285, y), 40, color, "d", grid_index, 5))
        grid.append(GridBox((340, y), 40, color, "d", grid_index,6))
        grid.append(GridBox((385, y), 40, color, "d", grid_index, 7))
        grid.append(GridBox((430, y), 40, color, "d", grid_index, 8))

    add_row(30, startBoxColor, 0)
    add_row(75, startBoxColor, 1)
    add_row(120, startBoxColor, 2)
    add_row(175, startBoxColor, 3)
    add_row(220, startBoxColor, 4)
    add_row(265, startBoxColor, 5)
    add_row(320, startBoxColor, 6)
    add_row(365, startBoxColor, 7)
    add_row(410, startBoxColor, 8)


    def render_screen():
        global grid, box, blueMouse, redMouse, turn
        wn.fill(wnColor)

        for box in grid:
            box.draw()

        wn.blit(redMouse if turn is "r" else blueMouse, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))

        pygame.display.update()


    def location_to_play(a,b):
        print(bigGrid[a][b])
        if bigGrid[a][b]=="d":
            print("ok donne")        
            for i in range(3):
              for m in range(3):
                for w in range(3):
                  for c in range(3):
            
                    if gridData[i][m][w][c] == "d":
                        gridData[i][m][w][c]="n"
                        
            for i in range(3):
                for m in range (3) :
                    if gridData[a][b][i][m]== "d" or gridData[a][b][i][m]=="n":
                        gridData[a][b][i][m]="d"
        else:
            print("beter")
            for i in range(3):
              for m in range(3):
                for w in range(3):
                  for c in range(3):
            
                    if gridData[i][m][w][c] == "d" : 
                        gridData[i][m][w][c]="d"
                    if gridData[i][m][w][c]=="n":
                        gridData[i][m][w][c]="d"


    def update_grid(gridData):

        grid[0].data=gridData[0][0][0][0]
        grid[1].data=gridData[0][0][0][1]
        grid[2].data=gridData[0][0][0][2]
        grid[3].data=gridData[0][1][0][0]
        grid[4].data=gridData[0][1][0][1]
        grid[5].data=gridData[0][1][0][2]
        grid[6].data=gridData[0][2][0][0]
        grid[7].data=gridData[0][2][0][1]
        grid[8].data=gridData[0][2][0][2]
        grid[9].data=gridData[0][0][1][0]
        grid[10].data=gridData[0][0][1][1]
        grid[11].data=gridData[0][0][1][2]
        grid[12].data=gridData[0][1][1][0]
        grid[13].data=gridData[0][1][1][1]
        grid[14].data=gridData[0][1][1][2]
        grid[15].data=gridData[0][2][1][0]
        grid[16].data=gridData[0][2][1][1]
        grid[17].data=gridData[0][2][1][2]
        grid[18].data=gridData[0][0][2][0]
        grid[19].data=gridData[0][0][2][1]
        grid[20].data=gridData[0][0][2][2]
        grid[21].data=gridData[0][1][2][0]
        grid[22].data=gridData[0][1][2][1]
        grid[23].data=gridData[0][1][2][2]
        grid[24].data=gridData[0][2][2][0]
        grid[25].data=gridData[0][2][2][1]
        grid[26].data=gridData[0][2][2][2]
        grid[27].data=gridData[1][0][0][0]
        grid[28].data=gridData[1][0][0][1]
        grid[29].data=gridData[1][0][0][2]
        grid[30].data=gridData[1][1][0][0]
        grid[31].data=gridData[1][1][0][1]
        grid[32].data=gridData[1][1][0][2]
        grid[33].data=gridData[1][2][0][0]
        grid[34].data=gridData[1][2][0][1]
        grid[35].data=gridData[1][2][0][2]
        grid[36].data=gridData[1][0][1][0]
        grid[37].data=gridData[1][0][1][1]
        grid[38].data=gridData[1][0][1][2]
        grid[39].data=gridData[1][1][1][0]
        grid[40].data=gridData[1][1][1][1]
        grid[41].data=gridData[1][1][1][2]
        grid[42].data=gridData[1][2][1][0]
        grid[43].data=gridData[1][2][1][1]
        grid[44].data=gridData[1][2][1][2]
        grid[45].data=gridData[1][0][2][0]
        grid[46].data=gridData[1][0][2][1]
        grid[47].data=gridData[1][0][2][2]
        grid[48].data=gridData[1][1][2][0]
        grid[49].data=gridData[1][1][2][1]
        grid[50].data=gridData[1][1][2][2]
        grid[51].data=gridData[1][2][2][0]
        grid[52].data=gridData[1][2][2][1]
        grid[53].data=gridData[1][2][2][2]
        grid[54].data=gridData[2][0][0][0]
        grid[55].data=gridData[2][0][0][1]
        grid[56].data=gridData[2][0][0][2]
        grid[57].data=gridData[2][1][0][0]
        grid[58].data=gridData[2][1][0][1]
        grid[59].data=gridData[2][1][0][2]
        grid[60].data=gridData[2][2][0][0]
        grid[61].data=gridData[2][2][0][1]
        grid[62].data=gridData[2][2][0][2]
        grid[63].data=gridData[2][0][1][0]
        grid[64].data=gridData[2][0][1][1]
        grid[65].data=gridData[2][0][1][2]
        grid[66].data=gridData[2][1][1][0]
        grid[67].data=gridData[2][1][1][1]
        grid[68].data=gridData[2][1][1][2]
        grid[69].data=gridData[2][2][1][0]
        grid[70].data=gridData[2][2][1][1]
        grid[71].data=gridData[2][2][1][2]
        grid[72].data=gridData[2][0][2][0]
        grid[73].data=gridData[2][0][2][1]
        grid[74].data=gridData[2][0][2][2]
        grid[75].data=gridData[2][1][2][0]
        grid[76].data=gridData[2][1][2][1]
        grid[77].data=gridData[2][1][2][2]
        grid[78].data=gridData[2][2][2][0]
        grid[79].data=gridData[2][2][2][1]
        grid[80].data=gridData[2][2][2][2]
        


    def round_win_red(ver,hor):

        gridData[vert][hor][0][0] = "wr"
        gridData[vert][hor][0][1]= "wr"
        gridData[vert][hor][0][2]= "wr"
        gridData[vert][hor][1][0]= "wr"
        gridData[vert][hor][1][1]= "."
        gridData[vert][hor][1][2]= "wr"
        gridData[vert][hor][2][0]= "wr"
        gridData[vert][hor][2][1]= "wr"
        gridData[vert][hor][2][2]= "wr"




    def round_win_blue(vert,hor):
        gridData[vert][hor][0][0] = "wb"
        gridData[vert][hor][0][1]= "."
        gridData[vert][hor][0][2]= "wb"
        gridData[vert][hor][1][0]= "."
        gridData[vert][hor][1][1]= "wb"
        gridData[vert][hor][1][2]= "."
        gridData[vert][hor][2][0]= "wb"
        gridData[vert][hor][2][1]= "."
        gridData[vert][hor][2][2]= "wb"


    def check_round(data):
        

        for i in range(3):
            if data[0][i] == "r":
                if data[1][i] == "r":                 
                    if data[2][i] == "r":   
                        return "r"
            # -------------------------------------------
            if data[0][i] == "b":
                if data[1][i] == "b":
                    if data[2][i] == "b":
                        return "b"
            if data[i][0] == "r":
                if data[i][1] == "r":
                    if data[i][2] == "r":
                        return "r"
            # -------------------------------------------
            if data[i][0] == "b":
                if data[i][1] == "b":
                    if data[i][2] == "b":
                        return "b"
        # -----------------------------------------------
        if data[0][0] == "r":
            if data[1][1] == "r":
                if data[2][2] == "r":
                    return "r"
        # -----------------------------------------------
        if data[0][2] == "r":
            if data[1][1] == "r":
                if data[2][0] == "r":
                    return "r"
        # ------------------------------------------------
        if data[0][0] == "b":
            if data[1][1] == "b":
                if data[2][2] == "b":
                    return "b"
        # -----------------------------------------------       
        if data[0][2] == "b":
            if data[1][1] == "b":
                if data[2][0] == "b":
                    return "b"


    def check_winner(data):
        for row in data:
            if row == ["r", "r", "r"]:
                return "r"
            if row == ["b", "b", "b"]:
                return "b"
        # ------------------------------------------------
        for i in range(3):
            if data[0][i] == "r":
                if data[1][i] == "r":
                    if data[2][i] == "r":
                        return "r"
        # -------------------------------------------
            if data[0][i] == "b":
                if data[1][i] == "b":
                    if data[2][i] == "b":
                        return "b"
        # -----------------------------------------------
        if data[0][0] == "r":
            if data[1][1] == "r":
                if data[2][2] == "r":
                    return "r"
        # ------------------------------------------------
        if data[0][2] == "r":
            if data[1][1] == "r":
                if data[2][0] == "r":
                    return "r"
        # ------------------------------------------------
        if data[0][0] == "b":
            if data[1][1] == "b":
                if data[2][2] == "b":
                    return "b"
        # ------------------------------------------------
        if data[0][2] == "b":
            if data[1][1] == "b":
                if data[2][0] == "b":
                    return "b"


    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            for box in grid:
                
                if event.type == pygame.MOUSEBUTTONDOWN and box.touching_mouse():
                    
                    if box.data == "d":
                        
                        vert=box.vert/3
                        hor =box.hor/3
                        gridData[vert][hor][box.vert-3*(vert)][box.hor-3*(hor)] = turn
                        turn = "b" if turn == "r" else "r"
                        print(vert)
                        print(hor)

                        if check_round(gridData[vert][hor])== "r":
                            round_win_red(vert,hor)
                            bigGrid[vert][hor]="r"
                            
                    


                        if check_round(gridData[vert][hor])== "b":
                            round_win_blue(vert,hor)
                            bigGrid[vert][hor]="b"
                        location_to_play(box.vert-3*(vert),box.hor-3*(hor))
                        update_grid(gridData)

        if check_winner(bigGrid) == "r" or check_winner(bigGrid) == "b":
            time.sleep(3)
            run=False
            print("winn")


        render_screen()

    #######################################

    pressed = False
    tick = 0

    while not pressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tick > 60:
                    pressed = True

        wn.fill(wnColor)

        if check_winner(bigGrid) == "r":
            # RED HAS WON
            wn.blit(redWon, (wnWidth / 2 - redWon.get_width() / 2, wnHeight / 2 - redWon.get_height() / 2))
        elif check_winner(bigGrid) == "b":
            # BLUE HAS WON
            wn.blit(blueWon, (wnWidth / 2 - blueWon.get_width() / 2, wnHeight / 2 - blueWon.get_height() / 2))
        else:
            # DRAW
            wn.blit(drawImg, (wnWidth / 2 - drawImg.get_width() / 2, wnHeight / 2 - drawImg.get_height() / 2))

        if tick > 60:
            wn.blit(endImg, (wnWidth / 2 - endImg.get_width() / 2, 350))

        mousePos = pygame.mouse.get_pos()
        wn.blit(blueMouse if check_winner(gridData) == "b" else redMouse, (mousePos[0], mousePos[1]))

        pygame.display.update()

        tick += 1
   
