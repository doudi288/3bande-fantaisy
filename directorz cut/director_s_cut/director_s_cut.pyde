from math import sqrt
                                                 
   
coefficientDeRallentissement=0.9975            #Declaration des variables
GO = 0    #variable qui vérifie que le jeu a commencé depuis suffisament longtemps avant de lancer les boules
shoot = 1  #vérifie que le joueur a le droit de tirer
player = 1  #prend la valeur du joueur qui doit jouer
scoreun=0 
scoredeux=0
nomun="joueur 1"
nomdeux="joueur 2"
f1=color(58,137,35)
f2=color(34,120,15)

rayonBalle=25                                  #Variables de la balle 1
un=color(120,10,10)   #couleur de la boule 1
x=750                 # position en x de la boule 1
y=280                 # position en y de la boule 1
speed=0               #vitesse en x de la boule 1
speedDeux=0           #vitesse en y de la boule 1
verifBoule1=0         #vérifie que la boule 1 a été touché

deux=color(10,10,120)                          #Variables de la balle 2
xDeux=750
yDeux=220
speedTrois=0
speedQuatre=0
verifBoule2=0

trois=color(220,220,220)                       #Variables de la balle 3
xTrois=100
yTrois=250
speedCinq=0
speedSix=0


xrect=825                                      #Variables du billard
yrect=425 

xsize=850                                      #Variablse de la fenêtre de jeu
ysize=600

etat=0   
 
def setup():
    """Initialisation"""
    size(xsize,ysize,)
    background(255)
    frameRate(100)
    billotron = loadImage("billotron.png")     #Importation des images 
    tireur = loadImage("hqdefault2.jpg")
    global billotron, tireur
    
def accueil():
    """Affichage du menu principal"""
    global etat
    background(0,128,128)
    image(tireur,0,0)                                                                      
    rectMode(CORNERS)
 
    
    if (mousePressed) and mouseX<250 and mouseX>0 and mouseY<120 and mouseY>60:  #si on clique sur le rectangle jouer
        etat=1 #on passe en mode jeu
            

def draw():
    """fonction globale"""
    global player,shoot , verifBoule2,verifBoule1,scoreun,scoredeux,GO,etat,billotron
    
    if etat==0: #mode accueil
        
        accueil()

    if etat==1: #mode jeu 
        
        GO+=1
        
        if player == 1: #si c'est au tour du joueur 1
                        
            fond() #affichage du fond 
            move() #déplacement des boules
            display() #affichage des boules 
            fill(233,255,0) 
            triangle(5, 476, 5, 456, 15, 466) #dessin du triangle qui indique à qui est le tour 
            
            if shoot == 1: #si le joueur a le droit de tirer
                tir() 
                if sqrt(speedCinq**2 + speedSix**2) != 0: #si la boule blanche à été lancée
                    shoot = 0  #le joueur n'as plus le droit de tirer
                           
            
            if (sqrt(speed**2 + speedDeux**2) + sqrt(speedTrois**2 + speedQuatre**2) + sqrt(speedCinq**2 + speedSix**2))<=0.5 and shoot == 0: #si les boules vont assez lentement
                global x,speed,y,speedDeux,xDeux,yDeux,speedTrois,speedQuatre,xTrois,yTrois,speedCinq,speedSix,scoreun,scoredeux, verifBoule2,verifBoule1
                speed,speedDeux,speedTrois,speedQuatre,speedCinq,speedSix=0,0,0,0,0,0  # on arrête les boules 
                shoot = 1 #on redonne le droit de tirer 
                     
                if (verifBoule1 == 1) and (verifBoule2 == 1): #si les deux boules ont été touchées 
                    scoreun += 1 #le joueur 1 gagne 1 point
                    player = 1 # le joueur rejoue
                    
                else:
                    player = 2 # sinon c'est au joueur 2
                        
                verifBoule1,verifBoule2 = 0,0 # on réinitialise les variables 
                                   
        elif player == 2: #mêm chose pour le tour du joueur 2               
            
                        
            fond()    
            move()
            display()
            fill(233,255,0)
            triangle(5, 527, 5, 507, 15, 517)
            
            if shoot == 1:
                tir()
                if sqrt(speedCinq**2 + speedSix**2) != 0:
                    shoot = 0
                           
            
            if (sqrt(speed**2 + speedDeux**2) + sqrt(speedTrois**2 + speedQuatre**2) + sqrt(speedCinq**2 + speedSix**2))<=0.5 and shoot == 0:
                global x,speed,y,speedDeux,xDeux,yDeux,speedTrois,speedQuatre,xTrois,yTrois,speedCinq,speedSix,scoreun,scoredeux, verifBoule2,verifBoule1
                speed,speedDeux,speedTrois,speedQuatre,speedCinq,speedSix=0,0,0,0,0,0
                shoot = 1
                         
                if (verifBoule1 == 1) and (verifBoule2 == 1):
                    scoredeux += 1
                    player = 2
                else:
                    player = 1
                        
                verifBoule1,verifBoule2 = 0,0
                        
                                
                                                
