import math

# Physics constants
g = -9.81  # gravity acceleration (m/s²)

# User inputs
m = float(input("Enter your mass value (kg): "))
v0 = float(input("Enter your initial velocity (m/s): "))
x0 = float(input("Enter your initial x position (m): "))
y0 = float(input("Enter your initial y position (m): "))
angle = float(input("Enter your launch angle (degrees): "))

# Calculations
F = g * m  # Force
a = math.radians(angle)  # Convert angle to radians
v0x = v0 * math.cos(a)  # Initial horizontal velocity
v0y = v0 * math.sin(a)  # Initial vertical velocity

# Simulation variables
t = 0
x = x0
h = y0
iteration = 0
dt = 0.0001  # Time step

# Simulation loop - continues while object is above ground
while h >= 0:
    # Calculate velocities
    vx = v0x  # Horizontal velocity (constant)
    vy = v0y + g * t  # Vertical velocity (affected by gravity)
    v = math.sqrt(vx**2 + vy**2)  # Total velocity magnitude
    
    # Calculate positions
    x = x0 + v0x * t  # Horizontal position
    h = y0 + v0y * t + g * (t**2) / 2  # Vertical position (kinematic equation)
    
    # Print every 100 iterations
    if iteration % 100 == 0:
        print(f"Time: {round(t, 4)}s | Position: ({round(x, 4)}, {round(h, 4)})m | Velocity: ({round(vx, 4)}, {round(vy, 4)})m/s")
    
    t += dt
    iteration += 1

# Adjust final height if below ground
if h < 0:
    h = 0

# Final output
print("\n" + "="*60)
print("FINAL RESULTS")
print("="*60)
print(f"Time of flight: {round(t, 4)} seconds")
print(f"Final position: X = {round(x, 4)}m, Y = {round(h, 4)}m")
print(f"Final velocity magnitude: {round(v, 4)} m/s")
print(f"Final velocity components: Vx = {round(vx, 4)} m/s, Vy = {round(vy, 4)} m/s")
print(f"Force applied: {round(F, 4)} N")
print("="*60)
