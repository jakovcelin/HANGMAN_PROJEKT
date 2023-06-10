from tkinter import *
from tkinter import messagebox as tmsg
from tkinter import ttk
from playsound import playsound
import string
import random
import requests

root = Tk()
root.geometry("1150x750")
root.title("Hangman")
root.resizable(False, False)


hangman0 = PhotoImage(file = "./hangman0.png")
hangman1 = PhotoImage(file = "./hangman1.png")
hangman2 = PhotoImage(file = "./hangman2.png")
hangman3 = PhotoImage(file = "./hangman3.png")
hangman4 = PhotoImage(file = "./hangman4.png")
hangman5 = PhotoImage(file = "./hangman5.png")
hangman6 = PhotoImage(file = "./hangman6.png")

lst = [hangman0,hangman1,hangman2,hangman3,hangman4,hangman5,hangman6]
x = requests.get('https://random-word-api.herokuapp.com/word')

chances = Label(root,image = hangman0)
chances.pack()

#tu ide apipipipip
#fraza/rijec da len(s razmacima) bude <= 26
word = x.text[2:-2].upper()
random_word = []
check_word = []

word_label = Label(root,text = check_word,font= ("comicsans",30,"bold"))
word_label.pack()


num = 1
def res():
        global num
        global word
        global random_word
        global check_word
        global x
        x = requests.get('https://random-word-api.herokuapp.com/word')
        chances.configure(image = lst[0])
        random_word = []
        check_word = []
        word = x.text[2:-2].upper()
        for i in range(len(word)):
                if(word[i] != ' '): check_word.append('_')
                else: check_word.append(' ')
                
        random_word = [x for x in word]
        word_label.configure(text=' '.join(check_word), fg = "BLACK")
        num = 1;



def disab():
        A.config(state = "disabled")
        B.config(state = "disabled")
        C.config(state = "disabled")
        D.config(state = "disabled")
        E.config(state = "disabled")
        F.config(state = "disabled")
        G.config(state = "disabled")
        H.config(state = "disabled")
        I.config(state = "disabled")
        J.config(state = "disabled")
        K.config(state = "disabled")
        L.config(state = "disabled")
        M.config(state = "disabled")
        N.config(state = "disabled")
        O.config(state = "disabled")
        P.config(state = "disabled")
        Q.config(state = "disabled")
        R.config(state = "disabled")
        S.config(state = "disabled")
        T.config(state = "disabled")
        U.config(state = "disabled")
        V.config(state = "disabled")
        W.config(state = "disabled")
        X.config(state = "disabled")
        Y.config(state = "disabled")
        Z.config(state = "disabled")


def hi(temp):
        global num
        global random_word
        global check_word
        global word
        rt = 1
        if temp.capitalize() in random_word:
                for ind in range(len(random_word)):
                        if(random_word[ind] == temp.capitalize()):
                                check_word.pop(ind)
                                check_word.insert(ind,temp.capitalize())
                word_label.configure(text=' '.join(check_word))
        else :
                        rt = 0
                        if(num >= len(lst)):
                                vrati = "The word was " + word
                                playsound("./tuzno.mp3")
                                word_label.configure(text=' '.join(random_word), fg = "RED")
                                tmsg.showinfo("You lose", vrati)
                                disab()
                        else:
                                chances.configure(image= lst[num])
                                num += 1

        
        if "_" not in check_word:
                word_label.configure(text=' '.join(check_word), fg = "GREEN")
                playsound("./win.mp3")
                tmsg.showinfo("Well played","      You win       ")
                disab()
        return rt


