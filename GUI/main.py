from tkinter import *
from tkinter import ttk


class tkWindow:

    def __init__(self, root):
        
        def doNew():
            pass
        
        def doSave():
            pass
        
        def doPrint():
            pass
        
        def doPrint():
            pass
        
        menubar = Menu(root)
        menu_file = Menu(menubar, tearoff=0)
        menubar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New', command=doNew)
        menu_file.add_command(label='Save', command=doSave)
        menu_file.add_command(label='Print', command=doPrint)
        menu_file.add_separator()
        menu_file.add_command(label='Quit', command=root.destroy)
        
        root.config(menu=menubar)
        
        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
                        
        fluffframe = ttk.Frame(mainframe)
        fluffframe.grid(column=0, row=1, sticky=(N, W, E, S))
        
        name = StringVar()
        race = StringVar()
        size = StringVar()
        physical_trait1 = StringVar()
        physical_trait2 = StringVar()
        social_trait1 = StringVar()
        social_trait2 = StringVar()
        secret = StringVar()
                
        # stats = stats
        # banes = StringVar()
        # boons = StringVar()
        # feats = StringVar()

        Label(fluffframe, text="Name").grid(row=1, column=1, sticky=W)
        ttk.Entry(fluffframe, textvariable=name).grid(row=1, column=2, columnspan=3, sticky=W + E)
        
        Label(fluffframe, text="Race").grid(row=1, column=6, sticky=W)
        ttk.Entry(fluffframe, textvariable=race).grid(row=1, column=7, columnspan=3, sticky=W + E)

        Label(fluffframe, text="Size").grid(row=1, column=10, sticky=W)
        ttk.Combobox(fluffframe, textvariable=size, values=("Small", "Medium", "Large")).grid(row=1, column=11, columnspan=3, sticky=W + E)
        
        Label(fluffframe, text="Physical Trait 1").grid(row=2, column=1, sticky=W)
        ttk.Entry(fluffframe, textvariable=physical_trait1).grid(row=2, column=2, columnspan=13, sticky=W + E)
        
        Label(fluffframe, text="Physical Trait 2").grid(row=3, column=1, sticky=W)
        ttk.Entry(fluffframe, textvariable=physical_trait2).grid(row=3, column=2, columnspan=13, sticky=W + E)
        
        Label(fluffframe, text="Social Trait 1").grid(row=4, column=1, sticky=W)
        ttk.Entry(fluffframe, textvariable=physical_trait1).grid(row=4, column=2, columnspan=13, sticky=W + E)
        
        Label(fluffframe, text="Social Trait 2").grid(row=5, column=1, sticky=W)
        ttk.Entry(fluffframe, textvariable=physical_trait2).grid(row=5, column=2, columnspan=13, sticky=W + E)
        
        Label(fluffframe, text="Secret").grid(row=6, column=1, sticky=W)
        ttk.Entry(fluffframe, textvariable=secret).grid(row=6, column=2, columnspan=13, rowspan=3, sticky=W + E)
                  
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)


root = Tk()
tkWindow(root)
root.mainloop()