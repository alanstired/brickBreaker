from tkinter import *
from time import sleep
from random import randint

window = Tk()
window.title("Brick Breaker")

cvs = Canvas(window, height = 600, width = 800, bg='black')
cvs.pack()

ball_r = 5
ball_speed_x = 3
ball_speed_y = 3
ball = cvs.create_oval(20,20,35,35, fill='white')

bar_width = 200
bar_height = 6
bar = cvs.create_rectangle(0, 500 - bar_height,
                           bar_width, 500,
                           fill = 'white')

brick = []
brick_status = []
brick_width = 56
brick_height = 4
brick_gap = 4
brick_color = ['red','white','blue']
for i in range(0,10):
    for j in range(0,30):
        x = 100 + i*(brick_width + brick_gap)
        y = 50 + j*(brick_height + brick_gap)
        color = brick_color[(j % 6)//2]
        brick_id = cvs.create_rectangle(x-brick_width//2,
                                        y-brick_height//2,
                                        x+brick_width//2,
                                        y+brick_height//2,
                                        fill=color)
        
        brick.append(brick_id)
        brick_status.append(0)
score = 0
score_text = cvs.create_text(600,550,text = 'Score: 0',font=('Arial Rounded MT',20),fill='white')
def get_pos(id):
    pos = cvs.coords(id)
    x = (pos[0]+pos[2])/2
    y = (pos[1]+pos[3])/2
    return x,y

def move_ball():
    global ball_speed_x, ball_speed_y
    cvs.move(ball, ball_speed_x, ball_speed_y)

def det_wall_collision():
    global ball_speed_x, ball_speed_y
    x,y = get_pos(ball)
    if (y >= 600):
        cvs.create_text(400,300,text = 'Game Over!',font=('Arial Rounded MT',80),fill='White')

    if (y <= 0):
        ball_speed_y = 3
    if (x >= 800):
        ball_speed_x = -3
    if (x <= 0):
        ball_speed_x = 3
def det_paddle_collision():
    global ball_speed_x, ball_speed_y
    x,y = get_pos(ball)
    pos_paddle = cvs.coords(bar)
    if (x >= pos_paddle[0] and
            x <= pos_paddle[2] and
            y >= pos_paddle[1] and
            y <= pos_paddle[3]):
                   ball_speed_y = -ball_speed_y
def det_ball_brick_collision():
    global ball_speed_x, ball_speed_y,score
    x,y = get_pos(ball)
    for i in range(len(brick)-1,-1,-1):
        if (brick_status[i] > 0):
            continue
        pos_brick = cvs.coords(brick[i])
        if (x >= pos_brick[0] and
            x <= pos_brick[2] and
            y >= pos_brick[1] and
            y <= pos_brick[3]):
                   ball_speed_y = -ball_speed_y
                   brick_status[i] = 1
                   score = score + 1
                   cvs.itemconfig(score_text, text = 'Score: ' + str(score))
def update_brick_shrink():
    for i in range(len(brick)-1,-1,-1):
        if (brick_status[i] > 10):
            cvs.delete(brick[i])
            del brick [i]
            del brick_status[i]
        elif (brick_status[i] > 0):
            x,y = get_pos(brick[i])
            width = (10-brick_status[i])*4
            cvs.coords(brick[i],x-width//2,y-brick_height//2,x+width//2, y+brick_height//2)
            brick_status[i] = brick_status[i] + 1
def key_press(event):
    print(event.keysym)
    if (event.keysym == 'Left'):
        cvs.move(bar,-20,0)
    elif (event.keysym == 'Right'):
        cvs.move(bar,20,0)

cvs.bind_all('<Key>',key_press)

while(True):
    sleep(0.01)
    move_ball()
    det_wall_collision()
    
    det_ball_brick_collision()
    det_paddle_collision()
    update_brick_shrink()
    window.update()
    
