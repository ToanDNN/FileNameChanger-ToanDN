import os
import glob
import tkinter as tk
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def successWindow():
    window = tk.Toplevel()
    window.geometry("200x200")

    label = tk.Label(window, text="SUCCESS!", font=('Arial', 12))
    label.pack()

    closeButton = tk.Button(window,
                            text='Close',
                            font=('Arial', 11),
                            command=window.destroy)
    closeButton.pack()


def doSearchAndReplace(filePath, searchInput, replaceInput):
    print(filePath.get())
    print(searchInput.get())
    print(replaceInput.get())

    folder = filePath.get()
    search = searchInput.get()
    replace = replaceInput.get()

    paths = (os.path.join(temp, filename)
             for temp, _, filenames in os.walk(folder)
             for filename in filenames)

    for path in paths:
        newname = path.replace(search, replace)
        if newname != path:
            os.rename(path, newname)

    successWindow()


def doChangeOneFile(filePath, oldFileInput, newFileInput, fileExtensionInput):
    print(filePath.get())
    print(oldFileInput.get())
    print(newFileInput.get())

    folder = filePath.get()
    filename = oldFileInput.get()
    newFileName = newFileInput.get()
    fileExtension = fileExtensionInput.get()

    dst = f"{newFileName}{fileExtension}"
    src = f"{folder}/{filename}{fileExtension}"
    dst = f"{folder}/{dst}"

    os.rename(src, dst)
    successWindow()


def getFiles(filename, fileExtension, path):
    answer = []
    search = filename
    search2 = fileExtension
    search = search + "*" + search2
    os.chdir(path)
    for file in glob.glob(search):
        answer.append(file)

    return answer


def doChangeMultipleFiles(filePath, oldFileInput, newFileInput, fileExtensionInput):
    folder = filePath.get()
    filename = oldFileInput.get()
    newFileName = newFileInput.get()
    fileExtension = fileExtensionInput.get()

    listOfFiles = getFiles(filename, fileExtension, folder)
    counter = 0
    for count in os.listdir(folder):
        if count in listOfFiles:
            counter = counter + 1
            os.rename(count, newFileName+str(counter)+fileExtension)

    successWindow()


def searchAndReplace():
    window = tk.Toplevel()
    window.title("Search and Replace")
    window.geometry("450x160")

    pathLabel = tk.Label(window, text="Path: ", font=('Arial', 12))
    pathLabel.grid(row=0, column=0, sticky=tk.W)

    pathEntry = tk.Entry(window, width=50)
    pathEntry.grid(row=0, column=1, sticky=tk.W)

    searchLabel = tk.Label(window, text="Find what: ",
                           font=('Arial', 12))
    searchLabel.grid(row=1, column=0, sticky=tk.W)

    searchEntry = tk.Entry(window, width=50)
    searchEntry.grid(row=1, column=1)

    replaceLabel = tk.Label(window, text="Replace with: ",
                            font=('Arial', 12))
    replaceLabel.grid(row=2, column=0, sticky=tk.W)

    replaceEntry = tk.Entry(window, width=50)
    replaceEntry.grid(row=2, column=1)

    button = tk.Button(window, text="CONFIRM", font=(
        'Arial', 11), command=lambda: doSearchAndReplace(pathEntry, searchEntry, replaceEntry))
    button.grid(row=3, column=1, pady=10)

    closeButton = tk.Button(window,
                            text='Close',
                            font=('Arial', 11),
                            command=window.destroy)
    closeButton.grid(row=4, column=1)


