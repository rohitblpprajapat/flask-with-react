def spiral_order(matrix):
    
    result = []
    rows = len(matrix)
    cols = len(matrix[0])
    
    top = 0
    bottom = rows -1
    left = 0
    right = cols-1
    while top <= bottom and left <= right:
        
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
         
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
         
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
         
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result
 # Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
spiral_result = spiral_order(matrix)
print(spiral_result)