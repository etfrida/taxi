import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from .multiplier_slider import MultiplierSlider
from .plot_calculator import update_plot, InvestmentParams


def create_gui():
    root = tk.Tk()
    root.title("Dynamic Plot App")
    root.geometry("800x600")

    main_frame = ttk.Frame(root, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)

    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=3)
    main_frame.grid_rowconfigure(0, weight=1)

    controls_frame = ttk.LabelFrame(main_frame, text="Controls", padding="10")
    controls_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    controls_frame.grid_rowconfigure(0, weight=1)

    yield_value = tk.DoubleVar()

    def update_plot_wrapper(*args):
        initial_sum = float(initial_sum_entry.get())
        yield_rate = float(yield_value.get()) / 100.0
        tax_exempt = float(tax_exempt_entry.get())
        expected_tax_rate = float(expected_tax_rate_entry.get()) / 100.0
        handling_fee = float(handling_fee_entry.get()) / 100.0
        inflation_rate = float(inflation_rate_entry.get()) / 100.0

        
        params = InvestmentParams(
            initial_sum=initial_sum,
            yield_rate=yield_rate,
            tax_exempt=tax_exempt,
            expected_tax_rate=expected_tax_rate,
            handling_fee=handling_fee,
            inflation_rate=inflation_rate
        )
        update_plot(ax, canvas, params, yield_label)


    initial_sum_label = ttk.Label(controls_frame, text="Initial Sum:")
    initial_sum_label.pack(pady=5)

    def _validate_numeric(new_value):
        """Allow only floating point numbers or an empty string."""
        if new_value == "":
            return True
        try:
            float(new_value)
            return True
        except ValueError:
            return False
        
    def pack_and_bind(entry: ttk.Entry, def_value: str):
        entry.insert(0, def_value)
        entry.pack(pady=5, fill=tk.X)
        entry.bind("<Return>", update_plot_wrapper)
        entry.bind("<FocusOut>", update_plot_wrapper)

    vcmd = (root.register(_validate_numeric), '%P')
    initial_sum_entry = ttk.Entry(controls_frame, validate='key', validatecommand=vcmd)
    pack_and_bind(initial_sum_entry, "1000.0")

    tax_exempt_label = ttk.Label(controls_frame, text="Tax Exempt:")
    tax_exempt_label.pack(pady=5)
    
    tax_exempt_entry = ttk.Entry(controls_frame, validate='key', validatecommand=vcmd)
    pack_and_bind(tax_exempt_entry, "450.0")

    expected_tax_rate_label = ttk.Label(controls_frame, text="Expected Tax Rate (%):")
    expected_tax_rate_label.pack(pady=5)
    
    def _validate_percentage(new_value):
        """Allow only percentage values between 0 and 100 or an empty string."""
        if new_value == "":
            return True
        try:
            value = float(new_value)
            return 0 <= value <= 100
        except ValueError:
            return False
    
    pcmd = (root.register(_validate_percentage), '%P')
    expected_tax_rate_entry = ttk.Entry(controls_frame, validate='key', validatecommand=pcmd)
    pack_and_bind(expected_tax_rate_entry, "48.0")

    handling_fee_label = ttk.Label(controls_frame, text="Handling fee (Provident fund) (%):")
    handling_fee_label.pack(pady=5)
    
    handling_fee_entry = ttk.Entry(controls_frame, validate='key', validatecommand=pcmd)
    pack_and_bind(handling_fee_entry, "0.5")

    inflation_rate_label = ttk.Label(controls_frame, text="Inflation rate (%):")
    inflation_rate_label.pack(pady=5)
    
    inflation_rate_entry = ttk.Entry(controls_frame, validate='key', validatecommand=pcmd)
    pack_and_bind(inflation_rate_entry, "1.5")

    plot_frame = ttk.LabelFrame(main_frame, text="Plot", padding="10")
    plot_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title("Investment Comparison")
    ax.set_xlabel("Years")
    ax.set_ylabel("Networth")

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)

    yield_label = ttk.Label(controls_frame)
    yield_label.pack(pady=5)

    multiplier_slider = MultiplierSlider(controls_frame, yield_value, update_plot_wrapper)

    toolbar = NavigationToolbar2Tk(canvas, plot_frame)
    toolbar.update()
    toolbar.pack(side=tk.TOP, fill=tk.X)

    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    update_plot_wrapper()

    def _on_closing():
        plt.close(fig)
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", _on_closing)
    root.mainloop()

def main():
    """Main entry point for the application."""
    create_gui()

if __name__ == "__main__":
    main()