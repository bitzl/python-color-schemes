from __future__ import division

import unittest
from color_schemes import rgb_to_html, html_to_rgb


class Test(unittest.TestCase):

    def test_rgb_to_html_black_white(self):
        self.assertEqual(rgb_to_html(0, 0, 0), '#000000')
        self.assertEqual(rgb_to_html(1, 1, 1), '#FFFFFF')

    def test_rgb_to_html_base_colors(self):
        self.assertEqual(rgb_to_html(1, 0, 0), '#FF0000')
        self.assertEqual(rgb_to_html(0, 1, 0), '#00FF00')
        self.assertEqual(rgb_to_html(0, 0, 1), '#0000FF')

    def test_rgb_to_html_mixed_colors(self):
        self.assertEqual(rgb_to_html(225 / 255, 162 / 255, 106 / 255), '#E1A26A')


    def test_html_to_rgb_black_white(self):
        self.assertEqual(html_to_rgb('#000000'), (0, 0, 0))
        self.assertEqual(html_to_rgb('#FFFFFF'), (1, 1, 1))
        
    def test_html_to_rgb_base_colors(self):
        self.assertEqual(html_to_rgb('#FF0000'), (1, 0, 0))
        self.assertEqual(html_to_rgb('#00FF00'), (0, 1, 0))
        self.assertEqual(html_to_rgb('#0000FF'), (0, 0, 1))

    def test_html_to_rbg_mixed_colors(self):
        r, g, b = html_to_rgb('#E1A26A')
        self.assertAlmostEqual(r, 225 / 255)
        self.assertAlmostEqual(g, 162 / 255)
        self.assertAlmostEqual(b, 106 / 255)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHtml']
    unittest.main()