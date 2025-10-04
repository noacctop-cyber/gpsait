import tkinter as tk
from tkinter import messagebox

def add_time(start_time, add_hours, add_minutes):
    try:
        hours, minutes = map(int, start_time.split(':'))
        if not (0 <= hours < 24 and 0 <= minutes < 60):
            raise ValueError
    except:
        messagebox.showerror("Ошибка", "Введите время в формате HH:MM (например, 12:00)")
        return None

    total_minutes = minutes + add_minutes
    extra_hours = total_minutes // 60
    total_minutes = total_minutes % 60

    total_hours = hours + add_hours + extra_hours
    total_hours = total_hours % 24

    return f"{total_hours:02d}:{total_minutes:02d}"

def calculate():
    start_time = entry_time.get()
    try:
        add_h = int(entry_hours.get())
        add_m = int(entry_minutes.get())
    except:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовые значения для времени")
        return

    result = add_time(start_time, add_h, add_m)
    if result:
        label_result.config(text=f"Результат: {result}")

# Создаем окно
root = tk.Tk()
root.title("Калькулятор времени")

# Ввод времени
tk.Label(root, text="Начальное время (HH:MM):").grid(row=0, column=0, padx=5, pady=5)
entry_time = tk.Entry(root)
entry_time.grid(row=0, column=1, padx=5, pady=5)

# Ввод добавляемых часов
tk.Label(root, text="Часов:").grid(row=1, column=0, padx=5, pady=5)
entry_hours = tk.Entry(root)
entry_hours.grid(row=1, column=1, padx=5, pady=5)

# Ввод добавляемых минут
tk.Label(root, text="Минут:").grid(row=2, column=0, padx=5, pady=5)
entry_minutes = tk.Entry(root)
entry_minutes.grid(row=2, column=1, padx=5, pady=5)

# Кнопка вычисления
btn = tk.Button(root, text="Рассчитать", command=calculate)
btn.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# Метка для вывода результата
label_result = tk.Label(root, text="Результат: ")
label_result.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()