def fond():
    """dessin du fond"""
    global scoreun,scoredeux,nomun,nomdeux,billotron,f1,f2
    background(255)
    rectMode(CORNERS)
    fill(25,100,25)
    rect(0,0,850,450) # grand rectangle 
    fill(f1)
    rect(25,25,825,425) # terrain de jeu 
    fill(0)
    textSize(25)
    a=nomun+":"+str(scoreun)+"point(s)"
    text(a,25,475)
    b=nomdeux+":"+str(scoredeux)+"point(s)"
    text(b,25,525)
    image(billotron,390,451)  
    
def move(): 
    """fonction de déplacement des boules"""
    
    global x,speed,y,speedDeux,xDeux,yDeux,speedTrois,speedQuatre,xTrois,yTrois,speedCinq,speedSix,scoreun,scoredeux,verifBoule2,verifBoule1,coefficientDeRallentissement
    
    x += speed               #déplacement des boules 
    y += speedDeux

    xDeux += speedTrois
    yDeux += speedQuatre
    
    xTrois += speedCinq
    yTrois += speedSix 
    
    speed=speed*coefficientDeRallentissement               #diminution de la vitesse des boules 
    speedDeux=speedDeux*coefficientDeRallentissement      
    speedTrois=speedTrois*coefficientDeRallentissement         
    speedQuatre=speedQuatre*coefficientDeRallentissement                  
    speedCinq=speedCinq*coefficientDeRallentissement                           
    speedSix=speedSix*coefficientDeRallentissement                                 
                                                    
                                                            
    distanceUNtoDEUX=sqrt((x-xDeux)**2+(y-yDeux)**2)                #calcul des distances entre les boules 
    distanceDEUXtoTROIS=sqrt((xTrois-xDeux)**2+(yTrois-yDeux)**2)
    distanceUNtoTROIS=sqrt((x-xTrois)**2+(y-yTrois)**2)
    
    if x> xrect-rayonBalle or x<rayonBalle+25:                     #calcul des rebonds contre les parois du terrain
        speed = -speed
        constrain(x,xrect-rayonBalle,rayonBalle+25)
        
    if y> yrect-rayonBalle or y<rayonBalle+25:
        speedDeux = -speedDeux
        constrain(y,yrect-rayonBalle,rayonBalle+25)
          
    if xDeux> xrect-rayonBalle or xDeux<rayonBalle+25 :
        speedTrois = -speedTrois
        constrain(xDeux,xrect-rayonBalle,rayonBalle+25)
        
    if yDeux> yrect-rayonBalle or yDeux<rayonBalle+25:
        speedQuatre = -speedQuatre
        constrain(yDeux,yrect-rayonBalle,rayonBalle+25)
         
    if xTrois> xrect-rayonBalle or xTrois<rayonBalle+25:
        speedCinq = -speedCinq 
        constrain(xTrois,xrect-rayonBalle,rayonBalle+25) 
        
    if yTrois> yrect-rayonBalle or yTrois<rayonBalle+25:
        speedSix = -speedSix
        constrain(yTrois,yrect-rayonBalle,rayonBalle+25)    
           
    if distanceUNtoDEUX<=2*rayonBalle :                        #calcul des rebonds entre les boules 
        
        dx=(x-xDeux)
        dy=(y-yDeux)
        
        sUn=speed
        sDeux=speedDeux
        sTrois=speedTrois
        sQuatre=speedQuatre
 
        correction = (2*rayonBalle - distanceUNtoDEUX)*0.5
        
        x=x+(dx/distanceUNtoDEUX)*correction                
        y=y+(dy/distanceUNtoDEUX)*correction
        xDeux=xDeux-(dx/distanceUNtoDEUX)*correction
        yDeux=yDeux-(dy/distanceUNtoDEUX)*correction
        
        dx=(x-xDeux)
        dy=(y-yDeux)
        
        nx=(dx)/(2*rayonBalle)
        ny=(dy)/(2*rayonBalle)
        gx=-ny
        gy=nx
        
        vAn=nx*sUn+ny*sDeux 
        vAg=gx*sUn+gy*sDeux
        vBn=nx*sTrois+ny*sQuatre
        vBg=gx*sTrois+gy*sQuatre
        
        speed= nx*vBn+gx*vAg
        speedDeux= ny*vBn+gy*vAg
        speedTrois = nx*vAn+gx*vBg
        speedQuatre = ny*vAn+gy*vBg
        
    if distanceUNtoTROIS<=2*rayonBalle :
        
        dx=(x-xTrois)
        dy=(y-yTrois)
        
        sUn=speed
        sDeux=speedDeux
        sTrois=speedCinq
        sQuatre=speedSix
 
        correction = (2*rayonBalle - distanceUNtoTROIS)*0.5
        
        x=x+(dx/distanceUNtoTROIS)*correction                
        y=y+(dy/distanceUNtoTROIS)*correction
        xTrois=xTrois-(dx/distanceUNtoTROIS)*correction
        yTrois=yTrois-(dy/distanceUNtoTROIS)*correction
        
        dx=(x-xTrois)
        dy=(y-yTrois)
        
        nx=(dx)/(2*rayonBalle)
        ny=(dy)/(2*rayonBalle)
        gx=-ny
        gy=nx
        
        vAn=nx*sUn+ny*sDeux
        vAg=gx*sUn+gy*sDeux
        vBn=nx*sTrois+ny*sQuatre
        vBg=gx*sTrois+gy*sQuatre
        
        speed= nx*vBn+gx*vAg
        speedDeux= ny*vBn+gy*vAg
        speedCinq = nx*vAn+gx*vBg
        speedSix = ny*vAn+gy*vBg
        
        verifBoule1 = 1
        
    if distanceDEUXtoTROIS<=2*rayonBalle :
        
        dx=(xDeux-xTrois)
        dy=(yDeux-yTrois)
        
        sUn=speedTrois
        sDeux=speedQuatre
        sTrois=speedCinq
        sQuatre=speedSix
 
        correction = (2*rayonBalle - distanceDEUXtoTROIS)*0.5
        
        xDeux=xDeux+(dx/distanceUNtoTROIS)*correction                
        yDeux=yDeux+(dy/distanceUNtoTROIS)*correction
        xTrois=xTrois-(dx/distanceUNtoTROIS)*correction
        yTrois=yTrois-(dy/distanceUNtoTROIS)*correction
        
        dx=(xDeux-xTrois)
        dy=(yDeux-yTrois)
        
        nx=(dx)/(2*rayonBalle)
        ny=(dy)/(2*rayonBalle)
        gx=-ny
        gy=nx
        
        vAn=nx*sUn+ny*sDeux
        vAg=gx*sUn+gy*sDeux
        vBn=nx*sTrois+ny*sQuatre
        vBg=gx*sTrois+gy*sQuatre
        
        speedTrois= nx*vBn+gx*vAg
        speedQuatre= ny*vBn+gy*vAg
        speedCinq = nx*vAn+gx*vBg
        speedSix = ny*vAn+gy*vBg 
        
        verifBoule2 = 1                             
                
def display():
    """fonction de dessin des boules"""
    fill(un)
    ellipse(x,y,2*rayonBalle,2*rayonBalle)
    
    fill(deux)
    ellipse(xDeux,yDeux,2*rayonBalle,2*rayonBalle) 
    
    fill(trois)
    ellipse(xTrois,yTrois,2*rayonBalle,2*rayonBalle)
    
def tir():
    """fonction de lancement des boules"""
    global xTrois,yTrois,speedCinq,speedSix,GO
    norme=sqrt((mouseX-xTrois)**2+(mouseY-yTrois)**2)
    xline=xTrois+(mouseX-xTrois)*1000
    yline=yTrois+(mouseY-yTrois)*1000
    strokeWeight(50)
    stroke(200+200*(norme/400), 255-200*(norme/400), 0,90)                                                                                                                           
    line(xTrois,yTrois,xline,yline)
    strokeWeight(1)
    stroke(0)
    norme=sqrt((mouseX-xTrois)**2+(mouseY-yTrois)**2)
    if mousePressed and GO>30:
        speedCinq=((mouseX-xTrois)/norme)*6.5*(norme/400)
        speedSix=((mouseY-yTrois)/norme)*6.5*(norme/400)
            