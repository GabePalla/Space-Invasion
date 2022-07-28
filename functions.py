import random

def status_hitbox(varRandomX, varRandomY, complementoY, tiroX, tiroY):
    posicaoComprimentoX = varRandomX + 44
    posicaoAtualizadaY = varRandomY + complementoY
    posicaoLarguraAtualizadaY = posicaoAtualizadaY + 36
    comprimentoLaserX = tiroX + 15
    larguraLaserY = tiroY + 9
    status_hitBox = True

    if(((tiroX < varRandomX and varRandomX <comprimentoLaserX) or
        (tiroX < posicaoComprimentoX and posicaoComprimentoX < comprimentoLaserX) or
        (varRandomX < tiroX and tiroX < posicaoComprimentoX and comprimentoLaserX < posicaoComprimentoX)) and
        (posicaoAtualizadaY < tiroY and tiroY < posicaoLarguraAtualizadaY and posicaoLarguraAtualizadaY < larguraLaserY)):
            status_hitBox = False

    return status_hitBox, posicaoAtualizadaY

#------------------------------------------------------------------------------------------------------------------------------------

def enemies_image(gameDisplayInimigo, imagem, varRandomX, varRandomY, complementoY):
    gameDisplayInimigo.blit(imagem, (varRandomX, varRandomY + complementoY))

#------------------------------------------------------------------------------------------------------------------------------------

def enemies_generator(lista_random):
    while(len(lista_random) != 10):
        varRandomX = random.randrange(0,750)
        varRandomY = random.randrange(-50, -10)
        lista_random.append(varRandomX)
        lista_random.append(varRandomY)
    return lista_random

def enemies_status(lista_status ,lista_random,statusInimigoAcertos, statusInimigosDerrota, tiroX):
    if(lista_status[0][0] == False):
        lista_random[0] = -50
        lista_random[1] = -50
        tiroX = -50
        statusInimigoAcertos = True
    elif(lista_status[0][1] > 600 and lista_status[0][1] < 602):
        statusInimigosDerrota = True

    if(lista_status[1][0] == False):
        lista_random[2] = -50
        lista_random[3] = -50
        tiroX = -50       
        statusInimigoAcertos = True
    elif(lista_status[1][1] > 600 and lista_status[1][1] < 602):
        statusInimigosDerrota = True

    if(lista_status[2][0] == False):
        lista_random[4] = -50
        lista_random[5] = -50
        tiroX = -50
        statusInimigoAcertos = True
    elif(lista_status[2][1] > 600 and lista_status[2][1] < 602):
        statusInimigosDerrota = True

    if(lista_status[3][0] == False):
        lista_random[6] = -50
        lista_random[7] = -50
        tiroX = -50        
        statusInimigoAcertos = True
    elif(lista_status[3][1] > 600 and lista_status[3][1] < 602):
        statusInimigosDerrota = True
        
    if(lista_status[4][0] == False):
        lista_random[8] = -50
        lista_random[9] = -50
        tiroX = -50       
        statusInimigoAcertos = True
    elif(lista_status[4][1] > 600 and lista_status[4][1] < 602):
        statusInimigosDerrota = True

    return statusInimigoAcertos, statusInimigosDerrota, tiroX






        