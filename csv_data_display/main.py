import tkinter as tk
from tkinter import HORIZONTAL, VERTICAL, StringVar, ttk
from tkinter import filedialog
import tkinter
from tokenize import String
import pandas as pd


class form_data:
    def __init__(self, data: list, master: tk.Tk):
        emp_id = StringVar(value=data[0])
        fname = StringVar(value=data[0])
        lname = StringVar(value=data[0])
        email = StringVar(value=data[0])
        hire_date = StringVar(value=data[0])
        jid = StringVar(value=data[0])
        salary = StringVar(value=data[0])
        commision_pct = StringVar(value=data[0])
        manager_id = StringVar(value=data[0])
        dep_id = StringVar(value=data[0])
        secondary_window = tk.Toplevel(master=master)
        secondary_window.geometry("500x500")


window = tk.Tk()

window.title("Main App")


def open_file():
    filename = filedialog.askopenfilename(
        initialdir="::[20D04FE0-3AEA-1069-A2D8-08002B30309D]",
        title="Select a File",
        filetypes=(("Comma-separated values", "*.csv*"),),
    )
    if filename.endswith("csv") is False:
        tkinter.messagebox.showerror(
            title="Error",
            message="Please Select File With CSV Format",
        )
        return
    frame = ttk.Frame(window)
    frame.pack()

    employee_attributes = {
        "EMPLOYEE_ID": 90,
        "FIRST_NAME": 150,
        "LAST_NAME": 150,
        "EMAIL": 210,
        "PHONE_NUMBER": 200,
        "HIRE_DATE": 100,
        "JOB_ID": 90,
        "SALARY": 90,
        "COMMISSION_PCT": 90,
        "MANAGER_ID": 90,
        "DEPARTMENT_ID": 100,
    }

    df = pd.read_csv(filename)
    tree = ttk.Treeview(frame, columns=[i for i in employee_attributes.keys()])
    for key, value in employee_attributes.items():
        tree.heading(key, text=key)
        tree.column(key, width=value, anchor=tk.CENTER)
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))
    tree["show"] = "headings"
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.bind("<Double-1>", lambda event: select(tree))

    # Pack the Treeview and scrollbar into the window
    tree.pack(side="left")
    scrollbar.pack(side="right", fill="y")


def select(tree: ttk.Treeview):
    second_window = form_data(tree.selection(), master=window)
    for i in tree.selection():
        print(tree.item(i)["values"])


window.geometry("1000x750")
menu = tk.Menu(tearoff=False)
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label="New", command=lambda: open_file())
menu.add_cascade(menu=file_menu, label="File")
window.configure(menu=menu)
label_var = StringVar()
ttk.Label(window, textvariable=label_var).pack()

window.mainloop()
