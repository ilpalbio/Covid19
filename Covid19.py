import pygame as py
from random import choice,randint
import os
import variabiliSchermo as vs

py.init()
dirname = os.path.dirname(__file__)
cartella = os.path.join(dirname, 'foto')
os.chdir(cartella)

FPS = 60
clock = py.time.Clock()
py.display.set_caption('Covid19')

x = 1600
y = 900
screen = py.display.set_mode((x,y))

# VARIABILI SCHERMATA INIZIALE
scritta = py.image.load('scritta.png')
start = py.image.load('start.png')
foto_home = py.image.load('ospedale.png')
istruzioni = py.image.load('regole.png')
istruzioni_foto = py.image.load('comandi.png')
tasto_uscita = py.image.load('uscita.png')
ospedale = py.image.load('ospedale_foto.png')
# personaggi
p1 = py.image.load('p1.png')
p1 = py.transform.scale(p1,(70,119))
p2 = py.image.load('p2.png')
p2 = py.transform.scale(p2,(60,119))

# tuple
DARK_RED = (143, 5, 13)
CRAZY_BLUE = (75, 70, 249)
BLUE = (0, 0, 238)
RED = (255, 57, 0)
BLACK = (0,0,0)
L_BLUE = (0, 186, 248)
GREY = (77, 77, 77)
L_GREEN = (208, 255, 106)
ORANGE = (255, 112, 45)
L_GREY = (243, 244, 238)
WHITE = (255,255,255)

# variabili boleane
mostraIstruzioni = True
iniziaGioco = True
togliIstruzioni = False
scegliPersonaggio = True
togliPersonaggi = False
personaggioDestra = False
personaggioSinistra = True
mostraScore = True
pFemmina = True
pMaschio = False
grandezzaSchermo = True
esciGrandezzeSchermo = False

# font
font = py.font.SysFont('Alien Encounters', 30)

# variabili dei punteggi
nPartite = 0
nNuke = 0
nRallentamenti = 0
partiteVinte = 0
partitePerse = 0
mediaPartite = 0

# posizione bottoni
posIstruzioni = (1506,20)
posStart = (700,418)
# funzioni
def draw_istruzioni():
    screen.blit(tasto_uscita,(100,100))
    screen.blit(istruzioni_foto, (329,200))
def draw_schermata():
    screen.blit(foto_home, (0,0))
    screen.blit(scritta, (500,0))
    screen.blit(start, (700,418))
    screen.blit(istruzioni, (1506,20))
    py.draw.rect(screen,DARK_RED,(1400,20,64,64))
    py.draw.rect(screen,DARK_RED,(20,20,64,64))
def draw_personaggi():
    py.draw.rect(screen,CRAZY_BLUE,(1300,0,300,900))
    py.draw.rect(screen, BLUE, (1310, 15, 95, 130))
    py.draw.rect(screen, BLUE, (1445, 15, 95, 130))
    # personaggi
    screen.blit(p1,(1315,15))
    screen.blit(p2,(1460,15))
    # tasto x uscire
    py.draw.circle(screen,RED,(1575,25),15)
def draw_grandezzeSchermo():
    py.draw.rect(screen,CRAZY_BLUE,(10,200,670,680))
    scrittaGrandezzaSchermo= font.render(str('Seleziona le dimensioni dello schermo'),True,(0,0,0))
    screen.blit(scrittaGrandezzaSchermo,(15,215))
    # rettangli blu
    py.draw.rect(screen,BLUE,(15,300,640,150))
    py.draw.rect(screen,BLUE,(15,500,640,150))
    # scritte
    scrittaSchermo1 = font.render(str('1600x900'),True,(0,0,0))
    screen.blit(scrittaSchermo1,(270,360))
    scrittaSchermo2 = font.render(str('1000x500'),True,(0,0,0))
    screen.blit(scrittaSchermo2,(270,560))
    # tasto di uscita
    py.draw.rect(screen,RED,(200,780,300,70))
    scrittaUscita = font.render(str('ESCI'),True,(0,0,0))
    screen.blit(scrittaUscita,(315,800))

