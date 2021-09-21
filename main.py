from tkinter import *
from functools import partial
from articles import collect_articles
import time


def validate_search(search_key, limit):
    print("Search Key Entered :", search_key.get())
    print("Limit entered :", limit.get())
    tkWindow.quit()
    return


if __name__ == '__main__':
    # q = str(input('Enter Search Key!'))
    # lim = int(input('Enter how much article you needed'))
    tkWindow = Tk()
    tkWindow.geometry('400x150')
    tkWindow.title('Google Scholar Search')

    # username label and text entry box
    search_keyLabel = Label(tkWindow, text="Search Key").grid(row=0, column=0)
    search_key = StringVar()
    search_keyEntry = Entry(tkWindow, textvariable=search_key).grid(row=0, column=1)

    # password label and password entry box
    limitLabel = Label(tkWindow, text="Limit").grid(row=1, column=0)
    limit = StringVar()
    limitEntry = Entry(tkWindow, textvariable=limit).grid(row=1, column=1)
    validate_search = partial(validate_search, search_key, limit)
    # Search button
    searchButton = Button(tkWindow, text="Search", command=validate_search).grid(row=4, column=0)
    tkWindow.mainloop()
    try:
        collect_articles(search_key=search_key.get(), limit=int(limit.get()))
    except Exception as e:
        exit()
