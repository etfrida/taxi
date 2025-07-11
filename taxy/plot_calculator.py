from typing import NamedTuple, List
import plotly.graph_objects as go

class InvestmentParams(NamedTuple):
    initial_sum: float
    yield_rate: float
    tax_exempt: float
    expected_tax_rate: float
    handling_fee: float
    inflation_rate: float

NUM_YEARS = 30
GAINS_ANNUAL_TAX_RATE = 0.25


def _calc_deferred_tax_method(params: InvestmentParams) -> List[float]:
    annual_yield_multiplier = 1.0 + params.yield_rate
    net_yield_with_fees = annual_yield_multiplier - params.handling_fee
    
    deferred_tax_values = list(range(NUM_YEARS))
    for year in range(NUM_YEARS):
        gross_value = params.initial_sum * (net_yield_with_fees ** year)
        adjusted_tax_exempt = params.tax_exempt * ((1.0 + params.inflation_rate) ** year)
        tax = (gross_value - adjusted_tax_exempt) * params.expected_tax_rate
        deferred_tax_values[year] = gross_value - tax
    
    return deferred_tax_values


def _calc_immediate_tax_method(params: InvestmentParams) -> List[float]:
    straight_up_tax = (params.initial_sum - params.tax_exempt) * params.expected_tax_rate
    reduced_initial_sum = params.initial_sum - straight_up_tax
    annual_yield_multiplier = 1.0 + params.yield_rate

    immediate_tax_values = list(range(NUM_YEARS))
    for year in range(NUM_YEARS):
        gross_value = reduced_initial_sum * (annual_yield_multiplier ** year)
        gains = gross_value - reduced_initial_sum
        net_value = gross_value - (gains * GAINS_ANNUAL_TAX_RATE)
        immediate_tax_values[year] = net_value
    
    return immediate_tax_values


def create_plotly_figure(params: InvestmentParams):
    """Create interactive Plotly figure for investment comparison."""
    years = list(range(NUM_YEARS))
    
    deferred_tax_values = _calc_deferred_tax_method(params)
    immediate_tax_values = _calc_immediate_tax_method(params)
    
    fig = go.Figure()
    
    # Add deferred tax line
    fig.add_trace(go.Scatter(
        x=years,
        y=deferred_tax_values,
        mode='lines+markers',
        name='Deferred tax (max tax rate on entire fund)',
        line=dict(color='blue', width=3),
        marker=dict(size=6, symbol='circle'),
        hovertemplate='<b>Year:</b> %{x}<br><b>Net Worth:</b> $%{y:,.2f}<extra></extra>'
    ))
    
    # Add immediate tax line
    fig.add_trace(go.Scatter(
        x=years,
        y=immediate_tax_values,
        mode='lines+markers',
        name='Immediate tax (taxable_portion * tax_rate, 25% on gains)',
        line=dict(color='red', width=3),
        marker=dict(size=6, symbol='square'),
        hovertemplate='<b>Year:</b> %{x}<br><b>Net Worth:</b> $%{y:,.2f}<extra></extra>'
    ))
    
    # Update layout
    fig.update_layout(
        title=f"Investment Comparison - Annual Yield: {(params.yield_rate * 100.0):.2f}%",
        xaxis_title="Years",
        yaxis_title="Net Worth ($)",
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        height=600,
        font=dict(size=12),
        plot_bgcolor='white'
    )
    
    # Add grid
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    
    return fig


