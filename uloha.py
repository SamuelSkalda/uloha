#uloha1
'''
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def kresli(event):
    x = event.x
    y = event.y
    meno=entry1.get()
    canvas.create_rectangle(x-15,y-15,x+15,y+15)
    canvas.create_text(x,y+20,text=meno,font='Arial 10 bold')

entry1 = tkinter.Entry()
entry1.pack()
canvas.bind('<Button-1>',kresli)
'''

#uloha2
'''
import tkinter
canvas=tkinter.Canvas(width=600,height=500,bg='white')
canvas.pack()

canvas.create_rectangle(0,350,600,500,fill='blue')

def obrazky(suradnice):
    x=suradnice.x
    y=suradnice.y
    if y<350:
        canvas.create_rectangle(x-10,y,x+10,y-20)
        canvas.create_line(x,y-20,x-10,y-40,x+10,y-40,x,y-20)
        canvas.create_oval(x-10,y-30,x+10,y-50,fill='white')
    else:
        canvas.create_line(x,y-10,x,y-30,x+10,y-20,x,y-15)

canvas.bind('<Button-1>', obrazky)
'''

#uloha3
'''
import tkinter
import random
canvas = tkinter.Canvas(height=300, width=300, bg="white")
canvas.pack()

def vypis_body(pocet_bodov):
    canvas.create_text(100,10,text='Počet získaných bodov:')
    canvas.create_text(200,10,text=pocet_bodov)
    
kocka1= random.randrange(1,7)
kocka2= random.randrange(1,6)
def kocky():
    global pocet_bodov, kocka1, kocka2
    canvas.delete('all')
    kocka1 = random.randrange(1,7)
    kocka2 = random.randrange(1,7)
    if kocka1 == 1:
        canvas.create_rectangle(50,50,100,100,fill='white',width=3)
        canvas.create_oval(70,70,80,80,fill='black')
    elif kocka1 == 2:
        canvas.create_rectangle(50,50,100,100,fill='white',width=3)
        canvas.create_oval(60,60,70,70,fill='black')
        canvas.create_oval(90,90,80,80,fill='black')
    elif kocka1 == 3:
        canvas.create_rectangle(50,50,100,100,fill='white',width=3)
        canvas.create_oval(60,60,70,70,fill='black')
        canvas.create_oval(90,90,80,80,fill='black')
        canvas.create_oval(70,70,80,80,fill='black')
    elif kocka1 == 4:
        canvas.create_rectangle(50,50,100,100,fill='white',width=3)
        canvas.create_oval(60,60,70,70,fill='black')
        canvas.create_oval(90,60,80,70,fill='black')
        canvas.create_oval(90,90,80,80,fill='black')
        canvas.create_oval(60,90,70,80,fill='black')
    elif kocka1 == 5:
        canvas.create_rectangle(50,50,100,100,fill='white',width=3)
        canvas.create_oval(70,70,80,80,fill='black')
        canvas.create_oval(60,60,70,70,fill='black')
        canvas.create_oval(90,60,80,70,fill='black')
        canvas.create_oval(90,90,80,80,fill='black')
        canvas.create_oval(60,90,70,80,fill='black')
    else:
        canvas.create_rectangle(50,50,100,100,fill='white',width=3)
        canvas.create_oval(60,55,70,65,fill='black')
        canvas.create_oval(90,55,80,65,fill='black')
        canvas.create_oval(90,95,80,85,fill='black')
        canvas.create_oval(60,95,70,85,fill='black')
        canvas.create_oval(60,70,70,80,fill='black')
        canvas.create_oval(90,70,80,80,fill='black')
        
    if kocka2 == 1:
        canvas.create_rectangle(200,50,250,100,fill='white',width=3)
        canvas.create_oval(220,70,230,80,fill='black')
    elif kocka2 == 2:
        canvas.create_rectangle(200,50,250,100,fill='white',width=3)
        canvas.create_oval(210,60,220,70,fill='black')
        canvas.create_oval(240,90,230,80,fill='black')
    elif kocka2 == 3:
        canvas.create_rectangle(200,50,250,100,fill='white',width=3)
        canvas.create_oval(210,60,220,70,fill='black')
        canvas.create_oval(240,90,230,80,fill='black')
        canvas.create_oval(220,70,230,80,fill='black')
    elif kocka2 == 4:
        canvas.create_rectangle(200,50,250,100,fill='white',width=3)
        canvas.create_oval(210,60,220,70,fill='black')
        canvas.create_oval(240,60,230,70,fill='black')
        canvas.create_oval(240,90,230,80,fill='black')
        canvas.create_oval(210,90,220,80,fill='black')
    elif kocka2 == 5:
        canvas.create_rectangle(200,50,250,100,fill='white',width=3)
        canvas.create_oval(220,70,230,80,fill='black')
        canvas.create_oval(210,60,220,70,fill='black')
        canvas.create_oval(240,60,230,70,fill='black')
        canvas.create_oval(240,90,230,80,fill='black')
        canvas.create_oval(210,90,220,80,fill='black')
    else:
        canvas.create_rectangle(200,50,250,100,fill='white',width=3)
        canvas.create_oval(210,55,220,65,fill='black')
        canvas.create_oval(240,55,230,65,fill='black')
        canvas.create_oval(240,95,230,85,fill='black')
        canvas.create_oval(210,95,220,85,fill='black')
        canvas.create_oval(210,70,220,80,fill='black')
        canvas.create_oval(240,70,230,80,fill='black')
    vypis_body(pocet_bodov)
    canvas.after(1000, kocky)
    print(kocka1,kocka2)
'''

