import re
from mapping import mapping_dict
from mapping import key_mapping_dict
def process_text(text):
    # pattern = r'(\d+)\. If the column "(.*?)" is (.*?) the column "(.*?)" (?:must be|can be either|is less likely|is likely|could be|would likely) ('r'.*?)\.'
    pattern = r'(\d+)\. If the column "(.*?)" is (.*?) the column "(.*?)" (?:must be|can be either|is less likely|is likely|could be|would likely) (.*)$'

    matches = []
    unmatched_lines = []

    for line in text.split('\n'):
        match = re.match(pattern, line)
        if match:
            number, column1, values1, column2, values2 = match.groups()
            # print(values2)
            matches1 = re.findall(r'"(.*?)"', values1)
            matches2 = re.findall(r'"(.*?)"', values2)
            # Process the 'values1' and 'values2' to split on 'or' if needed
            dict1 = {column1: matches1}
            # dict2 = {column2: [val.strip() for val in values2.replace('"', '').split(' or ')]}
            dict2 = {column2:matches2}
            # print(matches2)
            # print([val.strip() for val in values2.replace('"', '').split(' or ')])
            matches.append((dict1, dict2))

        else:

            unmatched_lines.append(line)

    return matches, unmatched_lines

# Example usage
# Process the example text
example_text = """
1. If the column "relationship" is "Husband", then the column "sex" must be "Male".
2. If the column "relationship" is "Wife", then the column "sex" must be "Female".
3. If the column "occupation" is "Armed-Forces", then the column "native-country" is likely to be "United-States".
4. If the column "workclass" is "Without-pay" or "Never-worked", then the column "capital-gain" and "capital-loss" would likely be "0".
5. If the column "education" is "Preschool", then the column "age" is likely to be less than "18".
6. If the column "class" is ">50K", then the column "education-num" is likely to be higher, probably above the average value "11.0".
7. If the column "workclass" is "Federal-gov" or "Local-gov" or "State-gov", then the column "native-country" is likely to be "United-States".
8. If the column "hours-per-week" is less than "20", then the column "workclass" could be "Without-pay" or "Never-worked".
9. If the column "age" is greater than "65", the column "workclass" is likely to be "Without-pay" or "Self-emp-inc".
10. If the column "native-country" is not "United-States", then the column "race" is less likely to be "White".
11. If the column "relationship" is "Own-child", then the column "age" is likely to be less than "18".
12. If the column "education" is "Doctorate" or "Prof-school", then the column "class" is likely to be ">50K".
13. If the column "workclass" is "Self-emp-inc", then the column "capital-gain" is likely to be higher than the average "2143.6".
14. If the column "education" is "HS-grad", then the column "education-num" is likely to be around "13.0".
15. If the column "relationship" is "Not-in-family", the person is likely to work more hours per week, possibly more than the average "36.4".
16. If the column "native-country" is "India", then the column "race" is likely to be "Asian-Pac-Islander".
17. If the column "occupation" is "Exec-managerial" or "Prof-specialty", then the column "class" is likely to be ">50K".
18. If the column "relationship" is "Unmarried" or "Divorced", then the column "marital-status" could be "Divorced" or "Separated".
19. If the column "class" is "<=50K", then the column "capital-loss" is likely to be higher than the average "0.0".
20. If the column "sex" is "Female" and the column "relationship" is "Unmarried", then the column "marital-status" is likely to be "Never-married" or "Divorced".
"""
processed_text, unmatch = process_text(example_text)
for centence in processed_text:
    print(centence)
# print(processed_text)
for centence in unmatch:
    print(centence)
print("*"*100)


def double_map_data(data, mapping_dict, new_mapping_dict):
    first_mapped_data = []

    # 第一次映射: 使用mapping_dict映射值
    for item in data:
        mapped_item = {}
        for dict_pair in item:
            for key, values in dict_pair.items():
                if key in mapping_dict:
                    mapping = mapping_dict[key]
                    if isinstance(mapping, dict):
                        # 映射字典值为字典类型，进行键值映射
                        mapped_values = [mapping.get(value, value) for value in values]
                        mapped_item[key] = mapped_values
                    else:
                        # 映射字典值为连续值，不进行映射
                        mapped_item[key] = values
                else:
                    # 映射字典中没有这个键，保留原始值
                    mapped_item[key] = values
        first_mapped_data.append(mapped_item)

    # 第二次映射: 使用new_mapping_dict映射键
    second_mapped_data = []
    second_mapped_data_unmatch = []
    for item in first_mapped_data:
        mapped_item = {}
        for key, values in item.items():
            if key in new_mapping_dict:
                # 使用新的映射规则
                mapped_key = new_mapping_dict[key]
                mapped_item[mapped_key] = values
                second_mapped_data.append(mapped_item)
            else:
                # 映射字典中没有这个键，保留原始键和值
                mapped_item[key] = values
                second_mapped_data_unmatch.append(mapped_item)


    return second_mapped_data, second_mapped_data_unmatch
# 使用函数



print(unmatch)
print("*"*80+"unmatch"+"*"*80)
mapped_data, unmatch = double_map_data(processed_text,mapping_dict,key_mapping_dict)
for ele in mapped_data:
    print(ele)
print("*"*100)
for ele in unmatch:
    print(ele)



