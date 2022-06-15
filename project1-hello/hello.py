
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello'
import Tkinter as Tk
win = Tk.Toplevel()
frame = Tk.Frame(master=win).grid(row=1, column=1)
button = Tk.Button(master=frame, text='press', command=action)
