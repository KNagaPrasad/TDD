class SparseMatrix:
    def __init__(self, number_rows, number_cols):
        self.number_rows = number_rows
        self.number_cols = number_cols
        self.data = {}  


    def set(self, row, col, value):
        if row < 0 or row >= self.number_rows:
            raise ValueError("Row is out of bound")
        if col < 0 or col >= self.number_cols:
            raise ValueError("Column is out of bound")
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]
        
    def get(self, row, col):
        for key, val in self.data.items():
            if key == (row, col):
                return val
        return 0

    def recommend(self, user_vector):
        if len(user_vector) != self.number_cols:
            raise ValueError("The size of User vector does not match with matrix col")
        result = [0] * self.number_rows
        for (row, col), value in self.data.items():
            mat_product = value * user_vector[col]
            result[row] = result[row] + mat_product
        return result

    def add_movie(self, matrix):
        if self.number_rows != matrix.number_rows or self.number_cols != matrix.number_cols:
            raise ValueError("Dimensions of matrix do not match")
        for (row, col), value in matrix.data.items():
            self.set(row, col, self.get(row, col) + value)
    
    def to_dense(self):
        dense_matrix  = [[0] * self.number_cols for _ in range(self.number_rows)]
        for row in range(self.number_rows):
            for col in range(self.number_cols):
                if (row, col) in self.data:
                    dense_matrix[row][col] = self.data[(row, col)]
                else:
                    dense_matrix[row][col] = 0

        return dense_matrix

#hiii
#hello