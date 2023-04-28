import tkinter as tk
import random
import time


class Ball:
    def __init__(self, canvas, paddle,score, color,):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 20, 20, fill=color)
        self.canvas.move(self.id, 240, 100)
        starts = [-2,-1,1,2]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False





    def draw(self,):
        self.canvas.move(self.id, self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(400, 400, text =(f'Вы проиграли:{self.score.score}'), font=('Arial', 15), fill = 'red')
        if self.hit_paddle(pos):
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3






    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<= paddle_pos[3]:
                self.score.hit()

                return True
        return False



class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 400, 700)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Right>',self.turnright)
        self.canvas.bind_all('<KeyPress-Left>', self.turnleft)


    def draw(self):
        self.canvas.move(self.id,self.x,0)
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x = 0
        elif pos[2]>=self.canvas_width:
            self.x=0

    def turnright(self,event ):
        self.x =+3

    def turnleft(self,event):
        self.x=-3


class Score:
    def __init__(self,canvas,color):
        self.score =0
        self.canvas = canvas
        self.id = canvas.create_text(700, 10, text =(f'Ваш текщий счет:{self.score}'), font=('Arial', 15), fill = color)
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text =(f'Ваш текщий счет:{self.score}'))






root = tk.Tk()
root.title("Арканоид ")
root.wm_attributes('-topmost', 1)  # топмост фиксирует положение окна
root.resizable(0, 0)



canvas = tk.Canvas(root, width=800, height=800, bg='white', bd=0, highlightthickness=0)
canvas.pack()
root.update()
score = Score(canvas,'red',)
paddle = Paddle(canvas,"black")
ball = Ball(canvas,paddle,score,'red')






while True:
    if not ball.hit_bottom:


        ball.draw()
        paddle.draw()
    else:
        break

    root.update_idletasks()
    root.update()
    time.sleep(0.01)

time.sleep(3)