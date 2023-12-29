import tkinter as tk
from tkinter import messagebox



functions = []

with open('functions.txt', 'r') as funtion:
    fun = funtion.readlines()

for line in fun:
    line = line.strip()
    functions.append(line)

functions

 
types = []

with open('type.txt', 'r') as typee:
    fun = typee.readlines()

for line in fun:
    line = line.strip()
    types.append(line)

types

 
header = []

with open('header.txt', 'r') as head:
    fun = head.readlines()

for line in fun:
    line = line.strip()
    header.append(line)

header

datatype_check = []

with open('datatype.txt', 'r') as data:
    fun = data.readlines()

for line in fun:
    line = line.strip()
    datatype_check.append(line)

datatype_check


c_code = []

# with open('input.c', 'r') as code:
#     fun = code.readlines()

# for line in fun:
#     line = line.strip()
#     c_code.append(line)

# c_code

displayed_text = []
output_text = []


def run_code():
    c_code.clear()
    displayed_text.clear()
    output_text.clear()
    text = text_entry.get("1.0", "end-1c")  # Retrieve text from the text entry widget
    text = text.strip()
    lines = text.split('\n')  # Split the text into lines
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    c_code.extend(lines)  # Append each line to the c_code list

    #Header Update

    header_line = []
    typ = tuple(types)

    for line in c_code:
        if not line.startswith(typ):
            header_line.append(line)
        else:
            break

    header_line

    for head in header_line:
        if not head.startswith('#'):
            messagebox.showerror("Syntax Error", "Wrong Header")
            raise SyntaxError("Wrong Header")


    header_divided = []

    for head in header_line:
        head = head.split()
        header_divided.append(head)

    header_divided

    for i in range(len(header_divided)):
        # print(header_divided[i][0])
        if header_divided[i][0] != '#include' and header_divided[i][0] != '#define':
            messagebox.showerror("Syntax Error", "Wrong #")
            raise SyntaxError("Wrong #") 

    flag_check = 0   
    for i in range(len(header_divided)):
        if header_divided[i][0] == '#include':
            flag_check = 0 
            for head in header:
                if header_divided[i][1] == head:
                    print("'", header_divided[i][1], "'"" is the header file used in the code")
                    displayed_text.append(["'", header_divided[i][1], "'"" is the header file used in the code"])
                    flag_check = 1
                    break

    if flag_check == 0:
        messagebox.showerror("Syntax Error", "Wrong HeaderFile")
        raise SyntaxError("Wrong HeaderFile")



    for i in range(len(header_divided)):
        if header_divided[i][0] == '#define':
            if len(header_divided[i]) != 3:
                messagebox.showerror("Syntax Error", "Wrong #define")
                raise SyntaxError("Wrong #define")
            else:
                print("'", header_divided[i][1], "'"" is the constant used in the code with ""'", header_divided[i][2], "'"" as its value")
                displayed_text.append(["'", header_divided[i][1], "'"" is the constant used in the code with ""'", header_divided[i][2], "'"" as its value"])
    print("\n")
    displayed_text.append([" "])


    
    ad_c_code = []

    for line in c_code:
        if line.startswith('printf'):
            ad_c_code.append([line])
        elif not line.startswith('#'):
            ad_c_code.append(line.split())
        else:
            pass


    ad_c_code

    
    # checking for main function
    flag_check = 0

    for ty in types:
        if ad_c_code[0][0] == ty:
            print("Type of function used is ""'", ad_c_code[0][0], "'")
            displayed_text.append(["Type of function used is ""'", ad_c_code[0][0], "'"])
            flag_check = 1
            break

    if flag_check == 0:
        messagebox.showerror("Syntax Error", "Not a valid function type")
        raise SyntaxError("Not a valid function type")

    if flag_check == 1:
        if ad_c_code[0][1] != 'main()':
            messagebox.showerror("Syntax Error", "There is no main() function to run the code")
            raise SyntaxError("There is no main() function to run the code")
        else:
            print("Name of the function is ' main() '")
            displayed_text.append(["Name of the function is ' main() '"])
    print("\n")
    displayed_text.append([" "])
    ad_c_code = ad_c_code[1:]
    # ad_c_code

    
    # for brackets
    with open('input.c', 'r') as file:
        content = file.read()
        if (content.count('(') != content.count(')')) or content.count('{') != content.count('}'):
            messagebox.showerror("Syntax Error", "Unbalanced brackets")
            raise SyntaxError("Unbalanced brackets")


    
    ad_c_code = ad_c_code[1:]
    ad_c_code = ad_c_code[:-1]
    ad_c_code

    
    for line in ad_c_code:
        if not line[-1].endswith(';'):
            messagebox.showerror("Syntax Error", "; Missing")
            raise SyntaxError("; Missing")

    
    #symbol table
    symbol = []
    current_type = None

    for i in range(len(ad_c_code)):
        # print(ad_c_code[i][0])
        for ty in types:
            if ad_c_code[i][0] == ty:
                current_type = ty
                # print(ad_c_code[i][0])
                for sym in ad_c_code[i]:
                    symbol.append([ad_c_code[i][0], sym[:-1]])
                    

    # symbol = symbol[1:]
    # symbol

    i = 1
    for line in ad_c_code:
        if '=' in line:
            symbol[i].append(line[2][:-1])
            i = i + 1

    for line in symbol:
        if len(line) == 3:  
            print(f"' {line[0]} ' type variable named ' {line[1]} ' with value ' {line[2]} ' is declared int the code")
            displayed_text.append([f"' {line[0]} ' type variable named ' {line[1]} ' with value ' {line[2]} ' is declared int the code"])
        elif line[0] == current_type:
            print(f"' {line[0]} ' type variable named ' {line[1]} '")
            displayed_text.append([f"' {line[0]} ' type variable named ' {line[1]} '"])
        current_type = line[0]
    print("\n")
    displayed_text.append([" "])


    
    i = 0
    for line in ad_c_code:
        if line[0].startswith(typ):
            i = i + 1

    ad_c_code = ad_c_code[i:]
    ad_c_code

    
    final_symbol = []
    only_symbol = []
    current_type = None

    for line in symbol:
        if current_type is None or line[0] != current_type:
            current_type = line[0]
            # print(current_type)
            continue  # Skip the first occurrence of a type change

        if len(line) == 3:
            final_symbol.append([line[0], line[1], line[2]])
        
        if len(line) == 2:
            final_symbol.append([line[0], line[1]])

    final_symbol
    for i in range(len(final_symbol)):
        only_symbol.append(final_symbol[i][1])

    only_symbol

    with open('symbol_table.txt', 'w') as output_file:
        output_file.write("Type\tName\tValue\n")
        for line in final_symbol:
            if len(line) == 3:  
                output_file.write(f"{line[0]}\t\t {line[1]}\t\t {line[2]}\n")
            else:
                output_file.write(f"{line[0]}\t\t {line[1]}\n")



    flag_check = 0
    correct_line = []

    for line in ad_c_code:
        # print("hi")
        for symbol in final_symbol:
            if line[0] == symbol[1]:
                flag_check = 1
                # print("ok")
        if flag_check == 0:
            if len(line) == 3:
                messagebox.showerror("Syntax Error", "Symbol not define")
                raise SyntaxError("Symbol not define")   
        else:
            # print(line)
            correct_line.append(line)
        flag_check = 0

    for line in correct_line:
        if line in ad_c_code:
            ad_c_code.remove(line)



    printf_contents = []

    for line in ad_c_code:
        if line[0].startswith('printf'):
            opening_index = line[0].find('(')
            closing_index = line[0].find(')')
            if opening_index != -1 and closing_index != -1:
                content_within_parentheses = line[0][opening_index + 1: closing_index]
                printf_contents.append([content_within_parentheses])
            else:
                messagebox.showerror("Syntax Error", "No parentheses found within printf statement")
                raise SyntaxError("No parentheses found within printf statement")
        else:
            messagebox.showerror("Syntax Error", "Wrong Statement used")
            raise SyntaxError("Wrong Statement used")

    printf_contents



    split_printf_contents = []

    for line in printf_contents:
        lin = line[0].split()
        split_printf_contents.append(lin)

    split_printf_contents



    opreations = ['+', '-' , '*', '/']
    store_val = []
    flag_check1 = 0
    flag_check2 = 0

    def get_symdol_value(sym):
        for line in final_symbol:
            for i in range(len(line)):
                if line[i] == sym and len(line) == 3:
                    return line[i+1]


    for line in split_printf_contents:
        flag_check1 = 0
        flag_check2 = 0
        store_val.clear()
        for i in range(len(line)):
            if line[i] in only_symbol:
                sym = line[i]
                val = get_symdol_value(sym)
                store_val.append(val)
        for j in range(len(line)):
            if line[j] in datatype_check:
                flag_check1 = 1
                for k in range(len(line)):
                    if line[k] in opreations:
                        flag_check2 = 1
                        if line[k] == '+':
                            print(int(store_val[0]) + int(store_val[1]))
                            output_text.append([str(int(store_val[0]) + int(store_val[1]))])
                        if line[k] == '-':
                            print(int(store_val[0]) - int(store_val[1]))
                            output_text.append([str(int(store_val[0]) - int(store_val[1]))])
                        if line[k] == '*':
                            print(int(store_val[0]) * int(store_val[1]))
                            output_text.append([str(int(store_val[0]) * int(store_val[1]))])
                        if line[k] == '/':
                            print(int(store_val[0]) / int(store_val[1]))
                            output_text.append([str(int(store_val[0]) / int(store_val[1]))])
                if flag_check2 == 0:
                    print(val)
                    output_text.append([val])
        if flag_check1 == 0:
            messagebox.showerror("Syntax Error", "Data type is Missing")
            raise SyntaxError("Data type is Missing")
               

    show_code()
    show_output()


def show_code():
    code_window = tk.Toplevel(root)  # Create a new window
    code_window.title("Lexical Analysis")
    code_text = tk.Text(code_window, height=20, width=80)

    for line in displayed_text:
        line_text = ' '.join(line)  # Convert inner lists to strings
        code_text.insert(tk.END, line_text + '\n')  # Insert collected code into the text box

    code_text.pack()


def show_output():
    code_window = tk.Toplevel(root)  # Create a new window
    code_window.title("Output")
    code_text = tk.Text(code_window, height=10, width=30)

    for line in output_text:
        line_text = ' '.join(line)  # Convert inner lists to strings
        code_text.insert(tk.END, line_text + '\n')  # Insert collected code into the text box

    code_text.pack()


# Create the main window
root = tk.Tk()
root.title("C Compiler")

# Text Entry
text_entry = tk.Text(root, height=40, width=50)
text_entry.pack()

# Run Button
run_button = tk.Button(root, text="Run", command=run_code)
run_button.pack()

root.mainloop()

# print(displayed_text)