#uloha4
'''
import tkinter
import random
canvas = tkinter.Canvas(bg="white",height=410)
canvas.pack()

uhol = random.randrange(10,90)
u = random.randrange(0,50)
farba = random.choice(("blue", "red", "yellow", "green", "orange", "black", "brown", "pink"))
def zmaz(suradnice):
    x=suradnice.x
    y=suradnice.y
    canvas.delete('all')
    
def setric():
    canvas.delete('all')
    uhol = random.randrange(10,90)
    u = random.randrange(10,90)
    farba = random.choice(("blue", "red", "yellow", "green", "orange", "black", "brown", "pink"))
    canvas.create_text(random.randrange(0,400),random.randrange(10,380),text=entry1.get(),fill=farba,angle=uhol+u)
    canvas.after(1000,setric)

entry1 = tkinter.Entry()
entry1.pack()

setric()

canvas.bind('<Button1>',zmaz)
'''

#uloha5
'''
import tkinter
import random
canvas = tkinter.Canvas(height=300, width=300, bg="white")
canvas.pack()



svetla = random.randrange(0,300)
def semafor():
    global svetla
    canvas.delete("all")
    svetla = random.randrange(0,300)
    if 250 < svetla <=300:
        canvas.create_rectangle(10, 10, 65, 180,fill="black")
        canvas.create_oval(12,12,62,62,fill="red")
        canvas.create_oval(12,65,62,115,fill="yellow")
        canvas.create_oval(12,117,62,167,fill="green")
        
    if 200 < svetla <= 250:
        canvas.create_rectangle(10, 10, 65, 180,fill="black")
        canvas.create_oval(12,65,62,115,fill="yellow")
        canvas.create_oval(12,117,62,167,fill="green")
        
    if 150 < svetla <= 200:
        canvas.create_rectangle(10, 10, 65, 180,fill="black")
        canvas.create_oval(12,12,62,62,fill="red")
        canvas.create_oval(12,117,62,167,fill="yellow")
        
    if 100 < svetla <= 150:
        canvas.create_rectangle(10, 10, 65, 180,fill="black")
        canvas.create_oval(12,12,62,62,fill="red")
        canvas.create_oval(12,117,62,167,fill="green")
        
    if 50 < svetla <= 100:
        canvas.create_rectangle(10, 10, 65, 180,fill="black")
        canvas.create_oval(12,12,62,62,fill="red")
        
    if 30 < svetla <= 50:
        canvas.create_rectangle(10, 10, 65, 180,fill="black")
        canvas.create_oval(12,65,62,115,fill="yellow")
                
    if 0 < svetla <= 30:
        canvas.create_rectangle(10, 10, 65, 180,fill="black")
        canvas.create_oval(12,117,62,167,fill="green")
            

    canvas.after(100, semafor)

semafor()
'''

