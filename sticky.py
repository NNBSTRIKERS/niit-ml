import tkinter as tk
from tkinter import ttk

def add_note():
    text = note_entry.get("1.0", "end-1c")
    if text.strip():  # Check if the note has any non-whitespace content
        notes_listbox.insert(tk.END, text)
        note_entry.delete("1.0", tk.END)

def delete_note():
    selected_index = notes_listbox.curselection()
    if selected_index:xxxxx
        notes_listbox.delete(selected_index)

# Create the main application window
app = tk.Tk()
app.title("Virtual Post-it Notes")
app.geometry("400x400")
app.resizable(False, False)

# Style for the widgets
style = ttk.Style(app)
style.configure("TLabel", font=("Montserrat", 12))
style.configure("TButton", font=("Montserrat", 12))

# Note Entry Field
note_entry = tk.Text(app, height=5, width=30, font=("Montserrat", 12))
note_entry.pack(pady=10)

# Add Note Button
add_button = ttk.Button(app, text="Add Note", command=add_note)
add_button.pack()

# Notes Listbox
notes_listbox = tk.Listbox(app, height=10, width=40, font=("Montserrat", 12))
notes_listbox.pack(pady=10)

# Delete Note Button
delete_button = ttk.Button(app, text="Delete Note", command=delete_note)
delete_button.pack()

# Run the application
app.mainloop()
