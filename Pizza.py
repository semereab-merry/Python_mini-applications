from tkinter import *
from tkinter import messagebox
# importing tkinter and message box to raise a pop up message


class PizzaShop:
    """"interface that allows user to choose toppings, size and type of a piza and tells the user the amount due """

    # initializing values
    def __init__(self):
        self.total = 0.0                       # initializing the price of the whole pizza
        self.type_txt = ""                      # initializing the text for the type of pizza to empty string
        self.tops = []                          # initializing the list that contains selected tops
        self.size_txt = ""                          # initializing the text for the size of pizza to empty string

        # Creating window using Class Tk()
        self.window = Tk()
        self.window.title('Home Style Pizza')                    # Providing title to the window
        self.window.geometry("530x550")                         # Providing Geometry to the window

        # add welcome label and it uses place( ) method  to place it
        self.label = Label(self.window, text="Welcome to Home Style Pizza Shop", fg="red", font=("Arial", 30), ).place(x=15, y=5)

        # add frame for topping and uses place() method  to place it
        self.frame_top = Frame(self.window, pady=10, padx=10)
        self.frame_top.place(x=20, y=60)
        # relief defines the type of border we use and we highlight the background which will give color to the solid border of px2
        self.frame_top.config(relief=SOLID, highlightbackground="red", highlightthickness=2)

        # add elements in the frame
        # add title label and use grid() method  to place it
        self.label1 = Label(self.frame_top, text="Each toppings: $1.50", fg="red", font=("Arial", 15), ).grid(row=1, column=1)

        # the checkboxes for toppings,
        # this creates Checkbutton widget and uses grid() method  to place it
        # we set them as Boolean False because they need to start unselected.
        self.tomato = BooleanVar()
        self.tomato.set(False)
        self.cb1 = Checkbutton(self.frame_top, text="Tomato", variable=self.tomato).grid(row=2, column=1, stick="w")
        self.green = BooleanVar()
        self.green.set(False)
        self.cb2 = Checkbutton(self.frame_top, text="Green Pepper", variable=self.green).grid(row=3, column=1,stick="w")
        self.black = BooleanVar()
        self.black.set(False)
        self.cb3 = Checkbutton(self.frame_top, text="Black Olives", variable=self.black).grid(row=4, column=1, stick="w")
        self.mushroom = BooleanVar()
        self.mushroom.set(False)
        self.cb4 = Checkbutton(self.frame_top, text="Mushrooms", variable=self.mushroom).grid(row=5, column=1, stick="w")
        self.cheese = BooleanVar()
        self.cheese.set(False)
        self.cb5 = Checkbutton(self.frame_top, text="Extra Cheese", variable=self.cheese).grid(row=6, column=1, stick="w")
        self.pepperoni = BooleanVar()
        self.pepperoni.set(False)
        self.cb6 = Checkbutton(self.frame_top, text="Pepperoni", variable=self.pepperoni).grid(row=7, column=1, stick="w")
        self.sausage = BooleanVar()
        self.sausage.set(False)
        self.cb7 = Checkbutton(self.frame_top, text="Sausage", variable=self.sausage).grid(row=8, column=1, stick="w")

        # add frame for pizza size and use place() method  to place it
        self.frame_middle = Frame(self.window, pady=10, padx=10)
        self.frame_middle.place(x=200, y=60)
        # relief defines the type of border we use and we highlight the background which will give color to the solid border of px2
        self.frame_middle.config(relief=SOLID, highlightbackground="red", highlightthickness=2)

        # add elements in the frame
        # add title label and use grid() method to place it
        self.label2 = Label(self.frame_middle, text="Pizza Size", fg="red", font=("Arial", 15), )
        self.label2.grid(row=1, column=1, stick="n")

        # the variable 'size' mentioned here holds Integer Value
        self.size = IntVar()
        self.size.set(None)  # set the size value to None inorder the program starts unselected and raise an error if it remains unselected

        # the radio buttons for size,
        # this creates 'Radio button' widget and uses grid() method to place them
        self.r1 = Radiobutton(self.frame_middle, text="Small $6.50", pady=5, variable=self.size, value=0).grid(row=2, column=1, stick="w")
        self.r2 = Radiobutton(self.frame_middle, text="Medium $8.50", pady=5, variable=self.size, value=1).grid(row=3, column=1, stick="w")
        self.r3 = Radiobutton(self.frame_middle, text="Large $10.0", pady=5, variable=self.size, value=2).grid(row=4, column=1, stick="w")

        # add frame for pizza type and uses place() method to place it
        self.frame_last = Frame(self.window, pady=10, padx=10)
        self.frame_last.place(x=360, y=60)
        # relief defines the type of border we use and we highlight the background which will give color to the solid border of px2
        self.frame_last.config(relief=SOLID, highlightbackground="red", highlightthickness=2)

        # add elements in the frame
        # add title label and use grid() method to place it
        self.label3 = Label(self.frame_last, text="Pizza Type", fg="red", font=("Arial", 15))
        self.label3.grid(row=1, column=1)

        # the variable 'type' mentioned here holds Integer Value
        self.type = IntVar()
        self.type.set(None)  # set the type value to None inorder the program starts unselected and raise an error if it remains unselected

        # the radio buttons for type,
        # this creates 'Radio button' widget and uses grid() method to place them
        self.r4 = Radiobutton(self.frame_last, text="Thin Crust", pady=5, variable=self.type, value=0).grid(row=2, column=1, stick="w")
        self.r5 = Radiobutton(self.frame_last, text="Medium Crust", pady=5, variable=self.type, value=1).grid(row=3, column=1, stick="w")
        self.r6 = Radiobutton(self.frame_last, text="Pan", pady=5, variable=self.type, value=2).grid(row=4, column=1, stick="w")

        # add select button to show the user's preferences and the amount due
        self.select_btn = Button(self.window, pady=5, padx=40, text="Process Selection", command=self.calculate_total)
        self.select_btn.place(x=200, y=220)

        # add a text area to show final result
        self.result = Text(self.window)

        self.window.mainloop()

    # this function operates the total cost based on the selected preferences
    def total_pay(self):
        # calculating the price of the toppings
        total_tops = 0             # this variable counts how many toppings have been selected by adding 1 for every True choice of checkboxes
        if self.tomato.get():       # this gets True if selected and False if not selected, same goes for all the toppings
            total_tops += 1
        if self.green.get():
            total_tops += 1
        if self.black.get():
            total_tops += 1
        if self.mushroom.get():
            total_tops += 1
        if self.cheese.get():
            total_tops += 1
        if self.pepperoni.get():
            total_tops += 1
        if self.sausage.get():
            total_tops += 1

        # calculating the price of size
        total_size = 0.0            # this variable sets the cost of the ordered pizza to 0 and add one of the amounts according the users selection
        size = self.size.get()      # this variable gets 0 if selected small, 1 if selected medium, and 2 if selected large
        if size == 0:
            total_size = 6.5                # price of small
        if size == 1:
            total_size = 8.50                # price of medium
        if size == 2:
            total_size = 10.0                # price of large

        # adds the price of selected size and 1.5 * number of toppings selected, the sum goes to total attribute
        self.total= int(total_tops)*1.5 + float(total_size)
        return self.total

    # this function returns all the selected toppings by the user
    def find_top(self):
        tops = []               # initializing an empty list that
        if self.tomato.get():       # true if selected and false if not selected, if selected the next line will be executed
            tops.append("Tomato")            # add each topping item that have been selected to the list,
        if self.green.get():
            tops.append("Green Pepper")
        if self.black.get():
            tops.append("Black Olives")
        if self.mushroom.get():
            tops.append("Mushrooms")
        if self.cheese.get():
            tops.append("Extra Cheese")
        if self.pepperoni.get():
            tops.append("Pepperoni")
        if self.sausage.get():
            tops.append("Sausage")
        if not tops:                    # if there is nothing in the tops list, nothing has been selected so it shows warning message
            messagebox.showwarning("Empty Fields", "Please choose toppings")
        self.tops = tops
        return ', '.join(self.tops)             # returns each elements in the list by as a single line string separated by ,

    # a function that executes the size choice of a user
    def find_size(self):
        try:                # use try and except blocks because if nothing is selected an exception will be raised
            type_s = ""                     # empty string to write the item selected
            size = self.size.get()          # this variable gets 0 if selected small, 1 if selected medium, and 2 if selected large
            if size == 0:
                type_s = "Small"
            elif size == 1:
                type_s = "Medium"
            elif size == 2:
                type_s = "Large"
            self.size_txt = type_s
            return self.size_txt            # return the size of the pizza selected
        except:                                # if there is a exception/ nothing is selected warning messagebox pops up
            messagebox.showwarning("Empty Fields", "Please choose pizza size")

    # a function that executes the type choice of a user
    def find_type(self):
        try:                    # use try and except blocks because if nothing is selected an exception will be raised
            total_type = ""
            type1 = self.type.get()         # this variable gets 0 if selected thin crust, 1 if selected medium crust, and 2 if selected pan
            if type1 == 0:
                total_type = "Thin Crust"
            elif type1 == 1:
                total_type = "Medium Crust"
            elif type1 == 2:
                total_type = "Pan"
            self.type_txt = total_type
            return self.type_txt             # return the type of the pizza selected
        except:                               # if there is a exception/ nothing is selected warning messagebox pops up
            messagebox.showwarning("Empty Fields", "Please choose pizza type")

    # a function that is called after the button clicked, and shows a text box that has information about the current pizza of choice
    def calculate_total(self):
        self.text1 = StringVar()                 # the variable text1 mentioned here holds String Value, your order
        self.text1.set("Your order:")
        self.text2 = Label(self.window, textvariable=self.text1)        # shows the string value in label
        self.text2.place(x=20, y=285)

        self.total_text = Text(self.window)         # the variable here holds text that has information of the pizza of user's choice
        self.total_text.insert(END, "Pizza type: " + str(self.find_type()) + "\nPizza Size: " + str(self.find_size()) + "\nToppings: " + str(self.find_top()) + "\nAmount due: $" + str(self.total_pay()))
        self.total_text.place(x=20, y=310)

# calling the class
mywindow = PizzaShop()
