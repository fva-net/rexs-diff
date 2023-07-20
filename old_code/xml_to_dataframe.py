import xml.etree.ElementTree as ET
from old_code.parse_xml_ET import parse_xml_ET
import pandas as pd


def xml_to_dataframe(filename):
    """
    This function takes an xml file and returns two dataframes. 
    - Input: 'filename': Path to the input xml data file
    - Output:   
        - 'components_df': pandas-dataframe including all components
        - 'relations_df': pandas-dataframe indluding all relations
    """
    data = parse_xml_ET(filename) # parse the xml file
    root = data.getroot() # get the root of the tree

    # set up empty dataframes for the components and the relations
    components_df = pd.DataFrame()
    relations_df = pd.DataFrame()

    # add all of the different components to the compoments dataframe
    for component in root.iter('component'):
        comp_dic = component.attrib
        comp_df = pd.DataFrame(comp_dic, index=[0])
        components_df = pd.concat([components_df,comp_df], ignore_index=True)

    for relation in root.iter('relation'):
        rel_dict = relation.attrib
        rel_df = pd.DataFrame(rel_dict, index = [0])
        relations_df = pd.concat([relations_df, rel_df], ignore_index=True)

    return components_df, relations_df

    