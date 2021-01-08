#Aashiq Adams
#importing modules
from tkinter import *
from tkinter import ttk

#function which calculates user bmi using weight and height
def CalcBMI(w,h):
    try:
        w1=int(w)
        h1=int(h)
        print(w1,h1)
        result = w1/(h1*h1)
        bmi_result_label.config(text="Done")
    except ValueError:
        return
    

#function which calculates ideal bmi using weight, height and age
def CalcIdealBMI(w,h,a):
    try:
        w1=int(w)
        h1=int(h)
        result = w1/(h1*h1)
        return result
    except ValueError:
        return

#combined functions
def combined():
    CalcBMI(weight,height)
    CalcIdealBMI(weight,height,age)
    return
#creating a new name for 'master' to callback easier
bmi = Tk()
bmi.title("Ideal BMI Calculator")

#create canvas for icon image and put image on canvas
icon_canvas = Canvas(bmi, width=500, height=100)
icon_canvas.grid()
icon = PhotoImage(file="gym.png")
icon_canvas.create_image(0, 0, anchor=NW, image=icon)

#label for heading and sub-heading
header = Label(bmi, text="--Ideal Body Mass Index Calculator--", font=("Arial", 25))
header.grid()

sub_header = Label(bmi,text ="Enter your Weight, Height and Gender Below:",font=("Arial", 18))
sub_header.grid()

#input weight and height
weight_label = Label(bmi, text="Weight (kg): ",font=("Arial", 12))
weight_label.grid(row=3, column=0, sticky = W,pady=8)
w = Entry(bmi)
weight=w.get()

w.grid(row=3, column=0,padx = 100, sticky=W,pady=8)


height_label = Label(bmi, text="Height (cm): ",font=("Arial", 12))
height_label.grid(row=4, column=0, sticky = W,pady=8)
h = Entry(bmi)
height=h.get()

h.grid(row=4, column=0, padx = 100, sticky=W,pady=8)


#select gender
gender_label = Label(bmi, text="Gender: ",font=("Arial", 12))
gender_label.grid(row=5, column=0, sticky = W,pady=8)
gender = ttk.Combobox(bmi, values=["Male","Female"])
gender.set("Select")
gender.grid(row=5, column=0, padx = 100, sticky=W,pady=8)

#enter age
age_label = Label(bmi, text="Age: ",font=("Arial", 12))
age_label.grid(row=5, column=0, sticky = W, padx=300,pady=8)
age = Entry(bmi)
age.grid(row=5, column=0,padx = 350, sticky=W,pady=8)
age.get()

#Calculate button

calc_btn = Button(bmi, text="Calculate Your BMI", command=CalcBMI(weight,height))
calc_btn.grid(row=6, sticky=W, padx=150, pady=25)

#display bmi solution
bmi_label = Label(bmi, text="BMI: ")
bmi_label.grid(row=7, sticky=W)

bmi_result_label = Label(bmi, borderwidth=2)
bmi_result_label.grid(row=7,padx=50, sticky=W)

#display ideal bmi solution
ideal_bmi_label = Label(bmi, text="Ideal BMI: ")
ideal_bmi_label.grid(row=7, sticky=W, padx=150,pady=10)

ideal_bmi_result_label = Label(bmi,borderwidth=2)
ideal_bmi_result_label.grid(row=7, sticky=W,padx=230,pady=10)

#clear button
clear_btn = Button(bmi, text="Clear")
clear_btn.grid(row=8, sticky=W, pady=10)

#exit button
exit_btn = Button(bmi, text="Exit")
exit_btn.grid(row=8,sticky=W,padx=100,pady=10)

bmi.mainloop()

#apologies for incomplete code. i was not good enough to make it work.