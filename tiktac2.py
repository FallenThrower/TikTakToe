
import pygame, time

logo=pygame.image.load('/Applications/code/tik tak project/mats/logo.png')

class tiktak:    
    def  __init__(self): # sets logo, displays plain white window
        print('initializing')
        pygame.init()
        self.white=(255, 255, 255, 255)
        self.black=(0,0,0, 0)
        pygame.display.set_icon(logo)
        pygame.display.set_caption('TikTak2.0')
        self.xaxis=600
        self.yaxis=600
        self.screen = pygame.display.set_mode(size=(self.xaxis,self.yaxis))
        self.screen.fill(self.white)
        self.turn=True
        
        self.cross=(self.xaxis/3)/5
        self.board()
        self.playing()

    def turns(self,drawing): # taking turns
        
        if self.turn:
            self.turn=False
            self.circle(drawing)
        else:
            self.turn=True
            self.crosss(drawing)
        
        
    def circle(self,dra): # draws circle
        radius=2*self.cross
        center=[(dra[0][0]+dra[1][0])/2,(dra[0][1]+dra[1][1])/2]
        pygame.draw.circle(self.screen,self.black,center,radius,10)
        pygame.display.update()
        print('circle')
                
        
    def crosss(self,dr): # draws cross
        print('cross')
        c1=[dr[0][0]+self.cross,dr[0][1]+self.cross]
        c2=[dr[1][0]-self.cross,dr[1][1]-self.cross]
        c3=[dr[2][0]-self.cross,dr[2][1]+self.cross]
        c4=[dr[3][0]+self.cross,dr[3][1]-self.cross]
        pygame.draw.line(self.screen, self.black,c1,c2,10)
        pygame.draw.line(self.screen, self.black,c3,c4,10)
        pygame.display.update()
        
    def board(self): # draws 4 lines for board and separates into 9 boxes
        print('board')
        
        self.line_x=self.xaxis/3
        self.line_y=self.yaxis/3
        self.line1, self.line2, self.line3, self.line4 = (self.line_x,0),(self.line_x*2,0),(0,self.line_y),(0,2*self.line_y)
        self.line10, self.line20, self.line30, self.line40 = (self.line_x,self.yaxis),(2*self.line_x,self.yaxis),(self.xaxis,self.line_y),(self.yaxis,self.line_y *2)
        pygame.draw.line(self.screen, self.black,self.line1,self.line10, 2 )
        pygame.draw.line(self.screen, self.black,self.line2,self.line20, 2 )
        pygame.draw.line(self.screen, self.black,self.line3,self.line30, 2 )
        pygame.draw.line(self.screen, self.black,self.line4,self.line40, 2 )

        self.box1=[(0,0), (self.line_x,self.line_y),(self.line_x,0),(0,self.line_y)]
        self.box2=[(self.line_x,0),(2*self.line_x, self.line_y),(2*self.line_x,0),(self.line_x,self.line_y)]
        self.box3=[(2*self.line_x,0),(self.xaxis, self.line_y),(self.xaxis,0),(2*self.line_x,self.line_y)]
        self.box4=[(0,self.line_y),(self.line_x,2*self.line_y),(self.line_x,self.line_y),(0,2*self.line_y)]
        self.box5=[(self.line_x,self.line_y),(2*self.line_x,2*self.line_y),(2*self.line_x,self.line_y),(self.line_x,2*self.line_y)]
        self.box6=[(2*self.line_x,self.line_y),(self.xaxis,2*self.line_y),(self.xaxis,self.line_y),(2*self.line_x,2*self.line_y)]
        self.box7=[(0,2*self.line_y),(self.line_x, self.yaxis),(self.line_x, 2*self.line_y),(0,self.yaxis)]
        self.box8=[(self.line_x,2*self.line_y),(2*self.line_x, self.yaxis),(2*self.line_x,2*self.line_y),(self.line_x,self.yaxis)]
        self.box9=[(2*self.line_x,2*self.line_y),(self.xaxis,self.yaxis),(self.xaxis,2*self.line_y),(2*self.line_x, self.yaxis)]

        pygame.display.flip()

    def playing(self): # looping the actual game
        print('playing')
        '''
        pygame.mixer.music.load('/Users/allangautam/Downloads/YOASOBI - Racing Into The Night Lyrics (JPNROMENG).mp3')
        pygame.mixer.music.play()
        '''
        running=True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                    #pygame.mixer.music.stop()
                    pygame.display.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    # finding which box user clicked
                    
                    if pos[0]>self.box1[0][0] and pos[0]<self.box1[1][0] and pos[1]>self.box1[0][1] and pos[1]<self.box1[1][1]:
                        self.turns(self.box1)
                        print('box 1')
                    if pos[0]>self.box2[0][0] and pos[0]<self.box2[1][0] and pos[1]>self.box2[0][1] and pos[1]<self.box2[1][1]:
                        self.turns(self.box2)
                        print('box 2')
                    if pos[0]>self.box3[0][0] and pos[0]<self.box3[1][0] and pos[1]>self.box3[0][1] and pos[1]<self.box3[1][1]:
                        self.turns(self.box3)
                        print('box 3')
                    if pos[0]>self.box4[0][0] and pos[0]<self.box4[1][0] and pos[1]>self.box4[0][1] and pos[1]<self.box4[1][1]:
                        self.turns(self.box4)
                        print('box 4')
                    if pos[0]>self.box5[0][0] and pos[0]<self.box5[1][0] and pos[1]>self.box5[0][1] and pos[1]<self.box5[1][1]:
                        self.turns(self.box5)
                        print('box 5')
                    if pos[0]>self.box6[0][0] and pos[0]<self.box6[1][0] and pos[1]>self.box6[0][1] and pos[1]<self.box6[1][1]:
                        self.turns(self.box6)
                        print('box 6')
                    if pos[0]>self.box7[0][0] and pos[0]<self.box7[1][0] and pos[1]>self.box7[0][1] and pos[1]<self.box7[1][1]:
                        self.turns(self.box7)
                        print('box 7')
                    if pos[0]>self.box8[0][0] and pos[0]<self.box8[1][0] and pos[1]>self.box8[0][1] and pos[1]<self.box8[1][1]:
                        self.turns(self.box8)
                        print('box 8')
                    if pos[0]>self.box9[0][0] and pos[0]<self.box9[1][0] and pos[1]>self.box9[0][1] and pos[1]<self.box9[1][1]:
                        self.turns(self.box9)
                        print('box 9')


