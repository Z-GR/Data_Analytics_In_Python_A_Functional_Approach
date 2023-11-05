import csv
import pandas as pd #DA Libary
import numpy as np
import _thread #multithreading
import re #regular expressions
import tracemalloc #memory monitoring
import tkinter as tk #GUI
import matplotlib.pyplot as plt #Data visualisation
from tkinter import ttk #Extended GUI Functions
from binarySearch import * #Custom binary search

#use standard python3 install (won't work with homebrew tk sys is depreciated)

arr =[] #Max 536,870,912 elements 32bit
arr_f1 =[] 
arr_f2 =[]
arr_f3 =[]  

progress = 0

def function0(select):
    runningTxt()
    #open .csv file
    with open('Data/311_Service_Requests_from_2010_to_Present_20231023.csv') as csv_file, \
        open('Data/out.csv', mode='w') as csv_file_out, \
        open('Data/f1.csv', mode='w') as csv_file_out_f1, \
        open('Data/f2.csv', mode='w') as csv_file_out_f2, \
        open('Data/f2.csv', mode='w') as csv_file_out_f3:

        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_writer = csv.writer(csv_file_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        #Fragments
        fragment1 = csv.writer(csv_file_out_f1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        fragment2 = csv.writer(csv_file_out_f2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        fragment3 = csv.writer(csv_file_out_f3, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_output = 0
        exit_condition = 0
        execute_condition = 1
        execute_condition1 = 0

        global line_select
        line_select = 300000

        global progress
        progress_step = 0
        progress = 0

        global line_count
        global line_count_t
        line_count = 0

        line_select = int(lines_entry.get())
        
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are : {", ".join(row)}')
                line_count += 1
                progress_step = 100 / line_select
                progress = progress_step
            else:
                #print(f'UIN:\t{row[0]}\tCreated date:\t{row[1]}\tClosed date:\t{row[2]}\tAgency:\t{row[3]}.\tAgency name:\t{row[4]}')
                line_count += 1

                #progress bar
                progressbar.step(progress_step)
                progress =  progress_step + progress #Increment progress bar

                if csv_output == 1:
                    csv_writer.writerow(['1', '0', '1'])

                #binary search array
                if execute_condition1 == 1:
                    arr.append(int(row[0]))
                
                exit_condition += 1

                #cases for data selection
                match select:
                    case 0:
                        print ('no query')
                    case 1:
                        x = re.search("^03.*$", str(row[1]))
                        if x:
                            print('HIT')
                            fragment1.writerow([row[0], row[1]])
                            arr_f1.append(int(row[0]))

                    case 2:
                        x = re.search("^08.*$", str(row[1]))
                        if x:
                            print('HIT')
                            fragment2.writerow([row[0], row[1]])
                            arr_f2.append(int(row[0]))
                    case 3:
                        csv_writer.writerow(['0', '1', '0'])
                        
                #Specify number of rows to process
                if execute_condition == 1:
                    if exit_condition == line_select - 1:
                        break
        print(f'Processed {line_count} lines.') 
        line_count_t = f"Processed {line_count} lines."
        label1.config(text = line_count_t)

def rowCount():
    with open('Data/311_Service_Requests_from_2010_to_Present_20231023.csv') as csv_file, open('Data/out.csv', mode='w') as csv_file_out:
        csv_reader = csv.reader(csv_file, delimiter=',')
        t.set('Running...')
        for row in csv_reader:
            row_count = sum(1 for row in csv_reader)
            print(row_count)
            t.set(f"{row_count}")

def arrCount(fragment):
    match fragment:
        case 0:
            print(len(arr))
        case 1:
            print(len(arr_f1))
        case 2:
            print(len(arr_f2))
        case 3:
            print(len(arr_f3))
    
def searchArr():
    x = 35734010
    result = binary_search(arr, 0, len(arr)-1, x)

    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")

def runningTxt():
    label1.config(text = "Running ...")

def plotH():
    x = np.array(["A", "B"])
    y = np.array([len(arr_f2), len(arr_f1)])

    plt.bar(x,y)
    plt.show()

def query0():
    function0(0)
    arrCount(0)

def query1():
    function0(1)
    arrCount(1)

def query2():
    function0(2)
    arrCount(2)

def query3():
    function0(3)

def openRCWindow():

    global t
    t = tk.StringVar()
    t.set('Waiting...')
     
    # Toplevel object which will 
    # be treated as a new window
    new_window = tk.Toplevel(root_window)
 
    # sets the title of the
    # Toplevel widget
    new_window.title("Row Counter")
 
    # sets the geometry of toplevel
    new_window.geometry("200x200")

    #Background
    root_window.configure(background="black")
 
    # A Label widget to show in toplevel
    tk.Label(new_window, 
          text ="Row Counter").pack()
    
    tk.Button(new_window, text="Row Count", command=lambda: [_thread.start_new_thread( rowCount, () )], highlightbackground='black').pack()

    tk.Label(new_window, textvariable= t, bg="black").pack()



if __name__ == "__main__":
    
    #Memory monitor
    tracemalloc.start()
       
    #Create window object
    root_window = tk.Tk("window")

    #Background
    root_window.configure(background="black")

    #Set window title
    root_window.title("311 Data Analysis")

    # Load the image file from disk.
    icon = tk.PhotoImage(file="/Users/zak/Documents/Panaseer/Icons/app_icon.png")
    # Set it as the window icon.
    root_window.iconphoto(True, icon)


    frame0 = tk.Frame(master=root_window, width=200, height=20, bg="black")
    frame0.pack(fill=tk.X)

    label0 = tk.Label(text="Select option", bg="black")
    label0.pack()
    frame1 = tk.Frame(master=root_window, width=400, height=20, bg="black")
    frame1.pack(fill=tk.X)

    #Start analysis
    b1 = tk.Button(root_window, text="Start",command=lambda:(_thread.start_new_thread( query0, () )), highlightbackground='black')
    b1.pack()

    frame1 = tk.Frame(master=root_window, width=200, height=20, bg="black")
    frame1.pack(fill=tk.X)

    label0 = tk.Label(text="Enter number of lines to process", bg="black")
    label0.pack()

    frame1 = tk.Frame(master=root_window, width=200, height=20, bg="black")
    frame1.pack(fill=tk.X)

    #create canvas
    canvas1 = tk.Canvas(root_window, width=200, height=30)
    canvas1.pack()

    frame1 = tk.Frame(master=root_window, width=200, height=20, bg="black")
    frame1.pack(fill=tk.X)

    entry = 0

    lines_entry = tk.Entry(root_window)
    canvas1.create_window(102, 20, window=lines_entry)

    b_exit = tk.Button(root_window, text="Exit", command=root_window.quit, highlightbackground='black')
    b_exit.pack()

    frame1 = tk.Frame(master=root_window, width=200, height=20, bg="black")
    frame1.pack(fill=tk.X)

    b_rowcount = tk.Button(root_window, text="Row Count", command=lambda: [openRCWindow()], highlightbackground='black')
    b_rowcount.pack()

    frame1 = tk.Frame(master=root_window, width=200, height=20, bg="black")
    frame1.pack(fill=tk.X)

    b_q0 = tk.Button(root_window, text="Query 0", command=lambda:(_thread.start_new_thread( query0, () )), highlightbackground='black')
    b_q0.pack()

    b_q1 = tk.Button(root_window, text="Query 1", command=lambda:(_thread.start_new_thread( query1, () )), highlightbackground='black')
    b_q1.pack()

    b_q2 = tk.Button(root_window, text="Query 2", command=lambda:(_thread.start_new_thread( query2, () )), highlightbackground='black')
    b_q2.pack()

    b_q3 = tk.Button(root_window, text="Query 3", command=lambda:(_thread.start_new_thread( query3, () )), highlightbackground='black')
    b_q3.pack()

    frame2 = tk.Frame(master=root_window, width=200, height=20, bg="black")
    frame2.pack(fill=tk.X)

    label1 = tk.Label(text=f"Waiting...", bg="black")
    label1.pack()

    frame3 = tk.Frame(master=root_window, width=200, height=20, bg="black")
    frame3.pack(fill=tk.X)

    progressbar = ttk.Progressbar(variable=progress, style="TProgressbar")
    progressbar.pack()

    print(tracemalloc.get_traced_memory())

    root_window.mainloop()

    plotH()