'''
def ridimensionaSchermo_home():
    x = 1000
    y = 500
    screen = py.display.set_mode((x,y))
    Rscritta = py.transform.scale(scritta, (vs.vRscritta[0],vs.vRscritta[1]))
    Rstart = py.transform.scale(start, (vs.vRstart[0],vs.vRstart[1]))
    Rfoto_home = py.transform.scale(foto_home, (vs.vRfoto_home[0],vs.vRfoto_home[1]))
    Ristruzioni = py.transform.scale(istruzioni, (vs.vRistruzioni[0],vs.vRistruzioni[1]))
    # apparizione delle immagini sullo schermo
    screen.blit(Rfoto_home,(vs.vRfoto_home[2],vs.vRfoto_home[3]))
    screen.blit(Rscritta,(vs.vRscritta[2],vs.vRscritta[3]))
    screen.blit(Rstart,(vs.vRstart[2],vs.vRstart[3]))
    screen.blit(Ristruzioni,(vs.vRistruzioni[2],vs.vRistruzioni[3]))
def ridimensionaIstruzioni(): 
    Ristruzioni_foto = py.transform.scale(istruzioni_foto, (vs.vRistruzioni_foto[0],vs.vRistruzioni_foto[1]))
    Rtasto_uscita  = py.transform.scale(tasto_uscita, (vs.vRtasto_uscita[0],vs.vRtasto_uscita[1]))
'''

draw_schermata()

home_page = True
while home_page:

    clock.tick(20)

    posizione_mouse = py.mouse.get_pos()

    for event in py.event.get():
        if event.type == py.QUIT:
            quit()
    if event.type == py.MOUSEBUTTONDOWN:
        # schermata iniziale
        if togliIstruzioni == True:
            if posizione_mouse[0] >= 100 and posizione_mouse[0] <= 164: 
                if posizione_mouse[1] >= 100 and posizione_mouse[1] <= 164:
                    togliIstruzioni = False
                    iniziaGioco = True
                    scegliPersonaggio = True
                    mostraScore = True
                    grandezzaSchermo = True
                    draw_schermata()

        # mostra istruzioni
        if mostraIstruzioni == True:
            if posizione_mouse[0] >= posIstruzioni[0] and posizione_mouse[0] <= posIstruzioni[0] + 64:
                if posizione_mouse[1] >= posIstruzioni[1] and posizione_mouse[1] <= posIstruzioni[1] + 64:
                    iniziaGioco = False
                    scegliPersonaggio = False
                    togliIstruzioni = True
                    mostraScore = False
                    grandezzaSchermo = False
                    draw_istruzioni()

        # scegli personaggio
        if scegliPersonaggio == True:
            if posizione_mouse[0] >= 1400 and posizione_mouse[0] <= 1400 + 64:
                if posizione_mouse[1] >= 20 and posizione_mouse[1] <= 20+ 64:
                    draw_personaggi()
                    mostraIstruzioni = False
                    iniziaGioco = False
                    togliIstruzioni = False
                    togliPersonaggi = True
                    mostraScore = False
                    grandezzaSchermo = False
            # scelta personaggio femmina
            if posizione_mouse[0] >= 1315 and posizione_mouse[0] <= 1315 + 95:
                if posizione_mouse[1] >= 15 and posizione_mouse[1] <= 15 + 130:
                    pFemmina = True
                    pMaschio = False
            # scelta del personaggio maschio
            if posizione_mouse[0] >= 1460 and posizione_mouse[0] <= 1460 + 95:
                if posizione_mouse[1] >= 15 and posizione_mouse[1] <= 15 + 130:
                    pMaschio = True
                    pFemmina = False

        # togli personaggio
        if togliPersonaggi == True:
            if posizione_mouse[0] >= 1560 and posizione_mouse[0] <= 1560 + 30:
                if posizione_mouse[1] >= 10 and posizione_mouse[1] <= 10 + 30:
                    togliPersonaggi = False
                    togliIstruzioni = False
                    iniziaGioco = True
                    scegliPersonaggio = True
                    mostraIstruzioni = True
                    mostraScore = True
                    grandezzaSchermo = True
                    draw_schermata()
        
        # scelta delle grandezze dello schermo
        if grandezzaSchermo == True:
            if posizione_mouse[0] >= 20 and posizione_mouse[0] <= 20 + 64:
                if posizione_mouse[1] >= 20 and posizione_mouse[1] <= 20 + 64:
                    esciGrandezzeSchermo = True
                    mostraIstruzioni = False
                    iniziaGioco = False
                    togliIstruzioni = False
                    togliPersonaggi = True
                    mostraScore = False
                    scegliPersonaggio = False
                    draw_grandezzeSchermo()
            # scelta grandezza 1600x900
            if posizione_mouse[0] >= 15 and posizione_mouse[0] <= 15 + 640:
                if posizione_mouse[1] >= 300 and posizione_mouse[1] <= 300 + 150:
                    print('grandezza scelta 1600x900')
            # scelta grandezza 1000x500
            if posizione_mouse[0] >= 15 and posizione_mouse[0] <= 15 + 640:
                if posizione_mouse[1] >= 500 and posizione_mouse[1] <= 500 + 150:
                    print('grandezza scelta 1000x500')

        if esciGrandezzeSchermo == True:
            if posizione_mouse[0] >= 200 and posizione_mouse[0] <= 200 + 300:
                if posizione_mouse[1] >= 780 and posizione_mouse[1] <= 780 + 70:
                    iniziaGioco = True
                    scegliPersonaggio = True
                    mostraScore = True
                    grandezzaSchermo = True
                    mostraIstruzioni = True
                    esciGrandezzeSchermo = False
                    draw_schermata()

            
              
        # inizio gioco
        if iniziaGioco == True:
            if posizione_mouse[0] >= posStart[0] and posizione_mouse[0] <= posStart[0] + 314:
                if posizione_mouse[1] >= posStart[1] and posizione_mouse[1] <= posStart[1] + 157:
                    home_page = False
                    nPartite += 1

    py.display.update()

