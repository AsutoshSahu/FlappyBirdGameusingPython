
import random
import pygame

#initializing pygame(compulsary line whenever pygame module is imported)
pygame.init()

##b = bird/boolean
##sr = star
##h = heart
##hc = heart collision
##sc = star collision
##p = pillar
##sp = special pillar

dispw = 1000
disph = 700
#creates a pygame window of size 1000x700 pixels
gameDisplay = pygame.display.set_mode((dispw, disph))


#loading sound effects, background music and setting their volumes
hsound = pygame.mixer.Sound("1upn.wav")
hsound.set_volume(0.5)
bulexps = pygame.mixer.Sound("bulexpl.wav")
bulexps.set_volume(0.1)
bulrels = pygame.mixer.Sound("bulrell.wav")
bulrels.set_volume(0.4)
eggrels = pygame.mixer.Sound("eggrel.wav")
loselife = pygame.mixer.Sound("loselife.wav")
impact = pygame.mixer.Sound("pillarimpact.wav")
starcollect = pygame.mixer.Sound("starcollectn.wav")
starcollect.set_volume(0.4)
pygame.mixer.music.load("bgmusic.mp3")
pygame.mixer.music.set_volume(0.25)


#loading required sprite images
#bird animation frames
b1 = pygame.image.load('b1.png')
b2 = pygame.image.load('b4.png')
b3 = pygame.image.load('b6.png')
b4 = pygame.image.load('b8.png')
b5 = pygame.image.load('b9.png')
b6 = pygame.image.load('b10.png')
b7 = pygame.image.load('b11.png')
b8 = pygame.image.load('b12.png')
b9 = pygame.image.load('b14.png')
b10 = pygame.image.load('b16.png')
b11 = b1
b12 = pygame.image.load('b20.png')
b13 = pygame.image.load('b22.png')
b14 = pygame.image.load('b24.png')
b15 = pygame.image.load('b26.png')
b16 = pygame.image.load('b27.png')
b17 = b8
b18 = b9
b19 = b10


#star animation frames
sr1 = pygame.image.load('s1.png')
sr2 = pygame.image.load('s2.png')
sr3 = pygame.image.load('s3.png')
sr4 = pygame.image.load('s4.png')
sr5 = pygame.image.load('s5.png')
sr6 = pygame.image.load('s6.png')
sr7 = pygame.image.load('s7.png')
sr8 = pygame.image.load('s8.png')
sr9 = pygame.image.load('s9.png')
sr10 = pygame.image.load('s10.png')
sr11 = pygame.image.load('s11.png')
sr12 = pygame.image.load('s12.png')


#heart animation frames
h1 = pygame.image.load('h1.png')
h2 = pygame.image.load('h2.png')
h3 = pygame.image.load('h3.png')
h4 = pygame.image.load('h4.png')
h5 = pygame.image.load('h5.png')
h6 = pygame.image.load('h6.png')
h7 = pygame.image.load('h7.png')
h8 = pygame.image.load('h8.png')
h9 = pygame.image.load('h9.png')
h10 = pygame.image.load('h10.png')
h11 = pygame.image.load('h11.png')


#heart dust(displayed after bird takes heart) animation frames
hc1 = pygame.image.load('hc1.png')
hc2 = pygame.image.load('hc2.png')
hc3 = pygame.image.load('hc3.png')
hc4 = pygame.image.load('hc4.png')
hc5 = pygame.image.load('hc5.png')
hc6 = pygame.image.load('hc6.png')


#star dust(displayed after bird takes star) animation frames
sc1 = pygame.image.load('sc1.png')
sc2 = pygame.image.load('sc2.png')
sc3 = pygame.image.load('sc3.png')
sc4 = pygame.image.load('sc4.png')
sc5 = pygame.image.load('sc5.png')
sc6 = pygame.image.load('sc6.png')


#pillar image
pimg = pygame.image.load('pil.png')


#special pillar image(a bit longer than the normal one)
spimg = pygame.image.load('spil.png')


#transforming images
pimg180 = pygame.transform.rotate(pimg, 180)
fpimg = pygame.transform.flip(pimg180, True, False)
fspimg = pygame.transform.flip(spimg, True, False)


eggimg = pygame.image.load('egg.png')
bulimg = pygame.image.load('bullet.png')


#if nothing to be displayed then instead of deleting transparent is displayed
timg = pygame.image.load('trans.png')


