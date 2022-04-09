import pygame 
import random
import math

player_list =[]
bulet_list = []
weapons = []
stages_library =[]
stages_library_flip = []
weapon_list = []
weapons_view = []
yellow = (255,242,0)
white = (255,255,255)
red = (255, 0, 0)
black = (0,0,0)
display_width = int(1280)
display_heigth = int(720)
pygame.init()
pygame.font.init()
textfont = pygame.font.SysFont('Comic Sans MS', 30)
background = pygame.image.load('spring_bg.png')
def win():
    textsurface = textfont.render('please send money on +79655820122', False, red)
    # pygame.mixer.music.load('.mp3')
    # pygame.mixer.music.play(0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        gameDisplay.blit(textsurface, (display_width/2,display_heigth/2))
        gameDisplay.blit(textsurface, (500,500))
        pygame.display.update()
        clock.tick(FPS)
class player:
    def __init__(self):
        self.color = 0
        self.color2 = 0
        self.speed = 5
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.size = 10
        self.pos_x = display_width//2
        self.pos_y = 650
        self.jump_speed = 0

    def walk_right(self):
        self.move_right = True
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def walk_left(self):
        self.move_left = True
        self.move_right = False
        self.move_up = False
        self.move_down = False

    def walk_up(self):
        self.move_right = False
        self.move_left = False
        if sum(self.color) < 450 or sum(self.color2) < 450:
            self.move_up = True
        self.move_down = False

    def walk_down(self):
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = True

    def stop(self):
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        try:
            self.color_right = gameDisplay.get_at((int(self.pos_x + self.size*2), int(self.pos_y + self.size/2)))
        except:
            self.color_right = black
        try:
            self.color_left = gameDisplay.get_at((int(self.pos_x - self.size*2), int(self.pos_y + self.size/2)))
        except:
            self.color_left = black
        try:
            self.color_up = gameDisplay.get_at((int(self.pos_x + self.size/2), int(self.pos_y - self.size)))
            self.color_up2 = gameDisplay.get_at((int(self.pos_x + self.size/2), int(self.pos_y - self.size*1.5)))
        except:
            self.color_up2 =black
            self.color_up =black
        try:
            self.color = gameDisplay.get_at((int(self.pos_x + self.size/2), int(self.pos_y + self.size)))
            self.color2 = gameDisplay.get_at((int(self.pos_x + self.size/2), int(self.pos_y + 1.5 * self.size)))
        except:
            print (self.color)
            self.color = black
        # print(self.color)
        if self.move_right == True and self.color_right != black :
            self.pos_x += self.speed
        if self.move_left == True and self.color_left != black:
            self.pos_x -= self.speed
        if self.move_up == True or self.color ==yellow and self.move_down != True:    
            self.jump_speed = 8
            self.pos_y -= 15
            self.move_up = False  
        elif self.move_up == False and sum(self.color) < 450 or sum(self.color2) < 450: 
            self.jump_speed = 0
            # print('чёрный под мной')
        elif (sum(self.color_up2) < 450 or sum(self.color_up) < 450) and self.jump_speed > 0:
            self.jump_speed *= -1
        else:
            if self.color == yellow:
                self.jump_speed = -2
            else:
                self.jump_speed = self.jump_speed - 1
        # print(self.pos_y)
        # print(self.color)
        # print(self.move_up)
        self.pos_y -= self.jump_speed
        if self.pos_y>0.98*display_heigth:
            exit()
        gameDisplay.blit(player1_viwe, (self.pos_x,self.pos_y))
class bulets:
    def __init__(self, object_type, x, y, speed, diraction):
        self.type = object_type
        self.size_dict = {'canon': 15}
        self.size = self.size_dict[self.type]
        self.pos_x = x
        self.pos_y = y + 30
        self.speed = speed
        self.diraction = diraction
    def update(self):
        global player1
        if self.speed == 0:
            pygame.draw.circle(gameDisplay,white,[self.pos_x,self.pos_y], self.size)
            return
        try:
            self.color_around = gameDisplay.get_at((int(self.pos_x), int(self.pos_y)))
        except IndexError:
            return
        print(self.color_around)
        if sum(self.color_around) < 450 :
            self.speed = 0
        elif self.color_around != black or player1.pos_y + player1.pos_x - self.pos_x - self.pos_y < self.size:    
            self.pos_y -= math.sin(math.pi * self.diraction/180)*self.speed
            self.pos_x += math.cos(math.pi * self.diraction/180)*self.speed
            pygame.draw.circle(gameDisplay,red,[self.pos_x,self.pos_y], self.size)
            if abs(player1.pos_y - self.pos_y) < self.size and abs(player1.pos_x - self.pos_x) < self.size :
                del player1 
                win()
        