# VARIABILI GIOCO
# variabili
y_list = [166,332,498,664]
cronometro = 0
sec = 0
minu = 0
font = py.font.SysFont('Alien Encounters', 70)
font_nuke = py.font.SysFont('BN Machine',200)
n_colpi = 5
meta_nemico = 47
kill = 0
kill_tot = 0
nuke = False
countdown = 240
nemico_vita = 100
rallentamento = False
kill_rall = 0
tempo_rall = 300
tempo = 0
haiVinto = False
haiPerso = False

class Personaggio:
    personaggioFemmina = py.image.load('infermiera.png')
    personaggioMaschio = py.image.load('infermiere.png')
    def __init__(self,y,w,h,color):
        self.x = 0
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    def draw(self,screen):
        if pFemmina == True:
            screen.blit(self.personaggioFemmina,(self.x,self.y))
        if pMaschio == True:
            screen.blit(self.personaggioMaschio,(self.x,self.y))


y_personaggio = 166

class Proiettile(object):
    proiettile = py.image.load('proiettile.png')
    def __init__(self,x,y,w,h,color,danno):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 8
        self.color = color 
        self.danno = danno
    def draw(self,screen):
        screen.blit(self.proiettile,(self.x,self.y))

bullet_list = []

class Nemico(object):
    zombie = (py.image.load('1.png'),py.image.load('2.png'),py.image.load('3.png'),py.image.load('4.png'),py.image.load('5.png'),py.image.load('6.png'),py.image.load('7.png') \
        ,py.image.load('8.png'),py.image.load('9.png'),py.image.load('10.png'),py.image.load('11.png'),py.image.load('12.png'),py.image.load('13.png'),py.image.load('14.png') \
        ,py.image.load('15.png'),py.image.load('16.png'),py.image.load('17.png'),py.image.load('18.png'),py.image.load('19.png'),py.image.load('20.png') \
        ,py.image.load('21.png'),py.image.load('22.png'),py.image.load('23.png'),py.image.load('24.png'),py.image.load('25.png'),py.image.load('26.png') \
        ,py.image.load('27.png'),py.image.load('28.png'),py.image.load('29.png'),py.image.load('30.png'),py.image.load('31.png'),py.image.load('32.png') \
        ,py.image.load('33.png'),py.image.load('34.png'),py.image.load('35.png'),py.image.load('36.png'),py.image.load('24.png'),py.image.load('25.png') \
        ,py.image.load('26.png'),py.image.load('27.png')\
        ,py.image.load('12.png'),py.image.load('13.png'),py.image.load('14.png'),py.image.load('15.png'),py.image.load('16.png'),py.image.load('17.png'),py.image.load('1.png') \
        ,py.image.load('2.png'),py.image.load('3.png'),py.image.load('4.png'),py.image.load('5.png'))
    def __init__(self,x,w,h,color,vita):
        self.x = x
        self.y = y_list.pop(y_list.index(choice(y_list)))
        self.w = w
        self.h = h
        self.speed = randint(1,4)
        self.color = color
        self.vita = vita
        self.walk = 0
    def move(self):
        self.x -= self.speed
    def draw(self,screen):
        self.move()
        if self.walk + 1 >= 51:
            self.walk = 0
        else:
            screen.blit(self.zombie[self.walk],(self.x,self.y))
            self.walk += 1

