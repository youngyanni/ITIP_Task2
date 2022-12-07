from random import randint
import array as arr
import getpass
from tkinter import *


def StartGame(window):
    wind = window
    wind.image = PhotoImage(file='E:\\Pictures\\leorio.png')
    bg_logo = Label(wind, image=wind.image)
    bg_logo.grid(row=0, column=0, columnspan=4)
    wind.title("Камень, ножницы, бумага")
    btn1 = Button(wind, text="Да", command=lambda: (ChooseGameMode(), wind.withdraw()))
    btn2 = Button(wind, text="Нет", command=lambda: exit(wind))
    btn1.grid(column=0, row=1, sticky=W + E, columnspan=2)
    btn2.grid(column=2, row=1, sticky=W + E, columnspan=2)


def MenuModePC():
    global mainmenu
    mainmenu = Toplevel(window)
    mainmenu.title("Мю")
    mainmenu.geometry('200x130+950+450')
    mainmenu.resizable(width=False, height=False)
    butmod2 = Button(mainmenu, text="Сменить режим", width=30,
                     command=lambda: (ChooseGameMode(), mainmenu.destroy(), mode2.destroy()))
    butmod2.grid(row=0, column=0, columnspan=2)
    butscore2 = Button(mainmenu, text="Показать счёт", width=30,
                       command=lambda: (BtnScoreModePC(), mainmenu.withdraw()))
    butscore2.grid(column=0, row=1, columnspan=2)
    butexit2 = Button(mainmenu, text="Выйти", width=30, command=lambda: exit(window))
    butexit2.grid(column=0, row=4, columnspan=2)
    butresume2 = Button(mainmenu, text="Возобновить", width=30,
                        command=lambda: (mainmenu.destroy(), mode2.deiconify()))
    butresume2.grid(column=0, row=3, columnspan=2)
    butrepeat2 = Button(mainmenu, text="Заново", width=30, command=lambda: (BtnRepeatModePC(), mainmenu.destroy()))
    butrepeat2.grid(column=0, row=2, columnspan=2)
    mainmenu.protocol("WM_DELETE_WINDOW", lambda: (mode2.deiconify(), mainmenu.destroy()))


def MenuModeFriends():
    global newwindow
    newwindow = Toplevel(window)
    newwindow.title("Меню")
    newwindow.geometry('200x130+950+450')
    newwindow.resizable(width=False, height=False)
    butmod = Button(newwindow, text="Сменить режим", width=30,
                    command=lambda: (ChooseGameMode(), newwindow.destroy(), mode1.destroy()))
    butmod.grid(row=0, column=0, columnspan=2)
    butscore = Button(newwindow, text="Показать счёт", width=30,
                      command=lambda: (BtnScoreModeFriends(), newwindow.withdraw()))
    butscore.grid(column=0, row=1, columnspan=2)
    butexit = Button(newwindow, text="Выйти", width=30, command=lambda: exit(window))
    butexit.grid(column=0, row=4, columnspan=2)
    butresume = Button(newwindow, text="Возобновить", width=30,
                       command=lambda: (mode1.deiconify(), newwindow.destroy()))
    butresume.grid(column=0, row=3, columnspan=2)
    butrepeat = Button(newwindow, text="Заново", width=30,
                       command=lambda: (BtnRepeatModeFriends(), newwindow.destroy()))
    butrepeat.grid(column=0, row=2, columnspan=2)
    newwindow.protocol("WM_DELETE_WINDOW", lambda: (mode1.deiconify(), newwindow.destroy()))


def ChooseGameMode():
    choose = Toplevel(window)
    choose.title("Выбор")
    choose.geometry('525x430+650+300')
    choose.image = PhotoImage(file='E:\\Pictures\\leorio2.png')
    choose.bg_logo = Label(choose, image=choose.image)
    choose.bg_logo.grid(row=0, column=0, columnspan=4)
    choose.btn1 = Button(choose, text="Против друга", command=lambda: (ModeFriends(), choose.destroy()))
    choose.btn2 = Button(choose, text="Против компьютера", command=lambda: (ModePC(), choose.destroy()))
    choose.btn1.grid(column=0, row=1, sticky=W + E, columnspan=2)
    choose.btn2.grid(column=2, row=1, sticky=W + E, columnspan=2)


