#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
from CoolProp.CoolProp import PropsSI
import matplotlib.pyplot as plt

if len(sys.argv) != 6:
    print "usage: <fluid> <min temperature [°C]> <max temperature [°C]>  <pressure [bar]>, <no. of points in range>"
    sys.exit()

fluid = sys.argv[1]
minTemp = float(sys.argv[2])+273.15
maxTemp = float(sys.argv[3])+273.15
pressure = float(sys.argv[4])*10**5
points = sys.argv[5]

def thermoProps(fluid, minTemp, maxTemp, pressure, points):
    tempRange = np.linspace(minTemp, maxTemp, points)
    density = np.zeros(len(tempRange))
    viscosity = np.zeros(len(tempRange))
    specHeat = np.zeros(len(tempRange))
    kappa = np.zeros(len(tempRange))

    for i, value in enumerate(tempRange):
        density[i] = PropsSI('D','T',value,'P',pressure,str(fluid)) #kg/m3
        viscosity[i] = PropsSI('V','T',value,'P',pressure,str(fluid)) #Pa*s
        specHeat[i] = PropsSI('C','T',value,'P',pressure,str(fluid)) #J/(kg*K)
        kappa[i] = PropsSI('L','T',value,'P',pressure,str(fluid)) #W/(m*K)

    molarMass = PropsSI('M','T',value,'P',pressure,str(fluid))
    
    return tempRange,density, viscosity, specHeat, kappa, molarMass

def curveFit(tempRange, thermoProp, degree):
    polyCoeff = np.polyfit(tempRange, thermoProp, degree)

    return polyCoeff

tempRange, density, viscosity, specHeat, kappa, molarMass = thermoProps(fluid, minTemp, maxTemp, pressure, points)
#print density, viscosity, specHeat


densFit = np.poly1d(np.polyfit(tempRange, density,6))
viscFit = np.poly1d(np.polyfit(tempRange, viscosity,6))
specHeatFit = np.poly1d(np.polyfit(tempRange, specHeat,6))
kappaFit = np.poly1d(np.polyfit(tempRange, kappa,6))

print "density: "+str(np.polyfit(tempRange, density,6)[::-1])
print "viscosity: "+str(np.polyfit(tempRange, viscosity,6)[::-1])
print "specHeat: "+str(np.polyfit(tempRange, specHeat,6)[::-1])
print "kappa: "+str(np.polyfit(tempRange, kappa,6)[::-1])
print "molarmassi = "+str(molarMass*1000)+" g/mol"

print np.poly1d(np.polyfit(tempRange, density,6))
print np.poly1d(np.polyfit(tempRange, density,6))(tempRange)

#plt.figure()
plt.plot(tempRange, density, label='1')
plt.plot(tempRange, densFit(tempRange), label='fit')
plt.legend() 
plt.show()
plt.plot(tempRange, viscosity, label='2')
plt.plot(tempRange, viscFit(tempRange), label='fit')
plt.legend() 
plt.show()
plt.plot(tempRange, specHeat, label='3')
plt.plot(tempRange, specHeatFit(tempRange), label='fit')
plt.legend()
plt.show()
plt.plot(tempRange, kappa, label='3')
plt.plot(tempRange, kappaFit(tempRange), label='fit')
plt.legend()
plt.show()









