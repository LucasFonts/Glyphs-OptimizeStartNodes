# encoding: utf-8
from __future__ import division, print_function, unicode_literals

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class OptimizeStartNodes(FilterWithoutDialog):

    @objc.python_method
    def settings(self):
        self.menuName = Glyphs.localize({
            'en': 'Optimize Start Nodes',
            'de': 'Startpunkte optimieren',
            'es': 'Optimizar los primeros nodos',
            'fr': 'Optimiser les nœuds prémiers',
        })

    @objc.python_method
    def filter(self, layer, inEditView, customParameters):
        for p in layer.paths:
            node_types = [n.type for n in p.nodes]
            if node_types[-1] != "line":
                if "line" in node_types:
                    i = node_types.index("line")
                    p.nodes[i].makeNodeFirst()

    @objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
