"""
Ordenar una llista de strings per la segona lletra de cada string, utilitzant el mètode sort/sorted i la funció lambda:
    Exemple:
        mesos = ['gener', 'març', 'abril', 'juny', 'agost']
    SOLUCIO:
        mesos = ['març', 'abril', 'gener', 'agost', 'juny']
"""
mesos = ['gener', 'març', 'abril', 'juny', 'agost']
ordenar = sorted(mesos, key=lambda segundaletra: segundaletra[1])
print(ordenar)
