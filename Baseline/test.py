import re
from mapping import mapping_dict
from mapping import key_mapping_dict
def process_text(text):
    pattern = r'(\d+)\. If the column "(.*?)" is (.*?), then the column "(.*?)" (?:must be|can be either|is likely|could be) (' \
              r'.*?)\.'
    matches = []
    unmatched_lines = []

    for line in text.split('\n'):
        match = re.match(pattern, line)
        if match:
            number, column1, values1, column2, values2 = match.groups()

            # Process the 'values1' and 'values2' to split on 'or' if needed
            dict1 = {column1: values1.replace('"', '').split(' or ')}
            dict2 = {column2: [val.strip() for val in values2.replace('"', '').split(' or ')]}

            matches.append((dict1, dict2))
        else:
            unmatched_lines.append(line)

    return matches, unmatched_lines

# Example usage



# Example text input
example_text = """1. If the column "relationship" is "Husband", then the column "sex" must be "Male".
2. If the column "relationship" is "Wife", then the column "sex" must be "Female".
3. If the column "marital-status" is "Married-civ-spouse" or "Married-AF-spouse", then the column "relationship" could be "Husband" or "Wife".
4. If the column "marital-status" is "Never-married", then the column "relationship" cannot be "Husband" or "Wife".
5. If the column "workclass" is "Without-pay" or "Never-worked", then the column "hours-per-week" must be 0.
6. If the column "education" is "Preschool", then the column "education-num" is likely to be lower than others.
7. If the column "native-country" is not "United-States", then the column "race" is likely not "White".
8. If the column "class" is ">50K", then the column "hours-per-week" is likely higher than the median value.
9. If the column "occupation" is "Armed-Forces", then the column "sex" is likely to be "Male".
10. If the column "marital-status" is "Divorced" or "Separated", then the column "relationship" is likely not "Husband" or "Wife"."""

# Process the example text
processed_text, unmatch = process_text(example_text)
print(processed_text)
# for centence in unmatch:
#     print(centence)

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
    second_unmatch_mapped_data = []
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
                second_unmatch_mapped_data.append(mapped_item)


    return second_mapped_data, second_unmatch_mapped_data







# 使用函数
mapped_data, unmatch = double_map_data(processed_text,mapping_dict,key_mapping_dict)
print(mapped_data)
# print(unmatch)
