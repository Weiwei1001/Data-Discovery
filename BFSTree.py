from summed import *

class TreeNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.children = []
        self.parent = parent


class BFSTree:
    def __init__(self):
        self.root = None
        self.CFDS = None
        self.res = {}
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
                    CFD = (tuple(current_node_v),tuple(child_v))
                    CFDS.append(CFD)
                    if CFD not in self.res:
                        def get_OX(CFD):
                            index1 = CFD[0]
                            index2 = CFD[1]
                            print("index:")
                            print(CFD)
                            print(index1)
                            print(index2)
                        self.res[CFD] = get_OX(CFD)

                    # CFDS.add((tuple(current_node.value), tuple(child.value)))

        def remove_duplicates(input_list):
            seen = set()
            output_list = []
            for item in input_list:
                if item not in seen:
                    output_list.append(item)
                    seen.add(item)
            return output_list
        self.CFDS = remove_duplicates(CFDS)
        # print(CFDS)
        # print(len(CFDS))





