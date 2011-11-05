from __future__ import division
from colorsys import rgb_to_hls, hls_to_rgb

class Color(object):
    def __init__(self, channel1, channel2, channel3, mode):
        self.channel1 = channel1
        self.channel2 = channel2
        self.channel3 = channel3
        if mode in set(['rgb', 'hls']):
            self.mode = mode
        else:
            raise Exception('Mode %s is not supported.' % mode)
    
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