def changeOneFile():
    window = tk.Toplevel()
    window.title("Change One File")
    window.geometry("500x200")

    pathLabel = tk.Label(window, text="Path: ", font=('Arial', 12))
    pathLabel.grid(row=0, column=0, sticky=tk.W)

    pathEntry = tk.Entry(window, width=50)
    pathEntry.grid(row=0, column=1)

    oldFileLabel = tk.Label(window, text="File Name: ",
                            font=('Arial', 12))
    oldFileLabel.grid(row=1, column=0, sticky=tk.W)

    oldFileEntry = tk.Entry(window, width=50)
    oldFileEntry.grid(row=1, column=1)

    newFileLabel = tk.Label(window, text="New File Name: ",
                            font=('Arial', 12))
    newFileLabel.grid(row=2, column=0, sticky=tk.W)

    newFileEntry = tk.Entry(window, width=50)
    newFileEntry.grid(row=2, column=1)

    fileExtensionLabel = tk.Label(window, text="File Extension Type: ",
                                  font=('Arial', 12))
    fileExtensionLabel.grid(row=3, column=0, sticky=tk.W)

    fileExtensionEntry = tk.Entry(window, width=50)
    fileExtensionEntry.grid(row=3, column=1)

    button = tk.Button(window, text="CONFIRM", font=(
        'Arial', 11), command=lambda: doChangeOneFile(pathEntry, oldFileEntry, newFileEntry, fileExtensionEntry))
    button.grid(row=4, column=1, pady=10)

    closeButton = tk.Button(window,
                            text='Close',
                            font=('Arial', 11),
                            command=window.destroy)
    closeButton.grid(row=5, column=1)


def changeMultipleFiles():
    window = tk.Toplevel()
    window.title("Change One File")
    window.geometry("500x200")

    pathLabel = tk.Label(window, text="Path: ", font=('Arial', 12))
    pathLabel.grid(row=0, column=0, sticky=tk.W)

    pathEntry = tk.Entry(window, width=50)
    pathEntry.grid(row=0, column=1)

    oldFileLabel = tk.Label(window, text="File Name: ",
                            font=('Arial', 12))
    oldFileLabel.grid(row=1, column=0, sticky=tk.W)

    oldFileEntry = tk.Entry(window, width=50)
    oldFileEntry.grid(row=1, column=1)

    newFileLabel = tk.Label(window, text="New File Name: ",
                            font=('Arial', 12))
    newFileLabel.grid(row=2, column=0, sticky=tk.W)

    newFileEntry = tk.Entry(window, width=50)
    newFileEntry.grid(row=2, column=1)

    fileExtensionLabel = tk.Label(window, text="File Extension Type: ",
                                  font=('Arial', 12))
    fileExtensionLabel.grid(row=3, column=0, sticky=tk.W)

    fileExtensionEntry = tk.Entry(window, width=50)
    fileExtensionEntry.grid(row=3, column=1)

    button = tk.Button(window, text="CONFIRM", font=(
        'Arial', 11), command=lambda: doChangeMultipleFiles(pathEntry, oldFileEntry, newFileEntry, fileExtensionEntry))
    button.grid(row=4, column=1, pady=10)

    closeButton = tk.Button(window,
                            text='Close',
                            font=('Arial', 11),
                            command=window.destroy)
    closeButton.grid(row=5, column=1)


root = tk.Tk()
root.title("File Name Changer")

# Create a button to create a new window
button1 = tk.Button(root, text="Search and Replace",
                    command=searchAndReplace)
button1.grid(row=0, sticky=tk.W+tk.E)

button2 = tk.Button(root, text="Change One File Name",
                    command=changeOneFile)
button2.grid(row=1, sticky=tk.W+tk.E)

button3 = tk.Button(root, text="Change Multiple Files Names",
                    command=changeMultipleFiles)
button3.grid(row=2, sticky=tk.W+tk.E)

# Start the main loop
root.mainloop()

"""
def searchAndReplace(folder):
    search = input("Find what: ")
    replace = input("Replace with: ")
    paths = (os.path.join(root, filename)
             for root, _, filenames in os.walk(folder)
             for filename in filenames)

    for path in paths:
        newname = path.replace(search, replace)
        if newname != path:
            os.rename(path, newname)
"""


"""
def changeFile(path):
    filename = input("Enter Filename you want to change: ")
    newFileName = input("Enter new Filename: ")
    fileExtension = input("Enter file type extension:")

    dst = f"{newFileName}{fileExtension}"
    src = f"{path}/{filename}{fileExtension}"
    dst = f"{path}/{dst}"

    os.rename(src, dst)
"""


"""
def changeBunchOfFiles(path):
    filename = input("Enter Filename you want to change: ")
    newFileName = input("Enter new Filename: ")
    fileExtension = input("Enter file type extension:")
    listOfFiles = getFiles(filename, fileExtension, path)
    counter = 0
    for count in os.listdir(path):
        if count in listOfFiles:
            counter = counter + 1
            os.rename(count, newFileName+str(counter)+fileExtension)
"""
