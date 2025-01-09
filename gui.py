import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import numpy as np

from keras.models import load_model
model = load_model('Age_Gender_Detection.keras')

top = tk.Tk()
top.geometry('800X600')
top.title('Age and Gender Detector')
top.configure(background = '#CDCDCD')

# Initializing the labels (1 for age, 2 for gender)

label1 = Label(top, background = '#CDCDCD', font = ('arial', 15, 'bold'))
label2 = Label(top, background = '#CDCDCD', font = ('arial', 15, 'bold'))
sign_image = Label(top)
label1.pack(side = "bottom", pady = 50)
label2.pack(side = "bottom", pady = 50)
heading = Label(top, text = "Age and Gender Detector", pady = 20, font = ('arial', 20, 'bold'))
heading.configure(background = "#CDCDCD", foreground = "#364156")
heading.pack()
top.mainloop()