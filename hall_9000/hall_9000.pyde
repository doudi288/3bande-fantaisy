from math import sqrt
                                                 
   
coefficientDeRallentissement=0.9975            #Declaration des variables
GO = 0    #variable qui vérifie que le jeu a commencé depuis suffisament longtemps avant de lancer les boules
shoot = 1  #vérifie que le joueur a le droit de tirer
player = 1  #prend la valeur du joueur qui doit jouer
scoreun=0 
scoredeux=0
nomun="joueur 1"
nomdeux="joueur 2"
scoreLimite=1
f1=color(58,137,35)
f2=color(34,120,15)

rayonBalle=25                                  #Variables de la balle 1
un=color(120,10,10)   #couleur de la boule 1
x=750                 # position en x de la boule 1
y=280                 # position en y de la boule 1
speed=0               #vitesse en x de la boule 1
speedYUn=0           #vitesse en y de la boule 1
verifBoule1=0         #vérifie que la boule 1 a été touché

deux=color(10,10,120)                          #Variables de la balle 2
xDeux=750
yDeux=220
speedXDeux=0
speedYDeux=0
verifBoule2=0

trois=color(220,220,220)                       #Variables de la balle 3
xTrois=100
yTrois=250
speedXTrois=0
speedYTrois=0


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
    feu = loadImage("feu-d-artifice.bmp")
    hall = loadImage("Hall 9000.bmp")
    
    global billotron, tireur,feu,hall
    
def accueil():
    """Affichage du menu principal"""
    global etat
    background(0,128,128)
    image(tireur,0,0)                                                                      
    rectMode(CORNERS)
    fill(100)
    rect(0,60,250,120)
    rect(500,60,750,120)
    fill(0)
    textSize(30)
    text("PVP",95,100) 
    text("ORDINATEUR",520,100)   
    if (mousePressed) and mouseX<250 and mouseX>0 and mouseY<120 and mouseY>60:  #si on clique sur le rectangle jouer
        etat=1 #on passe en mode jeu
    if (mousePressed) and mouseX<750 and mouseX>500 and mouseY<120 and mouseY>60: 
        etat=2    

