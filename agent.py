import numpy as np
import matplotlib.pyplot as plt

class Agent:
    def __init__(self, init_state=np.array([0, 0, 0, 0]), init_size=0.2, agent_type_in='Predator'):
        self.state_vector = init_state
        self.size = init_size
        self.type = agent_type_in

    def update(self, dt):
        self.state_vector[0] += self.state_vector[2] * dt
        self.state_vector[1] += self.state_vector[3] * dt

    def get_position(self):
        return self.state_vector[0:2]
    
    def get_velocity(self):
        return self.state_vector[2:4]
    
    def get_size(self):
        return self.size
    
    def get_animation_object(self):
        if self.type == 'Predator':
            clr = 'red'
        elif self.type == 'Agent':
            clr = 'blue'
        else:
            clr = 'green'
            
        return plt.Circle(self.get_position(), self.get_size(), color=clr)
