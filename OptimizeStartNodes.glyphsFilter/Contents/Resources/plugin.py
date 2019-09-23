# encoding: utf-8

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *


class OptimizeStartNodes(FilterWithoutDialog):

    def settings(self):
        self.menuName = Glyphs.localize({'en': u'Optimize Start Nodes', 'de': u'Startpunkte optimieren'})
        self.keyboardShortcut = None  # With Cmd+Shift

    def filter(self, layer, inEditView, customParameters):
        for p in layer.paths:
            node_types = [n.type for n in p.nodes]
            if node_types[-1] != "line":
                if "line" in node_types:
                    i = node_types.index("line")
                    p.nodes[i].makeNodeFirst()

    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
