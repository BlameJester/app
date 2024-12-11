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

        delete_button = tk.Button(button_frame,text="Удалить товар", command=self.delete_product)
        delete_button.pack(side=tk.LEFT, padx=5)
        
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

    def delete_product(self):
        try:
            selected_item = self.product_list.selection()[0]  # Получаем выбранный элемент
            self.product_list.delete(selected_item)  # Удаляем из списка
            index = self.product_list.index(selected_item)  # Получаем индекс выбранного элемента
            del self.catalog.products[index]  # Удаляем из каталога
        except IndexError:
            messagebox.showwarning("Внимание", "Пожалуйста, выберите продукт для удаления.")
            
class MainApp:
    def __init__(self):
        self.window = tk. Tk()
        self.window.title("Каталог товаров")
        self.ui = ProductUI(self.window)

        # Создаем элементы для отображения списка продуктов
        self.create_product_list()

    def create_product_list(self):
        # Список продуктов
        self.product_list = ttk.Treeview(self.window, columns=('Name', 'Price', 'Description'), show='headings')
        self.product_list.heading('Name', text='Название')
        self.product_list.heading('Price', text='Цена')
        self.product_list.heading('Description', text='Описание')
        self.product_list.pack(pady=10)

        # Кнопка для обновления списка
        view_button = tk.Button(self.window, text="Просмотреть продукты", command=self.view_product)
        view_button.pack(pady=10)

    def view_product(self):
        # Очищаем текущий список
        for row  in self.product_list.get_children():
            self.product_list.delete(row)

        # Получаем все продукты и добавляем их в таблицу
        for product in self.ui.catalog.get_all_products():
            self.product_list.insert("", "end", values=(product.name, product.price, product.description))

__name__ == "__main__"
main_app = MainApp()
main_app.window.mainloop()
            