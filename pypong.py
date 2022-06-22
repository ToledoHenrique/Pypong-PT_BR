import pygame
import sys

# INICIALIZAR PYGAME
jogador1 = input("Nome do jogador1: ")
jogador2 = input("Nome do jogador2: ")
email = input("Email de um dos jogadores: ")
open('historico.txt','a').write(f'Email{email}  |   GJogadores {jogador1} |  {jogador2}\n----------------------------------------------------------------------------------------------------------------\n')




pygame.init()

# TELA
LARGURA, ALTURA = 1500, 1000
VENCER = pygame.display.set_mode((LARGURA, ALTURA))
NOMEDAJANELA = "Ping Pong"
pygame.display.set_caption(NOMEDAJANELA)

# CORES
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)
AMARELO = (255, 255, 0)
ROXO = (128, 0, 128)
LARANJA = (255, 165, 0)
CINZA = (128, 128, 128)

lacuna = 10
# LIMITES DA TELA
borda_direita = ((lacuna, lacuna), (lacuna, ALTURA - lacuna))
borda_esquerda =  ((LARGURA - lacuna, lacuna), (LARGURA - lacuna, ALTURA - lacuna))
base = ((lacuna, ALTURA - lacuna), (LARGURA - lacuna, ALTURA - lacuna))
topo = ((lacuna, lacuna), (LARGURA - lacuna, lacuna))
# TAMANHO RAQUETE
raquete_largura = 20
raquete_altura = 100
# POSIÇÃO INICIAL 
raquete1_posx = borda_direita[0][0] + lacuna
raquete1_posy = borda_direita[0][1] + ALTURA / 2
raquete2_posx = borda_esquerda[0][0] - raquete_largura - lacuna
raquete2_posy =  borda_esquerda[0][1] + ALTURA / 2
# PONTUAÇÃO
raquete1_score = 0
raquete2_score = 0
# FONTES
SCORE_FONT = pygame.font.SysFont("comicsans", 45)
VENCER_FONT = pygame.font.SysFont("comicsans", 60)
# BOLA
velocidade_bolax = 8
velocidade_bolay = 8
largura_da_bola = 15
altura_da_bola = 15
velocidade_da_bola = [velocidade_bolay, velocidade_bolax]
bola_posx = (topo[1][0] - topo[0][0]) / 2 - largura_da_bola
bola_posy = (ALTURA - 15) / 2
bola_topo = bola_posy
bola_base = bola_posy + altura_da_bola
bola_direita = bola_posx
bola_esquerda = bola_posx + largura_da_bola
# VELOCIDADE DO PLAYER
velocidade_da_raquete = 12
pingpong = pygame.mixer.Sound("sounds/Ping.wav") 
pontução = 0 




def cria_borda(superfice):
    # BORDA DO CAMPO
    pygame.draw.line(superfice, BRANCO, borda_direita[0], borda_direita[1])
    pygame.draw.line(superfice, BRANCO, topo[0], topo[1])
    pygame.draw.line(superfice, BRANCO, borda_esquerda[0], borda_esquerda[1])
    pygame.draw.line(superfice, BRANCO, base[0], base[1])
    

def cria_raquetes(superfice, pos_x, pos_y):
    raquete1 = pygame.draw.rect(superfice, BRANCO, (pos_x, pos_y, raquete_largura, raquete_altura))
    raquete2 = pygame.draw.rect(superfice, BRANCO, (pos_x, pos_y, raquete_largura, raquete_altura))

def cria_meio(superfice):
    inicia_posicao_meio = topo[0][1] 
    posicao_meio = (topo[1][0] - topo[0][0]) / 2
    termina_posicao_meio = base[0][1]
    borda_potuacao = base[0][1] - topo[0][1] + 5
    pygame.draw.line(superfice, BRANCO, (posicao_meio, inicia_posicao_meio), (posicao_meio, termina_posicao_meio))
    for i in range(10, int(borda_potuacao)):
        if i % 10 == 0:
            j = i
        pygame.draw.rect(superfice, PRETO, (posicao_meio, j, 10, 5))

def cria_bola(superfice, posx, posy, largura, altura):
    pygame.draw.circle(superfice, VERDE, 
    [posx, posy], largura, altura)

def placar(superfice):
    pontos1 = SCORE_FONT.render(f"{jogador1}: {str(raquete1_score)}", 1, BRANCO)
    pontos2 = SCORE_FONT.render(f"{jogador2}: {str(raquete2_score)}",  1, BRANCO)
    superfice.blit(pontos1, (borda_direita[0][0] + 50, borda_direita[0][1] + 20))
    superfice.blit(pontos2, (borda_esquerda[0][0] - pontos1.get_width() - 50, borda_esquerda[0][1] + 20))

