import random
import tkinter as tk

r = lambda: random.randint(15, 20)

hp = ehp = dmg = edmg = 0

def start_game():
    global hp, dmg
    hp, dmg = r(), r()
    text_label.config(text=f"Your stats:\nhp = {hp} / dmg = {dmg} \n\nChoose a road:")
    btn1.config(text="Road 1", command=choose_road1, state="normal")
    btn2.config(text="Road 2", command=choose_road2, state="normal")
    btn3.config(text="Quit", command=window.destroy, state="normal")
    btn1.pack(pady=5)
    btn2.pack(pady=5)
    btn3.pack(pady=5)

def choose_road1():
    global ehp, edmg
    ehp, edmg = r(), r()
    text_label.config(text=f"You've stumbled across a enemy:\nenemy stats:\nhp = {ehp} / dmg = {edmg}")
    btn1.config(text="Attack", command=attack)
    btn2.config(text="Flee", command=flee)
    btn3.pack_forget()

def choose_road2():
    text_label.config(text="You've stumbled across the safe path")
    btn1.config(text="Play Again", command=start_game)
    btn2.config(text="Quit", command=window.destroy)
    btn3.pack_forget()

def attack():
    global hp, ehp
    hp -= edmg
    ehp -= dmg

    if hp > ehp:
        text_label.config(text="You've won")
    else:
        text_label.config(text="You've lost")
    btn1.config(text="Play Again", command=start_game)
    btn2.config(text="Quit", command=window.destroy)

def flee():
    text_label.config(text="You've sucesfully fled")
    btn1.config(text="Play Again", command=start_game)
    btn2.config(text="Quit", command=window.destroy)

window = tk.Tk()
window.title("Text RPG Game")
window.geometry("350x250")

# Text Display
text_label = tk.Label(window, text="", font=("Arial", 11), wraplength=300)
text_label.pack(pady=20)

# Choice Buttons
btn1 = tk.Button(window, text="", width=15)
btn1.pack(pady=5)

btn2 = tk.Button(window, text="", width=15)
btn2.pack(pady=5)

btn3 = tk.Button(window, text="", width=15)
btn3.pack(pady=5)

# Start the game initially
start_game()

# Run GUI
window.mainloop()