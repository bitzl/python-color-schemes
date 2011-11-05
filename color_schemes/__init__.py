from __future__ import division
from colorsys import rgb_to_hls, hls_to_rgb
from color_schemes.util import html_to_rgb

class Color(object):
    def __init__(self, *args):
        """
        Creates a instance of Color:
        
            Color('#FF0000')
            Color(channel1, channel2, channel3, mode)
            
        with mode one of 'rgb' or 'hls'.
        """ 
        if len(args) == 1:
            self.mode = 'rgb'
            self.channel1, self.channel2, self.channel3 = html_to_rgb(args[0])
        elif len(args) == 4:
            self.channel1 = args[0]
            self.channel2 = args[1]
            self.channel3 = args[2]
            mode = args[3]
            if mode in set(['rgb', 'hls']):
                self.mode = mode
            else:
                raise Exception('Mode %s is not supported.' % mode)
        else:
            raise Exception('Color takes exaclty one or four argument, but got %d.' % len(args))
    
    def hls(self):
        if self.mode == 'rgb':
            hls =  rgb_to_hls(self.channel1, self.channel2, self.channel3)
        elif self.mode == 'hls':
            hls = (self.channel1, self.channel2, self.channel3)
        return hls
        
    def rgb(self):
        if self.mode == 'rgb':
            rgb = (self.channel1, self.channel2, self.channel3)
        elif self.mode == 'hls':
            rgb =  hls_to_rgb(self.channel1, self.channel2, self.channel3)
        return rgb

