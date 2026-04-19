# Wenn der Code im Notebook der Uebung nicht ordentlich kompiliert, nutzt dieses Script

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Beispielwerte für die Partikelpositionen
num_particles = 50
num_steps = 100

# Zufällige Startpositionen
x = np.random.rand(num_particles)
y = np.random.rand(num_particles)

# Zufällige Bewegungen für die Partikel
dx = (np.random.rand(num_particles) - 0.5) * 0.05
dy = (np.random.rand(num_particles) - 0.5) * 0.05

fig, ax = plt.subplots()

#Dynamik der Partikel
def evolve(i):
    pass

def interact(i,j):
    pass


# Grenzen des Plots festlegen
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Die Update-Funktion für jede Animation-Iteration
def update(frame):
    global x, y
    ax.clear()  # Clear the axes for each frame
    ax.set_xlim(0, 1)  # Grenzen neu setzen
    ax.set_ylim(0, 1)
    
    #State Transition Step
    for i in range(len(x)):
        for j in range(len(x)):
            interact(i,j)
    for i in range(len(x)):
        evolve(i)
    
    ax.scatter(x, y)  # Zeichnet die Partikel neu
    return ax,

# Animation erstellen
ani = animation.FuncAnimation(fig, update, frames=range(num_steps), interval=50, blit=True)

plt.show() 