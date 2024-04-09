import numpy as np
from agent import Agent
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from general_support import random_state, is_inside_box

# Create a figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Initialize the valid region as a rectangle
x_min = -4
x_max = 4
y_min = -4
y_max = 4
lower_left_corner = (x_min, y_min)
width = x_max - x_min
height = y_max - y_min

# Create the rectangle object
# 'linewidth' is the border line width, 'edgecolor' is the border color, and 'facecolor' is the fill color
# 'facecolor' set to 'none' means the rectangle will not be filled
area_rectangle = plt.Rectangle(lower_left_corner, width, height, linewidth=1, edgecolor='r', facecolor='none')

# Add the rectangle to the plot
ax.add_patch(area_rectangle)

# Initialize the main agent
agent = Agent(init_state=random_state(), init_size=0.2, agent_type_in='Agent')

# Create animation objects for the agent and predators
agent_circle = agent.get_animation_object()
ax.add_patch(agent_circle)

dt = 0.1
def animate(i):
    # Update the agent's position
    agent.update(dt)
    f_agent_in_bounds = is_inside_box(agent.get_position(), area_rectangle)
    if f_agent_in_bounds:
        agent_circle.center = agent.get_position()
    else:
        agent_circle.set_visible(False)

    return [agent_circle]

ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

plt.show()