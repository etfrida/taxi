"""
Taxy - Investment Strategy Comparison Tool

A web application for comparing investment strategies with different tax implications.
Built with Streamlit and Plotly for interactive visualizations.
"""

__version__ = "0.2.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .plot_calculator import create_plotly_figure, InvestmentParams

__all__ = ["create_plotly_figure", "InvestmentParams"]