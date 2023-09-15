import customtkinter
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()
root.title('My Todo App')
root.geometry('900x500')

# the get() was used here to get the text being saved
# the second  label was created to add the text written in the entry box ro be saved into the scrollable frame and then pack
# delete() was used to remove previous text in other to add a new one

def add_todo():
    Todo = entry_text.get()
    my_label2 = customtkinter.CTkLabel(scrollable_frame, text=Todo)
    my_label2.pack()
    entry_text.delete(0, 'end')

# create a label
my_label = customtkinter.CTkLabel(root, text='Daily Task', font=('Times New Roman', 30, 'bold'))
my_label.pack(padx=30, pady=10)

# create a scrollable frame
scrollable_frame = customtkinter.CTkScrollableFrame(root, width=400, height=250)
scrollable_frame.pack(pady=10)

# the fill = 'x' is to stretch the entry box horizontally
entry_text = customtkinter.CTkEntry(scrollable_frame, placeholder_text='Add Task')
entry_text.pack(fill='x')

add_button = customtkinter.CTkButton(root, text='Add Task', font=('Times New Roman', 15), command=add_todo)
add_button.pack(pady=10)

exit_button = customtkinter.CTkButton(root, text="Exit", font=('Times New Roman',15), command=root.quit)
exit_button.pack(pady=5)



root.mainloop()













