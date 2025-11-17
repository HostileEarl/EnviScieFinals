trash_items = [
      Recyclable
    ("Paper", "Recyclable"),
    ("Plastic Bottle", "Recyclable"),
    ("Cardboard", "Recyclable"),
    ("Tin Can", "Recyclable"),
    ("Glass Bottle", "Recyclable"),
    ("Newspaper", "Recyclable"),
    ("Plastic Container", "Recyclable"),
    ("Aluminum Foil", "Recyclable"),
    ("Plastic Bag", "Recyclable"),
    ("Used Paper Carton", "Recyclable"),
    ("Magazines", "Recyclable"),
    ("Soda Can", "Recyclable"),
    ("Water Bottle Cap", "Recyclable"),
    ("Plastic Wrapper", "Recyclable"),
    ("Metal Lid", "Recyclable"),
    ("Carton Box", "Recyclable"),

      Biodegradable
    ("Banana Peel", "Biodegradable"),
    ("Apple Core", "Biodegradable"),
    ("Leftover Food", "Biodegradable"),
    ("Vegetable Scraps", "Biodegradable"),
    ("Leaves", "Biodegradable"),
    ("Eggshells", "Biodegradable"),
    ("Rice", "Biodegradable"),
    ("Fruit Peels", "Biodegradable"),
    ("Coffee Grounds", "Biodegradable"),
    ("Tea Leaves", "Biodegradable"),
    ("Bread Crumbs", "Biodegradable"),
    ("Corn Cob", "Biodegradable"),
    ("Coconut Shell", "Biodegradable"),
    ("Plant Trimmings", "Biodegradable"),
    ("Used Tea Bag", "Biodegradable"),
    ("Fish Bones", "Biodegradable"),

      Residual
    ("Broken Glass", "Residual"),
    ("Ceramics", "Residual"),
    ("Used Tissue", "Residual"),
    ("Diapers", "Residual"),
    ("Cigarette Butts", "Residual"),
    ("Styrofoam", "Residual"),
    ("Plastic Straw", "Residual"),
    ("Plastic Spoon/Fork", "Residual"),
    ("Hair", "Residual"),
    ("Rubber Band", "Residual"),
    ("Sanitary Napkin", "Residual"),
    ("Pet Waste", "Residual"),
    ("Used Mask", "Residual"),
    ("Chip Bag", "Residual"),
    ("Candy Wrapper", "Residual"),
    ("Foil Candy Wrapper", "Residual")
]

  -------------------- IMPORTS --------------------
import tkinter as tk
import tkinter.font as tkfont
import random
from tkinter import messagebox
from datetime import datetime

  PIL for background resizing
from PIL import Image, ImageTk

  -------------------- RESPONSIVE MANAGER --------------------
class ResponsiveManager:
    def __init__(self, root, base_width=1000, base_height=700):
        self.root = root
        self.base_w = base_width
        self.base_h = base_height

        self.fonts = {
            'title': tkfont.Font(family='Helvetica', size=36, weight='bold'),
            'header': tkfont.Font(family='Helvetica', size=24, weight='bold'),
            'subheader': tkfont.Font(family='Helvetica', size=18, weight='bold'),
            'normal': tkfont.Font(family='Helvetica', size=14),
            'small': tkfont.Font(family='Helvetica', size=12),
            'button': tkfont.Font(family='Helvetica', size=14, weight='bold'),
        }

        self.registrations = []
        self.scale = 1.0

        root.bind('<Configure>', self._on_configure)
        root.after(50, self._initial_apply)

    def _on_configure(self, event):
        try:
            w = max(200, self.root.winfo_width())
            h = max(200, self.root.winfo_height())
        except Exception:
            w, h = self.base_w, self.base_h

        new_scale = min(
            max(w / self.base_w, 0.5),
            max(h / self.base_h, 2.5)
        )

        if abs(new_scale - self.scale) > 0.02:
            self.scale = new_scale
            self.apply_scale()

    def _initial_apply(self):
        try:
            w = max(200, self.root.winfo_width())
            h = max(200, self.root.winfo_height())
        except Exception:
            w, h = self.base_w, self.base_h
        self.scale = min(max(w / self.base_w, 0.5), max(h / self.base_h, 2.5))
        self.apply_scale()

    def register(self, widget, base_props):
        self.registrations.append((widget, base_props))
        self._apply_to_widget(widget, base_props)

    def apply_scale(self):
        for key, f in self.fonts.items():
            try:
                base_size = int(abs(f.cget('size')))
            except Exception:
                base_size = 12
            new_size = max(8, int(base_size * self.scale))
            f.configure(size=new_size)
        for widget, props in self.registrations:
            self._apply_to_widget(widget, props)

    def _apply_to_widget(self, widget, props):
        fk = props.get('font_key')
        if fk and fk in self.fonts:
            try:
                widget.configure(font=self.fonts[fk])
            except Exception:
                pass
        for k in ('padx', 'pady', 'ipadx', 'ipady'):
            if k in props:
                try:
                    val = max(0, int(props[k] * self.scale))
                    widget.configure(**{k: val})
                except Exception:
                    pass
        if 'wraplength' in props:
            try:
                widget.configure(wraplength=max(40, int(props['wraplength'] * self.scale)))
            except Exception:
                pass



class MenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=" e8f5e9")
        self.controller = controller

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        title = tk.Label(self, text="♻ ECO-QUEST SUITE ♻", bg=" e8f5e9")
        title.grid(row=0, column=0, pady=(20, 6))
        controller.resp.register(title, {"font_key": "title", "padx": 10, "pady": 6})

        subtitle = tk.Label(
            self,
            text="Interactive Educational Games for Environmental Science",
            bg=" e8f5e9"
        )
        subtitle.grid(row=1, column=0)
        controller.resp.register(subtitle, {"font_key": "normal", "wraplength": 900})

        btn_frame = tk.Frame(self, bg=" e8f5e9")
        btn_frame.grid(row=2, column=0, padx=20, sticky="ew")
        btn_frame.columnconfigure(0, weight=1)

        b1 = tk.Button(btn_frame, text="1) Trash Sorter",
                       command=lambda: controller.show_frame("TrashSorterFrame"))
        b1.grid(row=0, column=0, sticky="ew", pady=6)
        controller.resp.register(b1, {"font_key": "button"})

        b2 = tk.Button(btn_frame, text="2) Climate Crisis Manager",
                       command=lambda: controller.show_frame("ClimateManagerFrame"))
        b2.grid(row=1, column=0, sticky="ew", pady=6)
        controller.resp.register(b2, {"font_key": "button"})

        b3 = tk.Button(btn_frame, text="3) Renewable Energy Builder",
                       command=lambda: controller.show_frame("RenewableBuilderFrame"))
        b3.grid(row=2, column=0, sticky="ew", pady=6)
        controller.resp.register(b3, {"font_key": "button"})

        guide_frame = tk.LabelFrame(self, text="Guidelines & Learning Goals",
                                    padx=10, pady=10, bg=" e8f5e9")
        guide_frame.grid(row=3, column=0, padx=40, sticky="ew")

        g_label = tk.Label(
            guide_frame,
            text=(
                "• Core themes: Waste management, Climate adaptation, Renewable energy.\n"
                "• Digital interactive games suitable for classroom.\n"
                "• Mechanics: Classification, resource management, decision-making.\n"
                "• Each game includes scoring and restart options."
            ),
            justify="left", bg=" e8f5e9"
        )
        g_label.pack(fill="x")


  -------------------- TRASH SORTER FRAME --------------------
class TrashSorterFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=" f0fff4")
        self.controller = controller

          Use the global trash_items (copied to avoid mutation of the global list)
        try:
            self.unused_items = trash_items.copy()
        except Exception:
            self.unused_items = [('Paper','Recyclable'), ('Banana Peel','Biodegradable'), ('Broken Glass','Residual')]

        self.current_item = None
        self.score = 0
        self.hearts = 3

          grid setup
        for i in range(8):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)

        header = tk.Label(self, text="♻ ECO-QUEST: TRASH SORTER", bg=" f0fff4")
        header.grid(row=0, column=0, pady=(8,6))
        if hasattr(controller, 'resp'):
            controller.resp.register(header, {"font_key":"header"})

        self.trash_label = tk.Label(self, text="Trash Item:", bg=" f0fff4")
        self.trash_label.grid(row=1, column=0)
        if hasattr(controller, 'resp'):
            controller.resp.register(self.trash_label, {"font_key":"subheader"})

        stats = tk.Frame(self, bg=" f0fff4")
        stats.grid(row=2, column=0)
        self.score_label = tk.Label(stats, text=f"Score: {self.score}", bg=" f0fff4")
        self.score_label.grid(row=0, column=0, padx=8)
        self.hearts_label = tk.Label(stats, text="❤ ❤ ❤", bg=" f0fff4")
        self.hearts_label.grid(row=0, column=1, padx=8)
        if hasattr(controller, 'resp'):
            controller.resp.register(self.score_label, {"font_key":"normal"})
            controller.resp.register(self.hearts_label, {"font_key":"subheader"})

        btn_frame = tk.Frame(self, bg=" f0fff4")
        btn_frame.grid(row=3, column=0, sticky='ew', padx=20)
        btn_frame.columnconfigure((0,1,2), weight=1)

        self.recyclable_btn = tk.Button(btn_frame, text="Recyclable", command=lambda: self.check_answer('Recyclable'))
        self.recyclable_btn.grid(row=0, column=0, sticky='ew', padx=6, pady=6)
        self.bio_btn = tk.Button(btn_frame, text="Biodegradable", command=lambda: self.check_answer('Biodegradable'))
        self.bio_btn.grid(row=0, column=1, sticky='ew', padx=6, pady=6)
        self.residual_btn = tk.Button(btn_frame, text="Residual", command=lambda: self.check_answer('Residual'))
        self.residual_btn.grid(row=0, column=2, sticky='ew', padx=6, pady=6)

        ctrl = tk.Frame(self, bg=" f0fff4")
        ctrl.grid(row=6, column=0)

        rbtn = tk.Button(ctrl, text='Restart Game', command=self.restart_game)
        rbtn.grid(row=0, column=0, padx=6)

        bbtn = tk.Button(ctrl, text='Back to Menu', command=self.back_to_menu)
        bbtn.grid(row=0, column=1, padx=6)

        self.next_item()

    def next_item(self):
        if not self.unused_items:
            self.trash_label.config(text="All items sorted! Restart to play again.")
            self.recyclable_btn.config(state='disabled')
            self.bio_btn.config(state='disabled')
            self.residual_btn.config(state='disabled')
            return
        item, cat = random.choice(self.unused_items)
        self.unused_items.remove((item, cat))
        self.current_item = (item, cat)
        self.trash_label.config(text=f"Trash Item: {item}")

    def check_answer(self, selected):
        if not self.current_item:
            return
        correct = self.current_item[1]
        if selected == correct:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            messagebox.showinfo("Correct", f"Correct — {self.current_item[0]} is {correct}.")
        else:
            self.hearts -= 1
            self.hearts_label.config(text="❤ " * self.hearts if self.hearts > 0 else "")
            messagebox.showwarning("Incorrect", f"Incorrect — {self.current_item[0]} is {correct}.")
            if self.hearts <= 0:
                self.trash_label.config(text="You ran out of hearts! Game Over.")
                self.recyclable_btn.config(state='disabled')
                self.bio_btn.config(state='disabled')
                self.residual_btn.config(state='disabled')
                return
        self.next_item()

    def restart_game(self):
        try:
            self.unused_items = trash_items.copy()
        except Exception:
            self.unused_items = [('Paper','Recyclable'), ('Banana Peel','Biodegradable'), ('Broken Glass','Residual')]
        self.score = 0
        self.hearts = 3
        self.score_label.config(text=f"Score: {self.score}")
        self.hearts_label.config(text="❤ ❤ ❤")
        self.recyclable_btn.config(state='normal')
        self.bio_btn.config(state='normal')
        self.residual_btn.config(state='normal')
        self.next_item()

    def back_to_menu(self):
        self.restart_game()
        self.controller.show_frame("MenuFrame")

  -------------------- CLIMATE MANAGER FRAME --------------------
class ClimateManagerFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=" fff8e1")
        self.controller = controller

          Game State
        self.turn = 1
        self.max_turns = 8
        self.temperature = 2.0
        self.budget = 100
        self.score = 0
        self.hearts = 3

          Grid config
        for i in range(8):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)

          Header
        header = tk.Label(self, text=" CLIMATE CRISIS MANAGER", bg=" fff8e1")
        header.grid(row=0, column=0, pady=(8, 6))
        if hasattr(controller, 'resp'):
            controller.resp.register(header, {"font_key": "header"})

          Instructions
        instr = tk.Label(
            self,
            text=(
                "You are the City Planner. Over a series of turns, select actions to reduce\n"
                "projected temperature rise while balancing budget. Keep temperature below 3.5°C by the final turn."
            ),
            bg=" fff8e1",
            justify='left'
        )
        instr.grid(row=1, column=0, sticky='ew', padx=10)
        if hasattr(controller, 'resp'):
            controller.resp.register(instr, {"font_key": "normal", "wraplength": 900})

          Info Panel
        info = tk.Frame(self, bg=" fff8e1")
        info.grid(row=2, column=0, sticky='ew', padx=10)
        info.columnconfigure(tuple(range(5)), weight=1)

        self.turn_label = tk.Label(info, text=f"Turn: {self.turn}/{self.max_turns}", bg=" fff8e1")
        self.turn_label.grid(row=0, column=0)

        self.temp_label = tk.Label(info, text=f"Projected Temp Rise: {self.temperature:.2f}°C", bg=" fff8e1")
        self.temp_label.grid(row=0, column=1)

        self.budget_label = tk.Label(info, text=f"Budget: ${self.budget}", bg=" fff8e1")
        self.budget_label.grid(row=0, column=2)

        self.score_label = tk.Label(info, text=f"Score: {self.score}", bg=" fff8e1")
        self.score_label.grid(row=0, column=3)

        self.hearts_label = tk.Label(info, text="❤ ❤ ❤", bg=" fff8e1")
        self.hearts_label.grid(row=0, column=4)

        if hasattr(controller, 'resp'):
            controller.resp.register(self.score_label, {"font_key": "normal"})
            controller.resp.register(self.hearts_label, {"font_key": "subheader"})

          Action Buttons
        actions = tk.Frame(self, bg=" fff8e1")
        actions.grid(row=3, column=0, sticky='ew', padx=10)
        actions.columnconfigure((0, 1, 2), weight=1)

        a1 = tk.Button(actions, text='Plant Urban Forest', command=lambda: self.take_action('forest'))
        a1.grid(row=0, column=0, sticky='ew', padx=6, pady=6)

        a2 = tk.Button(actions, text='Improve Public Transit', command=lambda: self.take_action('transit'))
        a2.grid(row=0, column=1, sticky='ew', padx=6, pady=6)

        a3 = tk.Button(actions, text='Subsidize Renewables', command=lambda: self.take_action('renewable'))
        a3.grid(row=0, column=2, sticky='ew', padx=6, pady=6)

        if hasattr(controller, 'resp'):
            controller.resp.register(a1, {"font_key": "button"})
            controller.resp.register(a2, {"font_key": "button"})
            controller.resp.register(a3, {"font_key": "button"})

          Message Box
        self.message_box = tk.Label(self, text='', bg=" fff8e1", wraplength=900, justify='center')
        self.message_box.grid(row=5, column=0, sticky='ew', padx=12)
        if hasattr(controller, 'resp'):
            controller.resp.register(self.message_box, {"font_key": "normal"})

          Control Buttons
        ctrl = tk.Frame(self, bg=" fff8e1")
        ctrl.grid(row=6, column=0)

        rbtn = tk.Button(ctrl, text='Restart Game', command=self.restart_game)
        rbtn.grid(row=0, column=0, padx=6)

        bbtn = tk.Button(ctrl, text='Back to Menu', command=self.back_to_menu)
        bbtn.grid(row=0, column=1, padx=6)

        self.update_ui()


    def update_ui(self):
        self.turn_label.config(text=f"Turn: {self.turn}/{self.max_turns}")
        self.temp_label.config(text=f"Projected Temp Rise: {self.temperature:.2f}°C")
        self.budget_label.config(text=f"Budget: ${self.budget}")
        self.score_label.config(text=f"Score: {self.score}")
        self.hearts_label.config(text="❤ " * self.hearts if self.hearts > 0 else "")

    def take_action(self, action):
        if self.turn > self.max_turns or self.hearts <= 0:
            return

        outcome = ""
        cost = 0
        delta = 0.0

        if action == 'forest':
            cost = 15
            delta = -0.15 + random.uniform(-0.05, 0.05)
            self.score += 10
            outcome = f"Planted urban trees. Cost ${cost}. Temp change {delta:.2f}°C."

        elif action == 'transit':
            cost = 25
            if random.random() < 0.75:
                delta = -0.25 + random.uniform(-0.05, 0.05)
                self.score += 14
            else:
                delta = 0.05
                self.score += 4
            outcome = f"Transit action. Cost ${cost}. Temp change {delta:.2f}°C."

        elif action == 'renewable':
            cost = 30
            if random.random() < 0.8:
                delta = -0.35 + random.uniform(-0.07, 0.07)
                self.score += 20
            else:
                delta = 0.10
                self.score += 2
            outcome = f"Renewable subsidy. Cost ${cost}. Temp change {delta:.2f}°C."

        else:
            return

        self.budget -= cost
        self.temperature += delta

        if self.budget < 0:
            self.hearts -= 1
            outcome += " Budget overspent! You lose a heart."

        self.update_ui()
        self.message_box.config(text=outcome)

        if self.turn >= self.max_turns or self.hearts <= 0:
            self.end_game()
        else:
            self.turn += 1
            self.temperature += random.uniform(0, 0.08)
            self.update_ui()


    def end_game(self):
        threshold = 3.5
        if self.hearts <= 0:
            messagebox.showinfo("Game Over", f"You ran out of hearts. Temp: {self.temperature:.2f}°C")
        else:
            if self.temperature <= threshold:
                messagebox.showinfo("Success!", f"You kept temperature to {self.temperature:.2f}°C. Well planned!")
            else:
                messagebox.showinfo("Result", f"Final temp: {self.temperature:.2f}°C. Try different strategies next time.")

    def restart_game(self):
        self.turn = 1
        self.temperature = 2.0 + random.uniform(0, 0.4)
        self.budget = 100
        self.score = 0
        self.hearts = 3
        self.message_box.config(text="")
        self.update_ui()

    def back_to_menu(self):
        self.restart_game()
        self.controller.show_frame("MenuFrame")

class RenewableBuilderFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="e6f0ff")
        self.controller = controller


        self.projects = [
            ("Sunny Plains", "Solar Farm", "High solar irradiance; large open land."),
            ("Coastal Area", "Offshore Wind", "Strong coastal winds ideal for turbines."),
            ("Mountain Stream", "Small Hydropower", "Flowing water for micro-hydro."),
            ("Urban Rooftops", "Rooftop Solar", "Distributed panels on buildings."),
            ("Rural Farmland", "Agrovoltaics", "Combine crops with solar panels."),
            ("Desert Basin", "Large Solar PV", "Vast sunny area for utility-scale PV."),
            ("Windy Plateau", "Onshore Wind", "High wind speeds; turbines on land."),
            ("Geothermal Field", "Geothermal Plant", "Heat from below the surface."),
            ("Island Community", "Hybrid Solar+Wind", "Combine small-scale systems for reliability."),
            ("Industrial Zone", "Waste-to-Energy", "Use industrial organic waste for energy."),
        ]

        self.unused_sites = self.projects.copy()
        self.score = 0
        self.hearts = 3

        for i in range(8):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)

        header = tk.Label(self, text=" RENEWABLE ENERGY BUILDER", bg="e6f0ff")
        header.grid(row=0, column=0, pady=(6, 8))
        if hasattr(controller, 'resp'):
            controller.resp.register(header, {"font_key": "header"})

        instr = tk.Label(
            self,
            text=(
                "Match the best renewable energy project to the given site.\n"
                "Choose wisely — you earn points for correct matches and have 3 hearts for mistakes."
            ),
            bg="e6f0ff",
            justify='left'
        )
        instr.grid(row=1, column=0, sticky='ew', padx=10)
        if hasattr(controller, 'resp'):
            controller.resp.register(instr, {"font_key": "normal", "wraplength": 900})

        self.site_label = tk.Label(self, text='Site:', bg="e6f0ff")
        self.site_label.grid(row=2, column=0)
        if hasattr(controller, 'resp'):
            controller.resp.register(self.site_label, {"font_key": "subheader"})

        choices = tk.Frame(self, bg="e6f0ff")
        choices.grid(row=3, column=0, sticky='ew', padx=10)
        choices.columnconfigure((0, 1, 2), weight=1)

        self.choice_buttons = []
        for i in range(3):
            b = tk.Button(choices, text=f'Choice {i+1}', command=lambda idx=i: self.select_choice(idx))
            b.grid(row=0, column=i, sticky='ew', padx=6, pady=6)
            self.choice_buttons.append(b)
            if hasattr(controller, 'resp'):
                controller.resp.register(b, {"font_key": "button"})

        stats = tk.Frame(self, bg="e6f0ff")
        stats.grid(row=4, column=0)

        self.score_label = tk.Label(stats, text='Score: 0', bg="e6f0ff")
        self.score_label.grid(row=0, column=0)

        self.hearts_label = tk.Label(stats, text='❤ ❤ ❤', bg="e6f0ff")
        self.hearts_label.grid(row=0, column=1)

        if hasattr(controller, 'resp'):
            controller.resp.register(self.score_label, {"font_key": "normal"})
            controller.resp.register(self.hearts_label, {"font_key": "subheader"})


        ctrl = tk.Frame(self, bg="e6f0ff")
        ctrl.grid(row=6, column=0)

        rbtn = tk.Button(ctrl, text='Restart Game', command=self.restart_game)
        rbtn.grid(row=0, column=0, padx=6)

        bbtn = tk.Button(ctrl, text='Back to Menu', command=self.back_to_menu)
        bbtn.grid(row=0, column=1, padx=6)

        self.hint_label = tk.Label(self, text='', bg="e6f0ff", wraplength=900, justify='left')
        self.hint_label.grid(row=7, column=0, sticky='ew', padx=10)
        if hasattr(controller, 'resp'):
            controller.resp.register(self.hint_label, {"font_key": "normal"})

        self.next_site()

  

    def next_site(self):
        if not self.unused_sites:
            self.site_label.config(text='No more sites! Well done — restart to play again.')
            for b in self.choice_buttons:
                b.config(state='disabled')
            return

        site_name, best_proj, expl = random.choice(self.unused_sites)
        self.unused_sites.remove((site_name, best_proj, expl))

        all_projects = [p for (_, p, _) in self.projects]
        wrongs = [p for p in all_projects if p != best_proj]

         Generate 3 choices (1 correct, 2 wrong)
        choices = random.sample(wrongs, 2) + [best_proj]
        random.shuffle(choices)

        self.site_label.config(text=f"Site: {site_name}")

        for i, b in enumerate(self.choice_buttons):
            b.config(text=choices[i], state='normal')

        self.correct = best_proj
        self.correct_expl = expl
        self.hint_label.config(text='')

    def select_choice(self, idx):
        choice = self.choice_buttons[idx].cget('text')

        if choice == self.correct:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            messagebox.showinfo("Correct", f"Good match! {self.correct}")
            self.next_site()
        else:
            self.hearts -= 1
            self.hearts_label.config(text="❤ " * self.hearts if self.hearts > 0 else "")

            self.hint_label.config(
                text=f"Incorrect. Best match: {self.correct}.\nReason: {self.correct_expl}"
            )

            if self.hearts <= 0:
                self.site_label.config(text="You ran out of hearts! Game Over.")
                for b in self.choice_buttons:
                    b.config(state='disabled')
            else:
                self.next_site()

    def restart_game(self):
        self.unused_sites = self.projects.copy()
        self.score = 0
        self.hearts = 3
        self.score_label.config(text="Score: 0")
        self.hearts_label.config(text="❤ ❤ ❤")

        for b in self.choice_buttons:
            b.config(state='normal')

        self.hint_label.config(text='')
        self.next_site()

    def back_to_menu(self):
        self.restart_game()
        self.controller.show_frame("MenuFrame")


class EcoQuestApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EcoQuest Suite — Environmental Science Games")
        self.geometry("1000x700")
        self.minsize(700, 500)
         Start maximized like your original basis
        try:
            self.state("zoomed")
        except Exception:
            pass

        self.resp = ResponsiveManager(self)

         Container that holds frames
        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky="nsew")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


        try:
            self._original_bg = Image.open("background.jpg")
        except Exception:

            self._original_bg = None

        self._bg_image_tk = None
        if self._original_bg:
              place background label behind frames
            self._bg_label = tk.Label(self.container)
            self._bg_label.place(x=0, y=0, relwidth=1, relheight=1)
              bind resize
            self.container.bind("<Configure>", self._resize_bg)
              initially set image to current container size once available
            self.after(50, lambda: self._resize_bg())

        self.frames = {}
        for F in (MenuFrame, TrashSorterFrame, ClimateManagerFrame, RenewableBuilderFrame):
            name = F.__name__
            frame = F(self.container, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MenuFrame")

    def _resize_bg(self, event=None):
          Determine size from container
        if not self._original_bg:
            return
        try:
            if event is not None:
                w = event.width
                h = event.height
            else:
                w = max(200, self.container.winfo_width())
                h = max(200, self.container.winfo_height())
            if w <= 1 or h <= 1:
                return
            resized = self._original_bg.resize((w, h))
            self._bg_image_tk = ImageTk.PhotoImage(resized)
              update label image
            self._bg_label.config(image=self._bg_image_tk)
        except Exception:
            pass

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

if __name__ == "__main__":
    app = EcoQuestApp()
    app.mainloop()
