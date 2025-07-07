import tkinter as tk
from tkinter import ttk


class MultiplierSlider:
    DEF_YIELD_PRECENT = 9.0
    STEP_SIZE = 0.05

    def __init__(self, parent_frame, yield_var, update_plot_func):
        self._yield_value = yield_var
        self.update_plot_func = update_plot_func

        self.slider = ttk.Scale(
            parent_frame,
            from_=0.0,
            to=30.0,
            orient=tk.HORIZONTAL,
            variable=self._yield_value,
            command=self._on_slider_move
        )
        self.slider.set(self.DEF_YIELD_PRECENT)
        self.slider.pack(pady=10, fill=tk.X)
        self.slider.focus_set()

    def _on_slider_move(self, *args):
        self.update_plot_func()

    def _move_slider_key(self, event):
        current_value = self._yield_value.get()

        if event.keysym in ("Right", "Up"):
            new_val = min(current_value + self.STEP_SIZE, self.slider.cget("to"))
        elif event.keysym in ("Left", "Down"):
            new_val = max(current_value - self.STEP_SIZE, self.slider.cget("from"))
        else:
            return

        self.slider.set(round(new_val, 2))
        self.update_plot_func()
        return "break"

    def set_value(self, value):
        self.slider.set(value)

    def reset(self):
        self.slider.set(self.DEF_YIELD_PRECENT)