def ModePC():
    global mode2, e3, pcentry
    global scr2
    scr2 = arr.array('i', [0, 0])
    mode2 = Toplevel(window)
    mode2.resizable(width=False, height=False)
    mode2.title("Против компьютера")
    mode2.geometry('737x470')
    mode2.image = PhotoImage(file='E:\\Pictures\\bg1.png')
    mode2.bg_logo = Label(mode2, image=mode2.image)
    mode2.bg_logo.grid(row=0, column=0, columnspan=4)
    mode2.btn4 = Button(mode2, text="Меню", command=lambda: (MenuModePC(), mode2.withdraw()))
    mode2.btn4.grid(row=2, columnspan=4, column=0, sticky=W + E)
    e3 = Entry(mode2, width=20, borderwidth=5)
    e3.insert(0, 'Ваш ход')
    e3.grid(row=1, column=0, sticky=W + E)
    e3.bind('<Enter>', ClearEntry)
    pcentry = Entry(mode2, width=20, borderwidth=5)
    pcentry.insert(0, 'Ход компьютера')
    pcentry.grid(column=2, row=1, sticky=W + E, columnspan=2)
    mode2.btn3 = Button(mode2, text="Играть", command=lambda: BtnPlayModePC())
    mode2.btn3.grid(column=1, row=1, sticky=W + E)


def ClearEntry(event):
    e3.delete(0, END)


def ModeFriends():
    global e1, e2
    global scr
    scr = arr.array('i', [0, 0])
    global mode1
    mode1 = Toplevel(window)
    mode1.resizable(width=False, height=False)
    mode1.title("Против друга")
    mode1.geometry('737x470')
    mode1.image = PhotoImage(file='E:\\Pictures\\bg1.png')
    mode1.bg_logo = Label(mode1, image=mode1.image)
    mode1.bg_logo.grid(row=0, column=0, columnspan=4)
    mode1.btn4 = Button(mode1, text="Меню", command=lambda: (MenuModeFriends(), mode1.withdraw()))
    mode1.btn4.grid(row=2, columnspan=4, column=0, sticky=W + E)
    e1 = Entry(mode1, width=20, borderwidth=5)
    e1.insert(0, 'Ход 1-го игрока')
    e1.grid(row=1, column=0, sticky=W + E)
    mode1.btn3 = Button(mode1, text="Играть", command=lambda: BtnPlayModeFriends())
    mode1.btn3.grid(column=1, row=1, sticky=W + E, columnspan=2)
    e2 = Entry(mode1, width=20, borderwidth=5)
    e2.grid(row=1, column=3, sticky=W + E)
    e2.insert(0, 'Ход 2-го игрока')
    e1.bind('<Enter>', Enter1)
    e2.bind('<Enter>', Enter2)


dictionary = {0: 'Камень',
              1: 'Ножницы',
              2: 'Бумага'}


def BtnPlayModePC():
    pl1 = e3.get()
    if pl1.isdigit() == False or int(pl1) > 2 or int(pl1) < 0:
        excpt = Toplevel(window)
        excpt.resizable(width=False, height=False)
        excpt.title("Ошибка")
        excpt.geometry('250x100')
        text = Text(excpt, width=250, height=100, bg='red', fg='white', font="Courier 20")
        text.insert(INSERT, "Неверный формат \nВведите: 0 или 1 или 2")
        text.pack()
    else:
        pc = randint(0, 2)
        result = int(pl1) - pc
        pcentry.delete(0, END)
        match result:
            case 0:
                e3.configure(bg="green")
                pcentry.configure(bg="green")
                pcentry.insert(0, f'{dictionary[pc]}')
            case 1:
                e3.configure(bg="red")
                pcentry.configure(bg="green")
                scr2[1] = scr2[1] + 1
                pcentry.insert(0, f'{dictionary[pc]}')
            case 2:
                e3.configure(bg="green")
                pcentry.configure(bg="red")
                scr2[0] = scr2[0] + 1
                pcentry.insert(0, f'{dictionary[pc]}')
            case -1:
                e3.configure(bg="green")
                pcentry.configure(bg="red")
                scr2[0] = scr2[0] + 1
                pcentry.insert(0, f'{dictionary[pc]}')
            case -2:
                e3.configure(bg="red")
                pcentry.configure(bg="green")
                scr2[1] = scr2[1] + 1
                pcentry.insert(0, f'{dictionary[pc]}')




