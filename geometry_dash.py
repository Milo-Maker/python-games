# Géométrie dash en phyton
import pygame
from math import *
pygame.init()

#----------
# variable 
#----------

# couleur
rouge=(255,0,0)
noire=(0,0,0)
noire_mort=(1,1,1)
bleu=(0,0,255)
blanc=(255,255,255)
lumi_ecriture=0
vert=(0,255,0)

# Fenetre
Largeur_fenetre=1550
Hauteur_fenetre=800
fenetre=pygame.display.set_mode((Largeur_fenetre,Hauteur_fenetre))
run=True
# jeu
yjoueur=630
vitesse_y=0
chute=0
deffilx=0
O=1
I=2
map=[
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,O,O,O,O,O,0,0,0,O,O,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,O,0,0,0,0,0,0,O,0,0,0,0,0,0,0,O,0,0,0,0,0,O,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,I,0,0,0,0,0,0,0,0,0,I,O,I,I,I,I,I,I,I,O,I,I,I,I,I,O,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
]
position_spike=[]
position_block=[]
for i in range(len(map)):  
    for j in range(len(map[0])):
        if map[i][j]==1:
            position_block.append([j*70,i*70])
        if map[i][j]==2:
            position_spike.append([j*70,i*70+70])

# autre
cycle_lumi=1
text_police=pygame.font.SysFont("Arial",30)      

#------------
# definition 
#------------

def affiche_text(text,police,text_col,x,y):
    img = police.render(text,True,text_col)
    fenetre.blit(img,(x,y))
logo=pygame.image.load("img/Logo_géométrie_dash.png")
block=pygame.image.load("img/Block_Géométrie_dash.png")

def menu(col_ecriture):
    global logo
    fenetre.fill(blanc)
    fenetre.blit(logo,(500,70))
    affiche_text("appuie sur espace pour continuer",text_police,col_ecriture,600,700)
    
    

def draw_spikes(fenetre): 
    """ Trace tous les triangles définis dans la variable map par le sigle I """
    global position_spike,deffilx
    for i in range (len(position_spike)):
        pygame.draw.polygon(fenetre,noire_mort,[(position_spike[i][0]-deffilx,position_spike[i][1]),(position_spike[i][0]+70-deffilx,position_spike[i][1]),(position_spike[i][0]+35-deffilx,position_spike[i][1]-70)])
        
def draw_block():
    global position_block,deffilx,block
    for i in range (len(position_block)):
        pygame.draw.rect(fenetre,noire,(position_block[i][0]-deffilx,position_block[i][1],70,70))
        pygame.draw.rect(fenetre,noire_mort,(position_block[i][0]-deffilx,position_block[i][1]+1,2,69))
        fenetre.blit(block,(position_block[i][0]-deffilx+1,position_block[i][1]+1))

def verification_collision_saut():
    global yjoueur,vitesse_y,chute,noire
    chute+=1
    for i in range(abs(floor(vitesse_y))):
        if vitesse_y >= 0:
            yjoueur-=1
        else :
            derniere_valeur=yjoueur
            yjoueur+=1
            if pygame.Surface.get_at(fenetre,(271,yjoueur+69))==(noire) or pygame.Surface.get_at(fenetre,(200,yjoueur+69))==(noire) or pygame.Surface.get_at(fenetre,(235,yjoueur+69))==(noire):
                chute=0
                vitesse_y=0
                yjoueur=derniere_valeur

def jeu():
    global run,yjoueur,chute,vitesse_y,deffilx,text_police
    yjoueur=630
    vitesse_y=0
    gravité=-0.017
    puissance_du_saut=3.3        
    chute=0
    deffilx=0
    fenetre.fill(rouge)
    dead=False
    joueurs=personnage(200,yjoueur)
    joueurs.draw(fenetre,yjoueur)
    sol1=sol(0,700)
    sol1.draw(fenetre)
    pause=0
    while not dead:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                dead=True
                run=False
            if event.type == pygame.KEYDOWN :
                pygame.key.set_repeat(10,10)
                if event.key == pygame.K_SPACE:
                    if chute==0: # Si le personnage est au sol
                        vitesse_y+=puissance_du_saut
                if event.key == pygame.K_p :
                    pause=1
                if event.key == pygame.K_r :
                    pause=0
        if pygame.Surface.get_at(fenetre,(270,yjoueur+69))==(noire_mort) or pygame.Surface.get_at(fenetre,(200,yjoueur+69))==(noire_mort):
            dead=True
        
          
            
        if pause:
            pygame.draw.rect(fenetre,rouge,(100,50,0,50))
            img_relance = text_police.render("appuie sur ' r ' pour relancer",True,noire)
            fenetre.blit(img_relance,(600,150))
            img_pause = text_police.render("Pause",True,noire)
            fenetre.blit(img_pause,(700,100))

        else:                     
            vitesse_y+=gravité
            verification_collision_saut()
            fenetre.fill(rouge)
            joueurs.draw(fenetre,yjoueur)
            sol1.draw(fenetre)
            draw_spikes(fenetre)
            draw_block()
            deffilx+=1
            img_pause2 = text_police.render("appuie sur 'p' pour faire pause",True,noire)
            fenetre.blit(img_pause2,(100,50))
        

#--------
# classe
#--------

class personnage(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image=pygame.Surface((70,70))
        self.image.fill(vert)
        self.image2=pygame.Surface((15,15))
        self.image2.fill(noire)
        self.rect=self.image.get_rect(x=x,y=y)
        self.rect2=self.image2.get_rect(x=x+45,y=y)

    def draw(self,fenetre,y):
        self.rect.y=y
        fenetre.blit(self.image,self.rect)
        self.rect2.y=y+10
        fenetre.blit(self.image2,self.rect2)

class sol(pygame.sprite.Sprite):
    def __init__(self,x,y):
       self.image=pygame.Surface((1550,100))
       self.image.fill(noire)
       self.rect=self.image.get_rect(x=x,y=y)

    def draw(self,fenetre):
       fenetre.blit(self.image,self.rect)

# class block(pygame.sprite.Sprite):
#     def __init__(self,x,y):
#         self.image=pygame.Surface((50,50))
#         self.image2=pygame.Surface((5,49))
#         self.image2.fill(noire_mort)
#         self.image.fill(noire)
#         self.rect=self.image.get_rect(x=x,y=y)
#         self.rect2=self.image2.get_rect(x=x,y=y)
#     def draw(self, fenetre):
#         fenetre.blit(self.image,self.rect)
#         fenetre.blit(self.image2,self.rect2)
        
#Boucle principal

while run:
    
    # menu avant du lancement du jeu avec la gestion du dégradé
    menu((lumi_ecriture,lumi_ecriture,lumi_ecriture))
    if cycle_lumi==1:
        lumi_ecriture+=0.5
        if lumi_ecriture==255:
            cycle_lumi=0
    else:
        lumi_ecriture-=0.5
        if lumi_ecriture==0:
            cycle_lumi=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run=False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE:
                jeu()
    pygame.display.flip()