a=tiktak()




















































































'''
pygame.init()
white=(255, 255, 255, 255)
black=(0,0,0, 0)
pygame.display.set_icon(logo)
pygame.display.set_caption('TikTak2.0')
xaxis=600
yaxis=600
screen = pygame.display.set_mode(size=(xaxis,yaxis))
screen.fill(white)


# Drawing outline for game
line_x=xaxis/3
line_y=yaxis/3
line1, line2, line3, line4 = (line_x,0),(line_x*2,0),(0,line_y),(0,2*line_y)
line10, line20, line30, line40 = (line_x,yaxis),(2*line_x,yaxis),(xaxis,line_y),(yaxis,line_y *2)
pygame.draw.line(screen, black,line1,line10, 2 )
pygame.draw.line(screen, black,line2,line20, 2 )
pygame.draw.line(screen, black,line3,line30, 2 )
pygame.draw.line(screen, black,line4,line40, 2 )

pygame.display.flip()

# to draw x's and 0's (coordinates)




# seperate areas where users click, 9 boxes

box1=[(0,0), (line_x,line_y)]
box2=[(line_x,0),(2*line_x, line_y)]
box3=[(2*line_x,0),(xaxis, line_y)]
box4=[(0,line_y),(line_x,2*line_y)]
box5=[(line_x,line_y),(2*line_x,2*line_y)]
box6=[(2*line_x,line_y),(xaxis,2*line_y)]
box7=[(0,2*line_y),(line_x, yaxis)]
box8=[(line_x,2*line_y),(2*line_x, yaxis)]
box9=[(2*line_x,2*line_y),(xaxis,yaxis)]

# running the game

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.display.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            # finding which box user clicked
            
            if pos[0]>box1[0][0] and pos[0]<box1[1][0] and pos[1]>box1[0][1] and pos[1]<box1[1][1]:
                print('box 1')
            if pos[0]>box2[0][0] and pos[0]<box2[1][0] and pos[1]>box2[0][1] and pos[1]<box2[1][1]:
                print('box 2')
            if pos[0]>box3[0][0] and pos[0]<box3[1][0] and pos[1]>box3[0][1] and pos[1]<box3[1][1]:
                print('box 3')
            if pos[0]>box4[0][0] and pos[0]<box4[1][0] and pos[1]>box4[0][1] and pos[1]<box4[1][1]:
                print('box 4')
            if pos[0]>box5[0][0] and pos[0]<box5[1][0] and pos[1]>box5[0][1] and pos[1]<box5[1][1]:
                print('box 5')
            if pos[0]>box6[0][0] and pos[0]<box6[1][0] and pos[1]>box6[0][1] and pos[1]<box6[1][1]:
                print('box 6')
            if pos[0]>box7[0][0] and pos[0]<box7[1][0] and pos[1]>box7[0][1] and pos[1]<box7[1][1]:
                print('box 7')
            if pos[0]>box8[0][0] and pos[0]<box8[1][0] and pos[1]>box8[0][1] and pos[1]<box8[1][1]:
                print('box 8')
            if pos[0]>box9[0][0] and pos[0]<box9[1][0] and pos[1]>box9[0][1] and pos[1]<box9[1][1]:
                print('box 9')
            
            


'''





        
