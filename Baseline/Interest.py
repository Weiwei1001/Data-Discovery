class Interest:
    def __init__(self, threshold):
        self.threshold = threshold
    def support(self, X, Y):
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
        # print(score)
        # print("*"*80)
        if score >= self.threshold:
            return True
        return False




#
# test = Interest(0.5)
# test.support(1,2)