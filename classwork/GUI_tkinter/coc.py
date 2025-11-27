import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import threading
import time

# ------------------------------
# CONFIGURATION
# ------------------------------
ROWS, COLS = 6, 6
CELL = 60

ARMY_CAMP_CAPACITY = 80  # max army camp space
NUM_BARRACKS = 2

# Troop info: HP increased, cost very low
TROOP_INFO = {
    "Barbarian": {"hp": 250, "damage": 50, "space": 1, "cost": 5, "train_time": 1, "color": "orange"},
    "Archer": {"hp": 150, "damage": 70, "space": 1, "cost": 7, "train_time": 1, "color": "pink"},
    "Giant": {"hp": 600, "damage": 40, "space": 5, "cost": 15, "train_time": 2, "color": "brown"},
    "Dragon": {"hp": 1000, "damage": 150, "space": 10, "cost": 25, "train_time": 3, "color": "red"},
}

# Building info
BUILDINGS = {
    "Town Hall": {"hp": 400, "color": "red", "gold":200, "elixir":200},
    "Gold Mine": {"hp": 200, "color": "yellow", "gold":100, "elixir":0},
    "Elixir Collector": {"hp": 200, "color": "purple", "gold":0, "elixir":100},
    "Cannon": {"hp": 250, "color": "gray", "gold":50, "elixir":50},
    "Archer Tower": {"hp": 250, "color": "green", "gold":50, "elixir":50}
}

