from tkinter import *
from tkinter import ttk
from tkinter import font


class tkWindow:
       
    def __init__(self, root):
    
                  
        def do_new():
            pass

        def do_save():
            pass

        def do_print():
            pass
        
        def calculate_cost(*args):
            COST_TO_INCREASE = {0: 0, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15}
            points = 40
            for stat in stats:
                points = points - COST_TO_INCREASE[stats[stat].get()]
            ability_points.set(points)
        
        def calculate_stats(*args):
            toughnessval.set(10 + stats['fortitudeval'].get() + stats['willval'].get())
            evasionval.set(10 + stats['agilityval'].get() + stats['willval'].get())
            resolveval.set(10 + stats['presenceval'].get() + stats['willval'].get())
            hpval.set(2 * (stats['fortitudeval'].get() + stats['presenceval'].get() + stats['willval'].get()) + 10)    
                
        menubar = Menu(root)
        menu_file = Menu(menubar, tearoff=0)
        menubar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New', command=do_new)
        menu_file.add_command(label='Save', command=do_save)
        menu_file.add_command(label='Print', command=do_print)
        menu_file.add_separator()
        menu_file.add_command(label='Quit', command=root.destroy)
        
        root.config(menu=menubar)

        mainframe = ttk.Frame(root)
        mainframe.grid(row=0, column=0, sticky=(N, W, E, S))

        abilitiesframe = ttk.Frame(mainframe, padding="5 5 5 5")
        abilitiesframe.grid(row=0, column=1, sticky=W)
        
        physicalframe = ttk.Frame(abilitiesframe)
        physicalframe.grid(row=1, column=0, sticky=W)
        
        mentalframe = ttk.Frame(abilitiesframe)
        mentalframe.grid(row=5, column=0, sticky=W)
        
        socialframe = ttk.Frame(abilitiesframe)
        socialframe.grid(row=10, column=0, sticky=W)
        
        extraordinaryframe = Frame(abilitiesframe)
        extraordinaryframe.grid(row=14, column=0, sticky=W)
 
        statframe = ttk.Frame(mainframe)
        statframe.grid(row=0, column=2, padx=25, pady=15, sticky=(N+E))
        
        fluffframe = Frame(mainframe, bg='green')
        fluffframe.grid(row=0, column=3, sticky=(N, W, E, S))
        
        featsframe = Frame(mainframe, bg='blue')
        featsframe.grid(row=1, column=3, sticky=(N, W, E, S))
 
        largefont = font.Font(size=22)
        
        ability_points = IntVar()
        
        stats = {}
                       
        toughnessval = IntVar()
        evasionval = IntVar()
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

        feat_points = IntVar()
        
        feats = list()
        
        
        
        # banes = StringVar()        
        # boons = StringVar()
        # feats = StringVar()
        
        def add_spinboxes(group, frame):
            abilities = list()
            
            groups = {'Physical':('Agility', 'Fortitude', 'Might'), 'Mental':('Learning', 'Logic', 'Perception', 'Will'), \
                    'Social':('Deception', 'Persuasion', 'Presence'), 'Extraordinary':('Alteration', 'Creation', 'Energy', \
                    'Entropy', 'Influence', 'Movement', 'Prescience', 'Protection')}
            for i in range(0,len(groups[group])):
                abilities.append(Spinbox(frame, from_=0, to=5, width=4))
                abilities[i].var = IntVar()
                abilities[i]['textvariable'] = abilities[i].var
                stats[groups[group][i].lower() + 'val'] = abilities[i].var
                if group != "Extraordinary":
                    abilities[i].grid(row=i+1, column=1, padx=(35, 0))
                else: 
                    abilities[i].grid(row=i+1, column=1)
        
        Label(abilitiesframe, text="Points Remaining:").grid(row=0, column=0, sticky=W)
        Label(abilitiesframe, textvariable=ability_points).grid(row=0, column=1, sticky=W)
        
        Label(physicalframe, text="Physical", font="bold").grid(row=0, column=0, sticky=W)
        Label(physicalframe, text="Agility").grid(row=1, column=0, sticky=W)
        Label(physicalframe, text="Fortitude").grid(row=2, column=0, sticky=W)
        Label(physicalframe, text="Might").grid(row=3, column=0, sticky=W)
        add_spinboxes("Physical", physicalframe)
        
        Label(mentalframe, text="Mental", font="bold").grid(row=0, column=0, sticky=W)
        Label(mentalframe, text="Learning").grid(row=1, column=0, sticky=W)
        Label(mentalframe, text="Logic").grid(row=2, column=0, sticky=W)
        Label(mentalframe, text="Perception").grid(row=3, column=0, sticky=W)
        Label(mentalframe, text="Will").grid(row=4, column=0, sticky=W)
        add_spinboxes("Mental", mentalframe)
        
        Label(socialframe, text="Social", font="bold").grid(row=0, column=0, sticky=W)
        Label(socialframe, text="Deception").grid(row=1, column=0, sticky=W)
        Label(socialframe, text="Persuasion").grid(row=2, column=0, sticky=W)
        Label(socialframe, text="Presence").grid(row=3, column=0, sticky=W)
        add_spinboxes("Social", socialframe)
        
        Label(extraordinaryframe, text="Extraordinary", font="bold").grid(row=0, column=0, sticky=W)
        Label(extraordinaryframe, text="Alteration").grid(row=1, column=0, sticky=W)
        Label(extraordinaryframe, text="Creation").grid(row=2, column=0, sticky=W)
        Label(extraordinaryframe, text="Energy").grid(row=3, column=0, sticky=W)
        Label(extraordinaryframe, text="Entropy").grid(row=4, column=0, sticky=W)
        Label(extraordinaryframe, text="Influence").grid(row=5, column=0, sticky=W)
        Label(extraordinaryframe, text="Movement").grid(row=6, column=0, sticky=W)
        Label(extraordinaryframe, text="Prescience").grid(row=7, column=0, sticky=W)
        Label(extraordinaryframe, text="Protection").grid(row=8, column=0, sticky=W)
        add_spinboxes("Extraordinary", extraordinaryframe)
        
        Label(statframe, text="Toughness", font="bold").grid(row=0, column=0, sticky=W+E)
        Label(statframe, textvariable=toughnessval, font=largefont).grid(row=1, column=0)
        Label(statframe, text="Evasion", font="bold").grid(row=2, column=0, sticky=W+E)
        Label(statframe, textvariable=evasionval, font=largefont).grid(row=3, column=0)
        Label(statframe, text="Resolve", font="bold").grid(row=4, column=0, sticky=W+E)
        Label(statframe, textvariable=resolveval, font=largefont).grid(row=5, column=0)
        Label(statframe, text="Hit Points", font="bold").grid(row=6, column=0, sticky=W+E)
        Label(statframe, textvariable=hpval, font=largefont).grid(row=7, column=0)
              
        Label(fluffframe, text="Name").grid(row=0, column=0, sticky=W+E)
        ttk.Entry(fluffframe, textvariable=name).grid(row=0, column=1, columnspan=2, sticky=W + E)
        
        Label(fluffframe, text="Race").grid(row=0, column=3, sticky=W+E)
        ttk.Entry(fluffframe, textvariable=race).grid(row=0, column=4, columnspan=2, sticky=W + E)

        Label(fluffframe, text="Size").grid(row=0, column=6, sticky=W+E)
        ttk.Combobox(fluffframe, textvariable=size, values=("Small", "Medium", "Large"), width=10) \
            .grid(row=0, column=7, sticky=W + E)
        
        Label(fluffframe, text="Physical Trait 1").grid(row=3, column=0, sticky=W+E)
        ttk.Entry(fluffframe, textvariable=physical_trait1).grid(row=3, column=1, columnspan=7, sticky=W + E)
        
        Label(fluffframe, text="Physical Trait 2").grid(row=4, column=0, sticky=W+E)
        ttk.Entry(fluffframe, textvariable=physical_trait2).grid(row=4, column=1, columnspan=7, sticky=W + E)
        
        Label(fluffframe, text="Social Trait 1").grid(row=5, column=0, sticky=W+E)
        ttk.Entry(fluffframe, textvariable=social_trait1).grid(row=5, column=1, columnspan=7, sticky=W + E)
        
        Label(fluffframe, text="Social Trait 2").grid(row=6, column=0, sticky=W+E)
        ttk.Entry(fluffframe, textvariable=social_trait2).grid(row=6, column=1, columnspan=7, sticky=W + E)
        
        Label(fluffframe, text="Secret").grid(row=7, column=0, sticky=W+E)
        ttk.Entry(fluffframe, textvariable=secret).grid(row=7, column=1, columnspan=7, sticky=W+E)
        
        Label(featsframe, text="Available Feats").grid(row=0, column=3, sticky=W)
        Listbox(featsframe, height=10)
        Label(featsframe, text="Selected Feats").grid(row=0, column=4, sticky=W)
        Listbox(featsframe, height=10)
        
        stats['agilityval'].trace('w', calculate_stats)
        stats['fortitudeval'].trace('w', calculate_stats)
        stats['willval'].trace('w', calculate_stats)
        stats['presenceval'].trace('w', calculate_stats)   
        
        for stat in stats:
            stats[stat].trace_add('write', calculate_cost)
        

root = Tk()
root.title("Legendary Characters")
tkWindow(root)
root.mainloop()
