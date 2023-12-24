from BFSTree import *
from mapping import *

from Openai.chat import OpenAIInterface
from Openai.chat import prompt
from summed import summed


def create_value_index_dict(matrix):
    result = []
    for row in matrix:
        value_dict = {}
        for index, value in enumerate(row):
            if value in value_dict:
                value_dict[value].append(index)
            else:
                value_dict[value] = [index]
        result.append(value_dict)
    return result


def main():


    # 0 1 2
    # 0 0 0
    # 0 0 0
    # 1 0 0
    # 1 1 0
    # 2 1 1
    # 2 1 1

    matrix, continue_data = mapData('/Users/xuzhongwei/Berkeley/DataDiscovery/adult/adult.data')
    # matrix = [[0, 0, 1, 1, 2, 2], [0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 1]]
    # openai_interface = OpenAIInterface(200)
    #
    # print(continue_data)
    # analysis = openai_interface.analysis_data(continue_data)
    # print("analysis:")
    # print(analysis)
    #
    # completion_result = openai_interface.send_completion_job(analysis,
    #                                                          prompt_template=prompt)
    # print(completion_result)
    #
    # result = create_value_index_dict(matrix)
    # print(result)


    Tree = BFSTree(matrix, 0.3)
    Tree.generate_combination_tree(9)
    # Tree.generate_combination_tree(3)
    # Tree.print_res()
    # Tree.print_tree()
    # print(matrix)
    # Tree.print_res()
    Tree.bfs_traversal()
    # print(len(matrix))
    # print(len(matrix[0]))


if __name__ == '__main__':
    main()

