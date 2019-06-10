
import tkinter as Tkinter 
import random
def mathrandom(label):
 a=random.choice([1,2,3,4,5,6,7,8,9,0])
 b=random.choice([1,2,3,4,5,6,7,8,9,0])
 c=a+b
 print(f"{a} + {b} = ___ ")
 print("Options are : ")
 print(f"1) {b}\n2) {c}\n3) {a}\n4) 0")
 d=int(input("Enter your choice:--"))
 if c==d:
    print("Awesome!!Your Answer is Correct")
 else :
    print("Better luck next time")
counter = -1
running = False
def counter_label(label): 
    def count(): 
        if running: 
            global counter 
  
            # To manage the intial delay. 
            if counter==-1:             
                display="Starting..."
            else: 
                display=str(counter) 
  
            label['text']=display   
            label.after(1000, count)  
            counter += 1
  
    # Triggering the start of the counter. 
    count()      
  
# start function of the stopwatch 
def Start(label): 
    global running 
    running=True
    counter_label(label)
    mathrandom(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
  
# Stop function of the stopwatch 
def Stop(): 
    global running 
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
  
# Reset function of the stopwatch 
def Reset(label): 
    global counter 
    counter=-1
  
    # If rest is pressed after pressing stop. 
    if running==False:       
        reset['state']='disabled'
        label['text']='Welcome!'
  
    # If reset is pressed while the stopwatch is running. 
    else:                
        label['text']='Starting...'
  
root = Tkinter.Tk() 
root.title("Fastest Maths Challenge") 
  
# Fixing the window size. 
root.minsize(width=250, height=70) 
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold") 
label.pack() 
start = Tkinter.Button(root, text='Start Challenge',  
width=15, command=lambda:Start(label)) 
stop = Tkinter.Button(root, text='Stop',  
width=15, state='disabled', command=Stop) 
reset = Tkinter.Button(root, text='Play again', 
 width=15, state='disabled', command=lambda:Reset(label)) 
start.pack() 
stop.pack() 
reset.pack() 
root.mainloop() 
