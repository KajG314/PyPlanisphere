import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation

import numpy as np

from astropy.coordinates import SkyCoord
from astropy import units as u

class Planisphere(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid()


        


        

        