#uloha 6
'''
import tkinter
from random import *
canvas = tkinter.Canvas(bg='white', width=600, height=500)
canvas.pack()

x = 570
def titulky():
    global x
    canvas.delete('all')
    canvas.create_text(x,480,text=entry1.get(),fill="black")
    x-=10
    if x<-10:
        x=600
    canvas.after(100,titulky)

entry1 = tkinter.Entry()
entry1.pack()

titulky()
'''

#uloha 7
'''
import tkinter
import random
canvas=tkinter.Canvas()
canvas.pack()

kablik = random.randrange(1,5)
print(kablik)
sec = 61
k = 0
def odpocet():
    global k,sec,kablik 
    canvas.delete('all')
    sec-=1
    canvas.create_text(150,150,text=sec,font='Arial 20 bold',fill='red',tags='text')
    if sec > 0 and k!=kablik:
        canvas.after(1000, odpocet)
    elif sec == 0:
        canvas.delete('text')
        canvas.create_text(150,150,text='Bomba vybuchla',font='Arial 20 bold',fill='red')
    else:
        canvas.delete('text')
        canvas.create_text(150,150,text='Bombu si zneškodnil',font='Arial 20 bold',fill='green')
          
def cerveny():
    global k
    k=1
    
def modry():
    global k
    k=2

def zeleny():
    global k
    k=3

def zlty():
    global k
    k=4

odpocet()

button1 = tkinter.Button(text = 'cerveny kablik', command=cerveny)
button1.pack()
button2 = tkinter.Button(text = 'modry kablik', command=modry)
button2.pack()
button3 = tkinter.Button(text = 'zeleny kablik', command=zeleny)
button3.pack()
button4 = tkinter.Button(text = 'zlty kablik', command=zlty)
button4.pack()
'''

#uloha 8
'''
import tkinter
import random
canvas=tkinter.Canvas(width=300,height=300,bg="white")
canvas.pack()

x=50
y=10
y1=10
x2=200
y2=10
y3=10
def jezibaby():
    global x
    global y
    global y1
    global x2
    global y2
    global y3
    canvas.delete("all")
    rychlost=random.randrange(11)
    rychlost2=random.randrange(11)
    canvas.create_oval(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+10,x+10,y+30)
    canvas.create_line(x-40,y+20,x+20,y+20)
    canvas.create_oval(x2,y2,x2+10,y2+10)
    canvas.create_rectangle(x2,y2+10,x2+10,y2+30)
    canvas.create_line(x2-40,y2+20,x2+20,y2+20)
    if rychlost>0:
        y=y+rychlost
    y1=y-8
    for i in range(6):
        canvas.create_line(x-40,y1,x-20,y+13)
        y1=y1+7
    if rychlost2>0:
        y2=y2+rychlost
    y3=y2-8
    for i in range(6):
        canvas.create_line(x2-40,y3,x2-20,y2+13)
        y3=y3+7
    if y<270 and y2<270:
        canvas.after(50,jezibaby)
    if y>=270 and y2>=270:
        canvas.create_text(150,100,text="Remíza",font="Arial 15 bold")
    else:    
        if y>=270 and y2<270:
            canvas.create_text(150,100,text="Vyhrala jezibaba vlavo",font="Arial 15 bold")
        else:
            if y2>=270 and y<270:
                canvas.create_text(150,100,text="Vyhrala jezibaba vpravo",font="Arial 15 bold")
    print(rychlost)
    print(rychlost2)
        
    
   

jezibaby()
'''

