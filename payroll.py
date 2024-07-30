import tkinter as tk
from tkinter import ttk, messagebox
import csv

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class PayrollSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll System")
        self.root.geometry("800x600")

        # Create tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.frame1 = tk.Frame(self.notebook)
        self.frame2 = tk.Frame(self.notebook)
        self.frame3 = tk.Frame(self.notebook)
        self.frame4 = tk.Frame(self.notebook)

        self.notebook.add(self.frame1, text="Add Product")
        self.notebook.add(self.frame2, text="View Products")
        self.notebook.add(self.frame3, text="Generate Invoice")
        self.notebook.add(self.frame4, text="Save/Load Data")

        # Add product tab
        self.name_label = tk.Label(self.frame1, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.frame1)
        self.name_entry.pack()

        self.price_label = tk.Label(self.frame1, text="Price:")
        self.price_label.pack()
        self.price_entry = tk.Entry(self.frame1)
        self.price_entry.pack()

        self.quantity_label = tk.Label(self.frame1, text="Quantity:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(self.frame1)
        self.quantity_entry.pack()

        self.add_button = tk.Button(self.frame1, text="Add Product", command=self.add_product)
        self.add_button.pack()

        # View products tab
        self.view_text = tk.Text(self.frame2)
        self.view_text.pack()
        self.view_button = tk.Button(self.frame2, text="View Products", command=self.view_products)
        self.view_button.pack()

        # Generate invoice tab
        self.invoice_text = tk.Text(self.frame3)
        self.invoice_text.pack()
        self.generate_button = tk.Button(self.frame3, text="Generate Invoice", command=self.generate_invoice)
        self.generate_button.pack()

        # Save/Load data tab
        self.save_button = tk.Button(self.frame4, text="Save Data", command=self.save_data)
        self.save_button.pack()
        self.load_button = tk.Button(self.frame4, text="Load Data", command=self.load_data)
        self.load_button.pack()

        self.products = []

    def add_product(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        product = Product(name, price, quantity)
        self.products.append(product)
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Product added successfully")

    def view_products(self):
        self.view_text.delete(1.0, tk.END)
        for product in self.products:
            self.view_text.insert(tk.END, f"Name: {product.name}\nPrice: {product.price}\nQuantity: {product.quantity}\n\n")

    def generate_invoice(self):
        self.invoice_text.delete(1.0, tk.END)
        total_price = 0
        for product in self.products:
            self.invoice_text.insert(tk.END, f"Name: {product.name}\nPrice: {product.price}\nQuantity: {product.quantity}\nSubtotal: {int(product.price) * int(product.quantity)}\n\n")
            total_price += int(product.price) * int(product.quantity)
        self.invoice_text.insert(tk.END, f"Total Price: {total_price}\n")

    def save_data(self):
        with open('products.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Price", "Quantity"])
            for product in self.products:
                writer.writerow([product.name, product.price, product.quantity])
        messagebox.showinfo("Success", "Data saved successfully")

    def load_data(self):
        self.products = []
        try:
            with open('products.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    product = Product(row[0], row[1], row[2])
                    self.products.append(product)
            messagebox.showinfo("Success", "Data loaded successfully")
        except FileNotFoundError:
            messagebox.showerror("Error", "No data file found")

root = tk.Tk()
payroll_system = PayrollSystem(root)
root.mainloop()
