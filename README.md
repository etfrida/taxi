# Taxy - Investment Strategy Comparison Tool

A modern web application for comparing different investment strategies with tax implications, built with Streamlit and Plotly for interactive visualizations.

## Features

- **Modern web interface** with interactive sliders and input fields
- **Real-time interactive plotting** with hover tooltips, zoom, and pan
- **Professional Plotly visualizations** with responsive design
- **Tax strategy comparison** between:
  - Deferred tax strategy with customizable handling fees and inflation-adjusted tax-exempt amounts
  - Immediate tax strategy with 25% gains tax rate
- **Customizable parameters**:
  - Initial investment amount
  - Tax-exempt amount (inflation-adjusted over time)
  - Expected tax rate percentage
  - Yearly yield percentage (0-30%)
  - Inflation rate percentage (adjusts tax-exempt amount annually)
  - Handling fee percentage (customizable provident fund fees)
  - Investment timeframe (30 years)

## Screenshots

The application displays two investment strategies on the same plot:
- Blue line: Deferred tax strategy with customizable handling fees and inflation-adjusted tax exemptions
- Red line: Immediate tax strategy with 25% gains tax rate and reduced initial investment (tax paid upfront)
  
**In both cases your "Networth" is the total money your left with, _after taxes_, given you're withdrawing the funds at year X.**

## Installation

### From Source

1. Clone the repository:
```bash
git clone https://github.com/etfrida/taxy.git
cd taxy
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run streamlit_app.py
```

The application will open in your web browser at `http://localhost:8501`

### Using pip (when published)

```bash
pip install taxy
streamlit run streamlit_app.py
```

## Usage

1. **Launch the App**: Run `streamlit run streamlit_app.py` and open your browser to `http://localhost:8501`
2. **Set Initial Investment**: Enter your initial investment amount (default: $1,000)
3. **Configure Tax-Exempt Amount**: Enter the portion of investment that's tax-exempt (default: $400)
4. **Set Expected Tax Rate**: Use the slider to set your expected tax rate (default: 48%)
5. **Set Inflation Rate**: Use the slider to set annual inflation rate (default: 1.5%)
6. **Configure Handling Fee**: Set the provident fund handling fee percentage (default: 0.5%)
7. **Adjust Yield Rate**: Use the interactive slider to set yearly yield (0-30%, default: 9%)
8. **Explore Interactive Charts**: 
   - **Hover** over data points to see exact values
   - **Zoom and pan** to examine specific time periods
   - **Click legend items** to show/hide investment strategies
9. **Reset Parameters**: Click "Reset All Parameters" to return to defaults
10. **Mobile Friendly**: Works on desktop, tablet, and mobile devices

## Requirements

- Python 3.8+
- streamlit >= 1.28.0
- plotly >= 5.0.0

## Project Structure

```
taxy/
├── streamlit_app.py         # Main Streamlit web application
├── taxy/
│   ├── __init__.py          # Package exports
│   └── plot_calculator.py   # Investment calculation and Plotly visualization logic
├── requirements.txt         # Dependencies (Streamlit + Plotly)
└── README.md               # This file
```

## Development

To set up for development:

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install in development mode:
   ```bash
   pip install -e .
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Your Name - etfrida@gmail.com

## Acknowledgments

- Built with Streamlit for the modern web interface
- Uses Plotly for interactive financial data visualization
- Designed for educational purposes in financial planning
- Features responsive design for all devices
