from typing import List

# This method takes a weighted digraph as a 2D List and outputs a
# 2D List of the shortest weighted path between vertices
def Floyd_Warshall(input_matrix:List[List[int]]) -> List[List[int|float]]:
    # Create constant variables
    infinity = float('infinity')
    vertex_num = len(input_matrix)
    # Create matrix where all values are infinity
    output_matrix = [[infinity for _ in range(vertex_num)] for _ in range(vertex_num)]
    # Set all non zero values to the output_matrix
    for i in range(0, vertex_num):
        for j in range(0, vertex_num):
            if input_matrix[i][j] != 0:
                output_matrix[i][j] = input_matrix[i][j]
    # Employ the algorithm for each vertex k
    for k in range(0, vertex_num):
        for i in range(0, vertex_num):
            for j in range(0, vertex_num):
                # Compare the current distance with adding the intermediate vertex k
                output_matrix[i][j] = min(output_matrix[i][j], output_matrix[i][k] + output_matrix[k][j])
    # Return the final matrix
    return output_matrix

#Test cases begin here

inf = float('infinity')

#Floyd_Warshall([[0,7,0,5],[0,2,0,0],[0,3,0,4],[1,0,0,0]]) should return [[6,7,inf,5],[inf,2,inf,inf],[5,3,inf,4],[1,8,inf,6]]
print(Floyd_Warshall([[0,7,0,5],[0,2,0,0],[0,3,0,4],[1,0,0,0]]) == [[6,7,inf,5],[inf,2,inf,inf],[5,3,inf,4],[1,8,inf,6]])

#Floyd_Warshall([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]) should return  [[1,inf,inf,inf],[inf,1,inf,inf],[inf,inf,1,inf],[inf,inf,inf,1]]
print(Floyd_Warshall([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]) == [[1,inf,inf,inf],[inf,1,inf,inf],[inf,inf,1,inf],[inf,inf,inf,1]])

#Floyd_Warshall([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]]) should return [[4,1,2,3],[3,4,1,2],[2,3,4,1],[1,2,3,4]]
print(Floyd_Warshall([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]]) == [[4,1,2,3],[3,4,1,2],[2,3,4,1],[1,2,3,4]])

#Floyd_Warshall([[0,0,3,0],[2,0,0,0],[0,7,0,1],[6,0,0,0]]) should return [[10,10,3,4],[2,12,5,6],[7,7,10,1],[6,16,9,10]]
print(Floyd_Warshall([[0,0,3,0],[2,0,0,0],[0,7,0,1],[6,0,0,0]]) == [[10,10,3,4],[2,12,5,6],[7,7,10,1],[6,16,9,10]])

#Floyd_Warshall([[0,3,0,0,5,0,0,0], [0,0,4,4,0,0,0,0]),[1,0,0,0,2,5,4,0],[0,2,0,0,0,0,0,0],[0,0,0,0,0,0,2,8],[0,0,0,0,0,0,0,0],[0,0,9,0,2,0,0,6],[0,0,0,0,0,9,0,0]]) should return , [[8, 3, 7, 7, 5, 12, 7, 13], [5, 6, 4, 4, 6, 9, 8, 14], [1, 4, 8, 8, 2, 5, 4, 10], [7, 2, 6, 6, 8, 11, 10, 16], [12, 15, 11, 19, 4, 16, 2, 8], [inf, inf, inf, inf, inf, inf, inf, inf], [10, 13, 9, 17, 2, 14, 4, 6], [inf, inf, inf, inf, inf, 9, inf, inf]]
print(Floyd_Warshall([[0,3,0,0,5,0,0,0], [0,0,4,4,0,0,0,0],[1,0,0,0,2,5,4,0],[0,2,0,0,0,0,0,0],[0,0,0,0,0,0,2,8],[0,0,0,0,0,0,0,0],[0,0,9,0,2,0,0,6],[0,0,0,0,0,9,0,0]]) == [[8, 3, 7, 7, 5, 12, 7, 13], [5, 6, 4, 4, 6, 9, 8, 14], [1, 4, 8, 8, 2, 5, 4, 10], [7, 2, 6, 6, 8, 11, 10, 16], [12, 15, 11, 19, 4, 16, 2, 8], [inf, inf, inf, inf, inf, inf, inf, inf], [10, 13, 9, 17, 2, 14, 4, 6], [inf, inf, inf, inf, inf, 9, inf, inf]])

#Floyd_Warshall([[0,3,4,8,0,0,0,0], [5,0,1,6,0,0,1,0], [6,0,0,0,0,0,5,0],[0,4,0,0,0,5,0,8],[0,0,2,0,0,0,0,7],[0,2,0,0,0,0,0,0],[0,0,0,0,0,8,0,0],[0,0,0,0,0,0,8,0]]) should return [[8, 3, 4, 8, inf, 12, 4, 16], [5, 8, 1, 6, inf, 9, 1, 14], [6, 9, 10, 14, inf, 13, 5, 22], [9, 4, 5, 10, inf, 5, 5, 8], [8, 11, 2, 16, inf, 15, 7, 7], [7, 2, 3, 8, inf, 11, 3, 16], [15, 10, 11, 16, inf, 8, 11, 24], [23, 18, 19, 24, inf, 16, 8, 32]]
print(Floyd_Warshall([[0,3,4,8,0,0,0,0], [5,0,1,6,0,0,1,0], [6,0,0,0,0,0,5,0],[0,4,0,0,0,5,0,8],[0,0,2,0,0,0,0,7],[0,2,0,0,0,0,0,0],[0,0,0,0,0,8,0,0],[0,0,0,0,0,0,8,0]]) == [[8, 3, 4, 8, inf, 12, 4, 16], [5, 8, 1, 6, inf, 9, 1, 14], [6, 9, 10, 14, inf, 13, 5, 22], [9, 4, 5, 10, inf, 5, 5, 8], [8, 11, 2, 16, inf, 15, 7, 7], [7, 2, 3, 8, inf, 11, 3, 16], [15, 10, 11, 16, inf, 8, 11, 24], [23, 18, 19, 24, inf, 16, 8, 32]])

#Floyd_Warshall([[0,7,0,5],[0,2,0,0],[0,3,0,4],[1,0,0,0]]) should return [[6,7,inf,5],[inf,2,inf,inf],[5,3,inf,4],[1,8,inf,6]]
print(Floyd_Warshall([[0,7,0,5],[0,2,0,0],[0,3,0,4],[1,0,0,0]])== [[6,7,inf,5],[inf,2,inf,inf],[5,3,inf,4],[1,8,inf,6]])

#Floyd_Warshall([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]) should return [[inf, inf, inf, inf], [inf, inf, inf, inf], [inf, inf, inf, inf], [inf, inf, inf, inf]]
print(Floyd_Warshall([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]) == [[inf, inf, inf, inf], [inf, inf, inf, inf], [inf, inf, inf, inf], [inf, inf, inf, inf]])

#Floyd_Warshall([[1,1,1,1],[1,1,1,0],[1,1,0,0],[1,0,0,0]]) should return [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2]]
print(Floyd_Warshall([[1,1,1,1],[1,1,1,0],[1,1,0,0],[1,0,0,0]]) == [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2]])