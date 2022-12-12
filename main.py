import numpy
import physics_functions as fisica



print("Massa (m): ")
m = int(input())

print("Altura (h): ")
h = int(input())

Ep = numpy.round(fisica.PotentialEnergyG(m, h),2)
Em = numpy.round(fisica.MechanicalEnergy(Ep),2)
print("Energia Potencial: " + str(Ep) + "N")
print("Energia Cinética: " + str(Ep) + "N")
print("Energia Mecânica: " + str(Em) + "N")