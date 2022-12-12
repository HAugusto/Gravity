import numpy
import time

g = 9.8

def TimeCalculus(height):
    return numpy.sqrt((h*2)/g)

def PotentialEnergy(mass, height):
    return m * g * h

print("Massa (m): ")
m = int(input())

print("Altura (h): ")
h = int(input())

tempo = TimeCalculus(h)
print(tempo)