import tkinter as tk

def run_code():
    text = text_entry.get("1.0", "end-1c")  # Retrieve text from the text entry widget
    print(text)  # Print the text in the terminal

# Create the main window
root = tk.Tk()
root.title("Text Editor")

# Text Entry
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

# Run Button
run_button = tk.Button(root, text="Run", command=run_code)
run_button.pack()

root.mainloop()
