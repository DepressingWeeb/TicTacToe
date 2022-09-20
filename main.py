import sys
import pygame
from pygame.locals import *

WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
pygame.init()


class Cell:
    def __init__(self, rect):
        self.rect = rect
        self.text = ""
        self.color = BLACK
        self.color_border = BLACK

    def draw_cell(self):
        pygame.draw.rect(SCREEN, self.color_border, self.rect, 1)
        f = pygame.font.Font("freesansbold.ttf", 100)
        textSurface = f.render(self.text, True, self.color)
        textRect = textSurface.get_rect(center=self.rect.center)
        SCREEN.blit(textSurface, textRect)


class Board:
    def __init__(self):
        self.board = []
        self.p1_score=0
        self.p2_score=0
        self.p1=True
        self.new_game=False
        for i in range(3):
            temp_list = []
            for j in range(3):
                temp_list.append(Cell(pygame.rect.Rect(j * 200, i * 200, 200, 200)))
            self.board.append(temp_list)

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j].draw_cell()
        createText("SCORE",700,100,30)
        createText("P1 :",650,150,30)
        createText("P2 :", 750, 150, 30)
        createText(str(self.p1_score),640,200,30)
        createText(str(self.p2_score), 740, 200, 30)


    def check_win(self):
        for i in range(3):
            lst_temp = []
            for j in range(3):
                lst_temp.append(self.board[i][j].text)
            if "X" in lst_temp and "O" not in lst_temp and "" not in lst_temp:
                self.p1_score+=1
                return True
            elif "O" in lst_temp and "X" not in lst_temp and "" not in lst_temp:
                self.p2_score+=1
                return True

        for i in range(3):
            lst_temp=[]
            for j in range(3):
                lst_temp.append(self.board[j][i].text)
            if "X" in lst_temp and "O" not in lst_temp and "" not in lst_temp:
                self.p1_score += 1
                return True
            elif "O" in lst_temp and "X" not in lst_temp and "" not in lst_temp:
                self.p2_score += 1
                return True
        lst_temp=[]
        for i in range(3):
            lst_temp.append(self.board[i][i].text)
        if "X" in lst_temp and "O" not in lst_temp and "" not in lst_temp:
            self.p1_score += 1
            return True
        elif "O" in lst_temp and "X" not in lst_temp and "" not in lst_temp:
            self.p2_score += 1
            return True
        lst_temp = []
        for i in range(3):
            lst_temp.append(self.board[i][2-i].text)
        if "X" in lst_temp and "O" not in lst_temp and "" not in lst_temp:
            self.p1_score += 1
            return True
        elif "O" in lst_temp and "X" not in lst_temp and "" not in lst_temp:
            self.p2_score += 1
            return True
        return False




        pass

    def isfull(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j].text=="":
                    return False
        return True
    def check_draw(self):
        if self.isfull():
            if not self.check_win():
                return True
        return False

    def check_mouse(self):
        if pygame.mouse.get_pressed()[0]:
            if not self.new_game:
                x,y=pygame.mouse.get_pos()
                row,col=self.get_cell(x,y) if x<=600 else (None,None)
                if row is None:
                    return
                else:
                    if self.p1 and self.board[row][col].text=="":
                        self.p1=False
                        self.board[row][col].text="X"
                    elif (not self.p1) and self.board[row][col].text=="":
                        self.p1 = True
                        self.board[row][col].text = "O"
            else:
                self.new_game=False


    def check_state(self):

        if self.check_win():
            print("WIN")
            SCREEN.fill(WHITE)
            self.draw_board()
            pygame.display.update()
            pygame.time.wait(3000)
            self.clear_board()
            self.new_game=True
        elif self.check_draw():
            print("DRAW")
            SCREEN.fill(WHITE)
            self.draw_board()
            pygame.display.update()
            pygame.time.wait(3000)
            self.clear_board()
            self.new_game=True


    def play_computer(self):
        pass

    def get_cell(self,x,y):
        return y//200,x//200

    def clear_board(self):
        self.board=[]
        for i in range(3):
            temp_list = []
            for j in range(3):
                temp_list.append(Cell(pygame.rect.Rect(j * 200, i * 200, 200, 200)))
            self.board.append(temp_list)



myboard = Board()


def check_quit():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def update_screen():
    pygame.display.update()
    CLOCK.tick(20)

def createText(text, x, y, fontSize=20):
    mytext = pygame.font.Font("freesansbold.ttf", fontSize)
    textSurface = mytext.render(text, True, BLACK)
    textRect = textSurface.get_rect()
    textRect.center = (x, y)
    SCREEN.blit(textSurface, textRect)

def main():
    game = True
    while game:
        SCREEN.fill(WHITE)
        myboard.draw_board()
        myboard.check_mouse()
        myboard.check_state()
        check_quit()
        update_screen()


main()
