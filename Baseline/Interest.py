class Interest:
    def __init__(self, threshold):
        self.threshold = threshold
        self.chi_squre_v = {}
    def support(self, X, Y):
        # print("*"*100)
        # print(X)
        # print(Y)

        keyX = list(X.keys())
        keyY = list(Y.keys())
        # print(keyX)
        # print(keyY)
        numerator = 0
        denominator = 0
        for key in keyY:
            denominator = denominator + len(Y[key])
            # print(X[key[0]])
            # print(Y[key])
            if key[0] not in X:
                continue
            if X[key[0]] == Y[key]:
                numerator = numerator + len(Y[key])

        # print(numerator)
        score = float(numerator / denominator)
        # print("Interest:")
        # print(score)
        # print("*"*80)
        if score >= self.threshold:
            return True, score
        return False,0

    def chi_squre(self, X, A, Y, CFD, seq):

        print("*"*80)

        # self.chi_squre_v[tuple(CFD)] = []
        CFD_0 = tuple(CFD[0])
        CFD_1 = tuple(CFD[1])
        self.chi_squre_v[(CFD_0,CFD_1)] = []
        print(CFD)
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

            VX = len(X[Key_X])
            _VX = N - VX
            VA = len(A[Key_A])
            _VA = N - VA
            XA = len(Y[tuples])
            _VAVX = 0
            VA_VX = 0
            _VA_VX = 0
            index_X = tuples[0]
            index_A = tuples[1]
            for ele in Y:
                # VX
                if ele[0] == index_X:
                    # VAVX
                    if ele[1] == index_A:
                        continue
                    # _VAVX
                    else:
                        _VAVX = _VAVX + len(Y[ele])
                # _VX
                else:
                    if ele[1] ==  index_A:
                        VA_VX = VA_VX + len(Y[ele])
                    else:
                        _VA_VX = _VA_VX + len(Y[ele])

            def calculate_statistic(VX, VA, _VX, _VA, _VXVA, VX_VA, _VX_VA, VXVA, N):
                """
                Calculate the statistic based on the provided formula and inputs.
                :param VX: Input variable
                :param VA: Input variable
                :param _VX: Input variable
                :param _VA: Input variable
                :param _VXVA: Input variable
                :param VX_VA: Input variable
                :param _VX_VA: Input variable
                :param VXVA: Input variable
                :param N: Input variable (should not be zero)
                :return: Calculated statistic
                """
                if N == 0 or VX * VA == 0 or _VX * VA == 0 or VX * _VA == 0 or _VX * _VA == 0:
                    raise ValueError("Division by zero encountered in the calculation.")

                term1 = (((VX * VA) / N) - VXVA) ** 2 / ((VX * VA) / N)
                term2 = (((_VX * VA) / N) - _VXVA) ** 2 / ((_VX * VA) / N)
                term3 = (((VX * _VA) / N) - VX_VA) ** 2 / ((VX * _VA) / N)
                term4 = (((_VX * _VA) / N) - _VX_VA) ** 2 / ((_VX * _VA) / N)

                return term1 + term2 + term3 + term4
            print(VX, VA, _VX, _VA, VA_VX, _VAVX, _VA_VX, XA, N)
        # print(self.chi_squre_v)