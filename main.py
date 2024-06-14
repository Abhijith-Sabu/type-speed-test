from tkinter import *
from tkinter import filedialog,Label
from PIL import Image,ImageTk
import tkinter.messagebox
import ctypes
import random
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
ctypes.windll.shcore.SetProcessDpiAwareness(1)







def reseting_labels():
        possibleTexts = [
        'For writers, a random sentence can help them get their creative juices flowing. Since the topic of the sentence is completely unknown, it forces the writer to be creative when the sentence appears. There are a number of different ways a writer can use the random sentence for creativity. The most common way to use the sentence is to begin a story. Another option is to include it somewhere in the story. A much more difficult challenge is to use it to end a story. In any of these cases, it forces the writer to think creatively since they have no idea what sentence will appear from the tool.',
        'The goal of Python Code is to provide Python tutorials, recipes, problem fixes and articles to beginner and intermediate Python programmers, as well as sharing knowledge to the world. Python Code aims for making everyone in the world be able to learn how to code for free. Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.',
        'As always, we start with the imports. Because we make the UI with tkinter, we need to import it. We also import the font module from tkinter to change the fonts on our elements later. We continue by getting the partial function from functools, it is a genius function that excepts another function as a first argument and some args and kwargs and it will return a reference to this function with those arguments. This is especially useful when we want to insert one of our functions to a command argument of a button or a key binding.'
    ]
        text = random.choice(possibleTexts).lower()
        splitPoint=0
        # left label
        global labelLeft


        labelLeft=Label(window,text=text[0:splitPoint],fg='gray')
        labelLeft.place(relx=0.5,rely=0.5,anchor=E)
        global rightLabel
        
        # right_label 
        rightLabel=Label(window,text=text[splitPoint:],)
        rightLabel.place(relx=0.5,rely=0.5,anchor=W)

        # setting current label
        global currentLabel

        currentLabel = Label(window,text=text[splitPoint],fg='gray')
        currentLabel.place(relx=0.5,rely=0.6,anchor=N)

        # setting timeLeft label

        global timeLeftlabel

        timeLeftlabel=Label(window,text=f"0 time left",fg='gray')
        timeLeftlabel.place(relx=0.5,rely=0.4,anchor=S)



        global writeAble
        writeAble=True
        window.bind('<Key>',keyPress)


        global passedSeconds
        passedSeconds=0

        window.after(60000,stopTest)
        window.after(1000,addSecond)

    

def stopTest():
    global writeAble
    writeAble =False
    coountWords= len(labelLeft.cget('text').split(' '))
    #   destroying all unwantedwidgets

    timeLeftlabel.destroy()
    labelLeft.destroy()
    rightLabel.destroy()
    currentLabel.destroy()

    global resultWidget

    resultWidget=Label(window,text=f"'Words per Minute: {coountWords}",fg='black')
    resultWidget.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    global retryButton
    
    retryButton = Button(window, text='Retry', command=restart,
                        font=('Helvetica', 14, 'bold'), 
                        bg='green', fg='white',
                        activebackground='darkgreen',
                        activeforeground='white',
                        padx=10, pady=5,
                        relief='raised', bd=4)
    retryButton.place(relx=0.5,rely=0.7,anchor=CENTER)



def restart():
     resultWidget.destroy()
     retryButton.destroy()

     reseting_labels()

def addSecond():
     global passedSeconds
     passedSeconds+=1
     timeLeftlabel.configure(text=f"{passedSeconds} Seconds")
     global writeAble
     if writeAble:
          window.after(1000,addSecond)
          

def keyPress(event=None):
    try:
        if event.char.lower() == rightLabel.cget('text')[0].lower():
            # Deleting one from the right side.
            rightLabel.configure(text=rightLabel.cget('text')[1:])
            # Deleting one from the right side.
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            #set the next Letter Lavbel
            currentLabel.configure(text=rightLabel.cget('text')[0])
    except tkinter.TclError:
        pass
if __name__=="__main__":
    window=Tk()
    window.title('Typoing-Speed-Test')
    window.geometry("1080x900")
    # setting the font for all lables and button 
    window.option_add('*Label.Font',"consolas 30")
    window.option_add("*Button.Font","consolas 30")
    reseting_labels()





    window.mainloop()