# pip install tk
# pip install DateTime
from tkinter import *
import datetime
from datetime import date

def date_time():
	time=datetime.datetime.now()
	hr=time.strftime('%I')
	min=time.strftime('%M')
	sec=time.strftime('%S')
	apm=time.strftime('%p')
	lab_hr.config(text=hr)
	lab_min.config(text=min)
	lab_sec.config(text=sec)
	lab_apm.config(text=apm)
	today=date.today()
	datee=today.strftime('%d')
	month=today.strftime('%m')
	year=today.strftime('%Y')
	day=today.strftime('%a')
	lab_date.config(text=datee)
	lab_month.config(text=month)
	lab_year.config(text=year)
	lab_day.config(text=day)
	lab_hr.after(200,date_time)

clock=Tk()
clock.title("****Digital Clock****")
clock.geometry('800x500')
clock.config(bg="Gray")

lab_hr = Label(clock,text="00",font=("Time New Roman",60,'bold'),bg="Black",fg="White")
lab_hr.place(x=40,y=40,height=100,width=150)
lab_hr_txt = Label(clock,text="Hours",font=("Time New Roman",30,'bold'),bg="Black",fg="White")
lab_hr_txt.place(x=40,y=160,height=50,width=150)

lab_min = Label(clock,text="00",font=("Time New Roman",60,'bold'),bg="Black",fg="White")
lab_min.place(x=230,y=40,height=100,width=150)
lab_min_txt = Label(clock,text="Minutes",font=("Time New Roman",30,'bold'),bg="Black",fg="White")
lab_min_txt.place(x=230,y=160,height=50,width=150)

lab_sec = Label(clock,text="00",font=("Time New Roman",60,'bold'),bg="Black",fg="White")
lab_sec.place(x=420,y=40,height=100,width=150)
lab_sec_txt = Label(clock,text="Seconds",font=("Time New Roman",27,'bold'),bg="Black",fg="White")
lab_sec_txt.place(x=420,y=160,height=50,width=150)

lab_apm = Label(clock,text="00",font=("Time New Roman",50,'bold'),bg="Black",fg="White")
lab_apm.place(x=610,y=40,height=100,width=150)
lab_apm_txt = Label(clock,text="Am/Pm",font=("Time New Roman",30,'bold'),bg="Black",fg="White")
lab_apm_txt.place(x=610,y=160,height=50,width=150)

lab_date = Label(clock,text="00",font=("Time New Roman",60,'bold'),bg="Black",fg="White")
lab_date.place(x=40,y=250,height=100,width=150)
lab_date_txt = Label(clock,text="Date",font=("Time New Roman",30,'bold'),bg="Black",fg="White")
lab_date_txt.place(x=40,y=370,height=50,width=150)

lab_month = Label(clock,text="00",font=("Time New Roman",60,'bold'),bg="Black",fg="White")
lab_month.place(x=230,y=250,height=100,width=150)
lab_month_txt = Label(clock,text="Month",font=("Time New Roman",30,'bold'),bg="Black",fg="White")
lab_month_txt.place(x=230,y=370,height=50,width=150)

lab_year = Label(clock,text="00",font=("Time New Roman",45,'bold'),bg="Black",fg="White")
lab_year.place(x=420,y=250,height=100,width=150)
lab_year_txt = Label(clock,text="Year",font=("Time New Roman",30,'bold'),bg="Black",fg="White")
lab_year_txt.place(x=420,y=370,height=50,width=150)
 
lab_day = Label(clock,text="00",font=("Time New Roman",50,'bold'),bg="Black",fg="White")
lab_day.place(x=610,y=250,height=100,width=150)
lab_day_txt = Label(clock,text="Day",font=("Time New Roman",30,'bold'),bg="Black",fg="White")
lab_day_txt.place(x=610,y=370,height=50,width=150)

date_time()
clock.mainloop()
