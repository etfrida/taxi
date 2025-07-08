# Taxy - Investment Strategy Comparison Tool

A GUI application for comparing different investment strategies with tax implications, built with Python and Tkinter.

## Features

- **Interactive GUI** with sliders and input fields
- **Real-time plotting** of investment growth over time
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
python -m taxy.main_gui
```

### Using pip (when published)

```bash
pip install taxy
taxy
```

## Usage

1. **Set Initial Investment**: Enter your initial investment amount (default: 1000)
2. **Configure Tax-Exempt Amount**: Enter the portion of investment that's tax-exempt (default: 450)
3. **Set Expected Tax Rate**: Enter your expected tax rate as a percentage (default: 48%)
4. **Set Inflation Rate**: Enter the annual inflation rate that adjusts tax-exempt amount (default: 1.5%)
5. **Configure Handling Fee**: Set the provident fund handling fee percentage (default: 0.5%)
6. **Adjust Yield Rate**: Use the slider to set yearly yield percentage (0-30%, default: 9%)
7. **Compare Strategies**: View both investment strategies plotted on the same graph over 30 years
8. **Navigate Plot**: Use the matplotlib toolbar to zoom, pan, and reset the plot view
9. **Reset All**: Click "Reset All" to return all parameters to default values

## Requirements

- Python 3.8+
- matplotlib >= 3.5.0
- tkinter (usually included with Python)

## Project Structure

```
taxy/
├── taxy/
│   ├── __init__.py
│   ├── main_gui.py          # Main GUI application
│   ├── multiplier_slider.py # Custom slider widget
│   └── plot_calculator.py   # Investment calculation logic
├── pyproject.toml           # Package configuration
├── requirements.txt         # Dependencies
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

- Built with Python's tkinter for the GUI
- Uses matplotlib for plotting financial data
- Designed for educational purposes in financial planning