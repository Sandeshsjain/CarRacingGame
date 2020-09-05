import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 600
gray = (119,118,110)
black = (0,0,0)
Red = (255,0,0)
gamedisplays = pygame.display.set_mode((display_width,display_height ))
pygame.display.set_caption("Car game")
clock = pygame.time.Clock()
caring = pygame.image.load('images(86).jpg')
backgroundpic = pygame.image.load('grass.jpg')
yellow_strip = pygame.image.load('yellow.jpg')
strip = pygame.image.load('white.jpg')
car_width = 94

def scoresystem(passed,score):
     font=pygame.font.Font("freesansbold.ttf",50)
     text=font.render("Passed"+str(passed),True,black)
     score = font.render("Score" + str(score), True,Red)
     gamedisplays.blit(text,(0,50))
     gamedisplays.blit(score,(0,10))

def obstacle(obs_startx,obs_starty,obs):
     if obs==0:
          obs_pic = pygame.image.load("obs.jpg")
     elif obs==1:
          obs_pic = pygame.image.load("obs.jpg")
     elif obs ==2:
          obs_pic = pygame.image.load("obs.jpg")
     elif obs == 3:
          obs_pic = pygame.image.load("obs.jpg")
     elif obs == 4:
          obs_pic = pygame.image.load("obs.jpg")
     elif obs == 5:
          obs_pic = pygame.image.load("obs.jpg")
     elif obs == 6:
          obs_pic = pygame.image.load("obs.jpg")
     gamedisplays.blit(obs_pic,(int(obs_startx),int(obs_starty)))



def text_objects(text,font):
     textsurface = font.render(text,True,black)
     return textsurface,textsurface.get_rect()


def message_display(text):
     largetext = pygame.font.Font("freesansbold.ttf",80)
     textsurf,textrect = text_objects(text,largetext)
     textrect.center = (int((display_width/2)),int((display_height/2)))
     gamedisplays.blit(textsurf,textrect)
     pygame.display.update()
     time.sleep(3)
     game_loop()

def crash():
     message_display(" YOU CRASHED")

def background():
     gamedisplays.blit(backgroundpic,(0,0))
     gamedisplays.blit(backgroundpic,(0,100))
     gamedisplays.blit(backgroundpic,(0,200))
     gamedisplays.blit(backgroundpic,(0,300))
     gamedisplays.blit(backgroundpic,(0,400))
     gamedisplays.blit(backgroundpic,(0,500))
     gamedisplays.blit(backgroundpic,(700,0))
     gamedisplays.blit(backgroundpic,(700,100))
     gamedisplays.blit(backgroundpic,(700,200))
     gamedisplays.blit(backgroundpic,(700,300))
     gamedisplays.blit(backgroundpic,(700,400))
     gamedisplays.blit(backgroundpic,(700,500))
     gamedisplays.blit(yellow_strip,(400,0))
     gamedisplays.blit(yellow_strip, (400,300))
     gamedisplays.blit(strip,(110,0))
     gamedisplays.blit(strip, (110,100))
     gamedisplays.blit(strip, (110,200))
     gamedisplays.blit(strip, (110,300))
     gamedisplays.blit(strip, (110,400))
     gamedisplays.blit(strip, (110,500))
     gamedisplays.blit(strip,(675,0))
     gamedisplays.blit(strip, (675,100))
     gamedisplays.blit(strip, (675,200))
     gamedisplays.blit(strip, (675,300))
     gamedisplays.blit(strip, (675,400))
     gamedisplays.blit(strip, (675,500))
     

def car(x,y):
     gamedisplays.blit(caring,(int(x),int(y)))
 
def game_loop():
     x = (display_width*0.45)
     y = (display_height*0.8)
     x_change = 0
     obstacles_speed=9
     obs = 0
     y_change=0
     obs_startx=random.randrange(110,(display_width-110))
     obs_starty=-750
     obs_width = 37
     obs_height = 68
     passed = 0
     level = 0
     score = 0

     bumped = False
     while not bumped:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  quit()
          if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_LEFT:
                    x_change = -5
               if event.key==pygame.K_RIGHT:
                    x_change = 5
               if event.key == pygame.K_a:
                    obstacles_speed+=2
               if event.key == pygame.K_b:
                    obstacles_speed-=2




          if event.type==pygame.KEYUP:
               if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change = 0
          x = x+x_change     
          gamedisplays.fill(gray)
          background()
          obs_starty -= (obstacles_speed/4)
          obstacle(obs_startx,obs_starty,obs)
          obs_starty+=obstacles_speed
          car(x,y)
          scoresystem(passed,score)
          if x>675-car_width or x<110:
               crash()
          if x>display_width-(car_width+110) or x<110:
               crash()
          if obs_starty>display_height:
               obs_starty = 0 - obs_height
               obs_startx=random.randrange(170,(display_width-170))
               obs = random.randrange(0,7)
               passed=passed+1
               score=passed*10
               if int(passed)%10==0:
                    level = level+1
                    obstacles_speed+=2
                    largetext = pygame.font.Font("freesansbold.ttf", 80)
                    textsurf, textrect = text_objects("LEVEL"+str(level), largetext)
                    textrect.center = (int((display_width / 2)), int((display_height / 2)))
                    gamedisplays.blit(textsurf, textrect)
                    pygame.display.update()
                    time.sleep(3)


          if y<obs_starty+obs_height:
               if x>obs_startx and x<obs_startx+obs_width or x+car_width>obs_startx and x+car_width<obs_startx+obs_width:
                    crash()

          pygame.display.update()
          clock.tick(60)
game_loop()
pygame.quit()
quit()
