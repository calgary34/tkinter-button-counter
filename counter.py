import tkinter as tk

window = tk.Tk()

counter = tk.Label(text="0")
counter.pack()

def increment_counter():
    counter['text'] = int(counter['text']) + 1

button = tk.Button(text="Click Me!", command=increment_counter)
button.pack()

window.mainloop()
