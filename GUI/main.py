from tkinter import *
from tkinter import ttk
from tkinter import font


ability_points = 40 
COSTS = {0: 0, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15}

class tkWindow:
       
    def __init__(self, root):
                   
        def do_new():
            pass

        def do_save():
            pass

        def do_print():
            pass

        def calculate_stats(*args):
            toughnessval.set(10 + fortitudeval.get() + willval.get())
            guardval.set(10 + agilityval.get() + willval.get())
            resolveval.set(10 + presenceval.get() + willval.get())
            hpval.set(2 * (fortitudeval.get() + presenceval.get() + willval.get()) + 10)    
                
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

        abilitiesframe = ttk.Frame(mainframe, padding="5 5 5 5")
        abilitiesframe.grid(row=0, column=1, sticky=(N, W, E, S))
        
        statframe = Frame(mainframe)
        statframe.grid(row=0, column=2, padx=25, pady=15, sticky=(N+E))

        fluffframe = Frame(mainframe, padding="5 5 5 5")
        fluffframe.grid(row=0, column=3, sticky=(N, W, E, S))
        
        largefont = font.Font(size=22)
        
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
        
        toughnessval = IntVar()
        guardval = IntVar()
        resolveval = IntVar()
        hpval = IntVar()        
        
        name = StringVar()
        race = StringVar()
        size = StringVar()
        physical_trait1 = StringVar()
        physical_trait2 = StringVar()
        social_trait1 = StringVar()
        social_trait2 = StringVar()
        secret = StringVar()

        # banes = StringVar()
        # boons = StringVar()
        # feats = StringVar()
                
        def add_spingboxes(group):
            group = list()
            for i in range(0,18):
                abilities.append(Spinbox(abilitiesframe, from_=0, to=5))
                abilities[i].var = IntVar()
                abilities[i].var.trace_add('write', lambda *_, 
                                                var=abilities[i].var:calculate_stats(var))
                abilities[i]['textvariable'] = abilities[i].var
                abilities[i].grid(row=i+1, column=2)
            
        Label(abilitiesframe, text="Physical", font="bold").grid(row=0, column=0, sticky=W)
        Label(abilitiesframe, text="Agility").grid(row=1, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=agilityval).grid(row=1, column=1)
        Label(abilitiesframe, text="Fortitude").grid(row=2, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=fortitudeval).grid(row=2, column=1)
        Label(abilitiesframe, text="Might").grid(row=3, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=mightval).grid(row=3, column=1)
        
        Label(abilitiesframe, text="Mental", font="bold").grid(row=4, column=0, sticky=W)
        Label(abilitiesframe, text="Learning").grid(row=5, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=learningval).grid(row=5, column=1)
        Label(abilitiesframe, text="Logic").grid(row=6, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=logicval).grid(row=6, column=1)
        Label(abilitiesframe, text="Perception").grid(row=7, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=perceptionval).grid(row=7, column=1)
        Label(abilitiesframe, text="Will").grid(row=8, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=willval).grid(row=8, column=1)
        
        Label(abilitiesframe, text="Social", font="bold").grid(row=9, column=0, sticky=W)
        Label(abilitiesframe, text="Deception").grid(row=10, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=deceptionval).grid(row=10, column=1)
        Label(abilitiesframe, text="Persuasion").grid(row=11, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=persuasionval).grid(row=11, column=1)
        Label(abilitiesframe, text="Presence").grid(row=12, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=presenceval).grid(row=12, column=1)
        
        Label(abilitiesframe, text="Extraordinary", font="bold").grid(row=13, column=0, sticky=W)
        Label(abilitiesframe, text="Alteration").grid(row=14, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=alterationval).grid(row=14, column=1)
        Label(abilitiesframe, text="Creation").grid(row=15, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=creationval).grid(row=15, column=1)
        Label(abilitiesframe, text="Energy").grid(row=16, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=energyval).grid(row=16, column=1)
        Label(abilitiesframe, text="Entropy").grid(row=17, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=entropyval).grid(row=17, column=1)
        Label(abilitiesframe, text="Influence").grid(row=18, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=influenceval).grid(row=18, column=1)
        Label(abilitiesframe, text="Movement").grid(row=19, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=movementval).grid(row=19, column=1)   
        Label(abilitiesframe, text="Prescience").grid(row=20, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=prescienceval).grid(row=20, column=1)
        Label(abilitiesframe, text="Protection").grid(row=21, column=0, sticky=W)
        #Spinbox(abilitiesframe, from_=0, to=5, textvariable=protectionval).grid(row=21, column=1)     
        
        Label(statframe, text="Toughness", font="bold").grid(row=0, column=0, sticky=W+E)
        Label(statframe, textvariable=toughnessval, font=largefont).grid(row=1, column=0)
        Label(statframe, text="Guard", font="bold").grid(row=2, column=0, sticky=W+E)
        Label(statframe, textvariable=guardval, font=largefont).grid(row=3, column=0)
        Label(statframe, text="Resolve", font="bold").grid(row=4, column=0, sticky=W+E)
        Label(statframe, textvariable=resolveval, font=largefont).grid(row=5, column=0)
        Label(statframe, text="Hit Points", font="bold").grid(row=6, column=0, sticky=W+E)
        Label(statframe, textvariable=hpval, font=largefont).grid(row=7, column=0)
        
        Label(fluffframe, text="Name").grid(row=1, column=1, sticky=W)
        ttk.Entry(fluffframe, textvariable=name).grid(row=1, column=2, columnspan=2, sticky=W + E)
        
        Label(fluffframe, text="Race").grid(row=1, column=6, sticky=W)
        ttk.Entry(fluffframe, textvariable=race).grid(row=1, column=7, columnspan=2, sticky=W + E)

        Label(fluffframe, text="Size").grid(row=1, column=10, sticky=W)
        ttk.Combobox(fluffframe, textvariable=size, values=("Small", "Medium", "Large"), width=10) \
            .grid(row=1, column=11, sticky=W + E)
        
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
        
        fortitudeval.trace('w', calculate_stats)
        willval.trace('w', calculate_stats)
        agilityval.trace('w', calculate_stats)
        presenceval.trace('w', calculate_stats)       
        

root = Tk()
root.title("Legendary Characters")
tkWindow(root)
root.mainloop()
