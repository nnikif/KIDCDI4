import tkinter as tk
import form_values as fv

class KeyboardInput():
    def __init__(self,ttype,array1):
        if ttype=="RCDI":
            self.texts=fv.CDI_QUESTIONS
        elif ttype=="KID":
            self.texts=fv.KID_QUESTIONS
        self.ttype=ttype
        self.q_number=len(self.texts)
        self.draw_window()
        self.load_answers(array1)
        self.i=0
        self.show_answ()
        self.window.grab_set()
        self.window.protocol("WM_DELETE_WINDOW",self.rollback_answers)
    
    def draw_window(self):
        self.window=tk.Toplevel()
        self.window.title("Ввод результатов из вопросника "+self.ttype)
        self.question=tk.StringVar()
        ques_text=tk.Label(self.window,height=10,width=110,
                           textvariable=self.question,
                           wraplength=460,justify="left")
        ques_text.grid(column=0,row=0,columnspan=3,sticky="W")
        
        answerL=tk.Label(self.window)
        self.answer_val=self._radio_button4(answerL,fv.ANSWERS)
        answerL.grid(column=0,row=1)
        
        tk.Button(self.window,text="<<Назад",command=self.move_left).grid(column=0,row=2)
        tk.Button(self.window,text="Сохранить и закрыть",command=self.close).grid(column=1,row=2)
        tk.Button(self.window,text="Вперед>>",command=self.move_right).grid(column=2,row=2)
        
        self.window.bind('0',self.ent_0)
        self.window.bind('1',self.ent_1)
        self.window.bind('2',self.ent_2)
        self.window.bind('3',self.ent_3)
        
    def _radio_button4(self,master,answer_var):
        v=tk.IntVar()
        for i in range(4):
            tk.Radiobutton(master,text=answer_var[i],value=i,variable=v).grid(column=0,row=i,sticky='W')
        return v
    def reset_answers(self):
        self.answers=[0]*self.q_number
        self.show_answ()
    def load_answers(self,array):
        self.answers=array[:]
        self.backup=array[:]
    
    def save_answ(self):
        self.answers[self.i]=self.answer_val.get()

    def show_answ(self):
        self.question.set("Вопрос "+str(self.i+1)+":\n"+self.texts[self.i])
        self.answer_val.set(self.answers[self.i])

    def ent_1(self,event):
        self.answer_val.set(1)
        self.move_right()

    def ent_0(self,event):
        self.answer_val.val.set(0)
        self.move_right()    

    def ent_2(self,event):
        self.answer_val.set(2)
        self.move_right()

    def ent_3(self,event):
        self.answer_val.set(3)
        self.move_right()

    def move_right(self):
        if self.i<self.q_number-1:
            self.save_answ()
            self.i+=1
            self.show_answ()

    def move_left(self):
        if self.i>0:
            self.save_answ()
            self.i-=1
            self.show_answ()

    def rollback_answers(self):
        self.answers=self.backup
        self.window.destroy()

    def return_answers(self):
        return self.answers

    def close(self):
        self.save_answ()
        self.window.destroy()
        
# if __name__ == '__main__':
#     work_window=KeyboardInput("RCDI")
#     work_window.reset_answers()
#     work_window.window.mainloop()
#         
#     