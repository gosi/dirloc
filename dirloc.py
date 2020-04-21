import os, tkinter, mimetypes
from os import walk
from tkinter import filedialog

# Setup a hidden Tkinter window for easy directory selection
tkinter.Tk().withdraw()
print("Select the directory you want to analyze: ")
path = filedialog.askdirectory()

# lines is total lines in folder
# files is total files in folder
# highest_line_count is the highest line count
# highest_line_path is the path to the file that has the highest line count
lines = 0
files = 0
highest_line_count = 0
highest_line_path = ""

# readlines() will return the number of lines in a file
def count_lines(file):
    return len(file.readlines())

def walk_path(path):
    global lines
    global files
    global highest_line_count
    global highest_line_path
    # Walk through each folder and file in given path
    for (dirpath, dirnames, filenames) in walk(path):
        for name in filenames:
            # Get the file path by joining the directory and file name
            filepath = os.path.join(dirpath, name)
            # Open the file, then try to read lines. If it's a non-text format,
            # then readlines() will fail, so that file will not count
            file = open(filepath, 'r')
            try:
                counted_lines = count_lines(file)
                lines += counted_lines
                # Empty files shouldn't be counted
                if (counted_lines > 0):
                    files += 1
                    print(filepath, "Lines: " + str(counted_lines))
                # Update highest line count
                if (counted_lines > highest_line_count):
                    highest_line_count = counted_lines
                    highest_line_path = filepath
            # Don't need to handle any exceptions that occur
            except Exception:
                pass

walk_path(path)
average = lines / files
print("This folder contains " + str(lines) + " lines.")
print("The average file contains " + str(average) + " lines of code.")
print("The file with the most code is " + highest_line_path + " with", str(highest_line_count), "lines of code.")
