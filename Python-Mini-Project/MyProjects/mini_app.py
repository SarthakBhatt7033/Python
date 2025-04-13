import tkinter as tk
from tkinter import ttk
import time
import math

class MiniApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini App Suite")
        self.root.geometry("600x500")
        self.root.configure(bg="#f8f8ff")  # Very light gray background

        # Style Configuration
        style = ttk.Style()
        style.configure("TButton", padding=5, font=('Segoe UI', 10), background="#e0f0ff")
        style.configure("TLabel", font=('Segoe UI', 12), background="#f8f8ff")
        style.configure("TEntry", font=('Segoe UI', 12))
        style.configure("TSpinbox", font=('Segoe UI', 10))

        # Calculator Frame
        self.calc_frame = ttk.Frame(root, padding="10 10 10 10")
        self.calc_frame.grid(row=0, column=0, sticky="nsew")

        self.calc_entry = ttk.Entry(self.calc_frame, width=25, justify="right")
        self.calc_entry.grid(row=0, column=0, columnspan=4, pady=5)

        buttons = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']
        row_val = 1
        col_val = 0
        for button in buttons:
            ttk.Button(self.calc_frame, text=button, width=5, style="TButton", command=lambda b=button: self.calc_click(b)).grid(row=row_val, column=col_val, padx=2, pady=2)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        ttk.Button(self.calc_frame, text='C', width=5, style="TButton", command=self.calc_clear).grid(row=5, column=0, padx=2, pady=2)

        # Pomodoro Frame
        self.pomodoro_frame = ttk.Frame(root, padding="10 10 10 10")
        self.pomodoro_frame.grid(row=0, column=1, sticky="nsew")

        self.work_time = tk.IntVar(value=25)
        self.break_time = tk.IntVar(value=5)
        self.timer_running = False
        self.time_left = tk.IntVar(value=self.work_time.get() * 60)

        ttk.Label(self.pomodoro_frame, text="Work (min):", style="TLabel").grid(row=0, column=0, padx=2, pady=2)
        ttk.Spinbox(self.pomodoro_frame, from_=1, to=60, textvariable=self.work_time, width=5, style="TSpinbox").grid(row=0, column=1, padx=2, pady=2)
        ttk.Label(self.pomodoro_frame, text="Break (min):", style="TLabel").grid(row=1, column=0, padx=2, pady=2)
        ttk.Spinbox(self.pomodoro_frame, from_=1, to=60, textvariable=self.break_time, width=5, style="TSpinbox").grid(row=1, column=1, padx=2, pady=2)

        self.timer_label = ttk.Label(self.pomodoro_frame, textvariable=self.time_left, font=("Segoe UI", 24), background="#f8f8ff")
        self.timer_label.grid(row=2, column=0, columnspan=2, pady=10)

        ttk.Button(self.pomodoro_frame, text="Start", style="TButton", command=self.start_timer).grid(row=3, column=0, columnspan=2, pady=5)
        ttk.Button(self.pomodoro_frame, text="Reset", style="TButton", command=self.reset_timer).grid(row=4, column=0, columnspan=2, pady=5)

        # Clock Frame
        self.clock_frame = ttk.Frame(root, padding="10 10 10 10")
        self.clock_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.time_string = tk.StringVar()
        self.date_string = tk.StringVar()

        self.time_label = ttk.Label(self.clock_frame, textvariable=self.time_string, font=("Segoe UI", 36), background="#f8f8ff")
        self.time_label.pack(pady=5)
        self.date_label = ttk.Label(self.clock_frame, textvariable=self.date_string, font=("Segoe UI", 18), background="#f8f8ff")
        self.date_label.pack()

        self.update_clock()

        # Grid Configurations
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)

    def calc_click(self, char):
        current = self.calc_entry.get()
        if char == '=':
            try:
                result = eval(current)
                self.calc_entry.delete(0, tk.END)
                self.calc_entry.insert(0, result)
            except Exception:
                self.calc_entry.delete(0, tk.END)
                self.calc_entry.insert(0, "Error")
        else:
            self.calc_entry.insert(tk.END, char)

    def calc_clear(self):
        self.calc_entry.delete(0, tk.END)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def reset_timer(self):
        self.timer_running = False
        self.time_left.set(self.work_time.get() * 60)

    def update_timer(self):
        if self.timer_running:
            if self.time_left.get() > 0:
                self.time_left.set(self.time_left.get() - 1)
                self.root.after(1000, self.update_timer)
            else:
                self.timer_running = False
                if self.time_left.get() == 0:
                    if self.time_left.get() ==0 and self.time_left.get() != self.work_time.get()*60:
                        if self.time_left.get() != self.break_time.get()*60:
                            self.time_left.set(self.break_time.get() * 60)
                            self.start_timer()
                        else:
                            self.time_left.set(self.work_time.get() * 60)
                            self.start_timer()
                    else:
                        self.time_left.set(self.break_time.get() * 60)
                        self.start_timer()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%Y-%m-%d")
        self.time_string.set(current_time)
        self.date_string.set(current_date)
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniApp(root)
    root.mainloop()