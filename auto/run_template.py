import matplotlib.pyplot as plt
from pid_template import make_car
from pid_template import update
from pid_template import calculate_desired_acceleration
from pid_template import acceleration_to_throttle_percentage

K_P = 0.85
K_I = 0.05
K_D = 0.2
 
STEPS = 550 # --> 55 Simulated Seconds with dt = 0.1
 
car = make_car(desired_v=20.0, dt=0.1)

#WRITE CODE HERE

vs, errs, ts = [], [], [] #making 3 lists to store plot history, as simulation only stores current plot

for _ in range(STEPS): #look counter not needed
    a_des, error = calculate_desired_acceleration(car, K_P, K_I, K_D)   #Calculating tuple --> desired acceleraction, error
    throttle = acceleration_to_throttle_percentage(a_des)               #Converts a_des (acceleration desired) to throttle percentage
    update(car, throttle)                                               #Applying throttle to car model
    vs.append(car["v"])                                                 #Appending Velocity to plot history
    errs.append(error)                                                  #Appending error to plot history
    ts.append(car["t"])                                                 #Appending time to car hisotry




#Making Plot

"""
plt.plot(ts, vs)
plt.show()
"""

#Other Plot:


fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))
ax1.plot(ts, vs)
ax1.axhline(car["desired_v"], linestyle="--", color="gray")
ax1.set_ylabel("velocity (m/s)")
ax1.set_title("Velocity over time")
ax2.plot(ts, errs)
ax2.axhline(0, linestyle="--", color="gray")
ax2.set_ylabel("error (m/s)")
ax2.set_xlabel("time (s)")
ax2.set_title("Error over time")
fig.tight_layout()
plt.show()