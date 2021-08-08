from tkinter import *
from tkinter import ttk
import random
from bubble import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort
root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
#config is used to access an object's attributes after its initialisation.
root.config(bg='black')

#variables
"""Since we are using two data arrays one for generating and one for starting the algo,
 so we need to declare global data array """
data = []
selected_alg = StringVar()

def drawData(data,colorarr):
    # DELETE SO THAT WE REDRAW FOR EVERY NEW INPUT
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    # offset so we don not start at the border
    offset = 30
    spacing = 10 #Between bars
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        # DRAWING BARS
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorarr[i])
        # LINE 34 SO THAT WE HAVE NUMS WRITTEN OVER BAR.
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    # Line 39 because we want to see data getting sorted step by step
    root.update_idletasks()
def Generate():
    global data

    print(f'Alg Selected:{selected_alg.get()}')
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())
    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data,['red' for x in range(len(data))])
def StartAlgo():
    global data
    if not data:
        return

    if algMenu.get()== "Quick Sort":
        quick_sort(data,0,len(data)-1,drawData,speed.get())

    if algMenu.get()=="Bubble Sort":
        bubble_sort(data,drawData,speed.get())

    if algMenu.get() == "Merge Sort":
        merge_sort(data, drawData, speed.get())

    drawData(data, ['green' for x in range(len(data))])



#frame / base layout
UI_frame = Frame(root, width= 600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
#Row[0]
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)

""" It is one of the Tkinter widgets where it contains a down arrow
to select from a list of options. 
It helps the users to select according to the list of options displayed."""

algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort',"Quick Sort"])
algMenu.grid(row=0, column=1, padx=5, pady=5)
# LINE 77 IS FOR DEFAULT(BUBBLE SORT)
algMenu.current(0)
# SPEED OF ALGO
speed = Scale(UI_frame,from_ =0.1, to = 2,length =200,digits =2,resolution = 0.2,orient = HORIZONTAL)
speed.grid(row = 0,column =2,padx = 5,pady =5)
Button(UI_frame, text="Start", command=StartAlgo, bg='red').grid(row=0, column=3, padx=5, pady=5)
#Row[1]

sizeEntry = Scale(UI_frame,from_ =3, to = 25,resolution = 1,orient = HORIZONTAL,label = "Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame,from_ =0, to = 10,resolution = 1,orient = HORIZONTAL,label = "Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame,from_ =10, to = 100,resolution = 1,orient = HORIZONTAL,label = "Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()