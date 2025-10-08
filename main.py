import tkinter as tk

counter = [0] 

def change_text():
    label.config(text="Button Clicked!")

def increment_counter():
    counter[0] += 1  
    label2.config(text=f"Counter: {counter[0]}")

root = tk.Tk()
root.title("Hello Tkinter")
root.geometry("300x300")

label = tk.Label(root, text="Welcome to Tkinter!")
label.pack(pady=20)

label2 = tk.Label(root, text=f"Counter: {counter[0]}")
label2.pack(pady=10)

button = tk.Button(root, text="Click Me", command=change_text)
button.pack(pady=10)

button2 = tk.Button(root, text="Add 1", command=increment_counter)
button2.pack(pady=10)

root.mainloop()