def draw():
    """fonction globale"""
    global player,shoot , verifBoule2,verifBoule1,scoreun,scoredeux,GO,etat,billotron,nomdeux,scoreLimite
    
    if etat==0: #mode accueil
        
        accueil()

    if etat==1: #mode jeu 
        
        GO+=1
        if scoreun==scoreLimite or scoredeux==scoreLimite:
            etat=4
        
        if player == 1: #si c'est au tour du joueur 1
                        
            fond() #affichage du fond 
            move() #déplacement des boules
            display() #affichage des boules 
            fill(233,255,0) 
            triangle(5, 476, 5, 456, 15, 466) #dessin du triangle qui indique à qui est le tour 
            
            if shoot == 1: #si le joueur a le droit de tirer
                tir() 
                if sqrt(speedXTrois**2 + speedYTrois**2) != 0: #si la boule blanche à été lancée
                    shoot = 0  #le joueur n'as plus le droit de tirer
                           
            
            if (sqrt(speed**2 + speedYUn**2) + sqrt(speedXDeux**2 + speedYDeux**2) + sqrt(speedXTrois**2 + speedYTrois**2))<=0.5 and shoot == 0: #si les boules vont assez lentement
                global x,speed,y,speedYUn,xDeux,yDeux,speedXDeux,speedYDeux,xTrois,yTrois,speedXTrois,speedYTrois,scoreun,scoredeux, verifBoule2,verifBoule1
                speed,speedYUn,speedXDeux,speedYDeux,speedXTrois,speedYTrois=0,0,0,0,0,0  # on arrête les boules 
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
                if sqrt(speedXTrois**2 + speedYTrois**2) != 0:
                    shoot = 0
                           
            
            if (sqrt(speed**2 + speedYUn**2) + sqrt(speedXDeux**2 + speedYDeux**2) + sqrt(speedXTrois**2 + speedYTrois**2))<=0.5 and shoot == 0:
                global x,speed,y,speedYUn,xDeux,yDeux,speedXDeux,speedYDeux,xTrois,yTrois,speedXTrois,speedYTrois,scoreun,scoredeux, verifBoule2,verifBoule1
                speed,speedYUn,speedXDeux,speedYDeux,speedXTrois,speedYTrois=0,0,0,0,0,0
                shoot = 1
                         
                if (verifBoule1 == 1) and (verifBoule2 == 1):
                    scoredeux += 1
                    player = 2
                else:
                    player = 1
                        
                verifBoule1,verifBoule2 = 0,0
                
                
    if etat==2: #mode joueur contre ia
        GO+=1
        nomdeux="HALL900"
        if scoreun==scoreLimite or scoredeux==scoreLimite:
            etat=4
            
        if player == 1: #si c'est au tour du joueur 1
                        
            fond() #affichage du fond 
            move() #déplacement des boules
            display() #affichage des boules 
            fill(233,255,0) 
            triangle(5, 476, 5, 456, 15, 466) #dessin du triangle qui indique à qui est le tour 
            
            if shoot == 1: #si le joueur a le droit de tirer
                tir() 
                if sqrt(speedXTrois**2 + speedYTrois**2) != 0: #si la boule blanche à été lancée
                    shoot = 0  #le joueur n'as plus le droit de tirer
                           
            
            if (sqrt(speed**2 + speedYUn**2) + sqrt(speedXDeux**2 + speedYDeux**2) + sqrt(speedXTrois**2 + speedYTrois**2))<=0.5 and shoot == 0: #si les boules vont assez lentement
                global x,speed,y,speedYUn,xDeux,yDeux,speedXDeux,speedYDeux,xTrois,yTrois,speedXTrois,speedYTrois,scoreun,scoredeux, verifBoule2,verifBoule1
                speed,speedYUn,speedXDeux,speedYDeux,speedXTrois,speedYTrois=0,0,0,0,0,0  # on arrête les boules 
                shoot = 1 #on redonne le droit de tirer 
                     
                if (verifBoule1 == 1) and (verifBoule2 == 1): #si les deux boules ont été touchées 
                    scoreun += 1 #le joueur 1 gagne 1 point
                    player = 1 # le joueur rejoue
                    
                else:
                    player = 2 # sinon c'est au joueur 2
                        
                verifBoule1,verifBoule2 = 0,0 # on réinitialise les variables 
                                   
        elif player == 2: #mêm chose pour le tour du bot
            
            fond()    
            move()
            display()
            fill(233,255,0)
            triangle(5, 527, 5, 507, 15, 517)
            
            if shoot == 1:
                if sqrt((x-xDeux)**2+(y-yDeux)**2) < 4*rayonBalle:
                    xTarget=(x+xDeux)/2
                    yTarget=(y+yDeux)/2
                    
                elif sqrt((xTrois-xDeux)**2+(yTrois-yDeux)**2)<=sqrt((x-xTrois)**2+(y-yTrois)**2):
                    xTarget=xDeux
                    yTarget=yDeux
                                    
                else:
                    xTarget=x
                    yTarget=y
                    
                xTarget+=random(-2*(rayonBalle),2*(rayonBalle))
                yTarget+=random(-2*(rayonBalle),2*(rayonBalle))
                dx=xTarget-xTrois
                dy=yTarget-yTrois
                norme=sqrt(dx**2 + dy**2)
                force=6.5+randomGaussian()
                speedXTrois=(dx/norme)*force
                speedYTrois=(dy/norme)*force
                      
                
                if sqrt(speedXTrois**2 + speedYTrois**2) != 0:
                    shoot = 0
                           
            if (sqrt(speed**2 + speedYUn**2) + sqrt(speedXDeux**2 + speedYDeux**2) + sqrt(speedXTrois**2 + speedYTrois**2))<=0.5 and shoot == 0:
                global x,speed,y,speedYUn,xDeux,yDeux,speedXDeux,speedYDeux,xTrois,yTrois,speedXTrois,speedYTrois,scoreun,scoredeux, verifBoule2,verifBoule1
                speed,speedYUn,speedXDeux,speedYDeux,speedXTrois,speedYTrois=0,0,0,0,0,0
                shoot = 1
                         
                if (verifBoule1 == 1) and (verifBoule2 == 1):
                    scoredeux += 1
                    player = 2
                else:
                    player = 1
                        
                verifBoule1,verifBoule2 = 0,0   
                
                                    
    if etat == 4:
        textSize(100)
        if scoreun>scoredeux:
            image(feu,0,0,850,600)
            fill(f1)
            text("joueur1 a gagné!!",0,500)
        elif  scoreun<scoredeux and nomdeux=="joueur 2":
            image(feu,0,0)
            fill(f1)
            text("joueur2 a gagné!!",0,500) 
        else:
            image(hall,-50,-75,1000,800)
            fill(255)
            text("vous avez échoué",0,500)                                                       
                                                
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
    
    global x,speed,y,speedYUn,xDeux,yDeux,speedXDeux,speedYDeux,xTrois,yTrois,speedXTrois,speedYTrois,scoreun,scoredeux,verifBoule2,verifBoule1,coefficientDeRallentissement
    
    x += speed               #déplacement des boules 
    y += speedYUn

    xDeux += speedXDeux
    yDeux += speedYDeux
    
    xTrois += speedXTrois
    yTrois += speedYTrois 
    
    speed=speed*coefficientDeRallentissement               #diminution de la vitesse des boules 
    speedYUn=speedYUn*coefficientDeRallentissement      
    speedXDeux=speedXDeux*coefficientDeRallentissement         
    speedYDeux=speedYDeux*coefficientDeRallentissement                  
    speedXTrois=speedXTrois*coefficientDeRallentissement                           
    speedYTrois=speedYTrois*coefficientDeRallentissement                                 
                                                    
                                                            
    distanceUNtoDEUX=sqrt((x-xDeux)**2+(y-yDeux)**2)                #calcul des distances entre les boules 
    distanceDEUXtoTROIS=sqrt((xTrois-xDeux)**2+(yTrois-yDeux)**2)
    distanceUNtoTROIS=sqrt((x-xTrois)**2+(y-yTrois)**2)
    
    if x> xrect-rayonBalle or x<rayonBalle+25:                     #calcul des rebonds contre les parois du terrain
        speed = -speed
        constrain(x,rayonBalle+25,xrect-rayonBalle)
        
    if y> yrect-rayonBalle or y<rayonBalle+25:
        speedYUn = -speedYUn
        constrain(y,rayonBalle+25,yrect-rayonBalle)
          
    if xDeux> xrect-rayonBalle or xDeux<rayonBalle+25 :
        speedXDeux = -speedXDeux
        constrain(xDeux,rayonBalle+25,xrect-rayonBalle)
        
    if yDeux> yrect-rayonBalle or yDeux<rayonBalle+25:
        speedYDeux = -speedYDeux
        constrain(yDeux,rayonBalle+25,yrect-rayonBalle)
         
    if xTrois> xrect-rayonBalle or xTrois<rayonBalle+25:
        speedXTrois = -speedXTrois 
        constrain(xTrois,rayonBalle+25,xrect-rayonBalle) 
        
    if yTrois> yrect-rayonBalle or yTrois<rayonBalle+25:
        speedYTrois = -speedYTrois
        constrain(yTrois,rayonBalle+25,yrect-rayonBalle)    
           
    if distanceUNtoDEUX<=2*rayonBalle :                        #calcul des rebonds entre les boules 
        
        dx=(x-xDeux)
        dy=(y-yDeux)
        
        sUn=speed
        sDeux=speedYUn
        sTrois=speedXDeux
        sQuatre=speedYDeux
 
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
        speedYUn= ny*vBn+gy*vAg
        speedXDeux = nx*vAn+gx*vBg
        speedYDeux = ny*vAn+gy*vBg
        
    if distanceUNtoTROIS<=2*rayonBalle :
         
        dx=(x-xTrois)
        dy=(y-yTrois)
        
        sUn=speed
        sDeux=speedYUn
        sTrois=speedXTrois
        sQuatre=speedYTrois
 
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
        speedYUn= ny*vBn+gy*vAg
        speedXTrois = nx*vAn+gx*vBg
        speedYTrois = ny*vAn+gy*vBg
        
        verifBoule1 = 1
        
    if distanceDEUXtoTROIS<=2*rayonBalle :
        
        dx=(xDeux-xTrois)
        dy=(yDeux-yTrois)
        
        sUn=speedXDeux
        sDeux=speedYDeux
        sTrois=speedXTrois
        sQuatre=speedYTrois
 
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
        
        speedXDeux= nx*vBn+gx*vAg
        speedYDeux= ny*vBn+gy*vAg
        speedXTrois = nx*vAn+gx*vBg
        speedYTrois = ny*vAn+gy*vBg 
        
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
    global xTrois,yTrois,speedXTrois,speedYTrois,GO
    norme=sqrt((mouseX-xTrois)**2+(mouseY-yTrois)**2)
    xline=xTrois+(mouseX-xTrois)*1000
    yline=yTrois+(mouseY-yTrois)*1000
    strokeWeight(2*rayonBalle)
    stroke(200+200*(norme/400), 255-200*(norme/400), 0,90)                                                                                                                           
    line(xTrois,yTrois,xline,yline)
    strokeWeight(1)
    stroke(0)
    norme=sqrt((mouseX-xTrois)**2+(mouseY-yTrois)**2)
    if mousePressed and GO>30:
        speedXTrois=((mouseX-xTrois)/norme)*6.5*(norme/400)
        speedYTrois=((mouseY-yTrois)/norme)*6.5*(norme/400)
            