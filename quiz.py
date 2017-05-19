import tkinter as tk
from tkinter import ttk
import form_values as fv
import datetime
from tkinter import messagebox
from functions_modules import read_datetime
from database_work import dbase

class Quiz():
    def __init__(self,master):
        self.dict={}
#         self.window=self.launch_window(master)
        self._fill_window(master)
        
        
    def _fill_window(self,master):
        nameL = tk.LabelFrame(master)
        nameL.grid(column=0, row=0, padx=8, pady=4,columnspan=3)

        ttk.Label(nameL, text="Фамилия, Имя").grid(column=0, row=0,sticky="W")
        self.dict['name']=tk.StringVar()
        nameEntered = ttk.Entry(nameL, width=34, textvariable=self.dict['name'])
        nameEntered.grid(column=1, row=0)

        col1L = tk.Label(master)
        col1L.grid(column=0, row=1)

        gendL=ttk.LabelFrame(col1L, text="Пол")
        gendL.grid(column=0, row=0,sticky='W')
        self.dict["gender"]=self._radioB(gendL,fv.GENDER)

        datesL=tk.Label(col1L)
        datesL.grid(column=0,row=1,sticky="W")
        birthL=ttk.LabelFrame(datesL,text="Дата рождения:")
        birthL.grid(column=0,row=0,sticky="W")
        self.dict["d_birth"]=tk.IntVar()
        ttk.Entry(birthL,width=3,textvariable=self.dict["d_birth"]).grid(row=0,column=0,sticky="W")
        self.dict["m_birth"]=tk.IntVar()
        ttk.Entry(birthL,width=3,textvariable=self.dict["m_birth"]).grid(row=0,column=1,sticky="W")
        self.dict["y_birth"]=tk.IntVar()
        ttk.Entry(birthL,width=5,textvariable=self.dict["y_birth"]).grid(row=0,column=2,sticky="W")
        fillL=ttk.LabelFrame(datesL,text="Дата заполнения:")
        fillL.grid(column=1,row=0,sticky="W")
        self.dict["d_fill"]=tk.IntVar()
        ttk.Entry(fillL,width=3,textvariable=self.dict["d_fill"]).grid(row=0,column=0,sticky="W")
        self.dict["m_fill"]=tk.IntVar()
        ttk.Entry(fillL,width=3,textvariable=self.dict["m_fill"]).grid(row=0,column=1,sticky="W")
        self.dict["y_fill"]=tk.IntVar()
        ttk.Entry(fillL,width=5,textvariable=self.dict["y_fill"]).grid(row=0,column=2,sticky="W")
        
        addressV=ttk.LabelFrame(col1L,text="Адрес: ")
        addressV.grid(column=0,row=2,sticky="W")
        self.dict["address"]=tk.StringVar()
        ttk.Entry(addressV,width=35,textvariable=self.dict["address"]).grid(row=0,column=0)
        
        phoneV=ttk.LabelFrame(col1L,text="Телефон: ")
        phoneV.grid(column=0,row=3,sticky="W")
        self.dict["phone"]=tk.StringVar()
        ttk.Entry(phoneV,width=35,textvariable=self.dict["phone"]).grid(row=0,column=0)
        
        numbercV=ttk.LabelFrame(col1L,text="Количество детей в семье: ")
        numbercV.grid(column=0,row=4,sticky="W")
        self.dict["numberofkids"]=tk.IntVar()
        ttk.Entry(numbercV,width=2,textvariable=self.dict["numberofkids"]).grid(row=0,column=0)
        
        birthWV=ttk.LabelFrame(col1L,text="На какой недели родился: ")
        birthWV.grid(column=0,row=5,sticky="W")
        self.dict["weekofbirth"]=tk.IntVar()
        ttk.Entry(birthWV,width=2,textvariable=self.dict["weekofbirth"]).grid(row=0,column=0)

        parentsW=ttk.LabelFrame(col1L,text="Данные о родителях: ")
        parentsW.grid(column=0,row=6)
        ttk.Label(parentsW,text="Возраст").grid(row=0,column=1)
        ttk.Label(parentsW,text="Образование").grid(row=0,column=2)
        ttk.Label(parentsW,text="Мать").grid(row=1,column=0)
        ttk.Label(parentsW,text="Отец").grid(row=2,column=0)
        ttk.Label(parentsW,text="Воспитатель").grid(row=3,column=0)
        self.dict["m_age"]=tk.IntVar()
        ttk.Entry(parentsW,width=3,textvariable=self.dict["m_age"]).grid(row=1,column=1)
        self.dict["f_age"]=tk.IntVar()
        ttk.Entry(parentsW,width=3,textvariable=self.dict["f_age"]).grid(row=2,column=1)
        self.dict["g_age"]=tk.IntVar()
        ttk.Entry(parentsW,width=3,textvariable=self.dict["g_age"]).grid(row=3,column=1)
        
        m_edu=tk.StringVar()
        comboM=ttk.Combobox(parentsW,textvariable=m_edu,values=fv.P_EDUCATION,state="readonly")
        comboM.grid(row=1,column=2)
        self.dict['m_edu']=tk.IntVar()
        self.dict["m_edu"].get=comboM.current
        self.dict["m_edu"].set=comboM.current
      
        
        f_edu=tk.StringVar()
        comboF=ttk.Combobox(parentsW,textvariable=f_edu,values=fv.P_EDUCATION,state="readonly")
        self.dict['f_edu']=tk.IntVar()
        self.dict["f_edu"].get=comboF.current
        self.dict["f_edu"].set=comboF.current
        comboF.grid(row=2,column=2)
        
        
        g_edu=tk.StringVar()
        comboG=ttk.Combobox(parentsW,textvariable=g_edu,values=fv.P_EDUCATION,state="readonly")
        comboG.grid(row=3,column=2)
        self.dict['g_edu']=tk.IntVar()
        self.dict["g_edu"].get=comboG.current
        self.dict["g_edu"].set=comboG.current
        
