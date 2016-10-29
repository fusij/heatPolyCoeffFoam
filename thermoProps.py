#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
from CoolProp.CoolProp import PropsSI

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

    for i, value in enumerate(tempRange):
        density[i] = PropsSI('D','T',value,'P',pressure,str(fluid)) #kg/m3
        viscosity[i] = PropsSI('V','T',value,'P',pressure,str(fluid)) #Pa*s
        specHeat[i] = PropsSI('D','T',value,'P',pressure,str(fluid)) #J/(kg*K)
        
    print density
    return density, viscosity, specHeat

#thermoProps(fluid, minTemp, maxTemp, pressure, points)



