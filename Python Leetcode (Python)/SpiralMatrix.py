# https://leetcode.com/problems/spiral-matrix/

class spiralMatrix:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        firstRow = 0
        lastRow = len(matrix)-1
        firstCol = 0
        lastCol = len(matrix[0])-1
        answer = []
        while firstRow<lastRow and firstCol<lastCol:
            for xfci in range(firstCol, lastCol):
                answer.append(matrix[firstRow][xfci])
            for x in range(firstRow, lastRow):
                answer.append(matrix[x][lastCol])
            for yx in range(lastCol, firstCol, -1):
                answer.append(matrix[lastRow][yx])
            for y in range(lastRow, firstRow, -1):
                answer.append(matrix[y][firstRow])
            firstRow +=1
            lastRow -=1
            firstCol +=1
            lastCol -=1
        if firstRow==lastRow:
            for xffci in range(firstCol, lastCol+1):
                answer.append(matrix[firstRow][xffci])
        elif firstCol == lastCol: 
            for g in range(firstRow, lastRow+1):
                answer.append(matrix[g][lastCol])
                
        return answer