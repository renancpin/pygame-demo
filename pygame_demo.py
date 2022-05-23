import pygame
from random import randint

pygame.init()
tela = pygame.display.set_mode([600,600])

fim = False

timer = pygame.time.Clock()

ret = pygame.Rect(int(tela.get_width()/2 - 20),int(tela.get_height()*3/4),40,40)
alvos = []

for i in range(5):
    alvos.append(pygame.Rect(randint(0,tela.get_width()-40),randint(0,80),40,20))

def atirar(ret):
    return pygame.Rect(int(ret.x + ret.width/2 - 3), ret.y, 6, 10)

raios = []
rgb = (randint(1,255),randint(1,255),randint(1,255))
sumir = False

while not fim:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                raios.append(atirar(ret))
    
    tela.fill((255,255,255))
    timer.tick(30)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        if ret.x > 0:
            ret.x -= 5
    elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        if ret.x < tela.get_width() - ret.width:
            ret.x += 5
    if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
        if ret.y > 0:
            ret.y -= 5
    elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
        if ret.y < tela.get_height() - ret.height:
            ret.y += 5
    
    r = min(255, 80 * len(raios))
    g = 120 * (len(raios)-5)
    if g > 255:
        g = 255
    elif g < 0:
        g = 0
    b = 100 * (len(raios)-6)
    if b > 255:
        b = 255
    elif b < 0:
        b = 0
    rgb = (r,g,b)
    
    i = 0
    
    while i < len(raios):
        if raios[i].y -10 > 0:
            prox = False
            
            raios[i].y -= 10
            for alvo in alvos:
                if alvo.colliderect(raios[i]):
                    alvos.remove(alvo)
                    prox = True

            if prox:
                raios.pop(i)
                continue
            else:
                pygame.draw.rect(tela,(0,0,0),raios[i])
                
            i+=1
        else:
            raios.pop(i)
    
    if len(raios) > 6:
        aura1 = pygame.Rect(ret.x-1*(len(raios)-6),ret.y-1*(len(raios)-6),ret.width+2*(len(raios)-6),ret.height+2*(len(raios)-6))
        if len(raios) > 8:
            aura2 = pygame.Rect(aura1.x-1*(len(raios)-6),aura1.y-1*(len(raios)-6),aura1.width+2*(len(raios)-6),aura1.height+2*(len(raios)-6))
            if len(raios) > 10:
                aura3 = pygame.Rect(aura2.x-1*(len(raios)-6),aura2.y-1*(len(raios)-6),aura2.width+2*(len(raios)-6),aura2.height+2*(len(raios)-6))
                pygame.draw.rect(tela,(b-50,b-50,b),aura3)
            pygame.draw.rect(tela,(b-100,b-100,b),aura2)
        pygame.draw.rect(tela,(0,0,b),aura1)

    for alvo in alvos:
        pygame.draw.rect(tela,(0,0,0),alvo)
    pygame.draw.rect(tela,rgb,ret)
    pygame.display.update()
    
pygame.quit()
