from typing import NamedTuple

class InvestmentParams(NamedTuple):
    initial_sum: float
    yield_rate: float
    tax_exempt: float
    expected_tax_rate: float
    handling_fee: float
    inflation_rate: float

NUM_YEARS = 30
GAINS_ANNUAL_TAX_RATE = 0.25


def update_plot(ax, canvas, params: InvestmentParams, yield_label):
    """Update investment comparison plot with two tax strategies."""
    yield_label.config(text=f"Yearly yield: {(params.yield_rate * 100.0):.2f}%")
    
    ax.clear()
    
    annual_yield_multiplier = 1.0 + params.yield_rate
    net_yield_with_fees = annual_yield_multiplier - params.handling_fee
    years = list(range(NUM_YEARS))
    
    # ------- Deferred tax method -------
    deferred_tax_values = list(range(NUM_YEARS))
    for year in range(NUM_YEARS):
        multiplier = net_yield_with_fees ** year
        adjusted_tax_exempt = params.tax_exempt * ((1.0 + params.inflation_rate) ** year)
        taxable_portion = (params.initial_sum * multiplier) - params.tax_exempt
        deferred_tax_values[year] = taxable_portion * (1.0 - params.expected_tax_rate) + adjusted_tax_exempt
    
    # ------- Immediate tax method -------
    reduced_initial_sum = (params.initial_sum - params.tax_exempt) * (1.0 - params.expected_tax_rate) + params.tax_exempt
    
    immediate_tax_values = list(range(NUM_YEARS))
    for year in range(NUM_YEARS):
        gross_value = reduced_initial_sum * (annual_yield_multiplier ** year)
        gains = gross_value - reduced_initial_sum
        net_value = gross_value - (gains * GAINS_ANNUAL_TAX_RATE)
        immediate_tax_values[year] = net_value
    
    ax.plot(
        years, 
        deferred_tax_values, 
        marker='o', 
        label='Deferred tax (max tax rate on entire fund)',
        linewidth=2
    )

    ax.plot(
        years, 
        immediate_tax_values, 
        marker='s', 
        color='red', 
        label='Immediate tax (taxable_portion * tax_rate, 25% on gains)',
        linewidth=2
    )
    
    ax.set_title(f"Investment Comparison - Annual Yield: {(params.yield_rate * 100.0):.2f}%")
    ax.set_xlabel("Years")
    ax.set_ylabel("Net Worth ($)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Auto-scale to fit data
    ax.relim()
    ax.autoscale_view()
    
    canvas.draw()