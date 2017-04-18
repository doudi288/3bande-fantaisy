from math import sqrt

scoreun=0
scoredeux=0
nomun="joueur 1"
nomdeux="joueur 2"
rayonBalle=25
un=color(120,0,0)
x=750
y=280
speed=0
speedDeux=0

deux=color(0,0,120)
xDeux=750
yDeux=220
speedTrois=0
speedQuatre=0

trois=color(240,240.240)
xTrois=100
yTrois=250
speedCinq=0
speedSix=0


xrect=825
yrect=425
xsize=850
ysize=600

def setup():
    size(xsize,ysize)
    background(255)
    frameRate(100)
    
def draw():
    fond()    
    move()
    display()
    if (sqrt(speed**2 + speedDeux**2) + sqrt(speedTrois**2 + speedQuatre**2) + sqrt(speedCinq**2 + speedSix**2))<=0.1:
        global x,speed,y,speedDeux,xDeux,yDeux,speedTrois,speedQuatre,xTrois,yTrois,speedCinq,speedSix,scoreun,scoredeux
        speedCinq,speedSix=0,0
        tir()
        
def fond():
    background(255)
    rectMode(CORNERS)
    fill(31,160,38)
    rect(25,25,825,425)
    fill(0)
    textSize(25)
    a=nomun+":"+str(scoreun)+"point(s)"
    text(a,25,475)
    b=nomdeux+":"+str(scoredeux)+"point(s)"
    text(b,25,525)    
    
def move():
    global x,speed,y,speedDeux,xDeux,yDeux,speedTrois,speedQuatre,xTrois,yTrois,speedCinq,speedSix,scoreun,scoredeux
    
    x += speed
    y += speedDeux

    xDeux += speedTrois
    yDeux += speedQuatre
    
    xTrois += speedCinq
    yTrois += speedSix 
    
    speed=speed*0.997
    speedDeux=speedDeux*0.997      
    speedTrois=speedTrois*0.997         
    speedQuatre=speedQuatre*0.997                  
    speedCinq=speedCinq*0.997                           
    speedSix=speedSix*0.997                                 
                                                    
                                                            
    distanceUNtoDEUX=sqrt((x-xDeux)**2+(y-yDeux)**2)
    distanceDEUXtoTROIS=sqrt((xTrois-xDeux)**2+(yTrois-yDeux)**2)
    distanceUNtoTROIS=sqrt((x-xTrois)**2+(y-yTrois)**2)
    
    if x> xrect-rayonBalle or x<rayonBalle+25:
        speed = -speed
    
    if y> yrect-rayonBalle or y<rayonBalle+25:
        speedDeux = -speedDeux
    
    if xDeux> xrect-rayonBalle or xDeux<rayonBalle+25 :
        speedTrois = -speedTrois
    
    if yDeux> yrect-rayonBalle or yDeux<rayonBalle+25:
        speedQuatre = -speedQuatre
        
    if xTrois> xrect-rayonBalle or xTrois<rayonBalle+25:
        speedCinq = -speedCinq   
        
    if yTrois> yrect-rayonBalle or yTrois<rayonBalle+25:
        speedSix = -speedSix    
           
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
                
def display():
    fill(un)
    ellipse(x,y,2*rayonBalle,2*rayonBalle)
    
    fill(deux)
    ellipse(xDeux,yDeux,2*rayonBalle,2*rayonBalle) 
    
    fill(trois)
    ellipse(xTrois,yTrois,2*rayonBalle,2*rayonBalle)
def tir():
        global xTrois,yTrois,speedCinq,speedSix
        line(xTrois,yTrois,mouseX,mouseY)
        norme=sqrt((mouseX-xTrois)**2+(mouseY-yTrois)**2)
        if mousePressed:
            speedCinq=((mouseX-xTrois)/norme)*5
            speedSix=((mouseY-yTrois)/norme)*5