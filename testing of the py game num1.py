from randomness import true_randomeness as random
import pygame, sys
import random as rand
import pygame.locals
from pygame.locals import *
pygame.font.init()


#vars 
text_keys='qwertyuiopasdfghjklzxcvbnm'
end_blocks=[[(0,0,0),(0,0,0)],[(0,0,0),(0,0,0)]]
main_blocks={}
main_points={}
reach = False
random()
keyboard = [K_q,K_w,K_e,K_r,K_t,K_y,K_u,K_i,K_o,K_p,K_a,K_s,K_d,K_f,K_g,K_h,K_j,K_k,K_l,K_z,K_x,K_c,K_v,K_b,K_n,K_m]

controler_dict={}
win_size=(900,900)
fps= pygame.time.Clock()
my_font = pygame.font.SysFont('Quicksand-Regular', 50)
pygame.init()

screen= pygame.display.set_mode(win_size,0,32)
end_game = False
text_surface = my_font.render('1 0', False, (234, 0, 0))

#class's and funcs
def input(key):
    if key == None:
        while True:
            for event in pygame.event.get():
                if event.type==  pygame.KEYDOWN:
                    ongoing ==False
                    break
        
    else:
        for i in range(0,keyboard):
            if text_keys[i] == key:
                key=keyboard[i]
        while True:
            for event in pygame.event.get():
                if event.type==  pygame.KEYDOWN:
                    if event.key == key:
                        ongoing ==False
                        break

def points(player):
    r=True
    sixth= 0

    player_points=0
    for i in range(0,len(end_blocks)):
         if  ('tag' in end_blocks[i] and f.color[player] == end_blocks[i][0])and r==True:
                player_points+=1
    for i in range(0,len(b.list_blocks_in_main_chain)):
        sixth=False
        if i > len(b.list_blocks_in_main_chain):
            break
        else:
            if 'tag' in b.list_blocks_in_main_chain[i]and f.color[player] == b.list_blocks_in_main_chain[i][0]:
                player_points+=1
                for i in range(0,len(b.list_blocks_in_main_chain)-5):
                    if len(b.list_blocks_in_main_chain[i]) != 4:
                        temp_1= b.list_blocks_in_main_chain[i]
                        temp_1.append((212,175,55))
                        
                        temp_1.append('tag')
                        
                        b.list_blocks_in_main_chain[i]=temp_1
                
                
                
            elif f.color[player] in b.list_blocks_in_main_chain[i]:
                sixth= True
                
            if sixth == True  :
                

                if  i-5 >0:
                    if len(b.list_blocks_in_main_chain[i-5]) == 2:
                        temp_1= b.list_blocks_in_main_chain[i-5]
                        temp_1.append((212,175,55))
                        
                        temp_1.append('tag')
                        
                        b.list_blocks_in_main_chain[i-5]=temp_1
    if main_blocks[player]<player_points:
        main_blocks[player]= player_points
        
    
def angled_draw(color,pos1y, pos2y,pos1x, pos2x,player):
    
    if pos1y==0 and pos2y==0:
        median_draw_y=0
    else:
        
        median_draw_y= (pos1y-pos2y)/(player+1)
    if pos1x==0 and pos2x==0:
        median_draw_x=0
    else:
        median_draw_x= (pos1x-pos2x)/(player+1)
    normal_draw=(pos2x,pos2y)
    this_font= pygame.font.SysFont('Quicksand-Regular', int((pos1y-pos2y)/(player+1)))
    text_surface = this_font.render("|", False, color)
    screen.blit(text_surface,normal_draw)
    pos1x+=player*2
    pos1y+=player*2
    x=pos2x+player*2
    y=pos2y+player*2
    for i in range(0,(player+1)):
        screen.blit(text_surface,normal_draw)
        x-=median_draw_x
        y+=median_draw_y
        normal_draw=(x,y)
        
        
        
    
class Block():
    def __init__(self=None):
        global f
        self.list_blocks_in_main_chain=[]
        self.player_blockinary = {}
        for i in range(0,f.amount):
             self.player_blockinary[i]=[]
    def generate_block(self):
        #generates block
        random()
        block = rand.randint(0,10000)
        if block < 1000:
            block = 'Green'
            return block
        else:
            block= 'Red'
            return block
    def add_to_chain(self,player_action,player):
        #player actions
        if player_action == 'push':
            
            push = 0
            if ((f.current_pos[player]  )/(13.75*2))+len(self.player_blockinary[player])> len(self.list_blocks_in_main_chain ):
                
                if    int(len(self.list_blocks_in_main_chain)-(f.current_pos[player]/(13.75*2)))>0:
                    
                    for i in range(0,len(self.list_blocks_in_main_chain)-int((f.current_pos[player]  /(13.75*2)))):
                        
                        try:    
                            del self.list_blocks_in_main_chain[-1]
                        except:
                            pass 
                for block in self.player_blockinary[player]:
                    self.list_blocks_in_main_chain.append([f.color[player],(90,90,90)])
                f.current_pos[player]=0+((len(self.list_blocks_in_main_chain))*13.75*2)
                for i in range(0,int(len(self.player_blockinary[player])/6)):
                    main_blocks[player]+=1
                self.player_blockinary[player]=[]
            else:
                return None
        elif player_action == 'catch':
            f.current_pos[player]=f.pos+(137.5/10)*2     
            self.player_blockinary[player]=[]       
