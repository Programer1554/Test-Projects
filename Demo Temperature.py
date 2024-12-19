from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f5cd573d2f042ffef20dc6a24b61a823").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])
    hum_label1.config(text=data["main"]["humidity"])

win=Tk()
win.title("Python Weather App")
win.config(bg= "skyblue")
win.geometry("500x500")

name_label= Label(win, text="Doon University Weather App",
                 font=("Time New Roman", 20, "italic", "bold", "underline"),bg= "skyblue")
name_label.place(x=25, y=50, height=50,width=450)

city_name= StringVar()

list_name=["Dehradun", "Haridwar", "Roorkee", "Haldwani", "Nainital", "Almora", "Pithoragarh", "Kichha", "Rudrapur", "Kashipur", "Rishikesh", "Kotdwara", "Ramnagar", "MAnglaur", "Jaspur"]
com= ttk.Combobox(win, text="Enter a City name.", values=list_name,
                  font=("Time New Roman", 15, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50,width=450)


w_label= Label(win, text="Weather Climate:",
                 font=("Time New Roman", 16),bg= "skyblue")
w_label.place(x=25, y=260, height=25,width=210)

w_label1= Label(win, text="",
                 font=("Time New Roman", 16),bg= "skyblue")
w_label1.place(x=250, y=260, height=25,width=210)



wb_label= Label(win, text="Weather Description:",
                 font=("Time New Roman", 14),bg= "skyblue")
wb_label.place(x=25, y=300, height=25,width=210)

wb_label1= Label(win, text="",
                 font=("Time New Roman", 14),bg= "skyblue")
wb_label1.place(x=250, y=300, height=25,width=210)



temp_label= Label(win, text="Temperature:",
                 font=("Time New Roman", 14),bg= "skyblue")
temp_label.place(x=25, y=340, height=25,width=210)

temp_label1= Label(win, text="",
                 font=("Time New Roman", 14),bg= "skyblue")
temp_label1.place(x=250, y=340, height=25,width=210)


per_label= Label(win, text="Air Pressure:",
                 font=("Time New Roman", 14),bg= "skyblue")
per_label.place(x=25, y=380, height=25,width=210)

per_label1= Label(win, text="",
                 font=("Time New Roman", 14),bg= "skyblue")
per_label1.place(x=250, y=380, height=25,width=210)


hum_label= Label(win, text="Humidity:",
                 font=("Time New Roman", 14),bg= "skyblue")
hum_label.place(x=25, y=420, height=25,width=210)

hum_label1= Label(win, text="",
                 font=("Time New Roman", 14),bg= "skyblue")
hum_label1.place(x=250, y=420, height=25,width=210)


done_button= Button(win, text="Done",
                  font=("Time New Roman", 15, "bold"),command=data_get)
done_button.place(x=200,y=190, height=50, width=75)

win.mainloop()
