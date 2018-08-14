from tkinter import *
from tkinter import ttk


class tkWindow:

    def __init__(self, root):
        def do_new():
            pass

        def do_save():
            pass

        def do_print():
            pass

        menubar = Menu(root)
        menu_file = Menu(menubar, tearoff=0)
        menubar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New', command=do_new)
        menu_file.add_command(label='Save', command=do_save)
        menu_file.add_command(label='Print', command=do_print)
        menu_file.add_separator()
        menu_file.add_command(label='Quit', command=root.destroy)
        
        root.config(menu=menubar)

        mainframe = ttk.Frame(root, padding="10 10 10 10")
        mainframe.grid(row=0, column=0, sticky=(N, W, E, S))
                        
        fluffframe = ttk.Frame(mainframe)
        fluffframe.grid(row=0, column=1, sticky=(N, W, E, S))

        statframe = ttk.Frame(mainframe)
        statframe.grid(row=0, column=0, sticky=(N, W, E, S))
        
        name = StringVar()
        race = StringVar()
        size = StringVar()
        physical_trait1 = StringVar()
        physical_trait2 = StringVar()
        social_trait1 = StringVar()
        social_trait2 = StringVar()
        secret = StringVar()

        agilityval = IntVar()
        fortitudeval = IntVar()
        mightval = IntVar()
        learningval = IntVar()
        logicval = IntVar()
        perceptionval = IntVar()
        willval = IntVar()
        deceptionval = IntVar()
        persuasionval = IntVar()
        presenceval = IntVar()
        alterationval = IntVar()
        creationval = IntVar()
        energyval = IntVar()
        entropyval = IntVar()
        influenceval = IntVar()
        movementval = IntVar()
        prescienceval = IntVar()
        protectionval = IntVar()

        # banes = StringVar()
        # boons = StringVar()
        # feats = StringVar()

        Label(fluffframe, text="Name").grid(row=1, column=1, sticky=W)
        ttk.Entry(fluffframe, textvariable=name).grid(row=1, column=2, columnspan=2, sticky=W + E)
        
        Label(fluffframe, text="Race").grid(row=1, column=6, sticky=W)
        ttk.Entry(fluffframe, textvariable=race).grid(row=1, column=7, columnspan=2, sticky=W + E)

        Label(fluffframe, text="Size").grid(row=1, column=10, sticky=W)
        ttk.Combobox(fluffframe, textvariable=size, values=("Small", "Medium", "Large")) \
            .grid(row=1, column=11, columnspan=2, sticky=W + E)
        
        Label(fluffframe, text="Physical Trait 1").grid(row=2, column=1, sticky=W)
        ttk.Entry(fluffframe, textvariable=physical_trait1).grid(row=2, column=2, columnspan=13, sticky=W + E)
        
        Label(fluffframe, text="Physical Trait 2").grid(row=3, column=1, sticky=W)
        ttk.Entry(fluffframe, textvariable=physical_trait2).grid(row=3, column=2, columnspan=13, sticky=W + E)
        
        Label(fluffframe, text="Social Trait 1").grid(row=4, column=1, sticky=W)
        ttk.Entry(fluffframe, textvariable=social_trait1).grid(row=4, column=2, columnspan=13, sticky=W + E)
        
        Label(fluffframe, text="Social Trait 2").grid(row=5, column=1, sticky=W)
        ttk.Entry(fluffframe, textvariable=social_trait2).grid(row=5, column=2, columnspan=13, sticky=W + E)
        
        Label(fluffframe, text="Secret").grid(row=6, column=1, sticky=W)
        ttk.Entry(fluffframe, textvariable=secret).grid(row=6, column=2, columnspan=13, rowspan=3, sticky=W + E)

        Label(statframe, text="Physical", font="bold").grid(row=0, column=0, sticky=W)
        Label(statframe, text="Agility").grid(row=1, column=0, sticky=W)
        Spinbox(statframe, from_=0, to=5, textvariable=agilityval).grid(row=1, column=1)
        Label(statframe, text="Mental", font="bold").grid(row=4, column=0, sticky=W)

        Label(statframe, text="Social", font="bold").grid(row=9, column=0, sticky=W)

        Label(statframe, text="Extraordinary", font="bold").grid(row=13, column=0, sticky=W)

root = Tk()
root.title("Legendary Characters")
tkWindow(root)
root.mainloop()
