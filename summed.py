def summed(matrix, row1, row2):
    result = {}  # 初始化结果字典

    # 获取给定行的值字典
    value_dict1 = matrix[row1]
    value_dict2 = matrix[row2]

    # 遍历第一行的键值对
    for key1, value1 in value_dict1.items():
        # 遍历第二行的键值对
        for key2, value2 in value_dict2.items():
            # 找到两行中相同键的值的交集
            common_values = list(set(value1) & set(value2))
            if common_values:
                new_key = (key1, key2)
                result.setdefault(new_key, []).extend(common_values)

    return result

result = [
    {0: [0, 1], 1: [2, 3], 2: [4, 5]},
    {0: [0, 1, 2, 3], 1: [4, 5]},
    {0: [0, 1, 2], 1: [3, 4, 5]}
]

combined_result = summed(result, 0, 1)
print(combined_result)
