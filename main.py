import feats as fts

import tkinter as tk  
from tkinter import ttk as ttk
from tkinter import font as tkfont


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        menubar = tk.Menu(self)
        menu_file = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(menu=menu_file, label="File")
        menu_file.add_command(label="New", command=lambda: self.show_frame("NewCharacter"))
        menu_file.add_command(label="Load", command=print("load"))
        menu_file.add_command(label="Save", command=print("save"))
        menu_file.add_command(label="Print", command=print("print"))
        menu_file.add_separator()
        menu_file.add_command(label="Quit", command=self.destroy)
        self.config(menu=menubar)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        for F in (MainMenu, NewCharacter):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()        
       
       
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        
class NewCharacter(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
    
        class Character:
            
            def __init__(self, stats):
                self.stats = stats
        
        def open_feats_window(*args, **kwargs):
            char = Character(stats)
            window = tk.Toplevel(self)

            tk.Label(window, text="Available Feats").grid(row=0, column=7, sticky="we")
            available_feats = tk.Listbox(window, height=10)
            available_feats.grid(row=1, column=7, sticky="w")

            for feat in fts.feat_list:
                if fts.meets_prereqs(char, feat):
                    available_feats.insert("end", fts.feat_list[feat].title)

        def calculate_cost(*args):
            cost_to_increase = {0: 0, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15}
            points = 40
            for stat in stats:
                points = points - cost_to_increase[stats[stat].get()]
                if points < 40:
                    pass  # alert user of 40 point limit
            ability_points.set(points)

        def calculate_stats(*args):
            toughnessval.set(10 + stats["fortitudeval"].get() + stats["willval"].get())
            guardval.set(10 + stats["agilityval"].get() + stats["willval"].get())
            resolveval.set(10 + stats["presenceval"].get() + stats["willval"].get())
            hpval.set(2 * (stats["fortitudeval"].get() + stats["presenceval"].get() + stats["willval"].get()) + 10)

        mainframe = tk.Frame(self)
        mainframe.grid(row=0, column=0, sticky="nsew")

        abilitiesframe = tk.Frame(mainframe)
        abilitiesframe.grid(row=0, column=0, sticky="w")

        physicalframe = tk.Frame(abilitiesframe)
        physicalframe.grid(row=1, column=0, sticky="w")

        mentalframe = tk.Frame(abilitiesframe)
        mentalframe.grid(row=5, column=0, sticky="w")

        socialframe = tk.Frame(abilitiesframe)
        socialframe.grid(row=10, column=0, sticky="w")

        extraordinaryframe = tk.Frame(abilitiesframe)
        extraordinaryframe.grid(row=14, column=0, sticky="w")

        statframe = tk.Frame(mainframe)
        statframe.grid(row=0, column=2, padx=25, pady=15, sticky="ne")

        fluffframe = tk.Frame(mainframe)
        fluffframe.grid(row=0, column=3, sticky="nsew")

        featsframe = tk.Frame(fluffframe)
        featsframe.grid(row=6, column=0, stick="nsew")

        largefont = tkfont.Font(size=22)

        ability_points = tk.IntVar()

        stats = {}

        toughnessval = tk.IntVar()
        guardval = tk.IntVar()
        resolveval = tk.IntVar()
        hpval = tk.IntVar()

        name = tk.StringVar()
        race = tk.StringVar()
        size = tk.StringVar()
        physical_trait1 = tk.StringVar()
        physical_trait2 = tk.StringVar()
        social_trait1 = tk.StringVar()
        social_trait2 = tk.StringVar()
        secret = tk.StringVar()

        # banes = tk.StringVar()
        # boons = tk.StringVar()
        # feats = tk.StringVar()

        def add_spinboxes(group, frame):
            abilities = list()

            groups = {'Physical': ('Agility', 'Fortitude', 'Might'),
                      'Social': ('Deception', 'Persuasion', 'Presence'),
                      'Extraordinary': ('Alteration', 'Creation', 'Energy',
                                        'Entropy', 'Influence', 'Movement', 'Prescience', 'Protection'),
                      'Mental': ('Learning', 'Logic', 'Perception', 'Will')}
            for i in range(0, len(groups[group])):
                abilities.append(tk.Spinbox(frame, from_=0, to=5, width=4))
                abilities[i].var = tk.IntVar()
                abilities[i]['textvariable'] = abilities[i].var
                stats[groups[group][i].lower() + 'val'] = abilities[i].var
                if group != "Extraordinary":
                    abilities[i].grid(row=i + 1, column=1, padx=(35, 0))
                else:
                    abilities[i].grid(row=i + 1, column=1)

        tk.Label(abilitiesframe, text="Points Remaining:").grid(row=0, column=0, sticky="w")
        tk.Label(abilitiesframe, textvariable=ability_points).grid(row=0, column=1, sticky="w")

        tk.Label(physicalframe, text="Physical", font="bold").grid(row=0, column=0, sticky="w")
        tk.Label(physicalframe, text="Agility").grid(row=1, column=0, sticky="w")
        tk.Label(physicalframe, text="Fortitude").grid(row=2, column=0, sticky="w")
        tk.Label(physicalframe, text="Might").grid(row=3, column=0, sticky="w")
        add_spinboxes("Physical", physicalframe)

        tk.Label(mentalframe, text="Mental", font="bold").grid(row=0, column=0, sticky="w")
        tk.Label(mentalframe, text="Learning").grid(row=1, column=0, sticky="w")
        tk.Label(mentalframe, text="Logic").grid(row=2, column=0, sticky="w")
        tk.Label(mentalframe, text="Perception").grid(row=3, column=0, sticky="w")
        tk.Label(mentalframe, text="Will").grid(row=4, column=0, sticky="w")
        add_spinboxes("Mental", mentalframe)

        tk.Label(socialframe, text="Social", font="bold").grid(row=0, column=0, sticky="w")
        tk.Label(socialframe, text="Deception").grid(row=1, column=0, sticky="w")
        tk.Label(socialframe, text="Persuasion").grid(row=2, column=0, sticky="w")
        tk.Label(socialframe, text="Presence").grid(row=3, column=0, sticky="w")
        add_spinboxes("Social", socialframe)

        tk.Label(extraordinaryframe, text="Extraordinary", font="bold").grid(row=0, column=0, sticky="w")
        tk.Label(extraordinaryframe, text="Alteration").grid(row=1, column=0, sticky="w")
        tk.Label(extraordinaryframe, text="Creation").grid(row=2, column=0, sticky="w")
        tk.Label(extraordinaryframe, text="Energy").grid(row=3, column=0, sticky="w")
        tk.Label(extraordinaryframe, text="Entropy").grid(row=4, column=0, sticky="w")
        tk.Label(extraordinaryframe, text="Influence").grid(row=5, column=0, sticky="w")
        tk.Label(extraordinaryframe, text="Movement").grid(row=6, column=0, sticky="w")
        tk.Label(extraordinaryframe, text="Prescience").grid(row=7, column=0, sticky="w")
        tk.Label(extraordinaryframe, text="Protection").grid(row=8, column=0, sticky="w")
        add_spinboxes("Extraordinary", extraordinaryframe)

        tk.Label(statframe, text="Toughness", font="bold").grid(row=0, column=0, sticky="we")
        tk.Label(statframe, textvariable=toughnessval, font=largefont).grid(row=1, column=0)
        tk.Label(statframe, text="Guard", font="bold").grid(row=2, column=0, sticky="we")
        tk.Label(statframe, textvariable=guardval, font=largefont).grid(row=3, column=0)
        tk.Label(statframe, text="Resolve", font="bold").grid(row=4, column=0, sticky="we")
        tk.Label(statframe, textvariable=resolveval, font=largefont).grid(row=5, column=0)
        tk.Label(statframe, text="Hit Points", font="bold").grid(row=6, column=0, sticky="we")
        tk.Label(statframe, textvariable=hpval, font=largefont).grid(row=7, column=0)

        tk.Label(fluffframe, text="Name").grid(row=0, column=0, sticky="w")
        tk.Entry(fluffframe, textvariable=name).grid(row=0, column=1, columnspan=2, sticky="we")

        tk.Label(fluffframe, text="Race").grid(row=0, column=3, sticky="w")
        tk.Entry(fluffframe, textvariable=race).grid(row=0, column=4, columnspan=2, sticky="we")

        tk.Label(fluffframe, text="Size").grid(row=0, column=7, sticky="w")
        ttk.Combobox(fluffframe, textvariable=size, values=("Small", "Medium", "Large"), width=10) \
            .grid(row=0, column=8, sticky="we")

        tk.Label(fluffframe, text="Physical Trait 1").grid(row=1, column=0, sticky="w")
        tk.Entry(fluffframe, textvariable=physical_trait1).grid(row=1, column=1, columnspan=8, sticky="we")

        tk.Label(fluffframe, text="Physical Trait 2").grid(row=2, column=0, sticky="w")
        tk.Entry(fluffframe, textvariable=physical_trait2).grid(row=2, column=1, columnspan=8, sticky="we")

        tk.Label(fluffframe, text="Social Trait 1").grid(row=3, column=0, sticky="w")
        tk.Entry(fluffframe, textvariable=social_trait1).grid(row=3, column=1, columnspan=8, sticky="we")

        tk.Label(fluffframe, text="Social Trait 2").grid(row=4, column=0, sticky="w")
        tk.Entry(fluffframe, textvariable=social_trait2).grid(row=4, column=1, columnspan=8, sticky="we")

        tk.Label(fluffframe, text="Secret").grid(row=5, column=0, sticky="w")
        tk.Entry(fluffframe, textvariable=secret).grid(row=5, column=1, columnspan=8, sticky="we")

        tk.Button(featsframe, text="Purchase Feats", command=open_feats_window).grid(row=1, column=3, sticky="we")
        tk.Label(featsframe, text="Selected Feats").grid(row=0, column=7, sticky="we")
        tk.Listbox(featsframe, height=10).grid(row=1, column=7, sticky="w")

        stats['agilityval'].trace('w', calculate_stats)
        stats['fortitudeval'].trace('w', calculate_stats)
        stats['willval'].trace('w', calculate_stats)
        stats['presenceval'].trace('w', calculate_stats)

        for stat in stats:
            stats[stat].trace_add('write', calculate_cost)

    
if __name__ == "__main__":
    app = Main()
    app.title("Legenardy Characters")
    app.mainloop()
