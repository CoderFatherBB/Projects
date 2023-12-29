# Header Errors Handling
if header_file not in header:
    messagebox.showerror("Syntax Error", "Invalid Header File")
    raise SyntaxError("Invalid Header File")