#uloha 9
'''
import tkinter
canvas=tkinter.Canvas(width=300,height=300,bg='white')
canvas.pack()

def kresli():
    canvas.create_oval(20,250,280,270,fill='')
    canvas.create_oval(20,280,280,300,fill='')
    canvas.create_line(20,260,20,290)
    canvas.create_line(280,260,280,290)
    
x = 140
y = 0
xv= 5 
yv=2
p=0
def voda():
    global x,y,xv,yv,p,start
    canvas.delete('kvapka')
    canvas.create_text(280,20,text=p,font='Arial 20 bold',tags='kvapka')
    canvas.create_oval(x,y,x+10,y+10,fill='blue',tags='kvapka')
    if y+10 < 290:
        y+=10
    else:
        canvas.create_oval(150-xv,290-yv,150+xv,290+yv,fill='blue')
        p+=1
        y=0
        if 150-xv>20:
            xv+=5
        if 290-yv>280:
            yv+=2
    if start == 1:
        canvas.after(10, voda)

start=1
def tlacitko():
    global start
    if start == 1:
        start = 0
    else:
        start=1
        voda()
    
kresli()
voda()
button1=tkinter.Button(text='start/stop',command=tlacitko)
button1.pack()
'''

#uloha 3
'''
from random import *

def nahodna_veta():
    mz = randrange(1,3)
    if mz == 1:
        kto = choice(('Kamarát','Spolužiak','Andrej','Roman'))
        corobil = choice(('videl','prezradil','povedal','napísal','zistil','nakreslil'))
    else:
        kto = choice(('Kamarátka','Spolužiačka','Andrea','Romana'))
        corobil = choice(('videla','prezradila','povedala','napísala','zistila','nakreslila'))
    ake = choice(('veľké','malé','obrovské','drobné','smutné','veselé'))
    co = choice(('tajomstvo','prekvapenie','predsavzatie'))
    spojene = kto +' '+corobil+' '+ake+' '+co+'.'
    print(spojene)
    
for i in range(1,21):
    nahodna_veta()
'''

#uloha 4 a 5
'''
import tkinter
from random import*
canvas=tkinter.Canvas(width=300,height=300,bg='white')
canvas.pack()

def slovo():
    global s,v
    slovas=('ahoj','videla','prezradila','povedala','napísala','zistila','nakreslila')
    slovan=('áhoj','vidäla','prezradiľa','povetala','napsala','zizdila','nagrezlila')
    v = randrange(1,3)
    if v == 1:
        s = choice(slovas)
    else:
        s = choice(slovan)
y = 0
p=0
k=0
def padaj():
    global y,k,p
    canvas.delete('all')
    canvas.create_text(150,y,text=s,font='Arial 20 bold')
    if y == 300 and v==1:
        p-=2
        y = 0
        k=0
        slovo()
    elif v==1 and k==1:
        p+=1
        y=0
        k=0
        slovo()
    elif v==2 and k==1:
        p-=2
        y=0
        k=0
        slovo()
    elif v==2 and k==0 and y==300:
        p+=1
        y=0
        slovo()
    else:
        y+=10
    canvas.create_text(280,20,text=p,font='Arial 20 bold')
    print(k)
    if p < 11:
        canvas.after(100,padaj)
    else:
        canvas.delete('all')
        canvas.create_text(150,150,text='Vyhral si',font='Arial 20 bold')
        ceny=('nový telefón','lístky do divadla','knihu s názvom bengoro','poukaz na doučovanie pravopisu')
        canvas.create_text(150,180,text=choice(ceny),font='Arial 10 bold')
        
    
def klik(suradnice):
    global k,y
    x = suradnice.x
    yy = suradnice.y
    if 100<x<200 and y+20>yy>y-20:
        k = 1
    

slovo()
padaj()
canvas.bind('<Button-1>',klik)
'''