#bullet explosion(displayed when egg hits bullet) animation frames
be1=pygame.image.load('be1.png')
be2=pygame.image.load('be2.png')
be3=pygame.image.load('be3.png')
be4=pygame.image.load('be4.png')
be5=pygame.image.load('be5.png')
be6=pygame.image.load('be6.png')
be7=pygame.image.load('be7.png')


#bullet smoke(displayed when bullet is released) animation frames
ee1=pygame.image.load('ee1.png')
ee2=pygame.image.load('ee2.png')
ee3=pygame.image.load('ee3.png')
ee4=pygame.image.load('ee4.png')
ee5=pygame.image.load('ee5.png')
ee6=pygame.image.load('ee6.png')


#yellow button animation frames
w1 = pygame.image.load('bu1.png')
w2 = pygame.image.load('bu2.png')
w3 = pygame.image.load('bu3.png')
w4 = pygame.image.load('bu4.png')
w5 = pygame.image.load('bu5.png')
w6 = pygame.image.load('bu6.png')
w7 = pygame.image.load('bu7.png')
w8 = pygame.image.load('bu8.png')
w9 = pygame.image.load('bu9.png')
w10 = pygame.image.load('bu10.png')


#creating lists for easy access of animation frames
waveimg = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10]
bimg = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19]
srimg = [sr1, sr2, sr3, sr4, sr5, sr6, sr7, sr8, sr9, sr10, sr11, sr12]
himg = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11]
hcimg = [hc1, hc2, hc3, hc4, hc5, hc6]
scimg = [sc1, sc2, sc3, sc4, sc5, sc6]
bulexp = [be1,be2,be3,be4,be5,be6,be7]
bulrel = [ee1,ee2,ee3,ee4,ee5,ee6]


offplay = pygame.image.load('playsmall.png')
onplay = pygame.image.load('playbig.png')
offplayag = pygame.image.load('playags.png')
onplayag = pygame.image.load('playagb.png')
intro1img = pygame.image.load('intro1.png')
intro2img = pygame.image.load('intro2.png')
backgnd = pygame.image.load("backgnd3.png")
gmovrimg = pygame.image.load('gameover.png')


#list of space(width) covered by 5 special pillars
slist = [473,536,662,999,851]


#defining Clock obj
clock = pygame.time.Clock()



def gamescore(score):
    
    
    msg = str(score)
    message_to_screen(msg, (0,0,0), 500, 12, 75)
    message_to_screen(msg, (255,255,255), 493, 5, 75)

    
    
def message_to_screen(msg, color, textX, textY, textSize):
    
    
    font = pygame.font.Font("flappy.TTF", textSize)
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [textX, textY])

    
    
def gameover():
    
    
    global gravity 
    global birdychange 
    global pxchange 
    global bgx1change 
    global bindexchange
    global bulxchange 
    global bulychange 
    global eggychange
    global bgupdate
    global hsmokechange
    global echange
    global achange
    global waitchange
    global wait2change
    global heart
    global wait3
    global windex
    global score
    global govr
    
    
    if wait3 == 0 and heart>0:
        pygame.mixer.Sound.play(loselife)
        wait3 = 1
    elif heart == 0:
        
            
        
        bgupdate += 1
        if bgupdate == 1:
            pygame.mixer.Sound.play(impact)
        if bgupdate == 3:
            
                           
            gameDisplay.fill((255,255,255))
            
                                    
        else:
            pygame.mixer.music.stop()
            gravity = 50
            birdychange = 0
            pxchange = 0
            bgx1change = 0
            bindexchange = 0
                    
            bulxchange = 0
            bulychange = 0
                    
            eggychange = 0
            hsmokechange = 0
            waitchange = 0
            wait2change = 0

            
            if bgupdate>3:
                
                
                windex = windex % 10
                gameDisplay.blit(waveimg[windex],(413,372))
                button(413,372,174,174,offplayag,onplayag,action = 'playagain')
                message_to_screen('Score = '+str(score), (0,0,0), 280, 255, 85)
                message_to_screen('Score = '+str(score), (255,255,255), 272, 247, 85)
                gameDisplay.blit(gmovrimg,(0,0))
                windex+=1
                
                
            govr = 1

            
            
