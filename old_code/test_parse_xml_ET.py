from old_code.xml_to_dataframe import xml_to_dataframe


filename = 'Sample_Data\model_matching_test_1.rexs'

components_df,relations_df = xml_to_dataframe(filename)
print(components_df)
print(relations_df)

