# Space Boxer
# Matt Licata (mattRicotta)

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3
rel_gravity = 0

# Write an if statement below:
if planet == 1:
    rel_gravity = 0.91
elif planet == 2:
    rel_gravity = 0.38
elif planet == 3:
    rel_gravity = 2.34
elif planet == 4:
    rel_gravity = 1.06
elif planet == 5:
    rel_gravity = 0.92
elif planet == 6:
    rel_gravity = 1.19

weight = weight * rel_gravity
print("Your weight: ", weight)