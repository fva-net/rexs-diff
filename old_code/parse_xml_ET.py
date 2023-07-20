import xml.etree.ElementTree as ET



def parse_xml_ET (filename):
    """
    This function parses the file for easier working with the data
    - 'filename': Path to the input xml data file 
    """
    data = ET.parse(filename)
    return data