def BtnPlayModeFriends():
    pl1 = e1.get()
    pl2 = e2.get()
    if pl1.isdigit() == False or pl2.isdigit() == False or int(pl1) > 2 or int(pl1) < 0 or int(pl2) > 2 or int(pl2) < 0:
        excpt = Toplevel(window)
        excpt.resizable(width=False, height=False)
        excpt.title("Ошибка")
        excpt.geometry('250x100')
        text = Text(excpt, width=250, height=100, bg='red', fg='white', font="Courier 20")
        text.insert(INSERT, "Неверный формат \nВведите: 0 или 1 или 2")
        text.pack()
    else:
        result = int(pl1) - int(pl2)
        match result:
            case 0:
                e1.configure(bg="green")
                e2.configure(bg="green")
            case 1:
                e1.configure(bg="red")
                e2.configure(bg="green")
                scr[1] = scr[1] + 1
            case 2:
                e1.configure(bg="green")
                e2.configure(bg="red")
                scr[0] = scr[0] + 1
            case -1:
                e1.configure(bg="green")
                e2.configure(bg="red")
                scr[0] = scr[0] + 1
            case -2:
                e1.configure(bg="red")
                e2.configure(bg="green")
                scr[1] = scr[1] + 1


def BtnRepeatModePC():
    ModePC()
    scr2 = [0, 0]


def BtnRepeatModeFriends():
    ModeFriends()
    scr = [0, 0]


def Enter1(event):
    e1.delete(0, END)
    e1['show'] = "*"
    e1['bg'] = 'white'


def Enter2(event):
    e2.delete(0, END)
    e2['show'] = "*"
    e2['bg'] = 'white'


def BtnScoreModeFriends():
    score = Toplevel(window)
    score.title("Счёт")
    score1 = Label(score, text="Ваш счёт", font="Arial 16")
    score1.grid(column=0, row=1, sticky=W + E)
    score2 = Label(score, text="Соперника", font="Arial 16")
    score2.grid(column=1, row=1, sticky=W + E, padx=10)
    score3 = Label(score, text=f'{scr[0]}', font="Arial 20")
    score4 = Label(score, text=f'{scr[1]}', font="Arial 20")
    score3.grid(column=0, row=2, sticky=W + E)
    score4.grid(column=1, row=2, sticky=W + E)
    score.geometry('220x80+950+450')
    score.resizable(width=False, height=False)
    score.protocol("WM_DELETE_WINDOW", lambda: (score.destroy(), newwindow.deiconify()))


def BtnScoreModePC():
    score5 = Toplevel(window)
    score5.title("Счёт")
    score1 = Label(score5, text="Ваш счёт", font="Arial 16")
    score1.grid(column=0, row=1, sticky=W + E)
    score2 = Label(score5, text="Компьютер", font="Arial 16")
    score2.grid(column=1, row=1, sticky=W + E, padx=10)
    score3 = Label(score5, text=f'{scr2[0]}', font="Arial 20")
    score4 = Label(score5, text=f'{scr2[1]}', font="Arial 20")
    score3.grid(column=0, row=2, sticky=W + E)
    score4.grid(column=1, row=2, sticky=W + E)
    score5.geometry('220x80+950+450')
    score5.resizable(width=False, height=False)
    score5.protocol("WM_DELETE_WINDOW", lambda: (score5.destroy(), mainmenu.deiconify()))


if __name__ == '__main__':
    window = Tk()
    window.geometry('525x430+650+300')
    window.resizable(width=False, height=False)
    StartGame(window)
    window.mainloop()
