from tkinter import *
from tkinter import ttk

from tkinter.filedialog import askopenfilename
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def import_csv_data():
    global v,a,df,b,c,one,two
    
    csv_file_path = askopenfilename()
    v.set(csv_file_path)
    df = pd.read_csv(csv_file_path)
    df.columns = df.columns.str.replace(' ','_')
    a=[]
    a=df.columns
    OPTIONS = sorted(a)
    b=sym1['values'] = OPTIONS 
    c=sym2['values'] = OPTIONS 
    
def plot():
    ss=one.get()
    ss1=two.get()
    plt.plot(df[ss],df[ss1])
    plt.xlabel(ss)
    plt.ylabel(ss1)
    plt.show()
def scatter():
    ss=one.get()
    ss1=two.get()
    #sns.scatterplot(x=ss, y=ss1, hue='Species', data=df)
    plt.scatter(df[ss], df[ss1])
    plt.xlabel(ss)
    plt.ylabel(ss1)
    plt.show()
    plt.legend(labels=[ss,ss1])
def hist():
    ss=one.get()
    ss1=two.get()
    plt.hist(df[ss])
    plt.xlabel(ss)
    plt.ylabel(ss1)
    plt.show()
    plt.legend(labels=[ss,ss1])
def every():
    df.plot.line()
    
root = Tk()

root.resizable(0,0)
v = StringVar()
entry = Entry(root,width = 35, textvariable=v).grid(row=0, column=2,pady=10)
Button(root, text='Browse Data Set',command=import_csv_data).grid(row=0, column=0,pady=10)


one = StringVar()
one.set(None)

two = StringVar()
two.set(None)

sym1 = ttk.Combobox(root, width = 35, textvariable = one) 
sym1.grid(row=3, column=2, pady=10)
sym1.current() 

sym2 = ttk.Combobox(root, width = 35, textvariable = two) 
sym2.grid(row=4, column=2, pady=10) 
sym2.current() 


S1Lb = Label(root,  text="First data")
S1Lb.config(font=("Elephant", 15))
S1Lb.grid(row=3, column=0, pady=10)

S2Lb = Label(root,  text="Second data")
S2Lb.config(font=("Elephant", 15))
S2Lb.grid(row=4, column=0, pady=10)

    
rs = Button(root, text="two columns\nplot", command=plot,height=2,width=10)
rs.config(font=("Elephant", 15))
rs.grid(row=5,column=1,padx=10,sticky=W)

rs = Button(root, text="scatter plot", command=scatter,height=2,width=10)
rs.config(font=("Elephant", 15))
rs.grid(row=5,column=0,padx=10,sticky=W)

rs = Button(root, text="histogram for\nsinlge plot", command=hist,height=2,width=10)
rs.config(font=("Elephant", 15))
rs.grid(row=6,column=0,padx=10,sticky=W)

rs = Button(root, text="whole\n dataset", command=every,height=2,width=10)
rs.config(font=("Elephant", 15))
rs.grid(row=6,column=1,padx=10,sticky=W)





root.mainloop()

#print(OPTIONS)