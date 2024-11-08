import tkinter
from tkinter import messagebox
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

'''Create a program for a BMI calculator that takes the name, age, height, and weight of a person and stores the data into a file. 
Allow the application to show weather the user is Underweight, Overweight, Obese, or Normal. Make sure you add validation rules. 
Add a ‘Show Graph’ button that display a pie chart of the data stored, showing the percentage of people under certain BMI categories. 
Challenge: Can you allow the chart to show on the same window? You may need to use another library'''

def calculate_bmi():
    try:
        height = float(heightentry.get())
        if height<3:
            height = height*100
        weight = float(weightentry.get())
        bmi = weight / ((height/100) ** 2)
        return round(bmi, 2)
    except ValueError:
        tkinter.messagebox.showwarning(title='Error: Incorrect Input', message='Please enter valid numbers for weight and height.')


def show_bmi():
    name = nameentry.get()
    age = ageentry.get()
    height = heightentry.get()
    weight = weightentry.get()

    if name == "" and age == "" and height == "" and weight == "":
        tkinter.messagebox.showwarning(title='Error: Missing Data', message='Please fill in all fields.')
        return

    try:
        age = int(age)
        height = int(height)
        weight = int(weight)
    except ValueError:
        tkinter.messagebox.showwarning(title='Error', message='Please enter a valid data.')
        return

    if age < 18:
        tkinter.messagebox.showwarning(title='Error!', message='BMI calculations for individuals under 18 may not be accurate.')
        return


    bmi = calculate_bmi()
    category = get_bmi_category(bmi)
    save_data(name, age, height, weight, bmi, category)
    print("BMI: " + str(bmi) + ", Category: " + category)
    outputlabel.config(text=name.upper() + "'S BMI = " + str(bmi) + '\n\nCategory: ' + category)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def save_data(name, age, height, weight, bmi, category):
    with open ('BMI_calculator.txt','a') as filewrite:
        filewrite.write(name+':\t'+str(height)+' m, '+str(weight)+' kg, '+str(age)+' years.\tBMI = '+str(bmi)+' Category: '+str(category)+'\n')

def extract_categories():
    categories=[]
    with open('BMI_calculator.txt','r') as file:
      for line in file:
        parts=line.split('Category: ')
        if len(parts) > 1:
            category=parts[1].strip()
            categories.append(category)
    return categories

def create_pie_chart():
    categories_list = extract_categories()
    category_count=Counter(categories_list)
    labels=list(category_count.keys())
    sizes=list(category_count.values())

    name = nameentry.get()
    age = ageentry.get()
    height = heightentry.get()
    weight = weightentry.get()

    if name == "" and age == "" and height == "" and weight == "":
        tkinter.messagebox.showwarning(title='Error: Missing Data', message='Please first fill in all fields.')
        return

    total_people = sum(sizes)

    fig,ax = plt.subplots(figsize=(4,4))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.set_title('BMI Categories Statistic')
    ax.text(0,-1.3,"Total participants:" + str(total_people), fontsize=12, color='black')

    canvas = FigureCanvasTkAgg(fig, master=piechartframe)
    canvas.draw()  # Draw the pie chart on the canvas
    canvas.get_tk_widget().pack()

window=tkinter.Tk()
window.title('BMI Calculator')

frame=tkinter.Frame(window)
frame.pack()

userinfoframe=tkinter.LabelFrame(frame,text="User's Data")
userinfoframe.grid(row=0,column=0)

#name
namelabel=tkinter.Label(userinfoframe,text='Name')
namelabel.grid(row=0,column=0)
nameentry=tkinter.Entry(userinfoframe)
nameentry.grid(row=0,column=1)
namelabel1=tkinter.Label(userinfoframe,text='        ')
namelabel1.grid(row=0,column=2)

#age
agelabel=tkinter.Label(userinfoframe,text='Age')
agelabel.grid(row=1,column=0)
ageentry=tkinter.Entry(userinfoframe)
ageentry.grid(row=1,column=1)

#height
heightlabel=tkinter.Label(userinfoframe,text='Height in cm')
heightlabel.grid(row=2,column=0)
heightentry=tkinter.Entry(userinfoframe)
heightentry.grid(row=2,column=1)

#weight
weightlabel=tkinter.Label(userinfoframe,text='Weight in kg')
weightlabel.grid(row=3,column=0)
weightentry=tkinter.Entry(userinfoframe)
weightentry.grid(row=3,column=1)

#calculate_BMI button
calculatebtn=tkinter.Button(frame,text='Calculate BMI',command=show_bmi)
calculatebtn.grid(row=1,column=0)

# BMI Output frame
outputframe = tkinter.LabelFrame(frame, text='BMI')
outputframe.grid(row=2, column=0)

# Create the output label for BMI results
outputlabel = tkinter.Label(outputframe, text='BMI CALCULATION\n')
outputlabel.grid(row=0, column=0)

#Show graph button
graphbtn = tkinter.Button(frame, text="Show Graph", command=create_pie_chart)
graphbtn.grid(row=4, column=0)

#Pie Chart Frame
piechartframe = tkinter.LabelFrame(frame, text='SEE CHART')
piechartframe.grid(row=4, column=0)

#BMI RANGE output
userinfoframe1=tkinter.LabelFrame(frame,text="BMI_RANGE\n")
userinfoframe1.grid(row=3,column=0)

Underweight=tkinter.Label(userinfoframe1,text='Underweight')
Underweight.grid(row=0,column=0)
Underweight1=tkinter.Label(userinfoframe1,text='Under 18.5')
Underweight1.grid(row=0,column=1)

Normal_weight=tkinter.Label(userinfoframe1,text='Normal weight')
Normal_weight.grid(row=1,column=0)
Normal_weight1=tkinter.Label(userinfoframe1,text='18.5 to 24.9')
Normal_weight1.grid(row=1,column=1)

Overweight=tkinter.Label(userinfoframe1,text='Overweight')
Overweight.grid(row=2,column=0)
Overweight1=tkinter.Label(userinfoframe1,text='25 to 29.9')
Overweight1.grid(row=2,column=1)

Obese=tkinter.Label(userinfoframe1,text='Obese\n')
Obese.grid(row=3,column=0)
Obese1=tkinter.Label(userinfoframe1,text='30 or above\n')
Obese1.grid(row=3,column=1)


window.mainloop()
