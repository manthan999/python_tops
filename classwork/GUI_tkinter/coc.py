import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import json
import os

# --------------------------
# GLOBAL VARIABLES
# --------------------------
ROWS, COLS = 6, 6
gold, elixir, stars = 500, 500, 0
troops = {"Barbarian": 0, "Archer": 0, "Giant": 0, "Dragon": 0}
heroes = {"Barbarian King": {"hp": 500, "damage": 60},
          "Archer Queen": {"hp": 400, "damage": 80}}
spells = {"Heal": 3, "Rage": 2, "Freeze": 2, "Lightning": 1}
SAVE_FILE = "coc_save.json"

# 6x6 grids
village_base = [[None for _ in range(COLS)] for _ in range(ROWS)]
enemy_base = [[None for _ in range(COLS)] for _ in range(ROWS)]

# Buildings & troops
BUILDINGS = {
    "Town Hall": {"hp": 400, "color": "red"},
    "Gold Mine": {"hp": 200, "color": "gold"},
    "Elixir Collector": {"hp": 200, "color": "violet"},
    "Cannon": {"hp": 250, "color": "gray"},
    "Archer Tower": {"hp": 250, "color": "lightgray"}
}

TROOPS_DATA = {
    "Barbarian": {"hp": 120, "damage": 40},
    "Archer": {"hp": 80, "damage": 60},
    "Giant": {"hp": 300, "damage": 30},
    "Dragon": {"hp": 400, "damage": 150}
}