#         
#         tk.Button(col1L,text="Сохранить изменения",command=self.read_with_dates).grid(row=7,column=0)
#         tk.Button(nameL,text="Загрузить RCDI тест",command=self.load_tmp).grid(row=0,column=2)
#         tk.Button(nameL,text="Ручной ввод теста RCDI",command=self.manualinputCDI).grid(row=0,column=3)

        col2L=tk.Label(master)
        col2L.grid(column=1, row=1)

        whoFillsL=ttk.LabelFrame(col2L, text="Кто заполняет анкету: ")
        whoFillsL.grid(column=0, row=0,sticky='W')
        self.dict["whofills"]=self._radioB(whoFillsL,fv.PEOPLE)
                
        healthL=ttk.LabelFrame(col2L, text="Состояние здоровья: ")
        healthL.grid(column=0, row=1,sticky='W')
        self.dict["health"]=self._radioB(healthL,fv.HEALTH)


        educL=ttk.LabelFrame(col2L, text="Где воспитывается ребенок: ")
        educL.grid(column=0, row=2,sticky='W')
        self.dict["where_edu"]=self._radioB(educL,fv.EDUCATION)

        whoEduL=ttk.LabelFrame(col2L, text="Кто воспитывает ребенка: ")
        whoEduL.grid(column=0, row=5,sticky='W')
        self.dict["who_edu"]=self._radioB(whoEduL,fv.WHOEDUS)


        whoBestL=ttk.LabelFrame(col2L, text="Что ценит воспитатель в детях: ")
        whoBestL.grid(column=0, row=6,sticky='W')
        self.dict["what_best"]=self._radioB(whoBestL,fv.BEST)
        

        col3L=tk.Label(master)
        col3L.grid(column=2, row=1)

        birthPL=ttk.LabelFrame(col3L, text="Были ли осложнения при родах: ")
        birthPL.grid(column=0, row=0,sticky='W')
        self.dict["birth_complications"]=self._radioB(birthPL,fv.BIRTH)

        seizuresL=ttk.LabelFrame(col3L, text="Бывают ли судороги: ")
        seizuresL.grid(column=0, row=1,sticky='W')
        self.dict["seizures"]=self._radioB(seizuresL,fv.SEIZURES)

        languagesL=ttk.LabelFrame(col3L, text="На каком языке говорят дома: ")
        languagesL.grid(column=0, row=2,sticky='W')
        self.dict["language"]=self._radioB(languagesL,fv.LANGUAGE)

        moodL=ttk.LabelFrame(col3L, text="Обычное настроение воспитателя: ")
        moodL.grid(column=0, row=3,sticky='W')
        self.dict["mood"]=self._radioB(moodL,fv.MOOD)

        financeL=ttk.LabelFrame(col3L, text="Финансовое положение семьи: ")
        financeL.grid(column=0, row=4,sticky='W')
        self.dict["finance"]=self._radioB(financeL,fv.FINANCE)        
        
     
    def _radioB(self,master,answers):
        v=tk.IntVar()
        v.set(0)
        
        for i in range(len(answers)):
            tk.Radiobutton(master,text=answers[i],value=i,variable=v).grid(column=i%2,row=2+i//2,sticky='W')
        return v       
        
    def _read(self):
        dict1={}
        for item in self.dict:

            dict1[item]=self.dict[item].get()
        
        return dict1
    
    def setbydict(self,dict1):
        for item in dict1:

            self.dict[item].set(dict1[item])

    def read_with_dates(self):
        dict_wd={}
        dict_raw=self._read()
        for key in dict_raw:
            if key not in fv.DATE_VALUES:
                dict_wd[key]=dict_raw[key]
            
        try:
            dict_wd["birthday"]=datetime.date(dict_raw["y_birth"],dict_raw["m_birth"],dict_raw["d_birth"])

        except:
            messagebox.showinfo("Ошибка даты", "Введите корректный день рождения")
            return
        try:
            dict_wd["day_filled"]=datetime.date(dict_raw["y_fill"],dict_raw["m_fill"],dict_raw["d_fill"])
        except:
            messagebox.showinfo("Ошибка даты", "Введите корректный день заполнения анкеты")
            return
        
#         print(dict_wd)
#         self.dict_temp=dict_wd
        return dict_wd
    
#     def load_tmp(self):
#         self.load_with_dates(self.dict_temp)    
    
    def load_with_dates(self,dict_incoming):
        dict1={}
        for key in dict_incoming:
            dict1[key]=dict_incoming[key]
            if dict1[key]==-1: 
                dict1[key]=0
                
#             print(key, dict1[key])
                
        dict1['d_fill'],dict1["m_fill"],dict1["y_fill"]=read_datetime(dict1.pop("day_filled"))
        dict1["d_birth"],dict1['m_birth'],dict1["y_birth"]=read_datetime(dict1.pop("birthday")) 
#         print(dict1)   
        self.setbydict(dict1)
        
    def load_name(self):
        dict1={}
        rp=dbase.load_name_only(self.child_id)
        dict1["name"] = rp["name"]
        dict1["d_birth"],dict1['m_birth'],dict1["y_birth"]=read_datetime(rp["birthday"]) 
        self.setbydict(dict1)   

    
if __name__ == '__main__':
    window = tk.Tk()
    tabcontrol=ttk.Notebook(window)
    
    
    qz=Quiz(window)
    window.mainloop()
    