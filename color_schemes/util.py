from __future__ import division

def rgb_to_html(red, green, blue):
    return '#%02X%02X%02X' % (int(round(red * 255)) , int(round(green * 255)) , int(round(blue * 255)))

def html_to_rgb(html):
    red = int(html[1:3], 16) / 255
    green = int(html[3:5], 16) / 255
    blue = int(html[5:], 16) / 255
    return (red, green, blue)