x_nemico = 1800
n_nemici = 4
nemico_list = []
for i in range(n_nemici):
    nemico_list.append(Nemico(x,50,100,L_GREEN,nemico_vita))
    n_nemici -= 1

class Bullet_Counter:
    def __init__(self,x,y,w,h,color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    def draw(self):
        py.draw.rect(screen, self.color,(self.x , self.y,self.w,self.h))

bullet_counter = Bullet_Counter(0,830,x,70,ORANGE)

class lineeStrada:
    def __init__(self,color):
        self.x = 0
        self.w = 1800
        self.h = 10
        self.color = color
    def draw(self,screen):
        py.draw.rect(screen,self.color,(self.x,254,self.w,self.h))
        py.draw.rect(screen,self.color,(self.x,418,self.w,self.h))
        py.draw.rect(screen,self.color,(self.x,584,self.w,self.h))
        py.draw.rect(screen,self.color,(self.x,750,self.w,self.h))


linee = lineeStrada(WHITE)


def barra_info():
    # n colpi
    text_colpi = font.render(str(n_colpi), True, (0,0,0))
    screen.blit(text_colpi, (1420, 840))
    # scritta colpi
    text = font.render(str('COLPI'), True, (0,0,0))
    screen.blit(text,(1180,840))
    # n secondi
    text_sec = font.render(str(sec // 60),True,(0,0,0))
    screen.blit(text_sec,(210,840))
    # scritta sec
    text_sec_scritta = font.render(str('SEC: '),True,(0,0,0))
    screen.blit(text_sec_scritta,(10,840))
    # n minuti
    text_min = font.render(str(minu),True,(0,0,0))
    screen.blit(text_min,(520,840))
    # scritta min
    text_min_scritta = font.render(str('MIN: '),True,(0,0,0))
    screen.blit(text_min_scritta,(320,840))
    # n kill
    text_kill = font.render(str(kill),True,(0,0,0))
    screen.blit(text_kill,(870,840))
    # scritta kill
    text_kill_scritta = font.render(str('KILL: '),True,(0,0,0))
    screen.blit(text_kill_scritta,(650,840))

def stopGioco():
    global cronometro
    global sec
    for zombie in nemico_list:
        zombie.speed = 0
    cronometro += 0
    n_nemici = 0
    y_personaggio = 0
    y_personaggio += 0
    sec += 0
def gameWindow():
    screen.fill(GREY)
    linee.draw(screen)
    py.draw.rect(screen,L_BLUE,(0,0,1800,186))
    bullet_counter.draw()
    barra_info()
    screen.blit(ospedale,(0,0))


game = True
while game:
    clock.tick(FPS)
# GIOCO
    # barra delle info sul personaggio
    gameWindow()

    # fine del gioco
    for zombie in nemico_list:
        if zombie.x <= 20:
            haiPerso = True
    
    if haiPerso == True:
        stopGioco()
        game = False

    if tempo // 60 >= 60: 
        haiVinto = True
    
    if haiVinto == True:
        stopGioco()
        game = False

    # controllo dei colpi
    if n_colpi >= 5:
        n_colpi = 5

    # aggiunta delle y in cui si creano gli zombie
    if y_list == []:
        y_list = [166,332,498,664]

    # definizione del personaggio
    personaggio = Personaggio(y_personaggio,20,100,L_BLUE)
    personaggio.draw(screen)

    x_proiettile = 20
    y_proiettile = y_personaggio + meta_nemico

    tempo += 1
    sec += 1
    if sec >= 3600:
        sec = 0
        minu += 1

    if cronometro == 120:
        cronometro = 0
        n_nemici += 4
        for i in range(n_nemici):
            nemico_list.append(Nemico(x,50,100,L_GREEN,nemico_vita))
            n_nemici -= 1
    else:
           cronometro += 1

    for nemico in nemico_list:
        nemico.draw(screen)
    for bullet in bullet_list:
        if bullet.x < 1800 and bullet.x > 0:
            bullet.x += bullet.speed
        else:
            bullet_list.pop(bullet_list.index(bullet))
            n_colpi += 1
    for bullet in bullet_list:
        for nemico in nemico_list:
            if bullet.x >= nemico.x:
                if bullet.y == nemico.y + meta_nemico :
                    bullet.speed -= bullet.speed
                    bullet.x = -30
                    bullet_list.remove(bullet)
                    n_colpi += 1
                    nemico.vita -= bullet.danno
                    if nemico.vita <= 0:
                        nemico_list.remove(nemico)
                        kill += 1
                        kill_tot += 1
                        kill_rall += 1 
# rallentamento
    if kill_rall >= 10:
        py.draw.rect(screen,RED,(980,830,70,70))
        rallentamento = True
        nRallentamenti += 1
# nuke
    if kill_tot == 25:
        kill_tot = 0
        nuke = True
        nNuke += 1
    
    if nuke:
        if countdown <= 0:
            countdown -= 0
        else:
            countdown -= 1
        # scritta nuke 
        text_nuke = font_nuke.render(str('VACCINO TRA: '),True,(0,0,0))
        screen.blit(text_nuke,(250,200))
        # countdown
        text_countdown = font_nuke.render(str(countdown // 60), True,(0,0,0))
        screen.blit(text_countdown,(800,450))
        if countdown == 0:
            screen.fill(L_GREY)
            personaggio.draw(screen)
            for nemico in nemico_list:
                nemico_list.remove(nemico)
                kill += 1  
            bullet_counter.draw()
            barra_info()
            for i in range(n_nemici):
                nemico_list.append(Nemico(x,50,100,L_GREEN,100))
            for nemico in nemico_list:
                nemico.draw(screen)
            countdown = 240
            nuke = False

# EVENTI DA TASTIERA
    for event in py.event.get():
        if event.type == py.QUIT:
            quit()

        elif event.type == py.KEYDOWN:
            if event.key == py.K_w:
                if y_personaggio <= 166:
                    y_personaggio += 0
                else:
                    y_personaggio -= 166
            if event.key == py.K_s:
                if y_personaggio >= 664:
                    y_personaggio += 0
                else:
                    y_personaggio += 166
            if event.key == py.K_SPACE:
                if len(bullet_list) < 5:
                    danno_proiettile = randint(48,60)
                    bullet_list.append(Proiettile(x_proiettile,y_proiettile,30,10,GREY,danno_proiettile))
                    n_colpi -= 1
            if event.key == py.K_e and rallentamento == True:
                tempo_rall -= 60
                for nemico in nemico_list:
                    nemico.speed = 0.5
                    if tempo_rall <= 0:
                        for nemico in nemico_list:
                            nemico.speed = randint(1,3)
                kill_rall = 0
                rallentamento = False

    for bullet in bullet_list:
        bullet.draw(screen)

    py.display.update()

# SCHERMATA DI FINE GIOCO
font_fine = py.font.SysFont('Chiller', 300)

fine = True
screen.fill(BLACK)
while fine:
    clock.tick(20)

    for event in py.event.get():
        if event.type == py.QUIT:
            fine = False

    if haiVinto == True:
        text_haiVinto = font_fine.render(str('HAI VINTO'),True,(ORANGE))
        screen.blit(text_haiVinto,(300,300))
        partiteVinte += 1
        haiVinto = False
    elif haiPerso == True:
        text_haiVinto = font_fine.render(str('HAI PERSO'),True,(ORANGE))
        screen.blit(text_haiVinto,(300,300))
        partitePerse += 1
        haiPerso = False

    py.display.update()
