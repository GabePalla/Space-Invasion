import pygame, functions, time

pygame.init()
pygame.font.init()

displayEixoX = 800
displayEixoY = 600

colorBackGorund = (255, 255, 255)
movimentoX = 0
posicaoX = 0
posicaoY = 0

triger = False
tiroY = -11
tiroX = -50
status_shoot = True

complementoY = 0
contadorInimigosDerrota = 0
contadorInimigoAcertos = 0
statusInimigoAcertos = False
statusInimigosDerrota = False
velocidadeInimigo = 1

lista_random = []
lista_status = []
lista_random = functions.enemies_generator(lista_random)

gameDisplay = pygame.display.set_mode((displayEixoX, displayEixoY))
clock = pygame.time.Clock()
mainCharacter = pygame.image.load('assets\Beholder\Beholder.png')
background = pygame.image.load('assets\Large 1024x1024\Purple Nebula\Purple Nebula 4 - 1024x1024.png')
shoot = pygame.image.load('assets\Beholder\BeholderBullets.png')
imagem_inimigo = pygame.image.load('assets\Emissary\Emissary.png')
fonteTexto = pygame.font.SysFont(None, 25)
laserSound = pygame.mixer.Sound('assets\laser.mp3')
pygame.mixer.music.load('assets\CrashLanding.mp3')
pygame.mixer.music.play(-2)

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_a):
                movimentoX = -5
            elif(event.key == pygame.K_d):
                movimentoX = 5
            if(event.key == pygame.K_m):
                triger = True 
        elif(event.type == pygame.KEYUP):
            if(event.key == pygame.K_a or event.key == pygame.K_d):
                movimentoX = 0
    
    gameDisplay.blit(background, (0, 0))
    
    posicaoX += movimentoX

    if(posicaoX < 0):
        posicaoX = 0
    elif(posicaoX > 750):
        posicaoX = 750

    if(triger == True and tiroY < 0):
        pygame.mixer.Sound.play(laserSound)   
        tiroX = posicaoX + 14
        tiroY = 550
        triger = False

    if(tiroY > -10):
        tiroY -= 10
    else:
        tiroY = -11

    complementoY += 1

    gameDisplay.blit(background, (0, 0))
    text = fonteTexto.render(f'ALVOS ABATIDOS: {contadorInimigoAcertos}', True, (255, 255, 255))
    gameDisplay.blit(text,(600, 25))


    gameDisplay.blit(shoot, (tiroX, tiroY))       
    
    status_estado1 = functions.status_hitbox(lista_random[0], lista_random[1], complementoY, tiroX, tiroY)
    status_estado2 = functions.status_hitbox(lista_random[2], lista_random[3], complementoY, tiroX, tiroY)
    status_estado3 = functions.status_hitbox(lista_random[4], lista_random[5], complementoY, tiroX, tiroY)
    status_estado4 = functions.status_hitbox(lista_random[6], lista_random[7], complementoY, tiroX, tiroY)
    status_estado5 = functions.status_hitbox(lista_random[8], lista_random[9], complementoY, tiroX, tiroY)
    lista_status.clear()
    lista_status.append(status_estado1)
    lista_status.append(status_estado2)
    lista_status.append(status_estado3)
    lista_status.append(status_estado4)
    lista_status.append(status_estado5)

    functions.enemies_image(gameDisplay, imagem_inimigo, lista_random[0], lista_random[1], complementoY)
    functions.enemies_image(gameDisplay, imagem_inimigo, lista_random[2], lista_random[3], complementoY)
    functions.enemies_image(gameDisplay, imagem_inimigo, lista_random[4], lista_random[5], complementoY)
    functions.enemies_image(gameDisplay, imagem_inimigo, lista_random[6], lista_random[7], complementoY)
    functions.enemies_image(gameDisplay, imagem_inimigo, lista_random[8], lista_random[9], complementoY)

    status_enemies = functions.enemies_status(lista_status, lista_random, statusInimigoAcertos, statusInimigosDerrota, tiroX)

    if(status_enemies[0] == True):
        contadorInimigoAcertos += 1
        tiroX = status_enemies[2]
    if(status_enemies[1] == True):
        contadorInimigosDerrota += 1

    if(contadorInimigosDerrota > 10):
        gameDisplay.blit(background, (0, 0))
        text2 = fonteTexto.render('A TERRA FOI CONQUISTADA PELOS INVASORES', True, (255, 255, 255))
        gameDisplay.blit(text2,(190, 300))
        pygame.display.update()
        time.sleep(3)
        break
    elif(contadorInimigoAcertos > 20):
        gameDisplay.blit(background, (0, 0))
        text = fonteTexto.render('PARABÉNS!!!!!', True, (255, 255, 255))
        text2 = fonteTexto.render('VOCÊ SALVOU A TERRA DOS INVASORES DO ESPAÇO', True, (255, 255, 255))
        gameDisplay.blit(text,(320, 295))
        gameDisplay.blit(text2,(170, 315))
        pygame.display.update()
        time.sleep(3)
        break

    if(complementoY > 700):
        if(len(lista_random) == 10):
            lista_random.clear()
        lista_random = functions.enemies_generator(lista_random)
        complementoY = 0

    gameDisplay.blit(mainCharacter, (posicaoX, 550))
    pygame.display.update()
    clock.tick(60)