def rs():
        res()
        A.config(bg = "YELLOW", state = "normal")
        B.config(bg = "YELLOW", state = "normal")
        C.config(bg = "YELLOW", state = "normal")
        D.config(bg = "YELLOW", state = "normal")
        E.config(bg = "YELLOW", state = "normal")
        F.config(bg = "YELLOW", state = "normal")
        G.config(bg = "YELLOW", state = "normal")
        H.config(bg = "YELLOW", state = "normal")
        I.config(bg = "YELLOW", state = "normal")
        J.config(bg = "YELLOW", state = "normal")
        K.config(bg = "YELLOW", state = "normal")
        L.config(bg = "YELLOW", state = "normal")
        M.config(bg = "YELLOW", state = "normal")
        N.config(bg = "YELLOW", state = "normal")
        O.config(bg = "YELLOW", state = "normal")
        P.config(bg = "YELLOW", state = "normal")
        Q.config(bg = "YELLOW", state = "normal")
        R.config(bg = "YELLOW", state = "normal")
        S.config(bg = "YELLOW", state = "normal")
        T.config(bg = "YELLOW", state = "normal")
        U.config(bg = "YELLOW", state = "normal")
        V.config(bg = "YELLOW", state = "normal")
        W.config(bg = "YELLOW", state = "normal")
        X.config(bg = "YELLOW", state = "normal")
        Y.config(bg = "YELLOW", state = "normal")
        Z.config(bg = "YELLOW", state = "normal")

resetiraj = Button(root, text = "NEW GAME", command = rs, height = 2, bg = "yellow")
resetiraj.pack(side = "left")

        
def a():
        rt = hi('A')
        if(rt == 1): A.config(bg = "GREEN", state= "disabled")
        else: A.config(bg = "RED", state = "disabled")

def b():
        rt = hi('B')
        if(rt == 1): B.config(bg = "GREEN", state= "disabled")
        else: B.config(bg = "RED", state = "disabled")

def c():
        rt = hi('C')
        if(rt == 1): C.config(bg = "GREEN", state= "disabled")
        else: C.config(bg = "RED", state = "disabled")

def d():
        rt = hi('D')
        if(rt == 1): D.config(bg = "GREEN", state= "disabled")
        else: D.config(bg = "RED", state = "disabled")
        
def e():
        rt = hi('E')
        if(rt == 1): E.config(bg = "GREEN", state= "disabled")
        else: E.config(bg = "RED", state = "disabled")
        
def f():
        rt = hi('F')
        if(rt == 1): F.config(bg = "GREEN", state= "disabled")
        else: F.config(bg = "RED", state = "disabled")

def g():
        rt = hi('G')
        if(rt == 1): G.config(bg = "GREEN", state= "disabled")
        else: G.config(bg = "RED", state = "disabled")

def h():
        rt = hi('H')
        if(rt == 1): H.config(bg = "GREEN", state= "disabled")
        else: H.config(bg = "RED", state = "disabled")

def i():
        rt = hi('I')
        if(rt == 1): I.config(bg = "GREEN", state= "disabled")
        else: I.config(bg = "RED", state = "disabled")

def j():
        rt = hi('J')
        if(rt == 1): J.config(bg = "GREEN", state= "disabled")
        else: J.config(bg = "RED", state = "disabled")
        
def k():
        rt = hi('K')
        if(rt == 1): K.config(bg = "GREEN", state= "disabled")
        else: K.config(bg = "RED", state = "disabled")

def l():
        rt = hi('L')
        if(rt == 1): L.config(bg = "GREEN", state= "disabled")
        else: L.config(bg = "RED", state = "disabled")

def m():
        rt = hi('M')
        if(rt == 1): M.config(bg = "GREEN", state= "disabled")
        else: M.config(bg = "RED", state = "disabled")

def n():
        rt = hi('N')
        if(rt == 1): N.config(bg = "GREEN", state= "disabled")
        else: N.config(bg = "RED", state = "disabled")

def o():
        rt = hi('O')
        if(rt == 1): O.config(bg = "GREEN", state= "disabled")
        else: O.config(bg = "RED", state = "disabled")

def p():
        rt = hi('P')
        if(rt == 1): P.config(bg = "GREEN", state= "disabled")
        else: P.config(bg = "RED", state = "disabled")

def q():
        rt = hi('Q')
        if(rt == 1): Q.config(bg = "GREEN", state= "disabled")
        else: Q.config(bg = "RED", state = "disabled")

def r():
        rt = hi('R')
        if(rt == 1): R.config(bg = "GREEN", state= "disabled")
        else: R.config(bg = "RED", state = "disabled")

def s():
        rt = hi('S')
        if(rt == 1): S.config(bg = "GREEN", state= "disabled")
        else: S.config(bg = "RED", state = "disabled")

