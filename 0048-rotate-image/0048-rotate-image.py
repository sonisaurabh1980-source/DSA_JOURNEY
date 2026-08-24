class Solution(object):
    def rotate(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(len(matrix)-i-1):
                matrix[i][j+i+1],matrix[j+1+i][i]=matrix[j+1+i][i],matrix[i][j+1+i]
        