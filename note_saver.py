import tkinter as tk

def save_note(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
        clear_text_box()

def load_note(filename):
    with open(filename, 'r') as f:
        clear_text_box()
        content = f.read()
        text_box.insert(tk.END, content)


def clear_text_box():
    text_box.delete("1.0", tk.END)

def load_popup():
    popup = tk.Toplevel(root)
    popup.title("Load")
    popup.geometry("300x200")

    label = tk.Label(popup, text="Enter File Name To Load:")
    label.pack()

    entry = tk.Entry(popup, width=40)
    entry.pack()

    error_label = tk.Label(popup, text="", fg="red")
    error_label.pack()

    def on_load():
        filename = entry.get()
        if filename:
            try:
                load_note(filename)
                popup.destroy()
            except FileNotFoundError:
                error_label.config(text="File not found.")
        else:
            error_label.config(text="Please enter a filename.")

    tk.Button(popup, text="Load", command=on_load).pack()
    tk.Button(popup, text="Cancel", command=popup.destroy).pack()

def save_popup():
    content = text_box.get("1.0", tk.END)
    popup = tk.Toplevel(root)
    popup.title("Save")
    popup.geometry("300x200")

    label = tk.Label(popup, text="Enter File Name:")
    label.pack()

    entry = tk.Entry(popup, width=40)
    entry.pack()

    error_label = tk.Label(popup, text="", fg="red")
    error_label.pack()

    def on_save():
        filename = entry.get().strip
        if filename:
            save_note(filename, content)
            popup.destroy()
        else:
            error_label.config(text="Please enter a filename.")

    tk.Button(popup, text="Save", command=on_save).pack()
    tk.Button(popup, text="Cancel", command=popup.destroy).pack()

if __name__ == '__main__':

    root = tk.Tk()
    root.title('Note saver')
    root.geometry('600x900')

    text_box = tk.Text(root, height=45, width=50)
    text_box.pack()

    frame = tk.Frame(root)
    frame.pack()

    tk.Button(frame, text='Save', command=save_popup).pack(side=tk.LEFT, padx=5, pady=15)
    tk.Button(frame, text='Load', command=load_popup).pack(side=tk.LEFT, padx=5, pady=15)
    tk.Button(frame, text='Clear', command=clear_text_box).pack(side=tk.LEFT, padx=5, pady=15)

    root.mainloop()