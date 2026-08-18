from unittest import TestCase
from py_text_clock.analogFace import AnalogClock
from py_text_clock.clockFace import TimeGenerator

class TestAnalogClock(TestCase):
    def test_analog_contains_fancy_tui_elements(self):
        clock = AnalogClock(10, 10, 30) # hr, min, sec
        panel = clock.generate_panel()
        
        from rich.panel import Panel
        self.assertIsInstance(panel, Panel)
        self.assertEqual(panel.title, "Analog Clock")

    def test_analog_clock_renders_hands(self):
        clock = AnalogClock(10, 10, 30)
        panel = clock.generate_panel()
        
        from rich.text import Text
        self.assertIsInstance(panel.renderable, Text)
        
        text_content = panel.renderable.plain
        self.assertIn("12", text_content)
        self.assertIn(" 3", text_content)
        self.assertIn(" 6", text_content)
        self.assertIn(" 9", text_content)

class TestClockFaceAnalogTUI(TestCase):
    def test_print_time_analog_generates_panel(self):
        generator = TimeGenerator()
        import unittest.mock as mock
        with mock.patch('py_text_clock.analogFace.AnalogClock.show') as mock_show:
            generator.print_time_analog()
            mock_show.assert_called_once()

    def test_print_time_analog_live(self):
        generator = TimeGenerator()
        import unittest.mock as mock
        with mock.patch('rich.live.Live') as mock_live:
            with mock.patch('py_text_clock.clockFace.sleep', side_effect=KeyboardInterrupt):
                generator.print_time_analog(live=True)
            mock_live.assert_called_once()