class Player():
    def __init__(self,amount):
        self.amount= amount
        self.color = {}
        self.bot_dict={}        
        self.current_pos= {}
        self.pos= 0
        self.color_player={}
        for i in range(0,amount):
            r=rand.randint(0,255)
            b=rand.randint(0,255)
            g=rand.randint(0,255)
            self.color_player[l]= i
            self.color[i]=(r,b,g)
            self.current_pos[i]=self.pos
            if r >= 255:
                r=255
    def reset(self):
        if reach==True:
            self.pos=(137.5/10)*2
        else:
            self.pos=0
        for i in range(0,self.amount):
            self.current_pos[i]=self.pos
    def show(self,num):
         global ongoing
         minus=1
         decoder = {
        'Green': (0,255 , 0),
        'Red':(255, 0 , 0)}
         if self.amount == 1:
             minus=0
         size= ((900/self.amount)-(self.amount*5))/4
         size = int(size)
         my_font = pygame.font.SysFont('Quicksand-Regular', int(size*(0.125*(self.amount))))
         mid_point= (450)/(self.amount)-(size/(self.amount-minus))*(self.amount+1)+(size/(self.amount*2.5))
         interprater={}
         mid_point= 450/self.amount
         for i in range(0,self.amount):
             if num ==1: 
                block=Block().generate_block()
                interprater[i]=decoder[block]
             else:
                 block= None
             constant = 137.5/10
             mid=700-(constant*2*(i+1))
             if players - i > 0:
                text_surface = my_font.render('player'+' '+str(i+1), False, self.color[i])
                screen.blit(text_surface,(800,mid))
             else:
                text_surface = my_font.render('bot'+' '+str(i+1-players), False, self.color[i])
                screen.blit(text_surface,(800,mid))
             if block == "Green" :
                passenger=b.player_blockinary[i]
                passenger.append(block)
                b.player_blockinary[i]=passenger
             angled_draw(self.color[i],700,700-(constant*2*(i+1)),self.current_pos[i],self.current_pos[i],i)
             if len(b.player_blockinary[i]) > 0:
                 possition= self.current_pos[i]
                 mid=700-(constant*2*(i+1))
                 for x in range(0,len(b.player_blockinary[i])):
                     pygame.draw.rect(screen,self.color[i],(possition,mid,constant,constant))
                     possition+= (constant*2)
                     if possition>((constant*2)*24):
                        ongoing = False
                        break
             if len(b.list_blocks_in_main_chain) > 0:
                 possition=0
                 for x in range(0,len(b.list_blocks_in_main_chain)):
                     
                     if len(b.list_blocks_in_main_chain[x])==4:
                        pygame.draw.rect(screen,b.list_blocks_in_main_chain[x][1],(possition+constant,700+(constant/4),constant,constant-(constant/2)))
                        pygame.draw.rect(screen,b.list_blocks_in_main_chain[x][2],(possition,700,constant+2,constant+2))
                        pygame.draw.rect(screen,b.list_blocks_in_main_chain[x][0],(possition,700,constant,constant))
                        
                     elif len(b.list_blocks_in_main_chain[x])==2:
                         pygame.draw.rect(screen,b.list_blocks_in_main_chain[x][1],(possition+constant,700+(constant/4),constant+2,constant-(constant/2)))
                         pygame.draw.rect(screen,b.list_blocks_in_main_chain[x][0],(possition,700,constant,constant))
                     if x==len(b.list_blocks_in_main_chain)-1:
                         if reach==True:
                            self.pos=possition+(137.5/10)*2
                         else:
                            self.pos=possition
                     possition+=constant*2
                 if possition>((constant*2)*24):
                     ongoing = False
                     
                     break
             if players - i > 0:
                text_surface = my_font.render('player'+' '+str(i+1), False, self.color[i])
                screen.blit(text_surface,(mid_point,100))
                text_surface = my_font.render('points:'+str(main_blocks[i]), False, self.color[i])
                screen.blit(text_surface,(mid_point,150))
                
             else:
                 text_surface = my_font.render('bot'+' '+str(i+1-players), False, self.color[i])
                 screen.blit(text_surface,(mid_point,100))
                 text_surface = my_font.render('points :'+str(main_blocks[i]), False, self.color[i])
                 screen.blit(text_surface,(mid_point,150))
             mid_point += 450/(self.amount/2)-size
    def bot(self,player):
        if ((self.current_pos[player]  )/(13.75*2))+len(b.player_blockinary[player])> len(b.list_blocks_in_main_chain ):
            b.add_to_chain('push',player)
            
        elif ((self.current_pos[player]  )/(13.75*2))+len(b.player_blockinary[player])< len(b.list_blocks_in_main_chain )-4:
            b.add_to_chain('catch',player)
