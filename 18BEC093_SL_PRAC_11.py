#----------------------------------------------FUNCTION TO SEARCH FROM JSON FILE--------------------------------------
def search():
    global w
    whole_output=''
    w=search_entry.get()
    w = w.lower()

    if w in data:
        output=data[w]
        if type(output) == list:
            for item in output:
                whole_output+=item+'\n'
            disp_label.configure(text='Meaning: \n {}'.format(whole_output))
        else:
            disp_label.configure(text='{}'.format(output))

    elif len(get_close_matches(w, data.keys())) > 0:
        disp_label.configure(text='Did you mean {} instead?'.format(str(get_close_matches(w, data.keys())[0])))
        yes_button.grid()
        no_button.grid()

    else:
        output="The word doesn't exist. Please double check it."

def yes():
    output=data[get_close_matches(w, data.keys())[0]]
    whole_output=''
    if type(output) == list:
        for item in output:
            whole_output+=item+'\n'
        disp_label.configure(text='Meaning: \n {}'.format(whole_output))
    else:
        disp_label.configure(text='Meaning: \n {}'.format(output))
    yes_button.grid_remove()
    no_button.grid_remove()

def no():
    output="The word doesn't exist. Please double check it."
    disp_label.configure(text='{}'.format(output))
    no_button.grid_remove()
    yes_button.grid_remove()

#-----------------------------------------------GUI CODE-----------------------------------------------------------
def gui():
    global search_entry,disp_label,ch_label,yes_button,no_button
#------------------------------------------------LABELS-------------------------------------------------------------
    search_label=Label(book,text="Enter A Word To Search",bg="gray25",font=('Comic Sans MS',17,'bold'))
    search_label.grid(row=0,column=0,padx=20,pady=40,ipadx=10,ipady=10)

    disp_label=Label(book,bg="gray25",font=('Comic Sans MS',15,'bold'))
    disp_label.grid(row=2,column=0,columnspan=3)
#------------------------------------------------ENTRIES-------------------------------------------------------------
    search_entry=Entry(book,font=('arial',24,'bold'),width=15)
    search_entry.grid(row=0,column=1,padx=10,pady=40)
#------------------------------------------------BUTTONS-------------------------------------------------------------
    search_button=Button(book,text='SEARCH',font=('Comic Sans MS',18,'bold'),width=10,activebackground='grey30',command=search,bd=5)
    search_button.grid(row=0,column=2,padx=30,pady=40)

    yes_button=Button(book,text="YES",font=('Comic Sans MS',18,'bold'),width=10,activebackground='grey30',command=yes,bd=5)
    yes_button.grid(row=3,column=0,columnspan=2,padx=0,pady=40)
    yes_button.grid_remove()

    no_button=Button(book,text="NO",font=('Comic Sans MS',18,'bold'),width=10,activebackground='grey30',command=no,bd=5)
    no_button.grid(row=3,column=1,columnspan=2,padx=0,pady=40)
    no_button.grid_remove()
#---------------------------------------------------MAIN------------------------------------------------------------
import json                                                                         #for reading from json file
from tkinter import *                                                               #for GUI
from difflib import get_close_matches                                               #for finding nearest string 

data = json.load(open("/home/artrimiss/Downloads/SL_PRAC_11/data.json"))            #loading json file
book=Tk()                                                                           #intializing book as Tk
book.geometry("800x350+280+150")    
book.title('ENGLISH DICTIONARY')                      
book.resizable(0,0)                                                                 #making window non resizeable
book.configure(bg="gray25")
gui()
book.mainloop()                                                 #infinte predefined funtion to always show Tk window                                                                 
