from tkinter import *
from tkinter import ttk
import random
from mergeSort import merge_sort
from bubbleSort import bubble_sort
from quciksort import quickSort
import copy
from tkinter import messagebox
import time


root = Tk()
root.title('Sorting Algorithm Visualization')
root.maxsize(900,600)
root.config(bg='black')

#Variables
selected_alg = StringVar()
data = []
data2= []
option = StringVar()

#Functions 



def drawData(data,colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 15
    spacing = 0
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):

        x0 = i*x_width + offset + spacing
        y0 = (c_height - height*340)
        
        x1 =(i+1)* x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0,y0,x1,y1, fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW, text=str(data[i]))

    root.update_idletasks()

def generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())  
   
    if minVal < 0 : minVal = 1
    if maxVal > 200 : maxVal = 200
    if size > 100 or size < 3: size = 25
    if minVal > maxVal : minVal, maxVal = maxVal,minVal

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal,maxVal+1))
    drawData(data,['red' for x in range(len(data))])

def StartAlgorithm():
    global data
    start = time.time()
    data2 = copy.deepcopy(data)

    if(selected_alg.get() == 'Quick Sort'):
        quickSort(data,0,len(data)-1,drawData,speedScale.get())
        
    if(selected_alg.get() == 'Bubble Sort'):
        bubble_sort(data,drawData,speedScale.get())

    if(selected_alg.get() == 'Merge Sort'):
        merge_sort(data, drawData, speedScale.get())

    drawData(data,['green' for x in range (len(data))])
    data = data2
    messagebox.showinfo("Data Sorted!: ", f"Sorting algorithm used: {selected_alg.get()} \nSpeed Scale: {speedScale.get()} \nTotal time taken: {time.time()-start} ")

UI_frame = Frame(root,width = 600, height=200, bg='grey')
UI_frame.grid(row=0,column=0,padx=10,pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1,column=0, padx=10,pady=5)

# Placements 
Label(UI_frame, text="Algorithm: ", bg="grey").grid(row=0,column=0,padx=0,pady=5,sticky=W)

#Menu
algMenu = ttk.Combobox(UI_frame,textvariable=selected_alg, values=['Bubble Sort','Quick Sort','Merge Sort'], state="readonly")
algMenu.place(x=65,y=25)
algMenu.current(0)

#Scales 
speedScale = Scale(UI_frame, from_ = 0.02 ,to=.2, length=200, digits=2, resolution=0.01,orient=HORIZONTAL,label='Select Speed [s]')
speedScale.grid(row=0,column=2,padx=5,pady=5)
speedScale.set(0.1)

sizeEntry = Scale(UI_frame, from_ = 3 ,to=50, length=150,  resolution=1,orient=HORIZONTAL,label='Data')
sizeEntry.grid(row = 1, column=0, padx=5,pady=5 )
sizeEntry.set(15)

minEntry = Scale(UI_frame, from_ = 1 ,to=50, length=150,  resolution=1,orient=HORIZONTAL,label='Min Value')
minEntry.grid(row = 1, column=1, padx=5,pady=5 )


maxEntry = Scale(UI_frame, from_ = 10 ,to=200, length=150,  resolution=1,orient=HORIZONTAL,label='Max Value')
maxEntry.grid(row = 1, column=2, padx=5,pady=5 )
maxEntry.set(20)

#Buttons
Button(UI_frame,text = "Start", command=StartAlgorithm, bg='red').grid(row=0,column=3,padx=5,pady=5) 
Button(UI_frame,text = "Generate", command=generate,bg='grey').grid(row=1,column=3,padx=5,pady=5)

root.mainloop()