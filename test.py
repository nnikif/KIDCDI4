import tkinter as tk
import keyboardinput

# from tkinter import ttk
class Test():
    def __init__(self, master,q_number):
        self.q_number=q_number
#         self.window=self.launch_window(master)
        self.answers=self._button_fill(q_number,master)
#         print(self.array)

    
    
    def _button_fill(self,q_number,master):
        x,y=0,0
        questions=[]
#         numb_master=[]
        for i in range(q_number):
            # print(x)
            y+=1
            if not i%4:
                numb_master2=tk.Label(master)
                numb_master2.grid(column=x,row=y)
                y+=1
                # print(y)

            if not i%20:
                x+=1
                y=0
            
            numb_master=tk.Label(master)
            numb_master.grid(column=x,row=y)
            questions.append((self._radio_button3(numb_master,i+1)))

        return questions
            

    def _radio_button3(self,master,number):
        v=tk.IntVar()
        
        tk.Label(master,text=str(number)).grid(row=0,column=0)
        for i in (1,2,3):
            tk.Radiobutton(master,value=i,variable=v).grid(row=0,column=i+1)
        return v
    
    def fill(self,number):
        for i in range(len(self.answers)):
            self.answers[i].set(number)
    
    def read_results(self):
        array=[]
#         print(len(self.answers))
        for i in range(len(self.answers)):
        
#             print(i, self.answers[i].get())
            array.append(self.answers[i].get())
#         print(array)
        return(array)
    
    def load_array(self,array):
        for i in range(len(array)):
            self.answers[i].set(array[i])
            
    def return_string(self):
        str1=''
        arr1=self.read_results()
        for answ in arr1:
            str1+=str(answ)
        return str1
    
    def read_string(self,str1):
        arr1=[]
        for char in str1:
            arr1.append(int(char))        
        self.load_array(arr1)

        




if __name__ == '__main__':
    window=tk.Tk()
#     test=Test(window,216)
#     test.fill(0)
    test=KIDTest(window)
    window.mainloop()
    