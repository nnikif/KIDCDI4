import tkinter as tk
from tkinter import ttk
from database_work import dbase
import qtest

class WidgetRoot():
    
    def __init__(self):
        self.win=tk.Tk()
        self.win.title("Тесты KID/RCDI-2000")
        self.tabcontrol=ttk.Notebook(self.win)
        self.tabcontrol.pack()
        self.tab01=ttk.Frame(self.tabcontrol)
        self.tabcontrol.add(self.tab01, text="База данных")
        self._setKidsList(self.tab01)
        self.showinTab('')
        
        self.tab02=ttk.Frame(self.tabcontrol)
        self.tabcontrol.add(self.tab02, text="Список тестов")
        self._setTestsList(self.tab02)

    def _setKidsList(self,master):


        self.nameS=tk.StringVar()
        searchN=tk.Entry(master,width=30,textvariable=self.nameS)
        searchN.grid(column=0,row=0,sticky="W")
        searchN.bind("<Return>",self.showInTabSearch)

        tk.Button(master,text="Новый ребенок, тест KID",command=self.runKID).grid(column=1,row=0)
        tk.Button(master,text="Новый ребенок, тест RCDI",command=self.runRCDI).grid(column=1,row=1,sticky="N")
        
        self.tree= ttk.Treeview(master,selectmode='browse')
        self.tree["columns"]="name","birthday"
        self.tree["height"]=25
        self.tree.heading('#0',text="ID")
        self.tree.column("#0",width=40,minwidth=0)
        self.tree.column("name",width=250)
        self.tree.heading("name",text="Фамилия, Имя")
        self.tree.column("birthday",width=100)
        self.tree.heading("birthday",text="День рождения")

        self.tree.bind('<Double-Button-1>',self._selectChild)
        self.tree.bind('<Return>',self._selectChild)
        self.tree.grid(column=0,row=1)  
        
    def _setTestsList(self,master):

        newTSTB=tk.Button(master,text="Новый тест KID",command=self.newKID)
        newTSTB.grid(column=2,row=0)
        newTSTB=tk.Button(master,text="Новый тест RCDI",command=self.newRCDI)
        newTSTB.grid(column=2,row=1,sticky="N")
        # self.newTSTB.idex_m=1
        self.kidname=tk.StringVar()
        tk.Label(master,textvariable=self.kidname).grid(column=0,row=0)
        self.treeR= ttk.Treeview(master,selectmode='browse')
        self.treeR["columns"]="date_fill"
        self.treeR["height"]=25
        self.treeR.heading('#0',text="ID")
        self.treeR.column("#0",width=0,minwidth=0)      
        self.treeR.column("date_fill",width=130)
        self.treeR.heading("date_fill",text="Тесты RCDI:")
        self.treeR.bind('<Double-Button-1>',self.loadRCDITest)
        self.treeR.bind('<Return>',self.loadRCDITest)
        self.treeR.grid(column=0,row=1)  
        
        self.treeK= ttk.Treeview(master,selectmode='browse')
        self.treeK["columns"]="date_fill"
        self.treeK["height"]=25
        self.treeK.heading('#0',text="ID")
        self.treeK.column("#0",width=0,minwidth=0)      
        self.treeK.column("date_fill",width=130)
        self.treeK.heading("date_fill",text="Тесты KID:")
        self.treeK.bind('<Double-Button-1>',self.loadKIDTest)
        self.treeK.bind('<Return>',self.loadKIDTest)
        self.treeK.grid(column=1,row=1)
        
    def _selectChild(self,a):
        curItem=self.tree.focus()
        curIdx=self.tree.item(curItem)["text"]
        self.showTests(curIdx)
        self.child_idx=curIdx

        self.tabcontrol.select(self.tab02)    
        
    def showTests(self,id):
        self.kidname.set(dbase.nameybyid(id))
        self.treeR.delete(*self.treeR.get_children())
        data=dbase.testlist(id,"RCDI")
        for test in data:
            self.treeR.insert("",1000,text=test[0],values=test[1]) 
        
        self.treeK.delete(*self.treeK.get_children())
        data=dbase.testlist(id,"KID")
        for test in data:
            self.treeK.insert("",1000,text=test[0],values=test[1])
           
#         
    def showinTab(self,nameS):
        data=dbase.kidslist(nameS)
        self.tree.delete(*self.tree.get_children())
        for person in data:
            self.tree.insert("",100000,text=person[0],values=(person[1],person[2]))   
     
    def showInTabSearch(self,a):
        self.showinTab(self.nameS.get()) 
    
    def runRCDI(self):
        qt=qtest.QTest("RCDI")
#         qt.ttype="RCDI"
        qt.setDBIDX(0, 0)
        self.win.wait_window(qt.window)
        self.showinTab('')
        
    def runKID(self):
        qt=qtest.QTest("KID")
#         qt.ttype="KID"
        qt.setDBIDX(0, 0)
        self.win.wait_window(qt.window)
        self.showinTab('')
    
    def newRCDI(self):
        self.newOLD("RCDI")
        
    def newKID(self):
        self.newOLD("KID")
    
    def newOLD(self,ttype):
        qt=qtest.QTest(ttype)

        qt.setDBIDX(self.child_idx, 0)
        qt.load_name()
        
        self.win.wait_window(qt.window)
        self.showinTab('')
        self.showTests(self.child_idx)
        self.tabcontrol.select(self.tab02)
        
        
    def loadRCDITest(self,a):
        curItem=self.treeR.focus()
        curIdx=self.treeR.item(curItem)["text"]
        self.loadAnyTest(curIdx)
        
    def loadKIDTest(self,a):
        curItem=self.treeK.focus()
        curIdx=self.treeK.item(curItem)["text"]
        self.loadAnyTest(curIdx)     
      
        
    def loadAnyTest(self,idx):
#         dict_load={}
        dict_load=dict(dbase.load_name_n_quiz(idx))

        qt=qtest.QTest(dict_load.pop("testtype"))
        qt.setDBIDX(dict_load.pop("child_id"), dict_load.pop("quiz_id"))
        dict_load.pop('id')
        qt.read_string(dict_load.pop("test"))
        qt.load_with_dates(dict_load)
        self.win.wait_window(qt.window)
        self.showinTab('')
        self.tabcontrol.select(self.tab01)
        
if __name__ == '__main__':
    rootwindow=WidgetRoot()
    rootwindow.win.mainloop()