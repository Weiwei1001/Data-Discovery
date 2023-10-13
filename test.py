class TreeNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.children = []
        self.parent = parent

class CombinationTree:
    def __init__(self):
        self.root = None

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

if __name__ == "__main__":
    combination_tree = CombinationTree()
    n = int(input("请输入一个数字 n: "))
    if n < 0:
        print("n必须为非负整数")
    else:
        combination_tree.generate_combination_tree(n)
        combination_tree.print_tree()