def button(bx, by, bwidth, bheight, offimg, onimg, action = None):
    
    
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    
    if bx + 10 < cur[0] < bx + bwidth - 10 and by + 10 < cur[1] < by + bheight - 10:
        
        gameDisplay.blit(onimg, (bx, by))
        
    else:
        
        gameDisplay.blit(offimg, (bx, by))


    if bx + 10 < cur[0] < bx + bwidth - 10 and by + 10 < cur[1] < by + bheight - 10:    
        if click[0] == 1 and action != None:    
            if action == 'play' or action == 'playagain':
                gameloop()
            

def intro():
    
 
    global bgx1 
    global bgx1change 
    global bgx2
    global windex
    
    
    windex = 0
    bgx1 = 0
    bgx1change = 2
    bgx2 = bgx1 + 1000
    

    play = False
    
    while not play:

        
        curcopy = pygame.mouse.get_pos()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

                
        windex = windex % 10
        
        gameDisplay.blit(backgnd, (bgx1, 0))
        gameDisplay.blit(backgnd, (bgx2, 0))
        
        if 443 < curcopy[0] < 443+114 and 402 < curcopy[1] < 402+114:
            
            gameDisplay.blit(intro2img,(0,0))
            
        else:
            
            gameDisplay.blit(intro1img,(0,0))
            
        gameDisplay.blit(waveimg[windex],(413,372))
        button(413,372,174,174,offplay,onplay,action = 'play')
           
        bgx1 -= bgx1change
        
        if bgx2 == 0:
            
            bgx1 = 0
            bgx2 = bgx1 + 1000
            
        else:
            
            bgx2 = bgx1 + 1000
            
        windex+=1
        
        pygame.display.update()
        
        clock.tick(15)


        
