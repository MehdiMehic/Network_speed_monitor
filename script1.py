
r = lambda: random.randint(15, 20)

name = input("Name: ")

hp, dmg = r(), r()

print(f"Hero: {name} | HP: {hp} | DMG: {dmg}")


if input("Choose Road (1 or 2): ") == "1":

ehp, edmg = r(), r()

print(f"Enemy appeared! HP: {ehp} | DMG: {edmg}")


if input("1: Fight, 2: Flee -> ") == "1":

hp, ehp = hp - edmg, ehp - dmg

print(f"Dealt {dmg} dmg | Took {edmg} dmg")

print(

"You win!"

if hp > 0 >= ehp

else ("Game Over!" if hp <= 0 else "Both survived!")

)

else:

print("You fled!")

else:

print("Road 2 is safe.") 