def t():
        rt = hi('T')
        if(rt == 1): T.config(bg = "GREEN", state= "disabled")
        else: T.config(bg = "RED", state = "disabled")

def u():
        rt = hi('U')
        if(rt == 1): U.config(bg = "GREEN", state= "disabled")
        else: U.config(bg = "RED", state = "disabled")

def v():
        rt = hi('V')
        if(rt == 1): V.config(bg = "GREEN", state= "disabled")
        else: V.config(bg = "RED", state = "disabled")

def w():
        rt = hi('W')
        if(rt == 1): W.config(bg = "GREEN", state= "disabled")
        else: W.config(bg = "RED", state = "disabled")

def x():
        rt = hi('X')
        if(rt == 1): X.config(bg = "GREEN", state= "disabled")
        else: X.config(bg = "RED", state = "disabled")

def y():
        rt = hi('Y')
        if(rt == 1): Y.config(bg = "GREEN", state= "disabled")
        else: Y.config(bg = "RED", state = "disabled")

def z():
        rt = hi('Z')
        if(rt == 1): Z.config(bg = "GREEN", state= "disabled")
        else: Z.config(bg = "RED", state = "disabled")
                
A = Button(root, text = "A", command = a,height= 2, bg = "yellow")
A.pack(side = "left")

B = Button(root, text = "B", command = b, height= 2,bg = "yellow")
B.pack(side = "left")

C = Button(root, text = "C", command = c,height= 2,bg = "yellow")
C.pack(side = "left")

D = Button(root, text = "D", command = d,height= 2,bg = "yellow")
D.pack(side = "left")

E = Button(root, text = "E", command = e,height= 2,bg = "yellow")
E.pack(side = "left")

F = Button(root, text = "F", command = f,height= 2,bg = "yellow")
F.pack(side = "left")

G = Button(root, text = "G", command = g,height= 2,bg = "yellow")
G.pack(side = "left")

H = Button(root, text = "H", command = h,height= 2,bg = "yellow")
H.pack(side = "left")

I = Button(root, text = "I", command = i,height= 2,bg = "yellow")
I.pack(side = "left")

J = Button(root, text = "J", command = j,height= 2,bg = "yellow")
J.pack(side = "left")

K = Button(root, text = "K", command = k,height= 2,bg = "yellow")
K.pack(side = "left")

L = Button(root, text = "L", command = l,height= 2,bg = "yellow")
L.pack(side = "left")

M = Button(root, text = "M", command = m,height= 2,bg = "yellow")
M.pack(side = "left")

N = Button(root, text = "N", command = n,height= 2,bg = "yellow")
N.pack(side = "left")

O = Button(root, text = "O", command = o,height= 2,bg = "yellow")
O.pack(side = "left")

P = Button(root, text = "P", command = p,height= 2,bg = "yellow")
P.pack(side = "left")

Q = Button(root, text = "Q", command = q,height= 2,bg = "yellow")
Q.pack(side = "left")

R = Button(root, text = "R", command = r,height= 2,bg = "yellow")
R.pack(side = "left")

S = Button(root, text = "S", command = s,height= 2,bg = "yellow")
S.pack(side = "left")

T = Button(root, text = "T", command = t,height= 2,bg = "yellow")
T.pack(side = "left")

U = Button(root, text = "U", command = u,height= 2,bg = "yellow")
U.pack(side = "left")

V = Button(root, text = "V", command = v,height= 2,bg = "yellow")
V.pack(side = "left")

W = Button(root, text = "W", command = w,height= 2,bg = "yellow")
W.pack(side = "left")

X = Button(root, text = "X", command = x,height= 2,bg = "yellow")
X.pack(side = "left")

Y = Button(root, text = "Y", command = y,height= 2,bg = "yellow")
Y.pack(side = "left")

Z = Button(root, text = "Z", command = z,height= 2,bg = "yellow")
Z.pack(side = "left")


check_word = []
for i in range(len(word)):
        if(word[i] != ' '): check_word.append('_')
        else: check_word.append(' ')
        
random_word = [x for x in word]
dobri = []
word_label.configure(text=' '.join(check_word))
                             
root.mainloop()
