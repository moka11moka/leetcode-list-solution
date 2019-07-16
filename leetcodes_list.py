#1051. Height Checker
# Students are asked to stand in non-decreasing order of heights for an annual photo.
#
# Return the minimum number of students not standing in the right positions.
# (This is the number of students that must move in order for all students to be standing
# in non-decreasing order of height.)

# Input: [1,1,4,2,1,3]
# Output: 3
# Explanation:
# Students with heights 4, 3 and the last 1 are not standing in the right positions.

def heightChecker(self, heights: List[int]) -> int:
        heights_new = sorted(heights)
        result = 0
        for i in range(len(heights)):
            if heights[i] != heights_new[i]:
                result += 1
        return result




# 1122. Relative Sort Array
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1
#
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    temp = arr1.copy()
    result = []
    for i in arr2:
        for index in arr1:
            if i == index:
                result.append(index)
                temp.remove(index)
    return result + sorted(temp)



# 883. Projection Area of 3D Shapes
# On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
# Now we view the projection of these cubes onto the xy, yz, and zx planes.
# A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.
# Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
# Return the total area of all three projections.


def projectionArea(self, grid: List[List[int]]) -> int:
    area = 0
    for i in range(len(grid)):
        row, col = 0, 0
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                area += 1
            row = max(row, grid[i][j])
            col = max(col, grid[j][i])
        area += row + col
    return area