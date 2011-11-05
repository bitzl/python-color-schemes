from __future__ import division
import unittest
from color_schemes import Color




class TestColor(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.places = 4

    def test_allowed_modes(self):
        Color(0, 0, 0, 'rgb')
        Color(0, 0, 0, 'hls')
        self.assertRaises(Exception, Color, 0, 0, 0, 'x')
    
    def test_rbg_to_hls(self):
        color = Color(0, 117 / 255, 226 / 255, 'rgb')
        h, l, s = color.hls()
        self.assertAlmostEqual(h, 148 / 255, self.places)
        self.assertAlmostEqual(l, 113 / 255, self.places)
        self.assertAlmostEqual(s, 255 / 255, self.places)
        
    def test_hls_to_rbg(self):
        color = Color(148 / 255, 113 / 255, 1, 'hls')
        red, green, blue = color.rgb()
        self.assertAlmostEqual(red, 0, self.places)
        self.assertAlmostEqual(green, 117 / 255, self.places)
        self.assertAlmostEqual(blue, 226 / 255, self.places)


if __name__ == "__main__":
    unittest.main()