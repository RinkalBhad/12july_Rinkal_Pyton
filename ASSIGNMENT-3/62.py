# Write a Python program to calculate surface volume and area of a cylinder


pi=22/7
height=float(input("height of cylindder:"))
radian=float(input("Radius of cylinder:"))
volume=pi*radian*radian*height
surface= ((2*pi*radian) * height) + ((pi*radian**2)*2)
print("vloume is:",volume)
print("surace area is:",surface)