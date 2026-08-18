from unittest import TestCase
from py_text_clock.fontMods import TimeFonts

class TestHighlighting(TestCase):
    def test_basic_word_locations(self):
        fonts = TimeFonts("it is ten minutes to twelve")
        # word_locations contains the list of lists
        # it: [0, 0, 2]
        # is: [0, 3, 5]
        # ten (minutes): [0, 9, 12]
        # minutes: [4, 1, 8]
        # to: [4, 9, 11]
        # twelve: [6, 6, 12]
        expected_locations = [[0, 0, 2], [0, 3, 5], [0, 9, 12], [4, 1, 8], [4, 9, 11], [6, 6, 12]]
        self.assertEqual(fonts.word_locations, expected_locations)
