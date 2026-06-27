# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:39:21 2026

@author: mjorg
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros físicos de la trampa
k = 0.2              # rigidez de la fuerza de gradiente (Hooke)
F_rad_value = 0.5    # magnitud de la fuerza de radiación cuando está activa
x_umbral = 0.5       # región central (|x|<=x_umbral) donde activa F_rad
gamma = 0.05         # coeficiente de amortiguamiento (drag)
dt = 0.05            # paso de tiempo
# Estado inicial de la partícula
x = 4.0              # posición inicial (alejada del centro x=0)
v = 0.0              # velocidad inicial

# Crear figura y eje
fig, ax = plt.subplots(figsize=(6,3))
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 1)
ax.set_xlabel('Posición 1D')
ax.set_yticks([])  # ocultar eje Y para claridad

# Función de actualización para cada frame de la animación
def update(frame):
    global x, v
    # Calcular fuerzas
    F_grad = -k * x                    # fuerza de gradiente (hacia x=0)
    F_rad = F_rad_value if abs(x) <= x_umbral else 0  # fuerza de radiación activa en zona central
    F_drag = -gamma * v               # amortiguamiento viscous
    
    # Integrar movimiento (m=1)
    a = F_grad + F_rad + F_drag
    v += a * dt
    x += v * dt
    
    # Dibujar estado actual
    ax.clear()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-1, 1)
    ax.axhline(0, color='gray', lw=1, linestyle='--')  # línea de referencia en y=0
    
    # Partícula (punto negro) en la posición x
    ax.plot(x, 0, 'ko', markersize=8)
    
    # Flecha de fuerza de gradiente (azul): siempre presente, apuntando hacia 0
    # Su longitud dibujada es proporcional a la distancia al foco (a modo ilustrativo).
    ax.arrow(x, 0, -x, 0, head_width=0.05, head_length=0.1, fc='blue', ec='blue')
    
    # Flecha de fuerza de radiación (roja): solo si está activa (cerca del foco)
    if abs(x) <= x_umbral:
        # Dibuja una flecha constante hacia la derecha desde la partícula
        ax.arrow(x, 0, 0.5, 0, head_width=0.05, head_length=0.1, fc='red', ec='red')
    
    # Título explicativo
    ax.set_title(f"x = {x:.2f}", fontsize=10)

# Crear animación
ani = FuncAnimation(fig, update, frames=200, interval=50, repeat=False)
plt.show()