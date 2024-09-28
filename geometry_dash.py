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
gravité=-0.02
puissance_du_saut=3             
chute=0
deffilx=0
position_spike=[
[1000,700],
[1050,700],
[1100,700]
]
position_block=[
[1600,630],
[1600,560],
[1600,320],
[1700,630]  
]

# autre
cycle_lumi=1
text_police=pygame.font.SysFont("Arial",30)      

#------------
# definition 
#------------

def affiche_text(text,police,text_col,x,y):
    img = police.render(text,True,text_col)
    fenetre.blit(img,(x,y))

def menu(col_ecriture):
    fenetre.fill(blanc)
    affiche_text("appuie sur espace pour continuer",text_police,col_ecriture,600,700)

def draw_spikes(fenetre):
    global position_spike,deffilx
    for i in range (len(position_spike)):
        pygame.draw.polygon(fenetre,noire_mort,[(position_spike[i][0]-deffilx,position_spike[i][1]),(position_spike[i][0]+50-deffilx,position_spike[i][1]),(position_spike[i][0]+25-deffilx,position_spike[i][1]-50)])
        
def draw_block(fenetre):
    global position_block,deffilx
    for i in range (len(position_block)):
        pygame.draw.rect(fenetre,noire,(position_block[i][0]-deffilx,position_block[i][1],70,70))
        pygame.draw.rect(fenetre,noire_mort,(position_block[i][0]-deffilx,position_block[i][1]+1,2,69))
#        pygame.draw.polygon(fenetre,noire_mort,[(position_block[i][0]-deffilx,position_block[i][1]),(position_block[i][0]+50-deffilx,position_spike[i][1]),(position_spike[i][0]+25-deffilx,position_spike[i][1]-50)])


def verification_collision_saut():
    global yjoueur,gravité,vitesse_y,chute,noire
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
    global run,puissance_du_saut,yjoueur,chute,gravité,vitesse_y,deffilx,text_police
    yjoueur=630
    vitesse_y=0
    gravité=-0.02
    puissance_du_saut=3.1             
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
            print(yjoueur)

        else:                     
            vitesse_y+=gravité
            verification_collision_saut()
            fenetre.fill(rouge)
            joueurs.draw(fenetre,yjoueur)
            sol1.draw(fenetre)
            draw_spikes(fenetre)
            draw_block(fenetre)
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

class block(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image=pygame.Surface((70,70))
        self.image2=pygame.Surface((5,69))
        self.image2.fill(noire_mort)
        self.image.fill(noire)
        self.rect=self.image.get_rect(x=x,y=y)
        self.rect2=self.image2.get_rect(x=x,y=y)
    def draw(self, fenetre):
        fenetre.blit(self.image,self.rect)
        fenetre.blit(self.image2,self.rect2)
        
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
    

    #pygame.Surface.get_at(10,10)
    pygame.display.flip()

#page 119 de mon doc

pygame.Surface.get_at(fenetre,(10,10))
#get_at()
#get the color value at a single pixel
#get_at((x, y)) -> Color
#Return a copy of the RGBA Color value at the given pixel. If the Surface has no per pixel alpha, then the alpha value will always be 255 (opaque). If the pixel position is outside the area of the Surface an IndexError exception will be raised.
#Getting and setting pixels one at a time is generally too slow to be used in a game or realtime situation. It is better to use methods which operate on many pixels at a time like with the blit, fill and draw methods - or by using pygame.surfarraypygame module for accessing surface pixel data using array interfaces/pygame.PixelArraypygame object for direct pixel access of surfaces.
#This function will temporarily lock and unlock the Surface as needed.
#New in pygame 1.9: Returning a Color instead of tuple. Use tuple(surf.get_at((x,y))) if you want a tuple, and not a Color. This should only matter if you want to use the color as a key in a dict.


#set_at()
#set the color value for a single pixel
#set_at((x, y), Color) -> None
#Set the RGBA or mapped integer color value for a single pixel. If the Surface does not have per pixel alphas, the alpha value is ignored. Setting pixels outside the Surface area or outside the Surface clipping will have no effect.
#Getting and setting pixels one at a time is generally too slow to be used in a game or realtime situation.
#This function will temporarily lock and unlock the Surface as needed.
#Note If the surface is palettized, the pixel color will be set to the most similar color in the palette.
