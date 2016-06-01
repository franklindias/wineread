from django import template
import os
import random

register = template.Library()

@register.filter(name='keyvalue')
def keyvalue(dict, key):    
    return dict[key]

@register.filter
def freqRelative(value):
    return str(100 * value / 178)+'%'

@register.tag(name="randomgen")
def randomgen(parser, token):
    items = []
    bits =  token.split_contents()
    for item in bits:
        items.append(item)
    return RandomgenNode(items[1:])

class RandomgenNode(template.Node):
    def __init__(self, items):
        self.items = []
        for item in items:
            self.items.append(item)
    
    def render(self, context):
        arg1 = self.items[0]
        arg2 = self.items[1]
        if "hash" in self.items:
            result = os.urandom(16).encode('hex')
        elif "float" in self.items:
            result = random.uniform(int(arg1), int(arg2))
        elif not self.items:
            result = random.random()
        else:
            result = random.randint(int(arg1), int(arg2))
        return result