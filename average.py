from tkinter import *


def get_delta():
    results1 = int(last_release.get())
    results2 = int(new_release.get())
    delta = results2 / results1 * 100 - 100
    a1 = Label(windows, width=30, text=delta, fg='red')
    a1.config(font=('Verdana', 15))
    a1.pack()

windows = Tk()
windows.title("Average Value")
windows.geometry('500x500')
#создаём главное окно
t1 = Label(windows, text='Enter your values', fg='black')
#задаём стиль окна
t1.config(font=('Verdana', 25))
t1.pack()
#задаём поля ввода для прошлого релиза


last_release = Entry(windows, width = 30, bg='white')
last_release.focus()
last_release.pack()

t2 = Label(windows, text='last realise here ⇑ ||| new realise here ⇓', fg='blue')
t2.config(font=('Verdana', 10))
t2.pack()
#задаём поле ввода для нового релиза
new_release = Entry(windows, width = 30, bg='white')
new_release.pack()

#создаём кнопку ,которая выводит нам результат
but = Button(windows, text = 'get the percentage difference', command= get_delta)
but.pack()
windows.mainloop()
