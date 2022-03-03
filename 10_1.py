class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrx = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrx[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrx]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrx]))

result = Matrix([[10, 6, 2],
                [13, 5, 11],
                [18, 67, 81]],
                [[11, 9, 1],
                [15, 19, 23],
                [71, 1, 65]])

print(result.__add__())