# import re
# from mapping import *
#
# def process_text(text):
#
#     unmatched_lines = []
#
#     # 正则表达式: 用于匹配包含一个或多个条件的句子
#     pattern = r'(\d+)\. If the column "(.*?)" is "(.*?)"( and "(.*?)" is "(.*?)")*?, then the column "(.*?)" (must be|is likely to be) "(.*?)"\.'
#     # pattern = r'(\d+)\. If the column "(.*?)" is "(.*?)"( and "(.*?)" is "(.*?)")? then the column "(.*?)" (?:must be|can be either|is less likely|is likely|could be|would likely) (.*?)\.$'
#     results = []
#     for line in text.split('\n'):
#         matches = []
#         match = re.match(pattern, line)
#         if match:
#             number = match.group(1)  # 提取编号
#             conditions = re.findall(r'"(.*?)" is "(.*?)"', line)  # 提取所有条件
#             # print(conditions)
#             result_column, condition_type, result_value = match.groups()[-3:]  # 提取结果部分
#
#             # 构建结果元组
#             result = [number]
#             # for col, val in conditions:
#             #     result.extend([col, val])
#             # result.extend([result_column, result_value])
#
#             matches.append(result)  # 将结果添加为元组
#             matches.append(tuple(conditions))
#             matches.append(tuple([result_column,result_value]))
#             # print(matches)
#             results.append(matches)
#         else:
#             unmatched_lines.append(line)
#     print(len(results))
#     return results, unmatched_lines
#
#
# example_text = '3. If the column "marital-status" is "Married-civ-spouse" and "relationship" is "Husband" and "xzw" is "hhhh", then the column "sex" must be "Male".'
# example_text_2 = """1. If the column "relationship" is "Husband", then the column "sex" must be "Male".
# 2. If the column "marital-status" is "Never-married", then the column "relationship" is likely to be "Not-in-family".
# 3. If the column "marital-status" is "Married-civ-spouse" and "relationship" is "Husband", then the column "sex" must be "Male".
# 4. If the column "relationship" is "Wife", then the column "sex" must be "Female".
# 5. If the column "marital-status" is "Married-civ-spouse" and "relationship" is "Wife", then the column "sex" must be "Female".
# 6. If the column "occupation" is "Armed-Forces", then the column "sex" is likely to be "Male".
# 7. If the column "marital-status" is "Divorced" or "Separated", then the column "relationship" is likely to be "Not-in-family".
# 8. If the column "native-country" is "Iran", then the column "race" is likely to be "Asian-Pac-Islander".
# 9. If the column "education" is "Preschool", then the column "education-num" is likely to be 1.
# 10. If the column "native-country" is "United-States", then the column "race" is likely to be "White".
# 11. If the column "marital-status" is "Widowed", then the column "relationship" is likely to be "Not-in-family" or "Unmarried".
# 12. If the column "education" is "Doctorate", then the column "education-num" must be 16.
# 13. If the column "occupation" is "Exec-managerial", then the column "workclass" is likely to be "Private" or "Self-emp-inc".
# 14. If the column "education" is "HS-grad", then the column "education-num" is likely to be 9.
# 15. If the column "workclass" is "Without-pay", then the column "class" is likely to be "<=50K".
# 16. If the column "occupation" is "Other-service", then the column "workclass" is likely to be "Private".
# 17. If the column "relationship" is "Own-child", then the column "marital-status" is likely to be "Never-married".
# 18. If the column "native-country" is "Cuba", then the column "race" is likely to be "White" or "Other".
# 19. If the column "workclass" is "Federal-gov", then the column "class" is likely to be ">50K".
# 20. If the column "education" is "Masters", then the column "education-num" must be 14."""
#
# processed_text, unmatch = process_text(example_text_2)
# for centence in processed_text:
#     print(centence)
# print("*"*100)
# # print(processed_text)
# # for centence in unmatch:
# #     print(centence)
#
#
#
#
#
#
#
# def map_attributes(key_mapping_dict, mapping_dict, inputs):
#     # Function to map single attributes
#     def map_single_attribute(attribute, value):
#         if attribute in mapping_dict and isinstance(mapping_dict[attribute], dict):
#             # Map the value using the provided dictionary, defaulting to value if not found
#             return key_mapping_dict[attribute], mapping_dict[attribute].get(value, value)
#         # If the attribute is not in the dictionary or it's marked as 'continuous'
#         return key_mapping_dict[attribute], value
#
#     mapped_outputs = []
#
#     for input_line in inputs:
#         record_id = input_line[0]
#         mapped_line = [record_id]
#
#         for attr_info in input_line[1]:
#             # print(attr_info)
#         # print("\n")
#             if isinstance(attr_info, tuple):  # It's a tuple of attribute info
#                 attr_key = attr_info[0]
#                 if isinstance(attr_info[1], tuple):
#         #             # Process each attribute in the tuple
#                     sub_attributes = [(map_single_attribute(attr_info[0], attr_info[1]))]
#                     mapped_line.append(tuple(sub_attributes))
#                 else:
#         #             # Process a single attribute
#                     mapped_line.append(map_single_attribute(attr_key, attr_info[1]))
#                     # print(map_single_attribute(attr_key, attr_info[1]))
#
#         # print("\n")
#         #         mapped_line.append(map_single_attribute(attr_info[0], attr_info[1]))
#
#         attr_info = input_line[2]
#
#         # sub_attributes = [(map_single_attribute(sub_attr[0], sub_attr[1])) for sub_attr in attr_info[1]]
#         sub_attributes = (map_single_attribute(attr_info[0], attr_info[1]))
#         # print((map_single_attribute(attr_info[0], attr_info[1])))
#         mapped_line.append(tuple(sub_attributes))
#         mapped_outputs.append(mapped_line)
#
#
#     return mapped_outputs
#
# mapped_result = map_attributes(key_mapping_dict, mapping_dict, processed_text)
# for item in mapped_result:
#     print(item)

from mapping import *


b = ((0,), (0, 1))
a = [(0,), 5]

b1 = ((8, 7), (8, 6, 7))
a1 = [(8,), 0]



def find_key_by_value_test(key_mapping_dict, value):
    # 在字典中查找给定值，并返回相应的键
    for key, val in key_mapping_dict.items():
        if val == value:
            return key
    # 如果值在字典中不存在，返回None
    return None


# key = find_key_by_value(key_mapping_dict, a[0][0])
# print(mapping_dict[key])
# key2 = find_key_by_value(mapping_dict[key],a[1])
# print(key2)
def ResultMap_test(a1,b1):
    string5 = "\""
    string6 = "\""
    for ele in b1[0]:
        string5 = string5 + find_key_by_value(key_mapping_dict, ele) + ", "
    for ele in b1[1]:
        string6 = string6 + find_key_by_value(key_mapping_dict, ele) + ", "
    # string6 = string5 + find_key_by_value(key_mapping_dict, b1[1][len(b1[1])-1]) + "\" "
    string5 = string5 + "\" "
    string6 = string6 + "\""
    string7 = find_key_by_value(key_mapping_dict, a1[1][0])
    string8 = find_key_by_value(mapping_dict[string7], a1[0])
    # print(string5)
    string1 = "If the column "
    string2 = " is equal to "
    string3 = ", then the column "
    string4 = "will decide the column "
    return string1 + string7 + string2 + string8 + string3 + string5 + string4 + string6
# print(mapping_dict[key][key2])




c = ((0,), (0, 2))
d = [5, (0,)]

# print(ResultMap_test(b,a))
print(ResultMap_test(d,c))

