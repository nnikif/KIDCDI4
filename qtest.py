import tkinter as tk
from tkinter import ttk
from quiz import Quiz
from test import Test
import read_xml
import tkinter.filedialog
import form_values as fv
import keyboardinput
from database_work import dbase
import read_pdf

class QTest(Quiz,Test):
    def __init__(self,ttype):
        self.ttype = ttype
        self.window = tk.Toplevel()
        self.window.title("Анкета+тестовый лист "+ttype)
        tabcontrol = ttk.Notebook(self.window)
        tabcontrol.pack()
        tab01=ttk.Frame(tabcontrol)
        tabcontrol.add(tab01,text="Анкета")
        tab02=ttk.Frame(tabcontrol)
        tabcontrol.add(tab02,text="Тест")
        Quiz.__init__(self,tab01)
        if ttype=="RCDI":
            Test.__init__(self,tab02, 216)
        elif ttype=="KID":
            Test.__init__(self,tab02, 252)
        
        self.window.grab_set()

        tk.Button(tab01,text="Загрузить из .pdf файла",command=self.read_from_pdf).grid(column=0,row=7)
        tk.Button(tab01,text="Ручной ввод теста",command=self.call_keyboard).grid(column=1,row=7)
        tk.Button(tab01,text="Сохранить данные",command=self.save_data).grid(column=2,row=7)
        
    
    def setDBIDX(self,child_id,quiz_id):
        self.child_id=child_id
        self.quiz_id=quiz_id
    

        
         
    def readfromXML(self):
        filename = tk.filedialog.askopenfilename(filetypes = (("XML files", "*.xml"),))
        dict1 = read_xml.parsexml_quiz(filename)
        self.setbydict(dict1)
        array1=read_xml.parsexml_test(filename,fv.QUESTLENGTH[self.ttype])
        self.load_array(array1)
        
    def read_from_pdf(self):
        filename = tk.filedialog.askopenfilename(filetypes = (("PDF files",
                                                               "*.pdf"),))
        dict1, array1 = read_pdf.get_form_fields(filename,
                                                 fv.QUESTLENGTH[self.ttype])
        self.setbydict(dict1)
        self.load_array(array1)
#         print(array1)
        
        
    
    def call_keyboard(self):
        ki=keyboardinput.KeyboardInput(self.ttype,self.read_results())
        self.window.wait_window(ki.window)
        self.load_array(ki.return_answers())
    
    def save_data(self):
        dict_write=self.read_with_dates()
        dict_child={}

        for key in fv.KEYSCHILD:
            dict_child[key]=dict_write.pop(key)
        test_string=self.return_string()
        dict_write["test"]=test_string

        
        if not self.child_id:
            self.child_id=dbase.insert_child(dict_child)[0] 
        else:
            dbase.update_child(dict_child,self.child_id)       
        dict_write['child_id']=self.child_id
        dict_write["testtype"]=self.ttype

        if not self.quiz_id:

            dbase.insert_quiz(dict_write)
        else:

            dbase.update_quiz(dict_write, self.quiz_id)
            
        self.window.destroy()  
    

# class CDIQTest(QTest):
#     def __init__(self):
#         super().__init__("RCDI")
#         self.ttype="RCDI"
#          
# class KIDQTest(QTest):
#     def __init__(self):
#         super().__init__("KID")
#         self.ttype="KID"

if __name__ == '__main__':
    window=tk.Tk()
#     qtest=CDIQTest()
    window.mainloop()
    
        