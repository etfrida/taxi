import streamlit as st
from taxy.plot_calculator import create_plotly_figure, InvestmentParams

# Default values
DEF_INITIAL_SUM = 1000.0
DEF_YIELD_PERCENT = 9.0
DEF_TAX_EXEMPT = 400.0
DEF_EXPECTED_TAX_RATE = 48.0
DEF_HANDLING_FEE = 0.5
DEF_INFLATION_RATE = 1.5

st.set_page_config(
    page_title="Investment Comparison Tool",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Investment Comparison Tool")
st.markdown("Compare deferred tax vs immediate tax investment strategies")

# Create two columns for layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Parameters")
    
    # Input fields with default values
    initial_sum = st.number_input(
        "Initial Sum ($)",
        min_value=0.0,
        value=DEF_INITIAL_SUM,
        step=100.0,
        format="%.2f"
    )
    
    yield_rate = st.slider(
        "Yearly Yield (%)",
        min_value=0.0,
        max_value=30.0,
        value=DEF_YIELD_PERCENT,
        step=0.05,
        format="%.2f%%"
    )
    
    tax_exempt = st.number_input(
        "Tax Exempt ($)",
        min_value=0.0,
        value=DEF_TAX_EXEMPT,
        step=50.0,
        format="%.2f"
    )
    
    expected_tax_rate = st.slider(
        "Expected Tax Rate (%)",
        min_value=0.0,
        max_value=100.0,
        value=DEF_EXPECTED_TAX_RATE,
        step=0.1,
        format="%.1f%%"
    )
    
    handling_fee = st.slider(
        "Handling Fee (Provident fund) (%)",
        min_value=0.0,
        max_value=10.0,
        value=DEF_HANDLING_FEE,
        step=0.1,
        format="%.1f%%"
    )
    
    inflation_rate = st.slider(
        "Inflation Rate (%)",
        min_value=0.0,
        max_value=10.0,
        value=DEF_INFLATION_RATE,
        step=0.1,
        format="%.1f%%"
    )
    
    # Reset button
    if st.button("Reset All Parameters"):
        st.rerun()

with col2:
    st.subheader("Investment Comparison")
    
    # Create parameters object
    params = InvestmentParams(
        initial_sum=initial_sum,
        yield_rate=yield_rate / 100.0,
        tax_exempt=tax_exempt,
        expected_tax_rate=expected_tax_rate / 100.0,
        handling_fee=handling_fee / 100.0,
        inflation_rate=inflation_rate / 100.0
    )
    
    # Create and display Plotly figure
    fig = create_plotly_figure(params)
    st.plotly_chart(fig, use_container_width=True)
    
    # Display current yield value
    st.info(f"**Current Yearly Yield:** {yield_rate:.2f}%")

# Add sidebar with information
with st.sidebar:
    st.subheader("About")
    st.markdown("""
    This tool compares two investment tax strategies:
    
    **🔵 Deferred Tax Method:**
    - Pay maximum tax rate on entire fund at withdrawal
    - Growth compounds without annual tax
    
    **🔴 Immediate Tax Method:**
    - Pay tax upfront on taxable portion
    - 25% annual tax on gains
    - Lower initial investment amount
    
    Use the sliders to adjust parameters and see how different scenarios affect your long-term returns.
    """)
    
    st.subheader("Instructions")
    st.markdown("""
    1. Adjust the **Initial Sum** you want to invest
    2. Use the **Yield slider** to set expected annual return
    3. Set your **Tax Exempt** amount
    4. Configure tax rates and fees
    5. Compare the two strategies in the chart
    """)