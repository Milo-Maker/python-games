#Géométrie dash en phyton
import pygame
from math import *
# from pygame.sprite import*
pygame.init()

#----------
# variable 
#----------

    #couleur
rouge=(255,0,0)
noire=(0,0,0)
bleu=(0,0,255)
blanc=(255,255,255)
lumi_ecriture=0
vert=(0,255,0)

    #Fenetre
Largeur_fenetre=1550
Hauteur_fenetre=800
fenetre=pygame.display.set_mode((Largeur_fenetre,Hauteur_fenetre))
run=True
    #jeu
yjoueur=630
vitesse_y=0
gravité=-0.02
puissance_du_saut=3.5                 
chute=0

    #autre
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

    



def jeu():
    global run,puissance_du_saut,yjoueur,chute,gravité,vitesse_y
    fenetre.fill(rouge)
    dead=False
    joueurs=personnage(200,yjoueur)
    joueurs.draw(fenetre,yjoueur)
    
    sol1.draw(fenetre)
    while not dead:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                dead=True
                run=False
            if event.type == pygame.KEYDOWN :
                pygame.key.set_repeat(10,10)
                if event.key == pygame.K_SPACE:
                    if chute==0:
                        vitesse_y+=puissance_du_saut
            
                        
        vitesse_y+=gravité
        joueurs.verification_collision_saut()
        fenetre.fill(rouge)
        joueurs.draw(fenetre,yjoueur)
        sol1.draw(fenetre)
        
                
        
       

          

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
    def verification_collision_saut(self):
        global yjoueur,gravité,vitesse_y,chute,sol1
        chute=1
        for i in range(abs(floor(vitesse_y))):
            if abs(vitesse_y)==vitesse_y:
                yjoueur-=1
            else :
                derniere_valeur=yjoueur
                yjoueur+=1
                if yjoueur>630:
                    chute=0
                    vitesse_y=0
                    yjoueur=derniere_valeur
        


            


        


class sol(pygame.sprite.Sprite):
    def __init__(self,x,y):
       self.image=pygame.Surface((1550,100))
       self.image.fill(noire)
       self.rect=self.image.get_rect(x=x,y=y)

    def draw(self,fenetre):
       fenetre.blit(self.image,self.rect)








sol1=sol(0,700)

while run:
    
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

#page 119 de mon doc
#dans mes classe je vais avoir une classe "élément de jeu", la classe "spike" en héritera tous come la classe "blocks", ma classe personnage n'en n'héritera pas