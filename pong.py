# jogo simples de ping-pong

import turtle
import os

# janela principal
window = turtle.Screen()
window.title("Ping-Pong / @paulo-sk")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# palyer a
player_a = turtle.Turtle()
player_a.speed(0) # velocida da animacao
player_a.shape('square')
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.color('green')
player_a.penup() # para nao desenha a linha enquanto se move
player_a.goto(-350, 0)

# player b
player_b = turtle.Turtle()
player_b.speed(0) # velocida da animacao
player_b.shape('square')
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.color('red')
player_b.penup() # para nao desenha a linha enquanto se move
player_b.goto(350, 0)

# bola
bola = turtle.Turtle()
bola.speed(0) # velocida da animacao
bola.shape('circle')
bola.color('white')
bola.penup() # para nao desenha a linha enquanto se move
bola.goto(0, 0)
# bola quando se mover, vai ser 2 pixel para cima ou para baixo
bola.dx = 0.3
bola.dy = 0.3


# placar
placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Player_A: 0    Player_B: 0", align="center", font=("Courier", 24, 'normal'))


# score
score_player_a = 0
score_player_b = 0

# funcoes player a
def player_a_sobe():
    y = player_a.ycor()
    y += 25
    player_a.sety(y)


def player_a_desce():
    y = player_a.ycor()
    y -= 25
    player_a.sety(y)

# funcoes player b
def player_b_sobe():
    y = player_b.ycor()
    y += 20
    player_b.sety(y)


def player_b_desce():
    y = player_b.ycor()
    y -= 20
    player_b.sety(y)

# keyboard bind
window.listen()
window.onkeypress(player_a_sobe, "w")
window.onkeypress(player_a_desce, "s")

window.onkeypress(player_b_sobe, "Up")
window.onkeypress(player_b_desce, "Down")


# Loop principal
while True:
    window.update()

    # mover a bola
    # esses metodos significam: "colocar a posicao da bola a partir da atual + distancia bola.dx ou dy, que é de 2 pixels"
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # borda do da janela para bola nao sair
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    elif bola.ycor() < -290:
        bola.setx(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        score_player_a += 1
        placar.clear()
        placar.write(f"Player_A: {score_player_a}    Player_B: {score_player_b}", align="center", font=("Courier", 24, 'normal'))
        bola.goto(0, 0)
        bola.dx *= -1 
    
    elif bola.xcor() < -390:
        score_player_b += 1
        placar.clear()
        placar.write(f"Player_A: {score_player_a}    Player_B: {score_player_b}", align="center", font=("Courier", 24, 'normal'))
        bola.goto(0, 0)
        bola.dx *= -1 
    
    # colisao da bola com players
    # bolca colide com player A
    if bola.xcor() < -335 and bola.ycor() < player_a.ycor() + 50 and bola.ycor() > player_a.ycor() - 50:
        bola.dx *= -1 
        
    # bolca colide com player B
    if bola.xcor() > 335 and bola.ycor() < player_b.ycor() + 50 and bola.ycor() > player_b.ycor() - 50:
        bola.dx *= -1 

    # finalizar jogo   
    # player A vence
    if score_player_a == 10:
        placar.clear()
        placar.goto(0, 0)
        placar.write(f"Fim de jogo, vencedor: Player A", align="center", font=("Courier", 24, 'normal'))
        if bola.xcor() < -335 and bola.ycor() < player_a.ycor() + 50 and bola.ycor() > player_a.ycor() - 50 or bola.xcor() < -350:
            break 

    # player B vence
    if score_player_b == 10:
        placar.clear()
        placar.goto(0, 0)
        placar.write(f"Fim de jogo, vencedor: Player B", align="center", font=("Courier", 24, 'normal'))
        if bola.xcor() > 335 and bola.ycor() < player_b.ycor() + 50 and bola.ycor() > player_b.ycor() - 50 or bola.xcor() > 350:
            break   