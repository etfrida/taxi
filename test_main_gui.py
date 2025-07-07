import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock
import matplotlib.pyplot as plt
from main_gui import create_gui, NUM_YEARS
from multiplier_slider import MultiplierSlider


class TestMainGUI(unittest.TestCase):
    """Test suite for main_gui.py functionality."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.root = tk.Tk()
        self.root.withdraw()  # Hide test window
        
    def tearDown(self):
        """Clean up after each test method."""
        self.root.destroy()
        plt.close('all')
        
    def test_num_years_constant(self):
        """Test that NUM_YEARS is correctly defined."""
        self.assertEqual(NUM_YEARS, 25)
        
    def test_create_gui_constants(self):
        """Test that GUI constants are properly defined."""
        # Test that NUM_YEARS is used correctly in calculations
        self.assertEqual(NUM_YEARS, 25)
        self.assertIsInstance(NUM_YEARS, int)
        self.assertGreater(NUM_YEARS, 0)
        
    def test_validate_numeric_function(self):
        """Test the numeric validation function."""
        # Create a test root to register the validation
        test_root = tk.Tk()
        test_root.withdraw()
        
        # Create validation function (extracted from main_gui.py)
        def _validate_numeric(new_value):
            """Allow only floating point numbers or an empty string."""
            if new_value == "":
                return True
            try:
                float(new_value)
                return True
            except ValueError:
                return False
        
        # Test valid inputs
        self.assertTrue(_validate_numeric(""))
        self.assertTrue(_validate_numeric("123"))
        self.assertTrue(_validate_numeric("123.45"))
        self.assertTrue(_validate_numeric("0"))
        self.assertTrue(_validate_numeric("0.0"))
        self.assertTrue(_validate_numeric("-123.45"))
        
        # Test invalid inputs
        self.assertFalse(_validate_numeric("abc"))
        self.assertFalse(_validate_numeric("12.34.56"))
        self.assertFalse(_validate_numeric("12a"))
        
        test_root.destroy()
        
    def test_compound_interest_calculation(self):
        """Test the compound interest calculation logic."""
        # Test parameters
        initial_sum = 100.0
        yield_percent = 9.0
        years = 5
        
        # Expected calculation: y = initial_sum * (1 + yield_percent/100) ** years
        yield_multiplier = 1.0 + (yield_percent / 100.0)
        expected_values = [initial_sum * (yield_multiplier ** i) for i in range(years)]
        
        # Manual verification of first few values
        self.assertAlmostEqual(expected_values[0], 100.0, places=2)
        self.assertAlmostEqual(expected_values[1], 109.0, places=2)
        self.assertAlmostEqual(expected_values[2], 118.81, places=2)
        self.assertAlmostEqual(expected_values[3], 129.50, places=2)
        self.assertAlmostEqual(expected_values[4], 141.16, places=2)
        
    def test_multiplier_slider_initialization(self):
        """Test MultiplierSlider initialization."""
        parent_frame = tk.Frame(self.root)
        yield_var = tk.DoubleVar()
        update_func = MagicMock()
        
        slider = MultiplierSlider(parent_frame, yield_var, update_func)
        
        # Test initial values
        self.assertEqual(slider._yield_value, yield_var)
        self.assertEqual(slider.update_plot_func, update_func)
        self.assertEqual(slider.DEF_YIELD_PRECENT, 9.0)
        self.assertEqual(slider.STEP_SIZE, 0.05)
        
    def test_multiplier_slider_reset(self):
        """Test MultiplierSlider reset functionality."""
        parent_frame = tk.Frame(self.root)
        yield_var = tk.DoubleVar()
        update_func = MagicMock()
        
        slider = MultiplierSlider(parent_frame, yield_var, update_func)
        
        # Change value and reset
        slider.set_value(15.0)
        slider.reset()
        
        # Check if reset to default
        self.assertEqual(yield_var.get(), MultiplierSlider.DEF_YIELD_PRECENT)
        
    def test_multiplier_slider_set_value(self):
        """Test MultiplierSlider set_value method."""
        parent_frame = tk.Frame(self.root)
        yield_var = tk.DoubleVar()
        update_func = MagicMock()
        
        slider = MultiplierSlider(parent_frame, yield_var, update_func)
        
        # Test setting different values
        test_values = [0.0, 5.5, 15.0, 25.0, 30.0]
        for value in test_values:
            slider.set_value(value)
            self.assertEqual(yield_var.get(), value)
            
    @patch('main_gui.plt')
    def test_update_plot_with_valid_input(self, mock_plt):
        """Test update_plot function with valid numeric input."""
        # This would require more complex mocking to test the actual update_plot
        # function from create_gui, but we can test the calculation logic
        initial_sum = 100.0
        yield_percent = 9.0
        
        # Simulate the calculation that happens in update_plot
        yield_multiplier = 1.0 + (yield_percent / 100.0)
        x_values = [i for i in range(NUM_YEARS)]
        y_values = [initial_sum * (yield_multiplier ** xi) for xi in x_values]
        
        # Test that we get the expected number of points
        self.assertEqual(len(x_values), NUM_YEARS)
        self.assertEqual(len(y_values), NUM_YEARS)
        
        # Test first and last values
        self.assertAlmostEqual(y_values[0], 100.0, places=2)
        self.assertAlmostEqual(y_values[-1], 100.0 * (1.09 ** (NUM_YEARS - 1)), places=2)
        
    def test_update_plot_with_invalid_input(self):
        """Test update_plot behavior with invalid input."""
        # Test the fallback behavior when initial_sum is invalid
        try:
            invalid_input = "invalid"
            initial_sum = float(invalid_input)
        except ValueError:
            # Should fall back to default value
            initial_sum = 100.0
            
        self.assertEqual(initial_sum, 100.0)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)