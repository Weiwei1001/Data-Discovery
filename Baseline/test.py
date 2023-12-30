import re


def process_text(text):

    unmatched_lines = []

    # 正则表达式: 用于匹配包含一个或多个条件的句子
    pattern = r'(\d+)\. If the column "(.*?)" is "(.*?)"( and "(.*?)" is "(.*?)")*?, then the column "(.*?)" (must be|is likely to be) "(.*?)"\.'
    # pattern = r'(\d+)\. If the column "(.*?)" is "(.*?)"( and "(.*?)" is "(.*?)")? then the column "(.*?)" (?:must be|can be either|is less likely|is likely|could be|would likely) (.*?)\.$'
    results = []
    for line in text.split('\n'):
        matches = []
        match = re.match(pattern, line)
        if match:
            number = match.group(1)  # 提取编号
            conditions = re.findall(r'"(.*?)" is "(.*?)"', line)  # 提取所有条件
            # print(conditions)
            result_column, condition_type, result_value = match.groups()[-3:]  # 提取结果部分

            # 构建结果元组
            result = [number]
            # for col, val in conditions:
            #     result.extend([col, val])
            # result.extend([result_column, result_value])

            matches.append(result)  # 将结果添加为元组
            matches.append(tuple(conditions))
            matches.append(tuple([result_column,result_value]))
            # print(matches)
            results.append(matches)
        else:
            unmatched_lines.append(line)
    print(len(results))
    return results, unmatched_lines


example_text = '3. If the column "marital-status" is "Married-civ-spouse" and "relationship" is "Husband" and "xzw" is "hhhh", then the column "sex" must be "Male".'
example_text_2 = """1. If the column "relationship" is "Husband", then the column "sex" must be "Male".
2. If the column "marital-status" is "Never-married", then the column "relationship" is likely to be "Not-in-family".
3. If the column "marital-status" is "Married-civ-spouse" and "relationship" is "Husband", then the column "sex" must be "Male".
4. If the column "relationship" is "Wife", then the column "sex" must be "Female".
5. If the column "marital-status" is "Married-civ-spouse" and "relationship" is "Wife", then the column "sex" must be "Female".
6. If the column "occupation" is "Armed-Forces", then the column "sex" is likely to be "Male".
7. If the column "marital-status" is "Divorced" or "Separated", then the column "relationship" is likely to be "Not-in-family".
8. If the column "native-country" is "Iran", then the column "race" is likely to be "Asian-Pac-Islander".
9. If the column "education" is "Preschool", then the column "education-num" is likely to be 1.
10. If the column "native-country" is "United-States", then the column "race" is likely to be "White".
11. If the column "marital-status" is "Widowed", then the column "relationship" is likely to be "Not-in-family" or "Unmarried".
12. If the column "education" is "Doctorate", then the column "education-num" must be 16.
13. If the column "occupation" is "Exec-managerial", then the column "workclass" is likely to be "Private" or "Self-emp-inc".
14. If the column "education" is "HS-grad", then the column "education-num" is likely to be 9.
15. If the column "workclass" is "Without-pay", then the column "class" is likely to be "<=50K".
16. If the column "occupation" is "Other-service", then the column "workclass" is likely to be "Private".
17. If the column "relationship" is "Own-child", then the column "marital-status" is likely to be "Never-married".
18. If the column "native-country" is "Cuba", then the column "race" is likely to be "White" or "Other".
19. If the column "workclass" is "Federal-gov", then the column "class" is likely to be ">50K".
20. If the column "education" is "Masters", then the column "education-num" must be 14."""

processed_text, unmatch = process_text(example_text_2)
for centence in processed_text:
    print(centence)
# print("*"*100)
# # print(processed_text)
# for centence in unmatch:
#     print(centence)

