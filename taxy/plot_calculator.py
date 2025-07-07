"""
Plot calculation module for investment comparison.

This module contains functions for calculating and updating investment plots
with different tax strategies and handling fees.
"""

NUM_YEARS = 30

def update_plot(
    ax, canvas, yield_value, initial_sum_entry, yield_label, tax_exempt_entry, expected_tax_rate_entry, *args
):
    """Update investment comparison plot with two tax strategies."""
    yield_label.config(text=f"Yearly yield: {yield_value.get():.2f}%")
    
    try:
        initial_sum = float(initial_sum_entry.get())
    except ValueError:
        initial_sum = 100.0
    
    tax_exempt = float(tax_exempt_entry.get())
    expected_tax_rate = float(expected_tax_rate_entry.get()) / 100.0
    
    ax.clear()
    
    annual_yield_multiplier = 1.0 + (yield_value.get() / 100.0)
    handling_fee_rate = 0.5 / 100.0
    net_yield_with_fees = annual_yield_multiplier - handling_fee_rate
    years = list(range(NUM_YEARS))
    
    deferred_tax_values = list(range(NUM_YEARS))
    for year in range(NUM_YEARS):
        multiplier = net_yield_with_fees ** year
        # total_deferred_tax = (initial_sum - tax_exempt) * expected_tax_rate
        deferred_tax_values[year] = ((initial_sum * multiplier) - tax_exempt) * (1.0 - expected_tax_rate) + tax_exempt
        # deferred_tax_values[year] = (initial_sum * multiplier) * (1.0 - expected_tax_rate) + tax_exempt
    

    ax.plot(
        years, 
        deferred_tax_values, 
        marker='o', 
        label='Deferred tax (max tax rate on entire fund)',
        linewidth=2
    )
    
    reduced_initial_sum = (initial_sum - tax_exempt) * (1.0 - expected_tax_rate) + tax_exempt
    gains_annual_tax_rate = 0.25
    
    immediate_tax_values = list(range(NUM_YEARS))
    for year in range(NUM_YEARS):
        gross_value = reduced_initial_sum * (annual_yield_multiplier ** year)
        gains = gross_value - reduced_initial_sum
        net_value = gross_value - (gains * gains_annual_tax_rate)
        immediate_tax_values[year] = net_value
    
    ax.plot(
        years, 
        immediate_tax_values, 
        marker='s', 
        color='red', 
        label='Immediate tax (taxable_portion * tax_rate, 25% on gains)',
        linewidth=2
    )
    
    ax.set_title(f"Investment Comparison - Annual Yield: {yield_value.get():.2f}%")
    ax.set_xlabel("Years")
    ax.set_ylabel("Net Worth ($)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    canvas.draw()