from tkinter import *
from tkinter import ttk


class tkWindow:

    def __init__(self, root):
        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        name = StringVar()
        # description = StringVar()()ription
        # stats = stats
        banes = StringVar(root)
        boons = StringVar(root)
        # feats = StringVar()

        banes_list = {'Blind', 'Silence', 'Knockdown', 'Stun', 'Immobilize'}
        banes.set('Stun')  # set the default option
        boons_list = {'Heal', 'Regeneration', 'Light'}
        boons.set('Heal')  # set the default option

        Label(mainframe, text="Name").grid(row=1, column=1, sticky=W)
        ttk.Entry(mainframe, textvariable=name).grid(row=1, column=2, columnspan=3, sticky=W + E)

        banesDropDown = OptionMenu(mainframe, banes, *banes_list)
        Label(mainframe, text="Choose a bane").grid(row=2, column=1, sticky=W)
        banesDropDown.grid(row=2, column=2)

        boonsDropDown = OptionMenu(mainframe, boons, *boons_list)
        Label(mainframe, text="Choose a boon").grid(row=3, column=1, sticky=W)
        boonsDropDown.grid(row=3, column=2)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)


root = Tk()
tkWindow(root)
root.mainloop()
