from lib2to3.pgen2.token import NEWLINE
from linecache import getline
from sre_parse import State
from tkinter import *

class GUI:
    def __init__(self, root):
        # base window attributes
        self.master = root
        self.master.title("Lexical Analyzer for TinyPie")
        self.master.geometry("1100x600")
        self.master.maxsize(1100,600)
        self.master.config(bg="black")

        self.line_num = 0 # number to hold current line

        # top left and right frames
        self.UI_frame_top_left = Frame(self.master,width=550,height=100,bg="black").grid(row=0,column=0)
        self.UI_frame_top_right = Frame(self.master,width=550,height=100,bg="black").grid(row=0,column=1)

        # UI left side
        self.UI_frame_left = Frame(self.master,width=550,height=320,bg="black").grid(row=1,column=0,padx=5,sticky=N)

        # source input
        Label(self.UI_frame_left,text="Sorce Code Input:").grid(row=0,column=0,padx=50,pady=5,sticky=S)
        self.input_code = Text(self.UI_frame_left,width=50,height=20)
        self.input_code.grid(row=1,column=0,sticky=N)

        # line reader
        Label(self.UI_frame_left,text="Current Processing Line:").grid(row=2,column=0,padx=80,pady=5,sticky=W)
        self.line = Entry(self.master)
        self.line.grid(row=2,column=0,padx=5,pady=5)
        self.line.insert(0,str(self.line_num))
        self.line.config(state=DISABLED)
    
        # next button
        self.next_button = Button(self.master,text="Next Line",command=self.get_line)
        self.next_button.grid(row=3,column=0)

        # UI right side
        self.UI_frame_right = Frame(self.master,width=550,height=320,pady=5,bg="black").grid(row=1,column=1,padx=5,sticky=N)

        # lex output
        Label(self.UI_frame_right,text="Lexical Analyzed Result:").grid(row=0,column=1,padx=50,pady=5,sticky=S)
        self.output_lex = Text(self.UI_frame_right,width=50,height=20,state=DISABLED)
        self.output_lex.grid(row=1,column=1,sticky=N)

        # quit button
        self.quit_button = Button(self.master,text="Quit",command=self.quit)
        self.quit_button.grid(row=3,column=1)

    ### FUNCTIONS ###

    # function to copy and paste line by line from input box to output box
    def get_line(self):
        if(self.input_code.get(str(self.line_num+1)+'.0',str(self.line_num+1)+".0 lineend") != ""):
            input = self.input_code.get(str(self.line_num+1)+'.0',str(self.line_num+1)+".0 lineend")
            self.line_num += 1
            self.line.config(state=NORMAL)
            self.line.delete(0,END)
            self.line.insert(0,str(self.line_num))
            self.line.config(state=DISABLED)

            self.output_lex.config(state=NORMAL)
            self.output_lex.insert(str(self.line_num)+'.0',input+'\n')
            self.output_lex.config(state=DISABLED)

    # function to reset both text boxes along with setting the initial value of line counter to 0
    def quit(self):
        self.line_num = 0
        self.line.config(state=NORMAL)
        self.line.delete(0,END)
        self.line.insert(0,"0")
        self.line.config(state=DISABLED)

        self.input_code.delete("1.0","end")

        self.output_lex.config(state=NORMAL)
        self.output_lex.delete("1.0","end")
        self.output_lex.config(state=DISABLED)

if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = GUI(myTkRoot)
    myTkRoot.mainloop()
    