nums=[K_0,K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8,K_9]
rounds=0
num_list=[]
text_surface = my_font.render('1 0', False, (234, 0, 0))
bot = None
while bot==None:
    text_surface = my_font.render('want bots Y or N', False, (255,255,255))
    screen.blit(text_surface,(450,450))
    for event in pygame.event.get():
        if event.type==  pygame.KEYDOWN:
            
            if event.key == K_y:
                bot = True  
                bots = 0
                
                
            if event.key == K_n:
                bot = False  
                bots = 0
    fps.tick(3)
    pygame.display.update()         
    screen.fill((0,0,0))
bot_list=[]
while bot==True and bots==0:
    n_b=bot_list[::-1]
    text_surface = my_font.render('how many bots?', False, (255,255,255))
    screen.blit(text_surface,(450,450))
    integerty = 0
    if len(bot_list)>0:
        for x in range(0,len(bot_list)):
            l=10**x
            integerty+=(n_b[x])*l
    for event in pygame.event.get():
        if event.type==  pygame.KEYDOWN:
            if event.key == K_EQUALS:
                bots=integerty   
            elif event.key == K_BACKSPACE:
                if len(bot_list) > 0:
                    del bot_list[-1]
            else:
                for i in range(0,9):
                    if event.key == nums[i]:
                        bot_list.append(i)
    text_surface = my_font.render(str(integerty), False, (255,255,255))
    screen.blit(text_surface,(450,600))
    fps.tick(3)
    pygame.display.update()         
    screen.fill((0,0,0))
p_l=[]
players = -1
while players ==-1: 
    n_p=p_l[::-1]
    text_surface = my_font.render('how many players?', False, (255,255,255))
    screen.blit(text_surface,(450,450))
    integerty = 0
    if len(p_l)>0:
        for x in range(0,len(p_l)):
            l=10**x
            integerty+=(n_p[x])*l
    for event in pygame.event.get():
        if event.type==  pygame.KEYDOWN:
            if event.key == K_EQUALS:
                players=integerty   
            elif event.key == K_BACKSPACE:
                if len(p_l) > 0:

                    del p_l[-1]
            else:
                for i in range(0,9):
                    
                    if event.key == nums[i]:
                        p_l.append(i)
                
    text_surface = my_font.render(str(integerty), False, (255,255,255))
    screen.blit(text_surface,(450,600))
    fps.tick(3)
    pygame.display.update()         
    screen.fill((0,0,0))
for i in range(0,players+bots):
    main_blocks[i]=0
    main_points[i]=0
counter =0
while players> len(controler_dict) and players>counter:
    
    for i in range(0,pygame.joystick.get_count()):
        controler_dict[i]=pygame.joystick.Joystick(i)
        controler_dict[i].init() 
    counter+=1
f=Player(players+bots)
b=Block()
while end_game==False:
    ongoing = True
    while ongoing == True:
        amnt_playing = len(controler_dict)
        for i in range(0,bots):
            f.bot(i+players)
        for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:        
                    for i in range(0,amnt_playing):
                        if controler_dict[i].get_button(0):
                            b.add_to_chain("push",i)
                        if controler_dict[i].get_button(1):
                            b.add_to_chain('catch',i)
                if event.type == pygame.QUIT: 
                    end_game=True
                    ongoing=False
                    break
                if event.type == pygame.KEYDOWN:
                    push_key=0
                    pull_key=1
                    for i in range(amnt_playing,f.amount-bots):
                        if  event.key == keyboard[push_key]:
                            b.add_to_chain('push',i)
                        elif event.key ==keyboard[pull_key]:
                            b.add_to_chain('catch',i)
                        pull_key+=4
                        push_key+=4
        for i in range(0,f.amount):
            points(i)    
        fps.tick(90)
        f.show(1)
        pygame.display.update() 
        screen.fill((0,0,0))
    f.show(0)
    pygame.display.update() 
    screen.fill((0,0,0))
    for i in range(0, players+bots):
        main_points[i]=main_blocks[i]
        f.current_pos[i]-=(137.5/10)*2
    f.pos-=(137.5/10)*2
    try:
        end_blocks.append(b.list_blocks_in_main_chain[0])
        del b.list_blocks_in_main_chain[0]
    except:
        pass