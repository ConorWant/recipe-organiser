import tkinter as tk

from pandas.core.apply import frame_apply


def save_note():
    with open("note.txt", 'w') as f:
        f.write(text_box.get(1.0, tk.END))
        clear_text_box()

def load_note():
    with open("note.txt", 'r') as f:
        clear_text_box()
        content = f.read()
        text_box.insert(tk.END, content)


def clear_text_box():
    text_box.delete("1.0", tk.END)

if __name__ == '__main__':

    root = tk.Tk()
    root.title('Note saver')
    root.geometry('600x900')

    text_box = tk.Text(root, height=45, width=50)
    text_box.pack()

    frame = tk.Frame(root)
    frame.pack()

    tk.Button(frame, text='Save', command=save_note).pack(side=tk.LEFT, padx=5, pady=15)
    tk.Button(frame, text='Load', command=load_note).pack(side=tk.LEFT, padx=5, pady=15)
    tk.Button(frame, text='Clear', command=clear_text_box).pack(side=tk.LEFT, padx=5, pady=15)

    root.mainloop()