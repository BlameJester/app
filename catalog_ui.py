import tkinter as tk
from tkinter import messagebox, ttk

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_all_products(self):
        return self.products
    
class ProductUI:
    def __init__(self, master):
        self.master = master
        self.catalog = ProductCatalog()
        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        title_label = tk.Label(self.master, text="Каталог товаров", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Поля для ввода данных о продукте
        entry_frame = tk.Frame(self.master)
        entry_frame.pack(pady=10)

        self.name_entry = tk.Entry(entry_frame, width=20)
        self.name_entry.grid(row=0, column=1)
        tk.Label(entry_frame, text="Название:").grid(row=0, column=0)

        self.price_entry = tk.Entry(entry_frame, width=20)
        self.price_entry.grid(row=1, column=1)
        tk.Label(entry_frame, text="Цена:").grid(row=1, column=0)

        self.desc_entry = tk.Entry(entry_frame, width=20)
        self.desc_entry.grid(row=2, column=1)
        tk.Label(entry_frame, text="Описание:").grid(row=2, column=0)

        # Кнопки
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10)
        
        add_button = tk.Button(button_frame, text="Добавить продукт", command=self.add_product)
        add_button.pack(side=tk.LEFT, padx=5)
        
    def add_product(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        description = self.desc_entry.get()

        if name and price and description:
            try:
                price = float(price)
                product = Product(name, price, description)
                self.catalog.add_product(product)

                # Очищаем поля ввода после добавления
                self.name_entry.delete(0, tk.END)
                self.price_entry.delete(0, tk.END)
                self.desc_entry.delete(0, tk.END)

                messagebox.showinfo("Успех", "Продукт добавлен!")
            except ValueError:
                messagebox.showwarning("Ошибка", "Цена должна быть числом!")
        else:
            messagebox.showwarning("Ошибка", "Заполните все поля!")