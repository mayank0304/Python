# Program that takes Mass and Velocity of an object as input and Calculate Momentum and Kinetic energy Of that Object.

m = float(input("Enter the mass of the object:"))
v = float(input("Enter the velocity of the object:"))
p = m*v
kineticEnergy =  (1/2)*m*(v**2)
print("The mass of object in kg: ",m)
print("The velocity of object in m/s: ",v)
print("The momentum of object in kgm/s: ",p)
print("The kinetic energy of object in joule: ", kineticEnergy)