from BFSTree import *
from summed import summed
# def find_CFD(OX, X, Y, k):
#     if k >= 2:
#         itn = 2
#     else:
#         itn = 1
#
#     for i in range(1, itn + 1):
#         # First check for CFDs with added variables
#         for qi in Q:
#             if all(val in OX for val in qi):
#                 if M(xi, yi) >= tau:
#                     phi = (X, A)  # Replace A with the actual attribute name
#                     CL.append(phi)
#                     OX = [val for val in OX if val != xi]
#
#         if CL:
#             break
#
#     return OX
#
#
# def generate_CFDs(Relation_R, current_level_k):
#     CL = []
#     G = {}
#
#     for X in level_k:
#         marked_edge = find_marked_edge(X, Y)  # Implement this function
#         if len(π_X) == len(π_Y):
#             unmark_edge(X, Y)
#             remove_supersets_from_G(X, Y)
#         else:
#             OX = subsumed_Xi
#             VX = list(set(X) - set(OX))
#             OX_prime = find_CFD(OX, X, Y, k)
#             if OX_prime:
#                 G[(X_prime, Y_prime, Q, P)] = (VX, OX_prime)
#
#     if k >= 2 and not G:
#         return CL
#
#     return CL
#

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

def generate_CFDs(Relation_R, current_level_k, level_n, ):
    CL = []
    G = {}
    for k in level_n:
        print(k)

def main():
    Tree = BFSTree()
    Tree.generate_combination_tree(3)
    matrix = [[0, 0, 1, 1, 2, 2], [1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1]]
    result = create_value_index_dict(matrix)

    print(result)
    combined_result = summed(result, 0, 1)
    print(combined_result)

    # for row in result:
    #     print(row)
    # tree = Node(-1)



if __name__ == '__main__':
    main()

