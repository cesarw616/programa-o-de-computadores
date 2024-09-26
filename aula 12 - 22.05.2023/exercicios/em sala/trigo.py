def hipotenusa(catO,catA):
    return (catO**2+catA**2)**0.5

def seno(catO,catA):
    return catO/hipotenusa(catO,catA)

def cosseno(catO,catA):
    return catA/hipotenusa(catO,catA)

def tangente(catO,catA):
    return seno(catO,catA)/cosseno(catO,catA)