# ------------------------------
# GRID CLASS
# ------------------------------
class BattleGrid:
    def __init__(self, root, title):
        self.frame = tk.Frame(root)
        self.frame.pack(side=tk.LEFT, padx=10)
        tk.Label(self.frame, text=title, font=("Arial", 16, "bold")).pack()
        self.canvas = tk.Canvas(self.frame, width=COLS*CELL, height=ROWS*CELL, bg="white")
        self.canvas.pack()
        self.grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                x1, y1 = c*CELL, r*CELL
                x2, y2 = x1+CELL, y1+CELL
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")
                item = self.grid[r][c]
                if item:
                    self.draw_building(r, c, item)

    def draw_building(self, r, c, b):
        x, y = c*CELL, r*CELL
        self.canvas.create_rectangle(x+5, y+5, x+CELL-5, y+CELL-5, fill=b["color"])
        self.canvas.create_text(x+CELL//2, y+CELL//2, text=b["name"])
        hp_ratio = b["hp"]/b["max_hp"]
        color = "green" if hp_ratio>0.4 else "orange" if hp_ratio>0.2 else "red"
        self.canvas.create_rectangle(x+5, y+CELL-10, x+5+(CELL-10)*hp_ratio, y+CELL-5, fill=color, width=0)

    def draw_troop(self, r, c, troop_type):
        x, y = c*CELL + CELL//2, r*CELL + CELL//2
        color = TROOP_INFO[troop_type]["color"]
        troop_id = self.canvas.create_oval(x-10, y-10, x+10, y+10, fill=color)
        hp_bar = self.canvas.create_rectangle(x-10, y-15, x+10, y-12, fill="green")  # troop HP bar
        return troop_id, hp_bar

# ------------------------------
# GAME CLASS
# ------------------------------
class Game:
    def __init__(self, root):
        self.root = root
        self.gold = 1000
        self.elixir = 1000
        self.loot = 0
        self.army_used = 0
        self.army_capacity = ARMY_CAMP_CAPACITY
        self.trained_troops = {}
        self.training_queue = [[] for _ in range(NUM_BARRACKS)]
        self.barracks_locks = [threading.Lock() for _ in range(NUM_BARRACKS)]

        # Grids
        self.player = BattleGrid(root, "YOUR BASE")
        self.enemy = BattleGrid(root, "ENEMY BASE")
        self.init_player_base()
        self.generate_enemy_base()

        # Menu
        menu = tk.Frame(root)
        menu.pack(pady=5)
        tk.Button(menu, text="Train Troops", command=self.open_training_window).grid(row=0, column=0, padx=5)
        tk.Button(menu, text="Attack Enemy Base", command=self.start_attack).grid(row=0, column=1, padx=5)

        # Status
        self.status = tk.Label(root, font=("Arial", 14))
        self.status.pack()
        self.update_status()

    # ------------------------------
    # Base Initialization
    # ------------------------------
    def init_player_base(self):
        self.player.grid[3][3] = {"name":"Town Hall","hp":400,"max_hp":400,"color":"red"}
        self.player.grid[0][0] = {"name":"Gold Mine","hp":200,"max_hp":200,"color":"yellow"}
        self.player.grid[0][1] = {"name":"Elixir Collector","hp":200,"max_hp":200,"color":"purple"}
        self.player.grid[1][1] = {"name":"Cannon","hp":250,"max_hp":250,"color":"gray"}
        self.player.grid[2][2] = {"name":"Archer Tower","hp":250,"max_hp":250,"color":"green"}
        self.player.draw_grid()

    def generate_enemy_base(self):
        buildings = list(BUILDINGS.keys())
        placed = 0
        while placed<8:
            r, c = random.randint(0,ROWS-1), random.randint(0,COLS-1)
            if self.enemy.grid[r][c] is None:
                name = random.choice(buildings)
                self.enemy.grid[r][c] = {"name":name,"hp":BUILDINGS[name]["hp"],"max_hp":BUILDINGS[name]["hp"],
                                         "color":BUILDINGS[name]["color"]}
                placed+=1
        self.enemy.draw_grid()

    # ------------------------------
    # Training
    # ------------------------------
    def open_training_window(self):
        win = tk.Toplevel(self.root)
        win.title("Train Troops")
        tk.Label(win, text="Train Your Army", font=("Arial",16,"bold")).pack(pady=10)
        frm = tk.Frame(win)
        frm.pack()
        row = 0
        for troop in TROOP_INFO:
            info = TROOP_INFO[troop]
            tk.Label(frm, text=f"{troop} - Cost:{info['cost']} Space:{info['space']}", font=("Arial",12)).grid(row=row,column=0)
            tk.Button(frm,text="Train",command=lambda t=troop:self.train_troop(t)).grid(row=row,column=1)
            row+=1

    def train_troop(self, troop):
        info = TROOP_INFO[troop]
        if self.elixir < info["cost"]:
            messagebox.showwarning("Not enough Elixir","You don't have enough Elixir")
            return
        if self.army_used + info["space"] > self.army_capacity:
            messagebox.showwarning("Army Full","Your Army Camp is full!")
            return
        self.elixir -= info["cost"]
        self.army_used += info["space"]

        for i in range(NUM_BARRACKS):
            if not self.barracks_locks[i].locked():
                threading.Thread(target=self.train_in_barracks,args=(i,troop),daemon=True).start()
                return
        self.training_queue[0].append(troop)

    def train_in_barracks(self,index,troop):
        with self.barracks_locks[index]:
            self.training_queue[index].append(troop)
            time.sleep(TROOP_INFO[troop]["train_time"])
            self.trained_troops[troop] = self.trained_troops.get(troop,0)+1
            self.training_queue[index].remove(troop)
            self.update_status()
            if self.training_queue[index]:
                next_troop = self.training_queue[index][0]
                self.train_in_barracks(index,next_troop)

    def update_status(self):
        troop_status = ", ".join([f"{t}:{q}" for t,q in self.trained_troops.items()])
        self.status.config(text=f"Gold:{self.gold} Elixir:{self.elixir} Loot:{self.loot} Army:{self.army_used}/{self.army_capacity} | Troops:{troop_status}")

    # ------------------------------
    # Animated Attack
    # ------------------------------
    def start_attack(self):
        if not self.trained_troops:
            messagebox.showinfo("No Troops","Train troops before attacking!")
            return
        threading.Thread(target=self.animate_attack,daemon=True).start()

    def animate_attack(self):
        targets = [(r,c,b) for r in range(ROWS) for c in range(COLS) if (b:=self.enemy.grid[r][c])]
        troop_list = []
        troop_health = {}
        for t, n in self.trained_troops.items():
            troop_list += [t]*n
            troop_health[t] = TROOP_INFO[t]["hp"]
        random.shuffle(troop_list)

        destroyed = 0
        gold_loot = 0
        elixir_loot = 0
        total_buildings = len(targets)

        for troop_type in troop_list:
            if not targets: break
            r,c,building = random.choice(targets)
            troop_hp = troop_health[troop_type]

            troop_id, hp_bar = self.enemy.draw_troop(0,0,troop_type)
            self.move_troop_to_target(troop_id, hp_bar, troop_type, r, c, building)

            damage = TROOP_INFO[troop_type]["damage"]
            building["hp"] -= damage
            troop_hp -= random.randint(0,20)  # troop loses some HP
            troop_health[troop_type] = max(0, troop_hp)

            if building["hp"] <= 0:
                destroyed += 1
                gold_loot += BUILDINGS[building["name"]].get("gold",0)
                elixir_loot += BUILDINGS[building["name"]].get("elixir",0)
                self.enemy.grid[r][c] = None
                targets = [(r,c,b) for r in range(ROWS) for c in range(COLS) if (b:=self.enemy.grid[r][c])]
            self.enemy.draw_grid()
            time.sleep(0.5)

        if destroyed==total_buildings:
            stars=3
        elif destroyed>=total_buildings/2:
            stars=2
        elif destroyed>0:
            stars=1
        else:
            stars=0

        self.gold += gold_loot
        self.elixir += elixir_loot
        self.loot += gold_loot + elixir_loot

        self.trained_troops = {}
        self.army_used = 0
        self.update_status()
        messagebox.showinfo("Attack Result",f"Destroyed {destroyed}/{total_buildings} buildings\nStars: {stars}\nLoot: {gold_loot} Gold, {elixir_loot} Elixir")

    def move_troop_to_target(self, troop_id, hp_bar, troop_type, r, c, building):
        target_x = c*CELL + CELL//2
        target_y = r*CELL + CELL//2
        x, y = 0,0

        def step():
            nonlocal x,y
            dx = (target_x - x)/5
            dy = (target_y - y)/5
            x += dx
            y += dy
            self.enemy.canvas.coords(troop_id,x-10,y-10,x+10,y+10)
            self.enemy.canvas.coords(hp_bar, x-10, y-15, x-10+20, y-12)
            if abs(x-target_x)<1 and abs(y-target_y)<1:
                self.enemy.canvas.delete(troop_id)
                self.enemy.canvas.delete(hp_bar)
                return
            self.enemy.canvas.after(50, step)
        step()

# ------------------------------
# RUN GAME
# ------------------------------
root = tk.Tk()
root.title("Mini COC - Troop HP & Low Cost")
game = Game(root)
root.mainloop()
