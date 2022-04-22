from cProfile import label
import tkinter
import time

root = tkinter.Tk()
root.title("Relogio")

def labelTime():
    string = time.strftime("%H:%M:%S")
    label.config(text=string)
    label.after(1000, labelTime)

if __name__ == "__main__":
    label = tkinter.Label(root,font=("alarm clock",80), background="black", foreground="#fff")
    label.pack(anchor="center")
    labelTime()
    
    root.mainloop()