def empate(superfice):
    empate = VENCER_FONT.render(f"Empate.",  1, BRANCO)
    superfice.blit(empate, (LARGURA / 2 - (empate.get_width() / 2), (ALTURA / 2 - (empate.get_height() / 2))))
    pygame.display.update()
    pygame.time.delay(2500)

def tela_vencedor(superfice, jogador, jogador_pontos):
    global topo, raquete1_score, raquete2_score

    vencedor = VENCER_FONT.render(f"{str(jogador)} Ganhou!!",  1, BRANCO)
    score_vencedor = SCORE_FONT.render(f"Pontuação: {str(jogador_pontos)}", 1, BRANCO)
    superfice.blit(vencedor, (LARGURA / 2 - (vencedor.get_width() / 2), (ALTURA / 2 - (vencedor.get_height() / 2))))
    superfice.blit(score_vencedor, (LARGURA / 2 - (vencedor.get_width() / 3) + 25, (ALTURA / 2 - (score_vencedor.get_height() / 2) + vencedor.get_height() + 10)))
    pygame.display.update()
    pygame.time.delay(2500)

def cria_janela_jogo(superfice):
    # FUNDO DA TELA
    superfice.fill(PRETO)
    cria_raquetes(superfice, raquete1_posx, raquete1_posy)
    cria_raquetes(superfice, raquete2_posx, raquete2_posy)
    cria_meio(superfice)
    cria_borda(superfice)
    cria_bola(superfice, bola_posx, bola_posy, largura_da_bola, altura_da_bola)
    placar(superfice)
    pygame.display.update()

def inicia_jogo(superfice):
    global raquete1_posy, raquete2_posy, bola_posx, bola_posy, largura_da_bola, velocidade_da_bola, raquete1_score, raquete2_score, score1_text, score2_text

    run = True
    clock = pygame.time.Clock()
    FPS = 60
    
    while run:
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                superfice.fill(PRETO)
                if raquete1_score > raquete2_score:
                    tela_vencedor(superfice, jogador1, raquete1_score)
                elif raquete1_score == raquete2_score:
                    empate(superfice)
                else:
                    tela_vencedor(superfice, jogador2, raquete2_score)
                run = False
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN] and raquete2_posy < base[0][1] - raquete_altura - lacuna:
            raquete2_posy += velocidade_da_raquete
        if keys[pygame.K_UP] and raquete2_posy > topo[0][1] + lacuna:
            raquete2_posy -= velocidade_da_raquete            
        if keys[pygame.K_w] and raquete1_posy > topo[0][1] + lacuna:
            raquete1_posy -= velocidade_da_raquete      
        if keys[pygame.K_s] and raquete1_posy < base[0][1] - raquete_altura - lacuna:
            raquete1_posy += velocidade_da_raquete

        bola_posx += velocidade_da_bola[0]
        bola_posy += velocidade_da_bola[1]

        if bola_posx + largura_da_bola >= borda_esquerda[0][0] - lacuna:
            bola_posx = (topo[1][0] - topo[0][0]) / 2 - largura_da_bola
            bola_posy = (ALTURA - 20) / 2
            raquete2_posy = (ALTURA - 20) / 2
            raquete1_posy = (ALTURA - 20) / 2
            pygame.time.delay(500)
            raquete1_score += 1
            print(f"{jogador1} pontuou \n {jogador1} pontos: {raquete1_score}")

        if bola_posx <= borda_direita[0][0] + lacuna:
            bola_posx = (topo[1][0] - topo[0][0]) / 2 - largura_da_bola
            bola_posy = (ALTURA - 20) / 2
            raquete2_posy = (ALTURA - 20) / 2
            raquete1_posy = (ALTURA - 20) / 2
            pygame.time.delay(500)
            raquete2_score += 1
            print(f"{jogador2} pontuou \n {jogador2} pontos: {raquete2_score}")

        # TOQUE DA BOLA NO BASE
        if bola_posy + altura_da_bola >= base[0][1] - lacuna:
            velocidade_da_bola[1] *= -1       
        # TOQUE DA BOLA NO TOPO
        if bola_posy <= topo[0][1] + lacuna:
            velocidade_da_bola[1] *= -1
        # TOQUE DA BOLA NA RAQUETE2
        if bola_posy >= raquete2_posy and bola_posy < raquete2_posy + raquete_altura and bola_posx + largura_da_bola >= raquete2_posx:
            velocidade_da_bola[0] *= -1
            pingpong.play()        
        # TOQUE DA BOLA NA RAQUETE1
        elif bola_posy >= raquete1_posy and bola_posy < raquete1_posy + raquete_altura and bola_posx <= raquete1_posx + raquete_largura:
            velocidade_da_bola[0] *= -1
            pingpong.play()
            

        cria_janela_jogo(superfice)   
        
inicia_jogo(VENCER)
pygame.quit()