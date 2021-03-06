from math import sqrt

coefficientDeRallentissement=0.9975
GO = 0
shoot = 1
player = 1
scoreun=0
scoredeux=0
nomun="joueur 1"
nomdeux="joueur 2"
f1=color(58,137,35)
f2=color(34,120,15)

rayonBalle=25
un=color(120,10,10)
x=750
y=280
speed=0
speedDeux=0
verifBoule1=0

deux=color(10,10,120)
xDeux=750
yDeux=220
speedTrois=0
speedQuatre=0
verifBoule2=0

trois=color(220,220,220)
xTrois=100
yTrois=250
speedCinq=0
speedSix=0


xrect=825
yrect=425
xsize=850
ysize=600

etat=0   
 
def setup():
    size(xsize,ysize,)
    background(255)
    frameRate(100)
    billotron = loadImage("billotron.png")
    tireur = loadImage("hqdefault2.jpg")
    global billotron, tireur
    
def accueil():
    global etat
    background(0,128,128)
    image(tireur,0,0)                                                                     
    rectMode(CORNERS)
 
    
    if (mousePressed) and mouseX<250 and mouseX>0 and mouseY<120 and mouseY>60:
        etat=1
            

def draw():
    
    global player,shoot , verifBoule2,verifBoule1,scoreun,scoredeux,GO,etat,billotron
    
    if etat==0:
        
        accueil()

    if etat==1:
        
        GO+=1
        
        if player == 1:
                        
            fond()    
            move()
            display()
            fill(233,255,0)
            triangle(5, 476, 5, 456, 15, 466)
            
            if shoot == 1:
                tir()
                if sqrt(speedCinq**2 + speedSix**2) != 0:
                    shoot = 0
                           
            
            if (sqrt(speed**2 + speedDeux**2) + sqrt(speedTrois**2 + speedQuatre**2) + sqrt(speedCinq**2 + speedSix**2))<=0.5 and shoot == 0:
                global x,speed,y,speedDeux,xDeux,yDeux,speedTrois,speedQuatre,xTrois,yTrois,speedCinq,speedSix,scoreun,scoredeux, verifBoule2,verifBoule1
                speed,speedDeux,speedTrois,speedQuatre,speedCinq,speedSix=0,0,0,0,0,0
                shoot = 1
                     
                if (verifBoule1 == 1) and (verifBoule2 == 1):
                    scoreun += 1
                    player = 1
                    
                else:
                    player = 2
                        
                verifBoule1,verifBoule2 = 0,0
                                   
        elif player == 2:               
            
                        
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
    global scoreun,scoredeux,nomun,nomdeux,billotron,f1,f2
    background(255)
    rectMode(CORNERS)
    fill(25,100,25)
    rect(0,0,850,450)
    fill(f1)
    rect(25,25,825,425)
    fill(0)
    textSize(25)
    a=nomun+":"+str(scoreun)+"point(s)"
    text(a,25,475)
    b=nomdeux+":"+str(scoredeux)+"point(s)"
    text(b,25,525)
    image(billotron,390,451)  
    
def move():
    global x,speed,y,speedDeux,xDeux,yDeux,speedTrois,speedQuatre,xTrois,yTrois,speedCinq,speedSix,scoreun,scoredeux,verifBoule2,verifBoule1,coefficientDeRallentissement
    
    x += speed
    y += speedDeux

    xDeux += speedTrois
    yDeux += speedQuatre
    
    xTrois += speedCinq
    yTrois += speedSix 
    
    speed=speed*coefficientDeRallentissement
    speedDeux=speedDeux*coefficientDeRallentissement      
    speedTrois=speedTrois*coefficientDeRallentissement         
    speedQuatre=speedQuatre*coefficientDeRallentissement                  
    speedCinq=speedCinq*coefficientDeRallentissement                           
    speedSix=speedSix*coefficientDeRallentissement                                 
                                                    
                                                            
    distanceUNtoDEUX=sqrt((x-xDeux)**2+(y-yDeux)**2)
    distanceDEUXtoTROIS=sqrt((xTrois-xDeux)**2+(yTrois-yDeux)**2)
    distanceUNtoTROIS=sqrt((x-xTrois)**2+(y-yTrois)**2)
    
    if x> xrect-rayonBalle or x<rayonBalle+25:
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
           
    if distanceUNtoDEUX<=2*rayonBalle :
        
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
    fill(un)
    ellipse(x,y,2*rayonBalle,2*rayonBalle)
    
    fill(deux)
    ellipse(xDeux,yDeux,2*rayonBalle,2*rayonBalle) 
    
    fill(trois)
    ellipse(xTrois,yTrois,2*rayonBalle,2*rayonBalle)
    
def tir():
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
            