def delete_fo():
    global bulet_list
    i=0
    while i < len(bulet_list):
        bulet_list[i].update()
        if bulet_list[i].pos_y > display_heigth - bulet_list[i].size - int(30/720*display_heigth):
            del bulet_list[i]
        # elif abs(bulet_list[i].pos_x - player1.pos_x) < player1.size + bulet_list[i].size and abs(bulet_list[i].pos_y - player1.pos_y) < player1.size + bulet_list[i].size:
        #     if bulet_list[i].object_type == 'snowball':
        #         player1.size += bulet_list[i].size//2
        #         player1.pos_y -= bulet_list[i].size//2
        #     if bulet_list[i].object_type == 'rock':
        #         player1.size -= bulet_list[i].size//2
        #         player1.pos_y += bulet_list[i].size//2
        #     del bulet_list[i]
        else:
            i+=1
def rot_center(image, angle, x, y): 
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
    return rotated_image, new_rect

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    # print(angle)
    surf.blit(rotated_image, new_rect)

class weapon:
    def __init__(self, weapon_type,pos_x,pos_y):
        self.angl = 0
        self.type= weapon_type
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.counter = 0
        print ('weapon_' + self.type + '.jpg')
        self.img = pygame.image.load('weapon_' + self.type + '.png')
        self.img = pygame.transform.scale(self.img, (70, 60))
        if self.pos_x > display_width//2:
            self.img = pygame.transform.flip(self.img, True, False)
        self.damage_dict = {'canon': 50}
        self.damage = self.damage_dict[self.type]
        self.reloading_time_dict = {'canon': 1}
        self.reloading_time = self.reloading_time_dict[self.type]
        self.bulets_dict = {'canon': 1}
        self.bulets = self.bulets_dict[self.type]
        self.delay_dict = {'canon': 0}
        self.delay = self.delay_dict[self.type]
        self.bulet_speed_dict = {'canon': 5}
        self.bulet_speed = self.bulet_speed_dict[self.type]
        self.bulet_types_dict = {'canon': 'shells'}
        self.bulets_type = self.bulet_types_dict[self.type]
    def update(self):
        # if self.angl == 0:
        #     gameDisplay.blit(self.img, (self.pos_x,self.pos_y))
        # else:
            # self.img, new_rect=rot_center(self.img, self.angl, self.pos_x, self.pos_y)
            # gameDisplay.blit(self.img, new_rect)
        blitRotateCenter(gameDisplay, self.img, (self.pos_x,self.pos_y), self.angl)
    def shoot(self):
        self.counter = self.counter + 1
        if self.counter > self.reloading_time:
            bulet_list.append(bulets(mywepon.type,mywepon.pos_x,mywepon.pos_y, \
                mywepon.bulet_speed,mywepon.angl))
            self.counter = 0
pygame.init()
pygame.font.init()
gameDisplay = pygame.display.set_mode((display_width, display_heigth))
# for i in range (4):5#     weapon_list.append(weapon)
# weapons_view = pygame.image.load('weapon_canon.jpg')
for i in range (4):
    weapon_list.append(weapon('canon',900,130 + i* 155))
    weapon_list.append(weapon('canon',335,130 + i* 155))
player1 = player()
player1_viwe = pygame.image.load('a0000723242_16.jpg')
player1_viwe = pygame.transform.scale(player1_viwe, (player1.size, player1.size))
running = True
FPS = 60
clock = pygame.time.Clock()
mywepon = 'None'
def aiming():
    mywepon = 'None'
    for i in range(len(weapon_list)):
        if abs(weapon_list[i].pos_y - player1.pos_y) <35 and abs(weapon_list[i].pos_x - player1.pos_x) < 3:
            mywepon = weapon_list[i]
            player1.pos_y = mywepon.pos_y
            player1.pos_x = mywepon.pos_x
            print(1)
            break
    print(2)
    return player1.pos_x, player1.pos_y, mywepon

for i in range (4):
    stages_library.append(pygame.image.load('stage('+str(random.randint(1,1))+').bmp'))
    stages_library_flip.append(pygame.image.load('stage_flip('+str(random.randint(1,1))+').bmp'))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if mywepon != 'None':
                    mywepon.angl -= 2
                    mywepon.update()
                else:
                    player1.walk_left()
            if event.key == pygame.K_d:
                if mywepon != 'None':
                    mywepon.angl += 2
                    mywepon.update()
                else:
                    player1.walk_right()                        
            if event.key == pygame.K_w and mywepon == 'None':
                player1.walk_up()
            if event.key == pygame.K_s and mywepon == 'None':
                print('пришёл')
                player1.walk_down()
                player1.pos_x, player1.pos_y, mywepon = aiming()
            if event.key == pygame.K_e and mywepon != 'None':
                mywepon.shoot()
            if event.key == pygame.K_q and mywepon != 'None':
                print(3)
                mywepon = 'None'
        if event.type == pygame.KEYUP:
            if mywepon != 'None':
                pass
                # mywepon.angl = 0
            else:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    player1.stop()
        # if event.type == pygame.K_s:
        #     player1.action()
        ############################
    gameDisplay.blit(background, (0,0))
    for i in range (len(stages_library)):
        gameDisplay.blit(stages_library[i], (910,520 - (160 * i)))
        gameDisplay.blit(stages_library_flip[i], (0,520 - (160 * i)))
    for bullet in bulet_list:
        bullet.update()
    for i in weapon_list:
        i.update()
    player1.update()
    pygame.display.update()
    delete_fo()
    clock.tick(FPS)