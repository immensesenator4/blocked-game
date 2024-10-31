from randomness import true_randomeness as random
import pygame, sys
import random as r
import pygame.locals
from pygame.locals import *

from datetime import datetime
import time
pygame.font.init()
import string

#vars 
text_keys='qwertyuiopasdfghjklzxcvbnm'
end_blocks=[[(0,0,0),(0,0,0)],[(0,0,0),(0,0,0)]]
main_blocks={}
main_points={}
reach = False
random()
keyboard = [K_q,K_w,K_e,K_r,K_t,K_y,K_u,K_i,K_o,K_p,K_a,K_s,K_d,K_f,K_g,K_h,K_j,K_k,K_l,K_z,K_x,K_c,K_v,K_b,K_n,K_m]
current_time = datetime.now()
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
    g=0
    e=0
    v=0
    for i in range(0,len(end_blocks)):
         if  ('tag' in end_blocks[i] and f.color[player] == end_blocks[i][0])and r==True:
                v+=1
    for i in range(0,len(b.list_blocks_in_main_chain)):
        sixth=False
        if i+e > len(b.list_blocks_in_main_chain):
            break
        else:
            
            qwerty=None  
            g=i+e
            
            if 'tag' in b.list_blocks_in_main_chain[g]and f.color[player] == b.list_blocks_in_main_chain[g][0]:
                v+=1
                for i in range(0,len(b.list_blocks_in_main_chain)-5):
                    if len(b.list_blocks_in_main_chain[i]) != 4:
                        z= b.list_blocks_in_main_chain[i]
                        z.append((212,175,55))
                        
                        z.append('tag')
                        
                        b.list_blocks_in_main_chain[i]=z
                
                
                
            elif f.color[player] in b.list_blocks_in_main_chain[g]:
                sixth= True
                
            if sixth == True  :
                

                if  g-5 >0:
                    if len(b.list_blocks_in_main_chain[g-5]) == 2:
                        z= b.list_blocks_in_main_chain[g-5]
                        z.append((212,175,55))
                        
                        z.append('tag')
                        
                        b.list_blocks_in_main_chain[g-5]=z
    if main_blocks[player]<v:
        main_blocks[player]= v
        
    
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
        blocke = r.randint(0,10000)
        if blocke < 1000:
            blocke = 'Green'
            return blocke
        else:
            blocke= 'Red'
            return blocke
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
                            pass #im too lazy to throw exception so n o
                        
                    
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
        
        self.player_cards_dict ={}
        self.amount= amount
        self.color = {}
        self.bot_dict={}        
        self.current_pos= { }
        self.pos= 0
        self.win_list={}
        self.color_player={}
        self.player_win=()
        for i in range(0,amount):
            l=r.randint(0,255)
            j=r.randint(0,255)
            d=r.randint(0,255)
            self.color_player[l]= i
            self.color[i]=(l,j,d)
            self.current_pos[i]=self.pos
            self.win_list[i]=0        
            if l >= 255:
                l=255
    # def hand(self):
        
    #     for i in range(self.amount):
    #         hand=[]
    #         for _ in range(6):
    #             hand.append()
    #         self.player_cards_dict[i]= hand
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
         decoder = {'Green': (0,255 , 0),
                    'Red':(255, 0 , 0)}
         if self.amount == 1:
             minus=0
         size= ((900/self.amount)-(self.amount*5))/4
         size = int(size)
         var_font = pygame.font.SysFont('Quicksand-Regular', int(size/(0.66667*(self.amount))))
         my_font = pygame.font.SysFont('Quicksand-Regular', int(size*(0.125*(self.amount))))
         font_player = pygame.font.SysFont('Quicksand-Regular', int(size*(0.5*(players))))
         mid_point= (450)/(self.amount)-(size/(self.amount-minus))*(self.amount+1)+(size/(self.amount*2.5))
         interprater={}
         
         mid_point= 450/self.amount
         for i in range(0,self.amount):
             
             if num ==1: 
                l=Block().generate_block()
                interprater[i]=decoder[l]
             else:
                 l= None
             
             d= 137.5/10
             m=700-(d*2*(i+1))
             
                            
                            
             if players - i > 0:
            
                text_surface = my_font.render('player'+' '+str(i+1), False, self.color[i])
                screen.blit(text_surface,(800,m))
            
    
             else:
                text_surface = my_font.render('bot'+' '+str(i+1-players), False, self.color[i])
                screen.blit(text_surface,(800,m))
             if l == "Green" :
                c=b.player_blockinary[i]
                c.append(l)
                
                b.player_blockinary[i]=c
             angled_draw(self.color[i],700,700-(d*2*(i+1)),self.current_pos[i],self.current_pos[i],i)
             if len(b.player_blockinary[i]) > 0:
                 
                 s= self.current_pos[i]
                 m=700-(d*2*(i+1))
                 
                 for x in range(0,len(b.player_blockinary[i])):
                     
                
                     
                     pygame.draw.rect(screen,self.color[i],(s,m,d,d))
                     s+= (d*2)
                     if s>((d*2)*24):
                        ongoing = False
                        break

             if len(b.list_blocks_in_main_chain) > 0:
                 s=0
                 
                 for x in range(0,len(b.list_blocks_in_main_chain)):
                     
                     
                     if len(b.list_blocks_in_main_chain[x])==4:
                        pygame.draw.rect(screen,b.list_blocks_in_main_chain[x][1],(s+d,700+(d/4),d,d-(d/2)))
                        pygame.draw.rect(screen,b.list_blocks_in_main_chain[x][2],(s,700,d+2,d+2))
                        pygame.draw.rect(screen,b.list_blocks_in_main_chain[x][0],(s,700,d,d))
                        
                     elif len(b.list_blocks_in_main_chain[x])==2:
                         pygame.draw.rect(screen,b.list_blocks_in_main_chain[x][1],(s+d,700+(d/4),d+2,d-(d/2)))
                         pygame.draw.rect(screen,b.list_blocks_in_main_chain[x][0],(s,700,d,d))
                     if x==len(b.list_blocks_in_main_chain)-1:
                         if reach==True:
                            self.pos=s+(137.5/10)*2
                         else:
                            self.pos=s
                     s+=d*2
                 if s>((d*2)*24):
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
    s=bot_list[::-1]
    text_surface = my_font.render('how many bots?', False, (255,255,255))
    screen.blit(text_surface,(450,450))
    integerty = 0
    if len(bot_list)>0:
        for x in range(0,len(bot_list)):
            l=10**x
            
            integerty+=(s[x])*l
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
    s=p_l[::-1]
    text_surface = my_font.render('how many players?', False, (255,255,255))
    screen.blit(text_surface,(450,450))
    integerty = 0
    if len(p_l)>0:
        for x in range(0,len(p_l)):
            l=10**x
            
            integerty+=(s[x])*l
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
                    l=0
                    g=1
                    for i in range(amnt_playing,f.amount-bots):
                        
                        if  event.key == keyboard[l]:
                            b.add_to_chain('push',i)
                        elif event.key ==keyboard[g]:
                            b.add_to_chain('catch',i)
                        g+=4
                        l+=4
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
        
    
    
   
    
    
    
    
    

            
