import shelve
from tkinter import *
from tkinter.messagebox import showinfo

from manager import Manager
from person import Person

bob = Person('Bob Smith', 42, 30000, 'Software')
sue = Person('Sue Jones', 45, 40000, 'Hardware')
tom = Manager('Tom Roberts', 35, 60000)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()

db = shelve.open('class-shelve')
for key in db:
    print(key, '|||', str(db[key]))

def reply():
    showinfo(title='popup', message='Button pressed!')

window = Tk()
button = Button(window, text='press', command=reply)
button.pack()
#window.mainloop()

l = ["some", "stuff", "here"]
d = {'foo': 'bar', 'wiz':'pop'}

def myp(*args, **kwargs):
    print("****")
    for x in args:
        print(x)
    for k in kwargs:
        print('%s => %s' % (k, kwargs[k]))

myp(*d)