# --------------------------
# SAVE / LOAD
# --------------------------
def save_game():
    data = {
        "gold": gold, "elixir": elixir, "stars": stars,
        "troops": troops, "heroes": heroes,
        "village_base": village_base, "enemy_base": enemy_base,
        "spells": spells
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    messagebox.showinfo("Save", "Game saved!")

def load_game():
    global gold, elixir, stars, troops, heroes, village_base, enemy_base, spells
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            gold = data.get("gold", 500)
            elixir = data.get("elixir", 500)
            stars = data.get("stars", 0)
            troops = data.get("troops", troops)
            heroes = data.get("heroes", heroes)
            village_base = data.get("village_base", village_base)
            enemy_base = data.get("enemy_base", enemy_base)
            spells = data.get("spells", spells)
        update_status()
        draw_base(player_frame, village_base, "Your Base")
        draw_base(enemy_frame, enemy_base, "Enemy Base")
        messagebox.showinfo("Load", "Game loaded!")

# --------------------------
# INIT BASES
# --------------------------
def place_building(base, r, c, name):
    base[r][c] = {"name": name, "hp": BUILDINGS[name]["hp"]}

def init_village():
    place_building(village_base, 3, 3, "Town Hall")
    place_building(village_base, 0, 0, "Gold Mine")
    place_building(village_base, 0, 1, "Elixir Collector")
    place_building(village_base, 1, 1, "Cannon")
    place_building(village_base, 2, 2, "Archer Tower")

def init_enemy():
    placed = 0
    while placed < 8:
        r, c = random.randint(0, ROWS-1), random.randint(0, COLS-1)
        if enemy_base[r][c] is None:
            place_building(enemy_base, r, c, random.choice(list(BUILDINGS.keys())))
            placed += 1

# --------------------------
# DRAW BASE
# --------------------------
def draw_base(frame, base, title):
    for widget in frame.winfo_children():
        widget.destroy()
    tk.Label(frame, text=title, font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=COLS)
    for r in range(ROWS):
        for c in range(COLS):
            b = base[r][c]
            text = b["name"] if b else "Empty"
            color = BUILDINGS[b["name"]]["color"] if b else "white"
            tk.Label(frame, text=text, bg=color, relief="ridge", width=12, height=3).grid(row=r+1, column=c, padx=2, pady=2)

# --------------------------
# TRAIN TROOPS
# --------------------------
def train_troop(t):
    global gold, elixir
    cost = {"Barbarian":50,"Archer":70,"Giant":120,"Dragon":200}
    
    try:
        num = int(simpledialog.askstring("Train Troops", f"How many {t}s to train?"))
        if num <= 0:
            messagebox.showwarning("Train", "Number must be at least 1!")
            return
    except:
        return
    
    total_cost = cost[t] * num
    if gold >= total_cost and elixir >= total_cost:
        gold -= total_cost
        elixir -= total_cost
        troops[t] += num
        update_status()
        messagebox.showinfo("Training", f"Trained {num} {t}(s)!")
    else:
        messagebox.showwarning("Training", "Not enough resources!")

# --------------------------
# PLAYER ATTACK
# --------------------------
def player_attack():
    global gold, elixir, stars
    if sum(troops.values()) == 0:
        messagebox.showwarning("Attack", "No troops!")
        return

    destroyed = 0
    total_buildings = sum(1 for r in enemy_base for b in r if b)
    attack_power = sum(TROOPS_DATA[t]["damage"] * troops[t] for t in troops)

    gold_loot = 0
    elixir_loot = 0

    for r in range(ROWS):
        for c in range(COLS):
            if enemy_base[r][c] and attack_power > 0:
                if random.random() < 0.6:
                    building = enemy_base[r][c]["name"]
                    enemy_base[r][c] = None
                    destroyed += 1
                    attack_power -= 1
                    # Loot scaling
                    if building == "Gold Mine":
                        gold_loot += 100
                    elif building == "Elixir Collector":
                        elixir_loot += 100
                    elif building == "Town Hall":
                        gold_loot += 200
                        elixir_loot += 200
                    else:
                        gold_loot += 50
                        elixir_loot += 50

    percent = destroyed / max(total_buildings, 1)
    if percent == 1:
        stars = 3
    elif percent >= 0.5:
        stars = 2
    elif percent > 0:
        stars = 1
    else:
        stars = 0

    gold += gold_loot
    elixir += elixir_loot

    for t in troops:
        troops[t] = 0

    draw_base(enemy_frame, enemy_base, "Enemy Base")
    update_status()
    messagebox.showinfo("Attack Result",
                        f"Destroyed {destroyed} buildings.\n"
                        f"Stars: {stars}\n"
                        f"Loot: {gold_loot} Gold, {elixir_loot} Elixir.")

# --------------------------
# ENEMY ATTACK
# --------------------------
def enemy_attack():
    global gold, elixir
    destroyed = 0
    attack_power = random.randint(100, 300)  # Random enemy power
    gold_loot = 0
    elixir_loot = 0

    for r in range(ROWS):
        for c in range(COLS):
            if village_base[r][c] and attack_power > 0:
                if random.random() < 0.5:
                    building = village_base[r][c]["name"]
                    village_base[r][c] = None
                    destroyed += 1
                    attack_power -= 1
                    # Enemy loot scaling (player loses resources)
                    if building == "Gold Mine":
                        gold_loot += 50
                    elif building == "Elixir Collector":
                        elixir_loot += 50
                    elif building == "Town Hall":
                        gold_loot += 100
                        elixir_loot += 100
                    else:
                        gold_loot += 25
                        elixir_loot += 25

    gold = max(0, gold - gold_loot)
    elixir = max(0, elixir - elixir_loot)
    draw_base(player_frame, village_base, "Your Base")
    update_status()
    # Next attack in 20 seconds
    root.after(20000, enemy_attack)

# --------------------------
# UPDATE STATUS
# --------------------------
def update_status():
    troop_status = ", ".join([f"{t}: {troops[t]}" for t in troops])
    status_label.config(text=f"Gold: {gold} | Elixir: {elixir} | Troops: {troop_status} | Stars: {stars}")

# --------------------------
# GUI SETUP
# --------------------------
root = tk.Tk()
root.title("Mini COC Game")

status_label = tk.Label(root, text="", font=("Arial", 14))
status_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()
player_frame = tk.Frame(frame)
player_frame.grid(row=0, column=0, padx=10)
enemy_frame = tk.Frame(frame)
enemy_frame.grid(row=0, column=1, padx=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Train Barbarian", command=lambda: train_troop("Barbarian")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Train Archer", command=lambda: train_troop("Archer")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Train Giant", command=lambda: train_troop("Giant")).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Train Dragon", command=lambda: train_troop("Dragon")).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Attack Enemy Base", command=player_attack).grid(row=0, column=4, padx=5)
tk.Button(btn_frame, text="Save Game", command=save_game).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Load Game", command=load_game).grid(row=1, column=1, padx=5, pady=5)

# --------------------------
# INIT
# --------------------------
init_village()
init_enemy()
draw_base(player_frame, village_base, "Your Base")
draw_base(enemy_frame, enemy_base, "Enemy Base")
update_status()

# Start enemy automatic attacks every 20 seconds
root.after(20000, enemy_attack)

root.mainloop()
