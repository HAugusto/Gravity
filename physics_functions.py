gravity = 9.8

# Cálculo de Tempo
def TimeCalculus(height):
    return numpy.sqrt((height*2)/gravity)

# Cálculo de Energia Potencial Gravitacional
def PotentialEnergyG(mass, height):
    return mass * gravity * height

# Cálculo Energia Mecânica (Queda Livre)
# Energia Cinética = Energia Potencial
# Em = Ep + Ec
def MechanicalEnergy(Epg):
    return 2 * Epg