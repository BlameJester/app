import tkinter as tk
from tkinter import ttk, messagebox

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
        