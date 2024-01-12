from BFSTree import *
from mapping import *
from processing import *
from Openai.chat import OpenAIInterface, prompt_chat_complete
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
    #######################################################Processing data part######################################################
    matrix, continue_data = mapData('/Users/xuzhongwei/Berkeley/DataDiscovery/adult/adult.data')
    # matrix = [[0, 0, 1, 1, 2, 2], [0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 1]]
    #
    # continue_data = [['39', '50', '38', '53', '28', '37', '49', '52', '31', '42'],
    #                  ['77516', '83311', '215646', '234721', '338409', '284582', '160187', '209642', '45781', '159449'],
    #                  ['13', '13', '9', '7', '13', '14', '5', '9', '14', '13'],
    #                  ['2174', '0', '0', '0', '0', '0', '0', '0', '14084', '5178'],
    #                  ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    #                  ['40', '13', '40', '40', '40', '40', '16', '45', '50', '40']]

    #####################################################ChatGPT part#################################################################

    openai_interface = OpenAIInterface(200)

    print(continue_data)
    analysis = openai_interface.analysis_data(continue_data)

    suggestion = ""
    completion_result, messages = openai_interface.send_chat_completion_job_gpt4(analysis,
                                                                                prompt_template=prompt_chat_complete)
    suggestion = suggestion + completion_result

    for i in range(1):
        completion_result, messages = openai_interface.send_chat_completion_job_gpt4_continue(messages)
        suggestion = suggestion +"\n" +completion_result
    llm_suggest = get_llm_suggest(suggestion)
    print(llm_suggest)

    ###########################################################Build Tree part###############################################################

    Tree = BFSTree(matrix, 0.01)
    Tree.generate_combination_tree(9)
    Tree.llm_suggestion = llm_suggest

    Tree.bfs_traversal()


if __name__ == '__main__':
    main()
