from lxml import etree
from lxml import objectify



class MessageCluster():
    def __init__(self, xml_tree):
        for element in xml_tree:
            setattr(self, element.tag, element.text)
        
class TimeCluster():
    def __init__(self, xml_tree):
        for element in xml_tree:
            setattr(self, element.tag, element.text)
    
class InstantaneousDemand():
    def __init__(self, xml_tree):
        for element in xml_tree:
            setattr(self, element.tag, element.text)
    
class NetworkInfo():
    def __init__(self, xml_tree):
        for element in xml_tree:
            setattr(self, element.tag, element.text)
    
class PriceCluster():
    def __init__(self, xml_tree):
        for element in xml_tree:
            setattr(self, element.tag, element.text)
    
class DeviceInfo():
    def __init__(self, xml_tree):
        for element in xml_tree:
            setattr(self, element.tag, element.text)
    
class CurrentSummationDelivered():
    def __init__(self, xml_tree):
        for element in xml_tree:
            setattr(self, element.tag, element.text)
    
class ScheduleInfo():
    def __init__(self, xml_tree):
        for element in xml_tree:
            setattr(self, element.tag, element.text)
    
class BlockPriceDetail():
    def __init__(self, xml_tree):
        for element in xml_tree:
            setattr(self, element.tag, element.text)