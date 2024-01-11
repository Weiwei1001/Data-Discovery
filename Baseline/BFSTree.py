from summed import *
from Interest import *
from itertools import combinations
from mapping import *

class TreeNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.children = []
        self.parent = parent


class BFSTree:
    def __init__(self, raw, threshold):
        self.root = None
        self.CFDS = None
        self.FDS = {}
        self.res = {}
        self.raw = raw
        self.chi_squre_v = {}
        self.interest = Interest(threshold)
        self.condition = {}
        self.score = {}
        self.llm_suggestion = []
    def generate_combination_tree(self, n):
        # 创建根节点
        self.root = TreeNode(set())

        def generate_combinations(node, remaining_values):
            if len(node.value) < n:
                for value in remaining_values:
                    # 生成新的子节点
                    child_node = TreeNode(node.value | {value}, parent=node)
                    node.children.append(child_node)

                    # 递归生成更多子节点
                    generate_combinations(child_node, remaining_values - {value})

        generate_combinations(self.root, set(range(n)))

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
        # # self.res = [{0: [0, 1], 1: [2, 3], 2: [4, 5]}, {0: [0, 1, 2], 1: [3, 4, 5]}, {0: [0, 1, 2, 3], 1: [4, 5]}]
        # print("*"*30)
        # print(create_value_index_dict(self.raw))
        i = 0
        for data_dict in create_value_index_dict(self.raw):
            key = (i,)  # 使用单元素元组表示索引
            self.res[key] = data_dict
            i = i + 1

    def print_tree(self, node=None, depth=0):
        if node is None:
            node = self.root
        # 打印树结构
        print("  " * depth + str(node.value))
        for child in node.children:
            self.print_tree(child, depth + 1)

    def print_res(self):
        print(self.res)

    def Rule1(self, X, Y):
        FDKeys = list(self.FDS.keys())
        for FD in FDKeys:
            if set(FD[1]).difference(set(FD[0])) == Y:
                return set(FD[0]).issubset(X)
        return False

    def Rule2(self):
        return False

    def Rule3(self,CFDS, CFD):
        # FDKeys = list(self.FDS.keys())
        X = set(CFD[0])
        Y = set(CFD[1]).difference(X)

        for FD in CFDS:
            if set(FD[0]).issubset(X) and Y == set(FD[1]).difference(set(FD[0])):
                return False

        return True
    def chi_squre(self, X, A, Y, CFD, seq):

        # print("*"*80)

        # self.chi_squre_v[tuple(CFD)] = []
        CFD_0 = tuple(CFD[0])
        CFD_1 = tuple(CFD[1])
        self.chi_squre_v[(CFD_0,CFD_1)] = []
        print(CFD)
        print(seq)
        # print(type(CFD))
        # # print(set(CFD[1]).difference(set(CFD[0])))
        print(X)
        print(A)
        print(Y)
        N = 0
        for tuples in X:
            N = N + len(X[tuples])

        for tuples in Y:
            # candidate = list(Y[])
            # print(tuple[0])
            candidate = []
            if isinstance(tuples, type(tuples[0])):
                candidate = (list(tuples[0]))
            else:
                candidate.append(tuples[0])
            candidate.append(tuples[1])

            def reorder_arrays(arr1, arr2, arr3):
                """
                Reorder the elements of the third array based on the order of elements in the first two arrays.
                :param arr1: First array (reference order)
                :param arr2: Second array (new order)
                :param arr3: Third array (to be reordered)
                :return: New reordered array
                """
                # Creating a mapping from elements of arr1 to their indices
                index_map = {element: index for index, element in enumerate(arr1)}

                # Reordering arr3 based on the order of elements in arr2
                reordered_arr3 = [arr3[index_map[element]] for element in arr2]

                return reordered_arr3
            seq_key = reorder_arrays(list(CFD[1]),seq,candidate)
            # print(seq_key)
            # Key_A, Key_X = find_difference_and_update(CFD,candidate)
            Key_A = seq_key[len(seq_key)-1]
            seq_key.pop()
            Key_X = seq_key
            if len(Key_X) > 1:
                Key_X = tuple(Key_X)
            else:
                Key_X = Key_X[0]
            print("*"*40)
            print(X[Key_X])
            print(A[Key_A])
            print(Y[tuples])

            if set(X[Key_X]).issubset(set(A[Key_A])):
                self.chi_squre_v[(CFD_0,CFD_1)].append(X[Key_X])


        def find_subset_key(dictionary, list_to_check, tuple_to_use):
            # Iterate over the length of the tuple
            print("QQQQQ:")

            print(dictionary)
            print(list_to_check)
            print(tuple_to_use)
            for r in range(1, len(tuple_to_use) + 1):
                # Generate all combinations of the given length
                for combo in combinations(tuple_to_use, r):
                    # print(combo)
                    # Check if the combination is in the dictionary
                    if combo in dictionary:
                        # print(dictionary[combo])
                        #     # Get the values from the dictionary

                        values = list(dictionary[combo].values())
                        print(combo)
                        print(values)
                        #     # Check if each list in list_to_check is a subset of any value in values
                        if all(any(set(sublist).issubset(set(value)) for value in values) for sublist in
                               list_to_check):
                            #         # If all lists are subsets, return the key (combination)
                            return combo
            # If no matching combination is found, return None
            return None

        comb = find_subset_key(self.res,self.chi_squre_v[(CFD_0, CFD_1)] , CFD_0)
        # print(CFD_0,CFD_1)
        self.condition[(CFD_0,CFD_1)] = [comb]

    def find_condition2(self, X, A, Y, CFD, seq):
        print(Y)
        print(CFD)
        print(X)
        print(A)
        for ele in X:
            for ele2 in A:
                if set(X[ele]).issubset(set(A[ele2])):
                    key_Y = (ele,)+(ele2,)
                    Key_X = ele
                    Key_A = ele2





    def find_condition(self, X, A, Y, CFD, seq):

        # print("*"*80)

        # self.chi_squre_v[tuple(CFD)] = []
        CFD_0 = tuple(CFD[0])
        CFD_1 = tuple(CFD[1])
        # print(CFD)
        self.chi_squre_v[(CFD_0,CFD_1)] = []
        for Key_X in X:
            for Key_A in A:
                if set(X[Key_X]).issubset(set(A[Key_A])):
                    self.chi_squre_v[(CFD_0,CFD_1)].append(X[Key_X])
                    def find_subset_key(dictionary, list_to_check, tuple_to_use):
                        # print(list_to_check)
                        for r in range(1, len(tuple_to_use) + 1):
                            # Generate all combinations of the given length
                            for combo in combinations(tuple_to_use, r):
                                # Check if the combination is in the dictionary
                                if combo in dictionary:
                                    #     # Get the values from the dictionary

                                    # values = list(dictionary[combo].values())
                                    keys = list(dictionary[combo].keys())
                                    # print("keys:")
                                    # print(keys)
                                    # print(values)
                                    #     # Check if each list in list_to_check is a subset of any value in values
                                    # if all(any(set(sublist).issubset(set(value)) for value in values) for sublist in
                                    #        list_to_check):
                                    #     #         # If all lists are subsets, return the key (combination)
                                    #     return combo
                                    for sublist in list_to_check:
                                        is_subset = False
                                        for key in keys:
                                            if set(sublist).issubset(set(dictionary[combo][key])):
                                                # 如果 sublist 是 value 的子集，标记为 True 并退出内层循环
                                                # print(key)
                                                self.condition[(CFD_0, CFD_1)] = [key]
                                                is_subset = True
                                                break
                                        if not is_subset:
                                            # 如果有任何一个 sublist 不是任何 value 的子集，则立即退出
                                            break
                                        else:
                                        # 只有当所有 sublist 都是某个 value 的子集时，才执行以下代码
                                        #     print(key)
                                            self.condition[(CFD_0, CFD_1)].append(combo)
                                            # print("ppp")
                                            # print(self.condition[(CFD_0, CFD_1)])

                                            return combo

                        # If no matching combination is found, return None
                        return None

                    comb = find_subset_key(self.res,self.chi_squre_v[(CFD_0, CFD_1)] , CFD_0)









    def bfs_traversal(self):
        # print("*"*100)
        if self.root is None:
            return

        queue = [self.root]  # 使用队列来进行BFS
        CFDS = []
        CFDS_res = []
        while queue:
            current_node = queue.pop(0)
          # 处理当前节点的值
            for child in current_node.children:
                queue.append(child)
                current_node_v = current_node.value
                child_v = child.value
                #not the empty decide the single ele
                if(len(current_node.value) != 0):
                    CFD = (set(current_node_v),set(child_v))
                    # print(CFDS)
                    if CFD not in CFDS_res:

                        CFDS_res.append(CFD)
                        # if CFD not in self.res:
                        def get_OX(CFD):
                            index1 = CFD[0]
                            index2 = CFD[1]


                            X = self.res[tuple(index1)]
                            Y = self.res[tuple(index2.difference(index1))]

                            if tuple(index2) in self.res:

                                seq = list(index1)
                                seq.append(list(index2.difference(index1))[0])
                                return seq, self.res[tuple(index2)]

                            # if in , just get it

                            # if not, generate one and store the into the res
                            # print("kkkkk")
                            # print("*"*700)
                            return index2, summed(X, Y)

                        def isFD(X, Y):
                            tempX = list(X.values())
                            tempY = list(Y.values())
                            if len(X) != len(Y):
                                return False
                            for i in range(len(tempX)):
                                if tempY[i] != tempX[i]:
                                    return False

                            return True

                        if not self.Rule3(CFDS,CFD):
                            continue
                        seq, candidate = get_OX(CFD)
                        isinterest, score = self.interest.support(self.res[tuple(current_node_v)], candidate)
                        if isinterest:
                            CFDS.append(CFD)
                            self.score[ (frozenset(CFD[0]), frozenset(CFD[1]))]= score
                            # print(score)

                        A = set(child_v).difference(set(current_node_v))
                        # print("*" * 800)
                        self.find_condition(self.res[tuple(current_node_v)], self.res[tuple(A)], candidate,CFD,list(seq))
                        # self.interest.chi_squre(self.res[tuple(current_node_v)], self.res[tuple(A)], candidate, CFD,list(seq))
                        # self.interest.support(self.res[tuple(current_node_v)],candidate)
                        self.res[tuple(child_v)] = candidate
                        if isFD(self.res[tuple(current_node_v)], candidate):
                            if not self.Rule1(current_node_v, child_v.difference(current_node_v)):
                                self.FDS[(tuple(current_node_v), tuple(child_v))] = candidate



        def remove_duplicates(input_list):
            seen = set()
            output_list = []
            for item in input_list:
                if item not in seen:
                    output_list.append(item)
                    seen.add(item)
            return output_list
        # print(CFDS)
        # print("pp")
        # self.CFDS = remove_duplicates(CFDS)

        print("*"*100)
        print("*"*45, "result","*"*45)
        print("*"*100)
        #check for CFDS

        print(CFDS)
        # print(self.res)
        print(len(CFDS))
        # print(len(self.res))
        # for item in self.res:
        #     print(item, self.res[item])
        # print(self.condition)
        print(len(self.score))
        # 假设 self.score 已经定义并包含数据
        # 对字典项按照score值排序，并取前20个
        sorted_scores = sorted(self.score.items(), key=lambda item: item[1], reverse=True)

        # 打印出来
        for pair in sorted_scores:
            print(pair)

        print("Condition:")
        # print(self.condition)
        for ele in self.condition:
            # print(ResultMap(self.condition[ele],ele))
            print(ele)
            print(self.condition[ele])












