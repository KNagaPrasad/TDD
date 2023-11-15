import pytest
from sparse_recommender import SparseMatrix

def test_set_get_value():
    matrix = SparseMatrix(4, 4)
    matrix.set(1, 0, 1)
    matrix.set(0, 1, 4)
    assert matrix.get(1, 0) == 1
    assert matrix.get(0, 1) == 4


def test_incorrect_set():
    matrix = SparseMatrix(4, 4)
    with pytest.raises(ValueError):
        matrix.set(4, 2, 8)   

def test_recommend():
    matrix = SparseMatrix(4, 4)
    matrix.set(0, 0, 2)
    matrix.set(1, 1, 2)
    matrix.set(2, 2, 3)
    matrix.set(3, 3, 3)
    user_vector = [0.5, 0, 0, 1]
    recommendations = matrix.recommend(user_vector)
    assert recommendations == [1.0, 0, 0, 3] 

def test_incorrect_recommendvector():
    matrix = SparseMatrix(4, 4)
    user_vector = [0.5, 2, 0.8]  
    with pytest.raises(ValueError):
        matrix.recommend(user_vector)

def test_add_movie():
    matrix_1 = SparseMatrix(4, 4)
    matrix_1.set(0, 0, 1)
    matrix_1.set(1, 1, 2)
    matrix_1.set(2, 2, 3)
    matrix_1.set(3, 3, 4)

    matrix_2 = SparseMatrix(4, 4)
    matrix_2.set(0, 0, 2)
    matrix_2.set(2, 2, 1)

    matrix_1.add_movie(matrix_2)
    assert matrix_1.get(0, 0) == 3   
    assert matrix_1.get(1, 1) == 2 
    

def test_matrix_conflict():
    matrix_1 = SparseMatrix(2, 2)
    matrix_2 = SparseMatrix(3, 4) 
    with pytest.raises(ValueError):
        matrix_1.add_movie(matrix_2)

def test_to_dense():
    matrix = SparseMatrix(4, 4)
    matrix.set(0, 0, 6)
    matrix.set(1, 1, 7)
    matrix.set(2, 2, 8)

    dense_matrix = matrix.to_dense()
    assert dense_matrix == [[6, 0, 0, 0], [0, 7, 0, 0], [0, 0, 8, 0],[0, 0, 0, 0]]

def test_incorrect_dense_conversion():
    matrix = SparseMatrix(4, 4)
    matrix.set(2, 2, 4.5)
    matrix.set(2, 3, 5)
    try:
        matrix.to_dense()
        assert True
    except ValueError as e:
        assert str(e) == "Invalid data"

if __name__ == "__main__":
    pytest.main()