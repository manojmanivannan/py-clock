from unittest import TestCase
from py_text_clock.fontMods import TimeFonts
from py_text_clock.clockFace import TimeGenerator

class TestTimeFonts(TestCase):
    def test_matrix_contains_fancy_tui_elements(self):
        # We expect a method generate_panel() to return a rich Renderable or formatted string
        fonts = TimeFonts("it is ten o'clock")
        panel = fonts.generate_panel()
        
        # In TUI, we expect some border or a rich Panel type. 
        # For simplicity, we can check its type or string representation.
        from rich.panel import Panel
        self.assertIsInstance(panel, Panel)
        self.assertEqual(panel.title, "Py-Clock")

    def test_matrix_highlights_correct_words(self):
        fonts = TimeFonts("it is ten o'clock")
        panel = fonts.generate_panel()
        
        # Test that the panel's renderable contains the highlighted words
        # The renderable should be a rich.text.Text or Table
        from rich.text import Text
        self.assertIsInstance(panel.renderable, Text)
        
        text_content = panel.renderable.plain
        # Verify that all characters are present in the grid
        self.assertIn("I T L I S A S T H T E N", text_content)

class TestClockFaceTUI(TestCase):
    def test_print_time_matrix_generates_panel(self):
        generator = TimeGenerator()
        # Mock the show method or rich console to ensure it's called
        import unittest.mock as mock
        with mock.patch('py_text_clock.fontMods.TimeFonts.show') as mock_show:
            generator.print_time_matrix()
            mock_show.assert_called_once()

    def test_print_time_matrix_live(self):
        generator = TimeGenerator()
        import unittest.mock as mock
        with mock.patch('rich.live.Live') as mock_live:
            # We need to simulate a KeyboardInterrupt on the first sleep to avoid infinite loop
            with mock.patch('py_text_clock.clockFace.sleep', side_effect=KeyboardInterrupt):
                generator.print_time_matrix(live=True)
            mock_live.assert_called_once()
