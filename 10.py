import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        value = float(entry_value.get())
        percent = float(entry_percent.get())
        operation = operation_var.get()

        if operation == "Increase":
            result = value * (1 + percent / 100)
        else:
            result = value * (1 - percent / 100)

        result_label.config(text=f"Result: {result:.2f}")

        # Calculate Grundwert, Prozentwert, and Prozentsatz
        if operation == "Increase":
            grundwert = result / (1 + percent / 100)
            prozentwert = result - value
            prozentsatz = percent
        else:
            grundwert = result / (1 - percent / 100)
            prozentwert = value - result
            prozentsatz = percent

        grundwert_label.config(text=f"Grundwert: {grundwert:.2f}")
        prozentwert_label.config(text=f"Prozentwert: {prozentwert:.2f}")
        prozentsatz_label.config(text=f"Prozentsatz: {prozentsatz:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Percentage Calculator")

# Entry fields and labels
label_value = tk.Label(root, text="Value:")
label_value.grid(row=0, column=0)
entry_value = tk.Entry(root)
entry_value.grid(row=0, column=1)

label_percent = tk.Label(root, text="Percent:")
label_percent.grid(row=1, column=0)
entry_percent = tk.Entry(root)
entry_percent.grid(row=1, column=1)

# Radio buttons for operation selection
operation_var = tk.StringVar()
operation_var.set("Increase")
radio_increase = tk.Radiobutton(root, text="Increase", variable=operation_var, value="Increase")
radio_increase.grid(row=2, column=0)
radio_decrease = tk.Radiobutton(root, text="Decrease", variable=operation_var, value="Decrease")
radio_decrease.grid(row=2, column=1)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

# Result labels
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

grundwert_label = tk.Label(root, text="Grundwert: ")
grundwert_label.grid(row=5, column=0, columnspan=2)

prozentwert_label = tk.Label(root, text="Prozentwert: ")
prozentwert_label.grid(row=6, column=0, columnspan=2)

prozentsatz_label = tk.Label(root, text="Prozentsatz: ")
prozentsatz_label.grid(row=7, column=0, columnspan=2)

# Run the application
root.mainloop()
