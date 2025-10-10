import tkinter as tk

counter = [0]


def change_text():
    label.config(text="Button Clicked!")

def increment_counter():
    counter[0] += 1  
    label2.config(text=f"Counter: {counter[0]}")

def submit():
    print(entry.get())
    label3.config(text=f"You entered: {entry.get()}")
    entry.delete(0, tk.END)
    
root = tk.Tk()
root.title("Hello Tkinter")
root.geometry("500x500")

label = tk.Label(root, text="Welcome to Tkinter!")
label2 = tk.Label(root, text=f"Counter: {counter[0]}")
button = tk.Button(root, text="Click Me", command=change_text)
button2 = tk.Button(root, text="Add 1", command=increment_counter)
entry = tk.Entry(root)
submit_button = tk.Button(root, text="Submit", command=submit)
label3 = tk.Label(root)

label.grid(row=0, column=3)
label2.grid(row=1, column=2)
button.grid(row=2, column=1)
button2.grid(row=3, column=0)
entry.grid(row=4, column=0, sticky="nswe")
submit_button.grid(row=4, column=1)
label3.grid(row=4, column=2)


root.mainloop()