def gameloop():
    
    
    #plays the music(-1 means music is played in infinite loops)
    pygame.mixer.music.play(-1)
    
    
    global birdychange 
    global eggychange 
    global bulxchange 
    global bulychange                                                                                       
    global gravity 
    global bgx1 
    global bgx1change 
    global bgx2 
    global pxchange 
    global bindexchange
    global bgupdate 
    global echange
    global achange
    global smokechange
    global hsmokechange
    global waitchange
    global wait2change
    global score
    global heart
    global wait3
    global govr
    
    
    '''the track of the game consists of pipes which are placed in a pattern i.e.
    a set of 9 equidistant normal pillars are followed by a special pillar and their are
    5 such special pillars so all these makes up a total of 50 pillars and the game track
    loops after every 50 pillars. The normal pillars have random y pos but fixed x pos
    whereas special pillars have both coordinates fixed'''
    
    govr = 0
    
    eggychange = 25
    
    bulxchange = 5
    bulychange = 15
    
    gravity = 8
    
    birdx = 150
    birdy = 100
    birdychange = 0
    
    bindex = 1
    hindex = 1
    
    plist = []
    srlist = []
    
    px=500
    pc = 0
    cc = 0
    pxchange = 5
    
    spx = 0
    k=-1
    
    rsr = 1
    
    windex = 0
    
    z=1
    z1=1
    
    smokec = 0
    hsmokec = 0
    hb = 0
    
    col = None
    wait = 0
    eggrel = False
    
    egglist = []
    bullist = []
    
    bcx = 0
    bcy = 0
    
    a=0
    e=0
    
    wait2 = 0
    
    bbx = 0
    bby = 0
    
    bblist = []
    
    srindexchange = 1
    bindexchange = 1
    hindexchange = 1
    bgupdate = 0
    echange = 1
    achange = 1
    smokechange = 1
    hsmokechange = 1
    waitchange = 1
    wait2change = 1
    
    score = 0
    heart = 0
    wait3 = 0
    
    '''the pillarlist consists of x, y coordinates, odd or even value(depending on
    this the pillar will be either up or down) of normal pillars. The 1st pillars are
    added to the pillarlist beforehand then as the leftmost pillar approaches the left
    boundary of the display screen it is deleted from the list and a new pillar is added
    depending on the pc(pillar counter) of the rightmost pillar, if it happens to be the
    last one in a set of 9 then the new pillar is placed little bit farther leaving space
    for the special pillar(this space info is taken from slist)'''
    
    for i in range(9):
        srx = px + 91
        sry = random.randrange(250, 350)
        srb = random.randrange(0, 2)
        srl = []
        srl.append(srx)
        srl.append(sry)
        srl.append(srb)
        srl.append(z)
        srlist.append(srl)
        pc+=1
        pl=[]
        pl.append(px)
        if pc%2==1:
            py = random.randrange(300, 580)
        else:
            py = random.randrange(-158, -38)
        pl.append(py)
        pl.append(pc)
        plist.append(pl)
        
        px += 180
        z+=5

    '''the bullets and stars are displayed randomly. The bullist and srlist consists of x,y
    coordinates along with a boolean value(dependingon which it is decided whether it will be
    displayed or not) of each bullet/star'''   

    Exit = False

    while not Exit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        birdychange = -25
                    
                    elif event.key == pygame.K_DOWN:
                        pygame.mixer.Sound.play(eggrels)
                        eggy = abirdy + 30
                        egglist.append(eggy)
 
            elif event.type == pygame.KEYUP:
                birdychange=0
                
        birdy += birdychange
        birdy += gravity
        abirdx = birdx + 47
        abirdy = birdy + 46
        
        eggx = abirdx + 5
        
        gameDisplay.blit(backgnd, (bgx1, 0))
        gameDisplay.blit(backgnd, (bgx2, 0))
     
        bgx1 -= bgx1change
        
        if bgx2 == 0:
            
            bgx1 = 0
            bgx2 = bgx1 + 1000
            
        else:
            
            bgx2 = bgx1 + 1000
       
        if len(egglist) != 0:
        
            for i in range(len(egglist)):    
                
                gameDisplay.blit(eggimg,(eggx,egglist[i]))

            
        for i in range(len(bullist)-1):
            
            if bullist[i][0] == bullist[i+1][0]:
                
                del bullist[i+1]

        if wait2 > 0 and wait2<50:
            
            wait2+=1

        elif wait2 == 50:
            
            e=0
            wait2 = 0
        
        for i in range(len(bullist)):
            
            if bullist[i][2] != 0:
                
                if e<6:
                    
                    gameDisplay.blit(bulrel[e],(bullist[i][0]-25,brsy-35))
                    e += echange
                    wait2 = wait2change

                #animation of bulrel consists of 6 frames but the sound needs to be played only once
                if e==1:
                    pygame.mixer.Sound.play(bulrels)
                    
                gameDisplay.blit(bulimg,(bullist[i][0],bullist[i][1]))
                

                #checking for collision of egg with bullet(if detected a smoke animation is displayed at the last pos of bullet)
                for j in range(len(egglist)):
                    if egglist[j]+7<bullist[i][1]+35 and egglist[j]+7>bullist[i][1] or egglist[j]+30<bullist[i][1]+35 and egglist[j]+30>bullist[i][1]:
                        if eggx+1<bullist[i][0]+35 and eggx+1>bullist[i][0] or eggx+24<bullist[i][0]+35 and eggx+24>bullist[i][0]:
                            bcx = bullist[i][0]-33
                            bcy = bullist[i][1]-72
                            bullist[i][1] = -25
                            egglist[j] = 700
                            
                            
                #checking for collision of bird with bullet            
                if abirdx>bullist[i][0] and abirdx< bullist[i][0]+25 or abirdx+35>bullist[i][0] and abirdx+35<bullist[i][0]+25:
                    if abirdy>bullist[i][1]+6 and abirdy< bullist[i][1]+41 or abirdy+35>bullist[i][1]+6 and abirdy+35<bullist[i][1]+41:
                        gameover()
                        
                        

        if bcx!=0 and bcy!=0:
            
            if a==7:
                
                a=0
                bcx = 0
                bcy = 0
                
            else:
                
                pygame.mixer.Sound.play(bulexps)
                gameDisplay.blit(bulexp[a],(bcx,bcy))
                bcx -= pxchange
                a+=achange
                

        #bindex value keeps on increasing but we have only 19 elements in the bimg list thats why modulus is taken so that bindex is always < 19
        bindex = bindex%19
        gameDisplay.blit(bimg[bindex], (birdx, birdy))
        
        
        #similar function as bindex(heart animation consists of 11 frames)
        hindex = hindex % 11
        for i in range(9):
            
            #displaying the normals pillars (placed up or down depending on their pc value)
            if plist[i][2] % 2 == 1:
                
                gameDisplay.blit(fpimg, (plist[i][0], plist[i][1]))
                
                #only down pillars shoot bullets depending on the third boolean parameter of each bullet
                if plist[i][0] < birdx+60 and plist[i][0] > birdx+50:
                    
                    bl = []
                    
                    bl.append(plist[i][0]+12)
                    brsy = plist[i][1]
                    
                    bl.append(plist[i][1])
                    bl.append(random.randrange(0,2))
                    
                    bullist.append(bl)
                    
            else:
                
                gameDisplay.blit(pimg, (plist[i][0], plist[i][1]))
                

            #displaying star(depending on before or after collision)
            #after collision
            if srlist[i][2] == 2 and smokec < 7:
                
                #as their are 6 star smoke animation frames
                if smokec < 6:
                    
                    gameDisplay.blit(scimg[smokec],(srlist[i][0], srlist[i][1]))
                    smokec += smokechange
                    
                else:
                    
                    smokec = 0
                    srlist[i][2] = 3
                    
            #before collision        
            elif srlist[i][2] == 1:
               
                srlist[i][3] = srlist[i][3] % 12
                gameDisplay.blit(srimg[srlist[i][3]] ,(srlist[i][0], srlist[i][1]))
                srlist[i][3] += srindexchange
                
            #after star smoke animation is completed a transparent image is displayed as deleting the star from list would creat much caios 
            else:
                
                gameDisplay.blit(timg,(srlist[i][0], srlist[i][1]))
                
                
        #displaying the soecial pillars        
        if k==0:
  
            gameDisplay.blit(pimg, (spx,-150))
            gameDisplay.blit(fpimg, (spx,400))
            
        elif k==1:
  
            gameDisplay.blit(pimg, (spx,-150))
            gameDisplay.blit(fpimg, (spx,400))
            gameDisplay.blit(pimg, (spx+63,-150))
            gameDisplay.blit(fpimg, (spx+63,400))
            
        elif k==2:

            gameDisplay.blit(pimg, (spx,-150))
            gameDisplay.blit(fpimg, (spx,400))
            gameDisplay.blit(pimg, (spx+63,-150))
            gameDisplay.blit(fpimg, (spx+63,400))
            gameDisplay.blit(pimg, (spx+126,-150))
            gameDisplay.blit(fpimg, (spx+126,400))
            gameDisplay.blit(pimg, (spx+189,-150))
            gameDisplay.blit(fpimg, (spx+189,400))

            #the heart is always displayed after the 3rd special pillar
            #before collision
            if hb == 0:
                
                gameDisplay.blit(himg[hindex], (spx+slist[k]-410+100, 50))
                
            #after collision
            elif hb == 1 and hsmokec < 7:
                
                #as their are 6 heart smoke animation frames
                if hsmokec < 6:
                    
                    gameDisplay.blit(hcimg[hsmokec], (spx+slist[k]-410+100, 50))
                    hsmokec += hsmokechange
                    
                else:
                    
                    hb = 2
                    hsmokec = 0
                    
            #after heart smoke animation is completed
            else:
                
                gameDisplay.blit(timg, (spx+slist[k]-410+100, 50))
                
        elif k==3:
   
            gameDisplay.blit(pimg, (spx,0))
            gameDisplay.blit(fspimg, (spx+275,250))
            gameDisplay.blit(pimg, (spx+550,0))
            
        elif k==4:

            gameDisplay.blit(pimg, (spx,-100))
            gameDisplay.blit(fpimg, (spx,500))
            
            gameDisplay.blit(pimg, (spx+63,-150))
            gameDisplay.blit(fpimg, (spx+63,450))
            
            gameDisplay.blit(pimg, (spx+126,-200))
            gameDisplay.blit(fpimg, (spx+126,400))
            
            gameDisplay.blit(pimg, (spx+189,-250))
            gameDisplay.blit(fpimg, (spx+189,350))
            
            gameDisplay.blit(pimg, (spx+252,-200))
            gameDisplay.blit(fpimg, (spx+252,400))
            
            gameDisplay.blit(pimg, (spx+315,-150))
            gameDisplay.blit(fpimg, (spx+315,450))
            
            gameDisplay.blit(pimg, (spx+378,-100))
            gameDisplay.blit(fpimg, (spx+378,500))

                        
        gamescore(score)    
            
            
        #touching the ground kills the bird
        if abirdy > 640:
            
            gameover()
            
        if abirdy > 720:
            
            gravity = 0
            
            
        #checking collisions with pillars
        for i in range(9):
            
            if abirdx+35 > plist[i][0] and abirdx+35 < plist[i][0]+63 or abirdx > plist[i][0] and abirdx < plist[i][0]+63:
                    
                if cc%2==1:
                    
                    if abirdy+35 > plist[i][1]:
                        gameover()
             
                else:
                    
                    if abirdy-35 < plist[i][1]+362:
                        gameover()
                        
                        
                        

            if k==0:
                if abirdx+35 > spx and abirdx+35 < spx+slist[k]-410 or abirdx > spx and abirdx < spx+slist[k]-410:
                    if abirdy < 250 or abirdy+35 > 400:
                        abirdx -= 35 + spx + slist[k] - 410
                        gameover()
                        
                        
                            
                        

            elif k==1:
                if abirdx+35 > spx and abirdx+35 < spx+slist[k]-410 or abirdx > spx and abirdx < spx+slist[k]-410:
                    if abirdy < 250 or abirdy+35 > 400:
                        abirdx -= 35 + spx + slist[k] - 410
                        gameover()
                        
                        

            elif k==2:
                if abirdx+35 > spx and abirdx+35 < spx+slist[k]-410 or abirdx > spx and abirdx < spx+slist[k]-410:
                    if abirdy < 250 or abirdy+35 > 400:
                        abirdx -= 35 + spx + slist[k] - 410
                        gameover()
                        
                        
                    '''as the heart is pretty big in comparision to the bird tahts why the bird remains in collision
                    for a few seconds as a result of which the heart smoke animation is displayed as many no. of times
                    as collision is detected. In order to solve this wait var is used which after first collision doesn't
                    allow checking for collision for a few seconds within which the bird crosses the heart and as only
                    one collision was detected therefoere the animation was displayed only once'''

                    #similar technique is used for gameover detection 
                    
                #checking collision of bird with heart
                elif abirdx > spx+slist[k]-410+100 and abirdx < spx+slist[k]-410+100+60 or abirdx+35 > spx+slist[k]-410+100 and abirdx+35 < spx+slist[k]-410+100+60:
                    if abirdy > 50 and abirdy < 50+60 or abirdy+35 > 50 and abirdy+35 < 50+60:
                        
                        if wait == 0:

                            pygame.mixer.Sound.play(hsound)
                            hb = 1
                            wait = 1
                            col = True
                            heart += 1
                            
                            
                  

            elif k==3:
                if abirdx+35 > spx-25 and abirdx+35 < spx-25+63 or abirdx > spx-25 and abirdx < spx-25+63:
                    if abirdy < 400:
                        abirdx -= 35 + spx + slist[k] - 410
                        gameover()
                        
                        
                elif abirdx+35 > spx+275 and abirdx+35 < spx+275+63 or abirdx > spx+275 and abirdx < spx+275+63:
                    if abirdy+35 > 250:
                        abirdx -= 35 + spx + slist[k] - 410
                        gameover()
                        
                        
                elif abirdx+35 > spx+550 and abirdx+35 < spx+550+63 or abirdx > spx+550 and abirdx < spx+550+63:
                    if abirdy < 400:
                        abirdx -= 35 + spx + slist[k] - 410
                        gameover()
                        
                 

            elif k==4:
                if abirdx+35 > spx and abirdx+35 < spx+63 or abirdx > spx and abirdx < spx+63:
                    if abirdy < 300 or abirdy+35 > 500:
                        abirdx = 35 + spx + slist[k] - 410
                        gameover()
                        
                        
                elif abirdx+35 > spx+63 and abirdx+35 < spx+63+63 or abirdx > spx+63 and abirdx < spx+63+63:
                    if abirdy < 250 or abirdy+35 > 450:
                        abirdx = 35 + spx + slist[k] - 410
                        gameover()
                        
                        
                elif abirdx+35 > spx+126 and abirdx+35 < spx+126+63 or abirdx > spx+126 and abirdx < spx+126+63:
                    if abirdy < 200 or abirdy+35 > 400:
                        abirdx = 35 + spx + slist[k] - 410
                        gameover()
                        
                        
                elif abirdx+35 > spx+189 and abirdx+35 < spx+189+63 or abirdx > spx+189 and abirdx < spx+189+63:
                    if abirdy < 150 or abirdy+35 > 350:
                        abirdx = 35 + spx + slist[k] - 410
                        gameover()
                        
                        
                elif abirdx+35 > spx+252 and abirdx+35 < spx+252+63 or abirdx > spx+252 and abirdx < spx+252+63:
                    if abirdy < 200 or abirdy+35 > 400:
                        abirdx = 35 + spx + slist[k] - 410
                        gameover()
                        
                        
                elif abirdx+35 > spx+315 and abirdx+35 < spx+315+63 or abirdx > spx+315 and abirdx < spx+315+63:
                    if abirdy < 250 or abirdy+35 > 450:
                        abirdx = 35 + spx + slist[k] - 410
                        gameover()
                        
                        
                elif abirdx+35 > spx+378 and abirdx+35 < spx+378+63 or abirdx > spx+378 and abirdx < spx+378+63:
                    if abirdy < 300 or abirdy+35 > 500:
                        abirdx = 35 + spx + slist[k] - 410
                        gameover()

                        

        #checking for collision of bird with star
        for i in range(9):
            
            if srlist[i][2]==1:
                
                if abirdx > srlist[i][0] and abirdx < srlist[i][0]+53 or abirdx+35 > srlist[i][0] and abirdx+35 < srlist[i][0]+53:
                    if abirdy > srlist[i][1] and abirdy < srlist[i][1]+60 or abirdy+35 > srlist[i][1] and abirdy+35 < srlist[i][1]+60:

                        pygame.mixer.Sound.play(starcollect)
                        srlist[i][2] = 2
                        score += 1
                        
        #checking if leftmost pillar i.e. 1st pillar in plist has crossed the left boundary       
        if plist[0][0]+63 < 0:
            if pc%50 == 9:
                pc+=2
                px=plist[8][0]+slist[0]
                spx = plist[8][0]+230
                k=0
                
            elif pc%50 == 19:
                pc+=2
                px=plist[8][0]+slist[1]
                spx = plist[8][0]+230
                k=1
                
            elif pc%50 == 29:
                pc+=2
                px=plist[8][0]+slist[2]
                spx = plist[8][0]+230
                k=2

                hb = 0
                
            elif pc%50 == 39:
                pc+=2
                px=plist[8][0]+slist[3]
                spx = plist[8][0]+230
                k=3
                
            elif pc%50 == 49:
                pc+=2
                px=plist[8][0]+slist[4]
                spx = plist[8][0]+230
                k=4
                
            else:
                pc+=1
                px=plist[8][0]+180
                
            del plist[0]
            
            
            pl=[]
            pl.append(px)
            
            if pc%2==1:
                
                py = random.randrange(300, 580)
                
            else:
                
                py = random.randrange(-158, -38)
                
            pl.append(py)
            pl.append(pc)
            plist.append(pl)
            


        if srlist[0][0]+60<0:
            del srlist[0]

            srx = plist[8][0] + 91
            sry = random.randrange(250, 350)
            srb = random.randrange(0, 2)
            srl = []
            srl.append(srx)
            srl.append(sry)
            srl.append(srb)
            srl.append(z1)
            srlist.append(srl)
            z1+=5
            
        

        
        if pc % 10 == 9 and plist[0][0] + 63 < abirdx:
            cc = pc + 1
        else:
            cc = pc

        
        for i in range(9):
            
            plist[i][0] -= pxchange
            srlist[i][0] -= pxchange
            
        spx -= pxchange
            
        bindex += bindexchange
        
        hindex += hindexchange


        if len(egglist)!=0:
            if egglist[0]>580:
                del egglist[0]
        
        for i in range(len(egglist)):
            egglist[i] += eggychange

        #if bullet goes above the top boundary then it is deleted from the list    
        if len(bullist)!=0:
            if bullist[0][1]<0:
                del bullist[0]
                
        if wait >=1 and wait < 100:
            wait+=1
        elif wait == 100:
            wait = 0

            
        if wait3 >= 1 and wait3 < 25:
            wait3 += 1
        elif wait3 == 25:
            wait3 = 0
            heart -= 1
            
        
        for i in range(len(bullist)):
             
            bullist[i][0] -= bulxchange
            bullist[i][1] -= bulychange
            
        #different FPS for different distances reached by the bird in the game
        if govr == 1:
            FPS = 25
        elif pc >= 9 and pc <= 40:
            FPS = 17
        elif pc > 40 and pc <= 59:
            FPS = 19
        elif pc > 59 and pc <= 100:
            FPS = 21
        elif pc > 100 and pc <= 200:
            FPS = 25
        else:
            FPS = 30
        
        
        pygame.display.update()
        clock.tick(FPS)
        
intro()    


        
    
    
    

    
    

