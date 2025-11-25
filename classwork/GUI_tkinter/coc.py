import tkinter as tk
from tkinter import messagebox
import random

# Game Variables
gold = 500
elixir = 500
troops = {"Barbarian": 0, "Archer": 0, "Dragon": 0}
stars = 0

ROWS, COLS = 5, 5
player_base = [["" for _ in range(COLS)] for _ in range(ROWS)]
enemy_base = [["" for _ in range(COLS)] for _ in range(ROWS)]

BUILDINGS = ["Town Hall", "Gold Mine", "Elixir Collector", "Cannon", "Archer Tower"]
TROOPS = {"Barbarian": 1, "Archer": 2, "Dragon": 3}  # attack strength

def init_bases():
    # Player Base
    player_base[2][2] = "Town Hall"
    player_base[0][0] = "Gold Mine"
    player_base[0][1] = "Elixir Collector"
    player_base[1][1] = "Cannon"
    player_base[1][2] = "Archer Tower"

    # Enemy Base
    for _ in range(7):
        while True:
            r, c = random.randint(0, ROWS-1), random.randint(0, COLS-1)
            if enemy_base[r][c] == "":
                enemy_base[r][c] = random.choice(BUILDINGS)
                break

def draw_base(frame, base, title):
    for widget in frame.winfo_children():
        widget.destroy()
    tk.Label(frame, text=title, font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=COLS)
    for r in range(ROWS):
        for c in range(COLS):
            b = base[r][c]
            text = b if b else "Empty"
            color = "white"
            if b == "Town Hall": color = "red"
            elif b == "Gold Mine": color = "gold"
            elif b == "Elixir Collector": color = "purple"
            elif b in ["Cannon", "Archer Tower"]: color = "gray"
            tk.Label(frame, text=text, bg=color, relief="ridge", width=12, height=3).grid(row=r+1, column=c, padx=2, pady=2)

def train_troop(troop_type):
    global gold, elixir, troops
    cost = {"Barbarian": 50, "Archer": 70, "Dragon": 200}
    if gold >= cost[troop_type] and elixir >= cost[troop_type]:
        gold -= cost[troop_type]
        elixir -= cost[troop_type]
        troops[troop_type] += 1
        update_status()
        messagebox.showinfo("Training", f"Trained 1 {troop_type}!")
    else:
        messagebox.showwarning("Training", "Not enough resources!")

def attack():
    global gold, elixir, stars, troops
    if sum(troops.values()) == 0:
        messagebox.showwarning("Attack", "No troops available!")
        return

    destroyed = 0
    total_buildings = sum(1 for r in enemy_base for b in r if b != "")
    
    # Calculate attack power
    attack_power = sum(TROOPS[t]*troops[t] for t in troops)
    
    for r in range(ROWS):
        for c in range(COLS):
            if enemy_base[r][c] != "" and attack_power > 0:
                if random.random() < 0.5:  # chance to destroy
                    enemy_base[r][c] = ""
                    destroyed += 1
                    attack_power -= 1
    
    # Calculate stars
    percent = destroyed / max(total_buildings, 1)
    if percent == 1:
        stars = 3
    elif percent >= 0.5:
        stars = 2
    elif percent > 0:
        stars = 1
    else:
        stars = 0

    # Loot resources
    gold_loot = destroyed * 50
    elixir_loot = destroyed * 50
    gold += gold_loot
    elixir += elixir_loot
    # All troops used in attack
    for t in troops:
        troops[t] = 0
    
    draw_base(enemy_frame, enemy_base, "Enemy Base")
    update_status()
    messagebox.showinfo("Attack Result", f"Destroyed {destroyed} buildings.\nStars: {stars}\nLoot: {gold_loot} Gold, {elixir_loot} Elixir.")

def update_status():
    troop_status = ", ".join([f"{t}: {troops[t]}" for t in troops])
    status_label.config(text=f"Gold: {gold} | Elixir: {elixir} | Troops: {troop_status} | Stars: {stars}")

# GUI setup
root = tk.Tk()
root.title("Mini COC Game - Advanced Version")

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
tk.Button(btn_frame, text="Train Dragon", command=lambda: train_troop("Dragon")).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Attack Enemy Base", command=attack).grid(row=0, column=3, padx=5)

init_bases()
draw_base(player_frame, player_base, "Your Base")
draw_base(enemy_frame, enemy_base, "Enemy Base")
update_status()

root.mainloop()

