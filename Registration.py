from tkinter import *
from tkinter import messagebox
from enum import *


class Countries(Enum):
    UAE = "United Arab Emirates"
    US = "United States"
    UK = "United Kingdom"
    Germany = "Germany"
    Austria = "Austria"


class Gender(Enum):
    Male = 0
    Female = 1


class MainForm:
    def __init__(self):
        # Creating form using Class Tk()
        self.form = Tk()

        # Providing Geometry to the form
        self.form.geometry("500x500")

        # Providing title to the form
        self.form.title('Registration form')

        # this creates 'Label' widget for Registration Form and uses place() method.
        self.label_0 = Label(self.form, text="Registration form", width=20, font=("bold", 20))
        # place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
        self.label_0.place(x=90, y=60)

        # this creates 'Label' widget for Fullname and uses place() method.
        self.label_1 = Label(self.form, text="FullName", width=20, font=("bold", 10))
        self.label_1.place(x=80, y=130)

        # this will accept the input string text from the user.
        self.name = Entry(self.form)
        self.name.place(x=240, y=130)

        # this creates 'Label' widget for Email and uses place() method.
        self.label_3 = Label(self.form, text="Email", width=20, font=("bold", 10))
        self.label_3.place(x=68, y=180)

        self.email = Entry(self.form)
        self.email.place(x=240, y=180)

        # this creates 'Label' widget for Gender and uses place() method.
        self.label_4 = Label(self.form, text="Gender", width=20, font=("bold", 10))
        self.label_4.place(x=70, y=230)

        # the variable 'gender' mentioned here holds Integer Value, by default 0 as Male
        self.gender = IntVar()

        # this creates 'Radio button' widget and uses place() method
        self.r1 = Radiobutton(self.form, text="Male", padx=5, variable=self.gender, value=0).place(x=235, y=230)
        self.r2 = Radiobutton(self.form, text="Female", padx=20, variable=self.gender, value=1).place(x=290, y=230)

        # this creates 'Label' widget for country and uses place() method.
        self.l5 = label_5 = Label(self.form, text="Country", width=20, font=("bold", 10))
        self.l5 = label_5.place(x=70, y=280)

        # the variable 'country' mentioned here holds String Value, by default "UAE"
        self.country = StringVar()
        # the dropdown list requires a list of values, therefore a for loop on the Countries enum
        self.droplist = OptionMenu(self.form, self.country, *[e.value for e in Countries])
        self.droplist.config(width=20)
        self.country.set(Countries.UAE.value)  # setting the first value from the list to be UAE
        self.droplist.place(x=240, y=280)

        # this creates 'Label' widget for Language and uses place() method.
        self.label_6 = Label(self.form, text="Programming", width=20, font=('bold', 10))
        self.label_6.place(x=75, y=330)

        # the variable 'JavaValue' mentioned here holds boolean Value, by default True
        self.javaValue = BooleanVar()
        self.javaValue.set(False)
        # this creates Checkbutton widget and uses place() method.
        self.cb1 = Checkbutton(self.form, text="Java", variable=self.javaValue).place(x=230, y=330)

        # the variable 'pythonValue' mentioned here holds  boolean, by default False
        self.pythonValue = BooleanVar()
        self.pythonValue.set(False)
        self.cb2 = Checkbutton(self.form, text="Python", variable=self.pythonValue).place(x=290, y=330)

        # this creates button for submitting the details provides by the user
        self.b0 = Button(self.form, text='Submit', width=20,  command=self.submit).place(x=180, y=380)

        # this will run the mainloop.
        self.form.mainloop()

    # funtion that gets the selection of the user's languages
    def getLanguages(self):
        languages = ""
        if self.javaValue.get():
            languages += "Java"
        if self.pythonValue.get():
            languages += " Python"
        return languages

    def submit(self):
        #  check whether necessary information is filled in
        if self.name.get() == "":           # calls messagebox if name is empty
            messagebox.showwarning("Empty Fields", "You must Enter name.")

        elif self.email.get() == "":                # calls messagebox if email is empty
            messagebox.showwarning("Empty Fields", "You must Enter email.")

        elif not (self.pythonValue.get() or self.javaValue.get()):  # calls when both of the check boxes are unselected, i.e, False or False that gives False, so we reverse it using not and shows a message to select one
            messagebox.showwarning("Empty Fields", "You must Enter programming.")
        else:                               # if all the information is filled, then we add the data to our text file
            file_object = open('q4-data.txt', 'a')
            file_object.write(
                "User's Name:{} Email:{} {} Country:{} Languages:{}\n".format(self.name.get(), self.email.get(),
                                                                              Gender(self.gender.get()), self.country.get(),
                                                                              self.getLanguages()))


mw = MainForm()
