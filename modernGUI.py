# import the customtkinter after installing it using pip install customtkinter in the command prompt
import customtkinter

# set the apperance mode and color theme for the GUI
# for the apperance mode (dark/light)
# for the color theme (blue, green, dark-blue)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# define the title and geometry
root = customtkinter.CTk()
root.title("Login Interface")
root.geometry("900x500+300+200")
root.resizable(True, True)


# define the login function
def login():
    print("Test SUCCESSFUL")

# create frames using customtkinter.CTKFrame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
#fill funtion is to fill the entire root window with the frame and the expand function is used to expand the frame

#create a label using customtkinter.CTKLabel
label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Times New Roman", 24))
label.pack(padx=10, pady=12)

#create an entry using customtkinter.CTKEntry
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

# create a button using customtkinter.CTKButton
button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

button_quit = customtkinter.CTkButton(master=frame, text='Exit', command=root.quit)
button_quit.pack()

# create a checkbox using customtkinter.CTKCheckbox
checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame, text="Forgot Password", width=2)
button2.pack(pady=12, padx=10)

root.mainloop()
