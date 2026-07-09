import matplotlib.pyplot as  plt
import numpy as np
fig = plt.subplots(subplot_kw={"projection":"3d"})[0]
ax=fig.gca()

# Generate parametric data

t= np.linspace(0,20,1000)
x= mp.sin(t)*np.exp(t/10)
y= mp.cos(t)*np.exp(t/10)
z=t
ax.plot(x,y,z,label="Parametric Spiral", color="purple")
ax.set_title("3D Space Trajectory")
plt.show()