from summed import *

class TreeNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.children = []
        self.parent = parent


class BFSTree:
    def __init__(self, raw):
        self.root = None
        self.CFDS = None
        self.res = {}
        self.raw = raw
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
    def bfs_traversal(self):
        if self.root is None:
            return

        queue = [self.root]  # 使用队列来进行BFS
        CFDS = []
        while queue:

            current_node = queue.pop(0)
            # print(current_node.value)  # 处理当前节点的值

            # 将当前节点的子节点加入队列
            for child in current_node.children:
                queue.append(child)
                current_node_v = current_node.value
                child_v = child.value
                if(len(current_node.value) != 0):
                    CFD = (set(current_node_v),set(child_v))
                    CFDS.append(CFD)
                    # if CFD not in self.res:
                    def get_OX(CFD):
                        index1 = CFD[0]
                        index2 = CFD[1]
                        print("index:")
                        print(CFD)
                        # print(index1)
                        # print(index2)
                        # #((0,), (0, 1))
                        # print(type(index1))
                        X = self.res[tuple(index1)]
                        Y = self.res[tuple(index2.difference(index1))]
                        #first find if the summed list is in res
                        if tuple(index2) in self.res:
                            return self.res[tuple(index2)]
                        #if in , just get it

                        #if not, generate one and store the into the res

                        return summed(X,Y)

                    self.res[tuple(child_v)] = get_OX(CFD)

                    # CFDS.add((tuple(current_node.value), tuple(child.value)))

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
        print(CFDS)
        print(len(CFDS))
        print(len(self.res))
        for item in self.res:
            print(item, self.res[item])





