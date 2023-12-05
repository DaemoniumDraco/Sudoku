import random
import time


class puzzle:
    def __init__(self):
        #self.__grid = [[0 for i in range(9)]for j in range(9)]
        """self.__grid = [ [3, 0, 0, 8, 0, 1, 0, 0, 2],#Test GRID
                        [2, 0, 1, 0, 3, 0, 6, 0, 4],
                        [0, 0, 0, 2, 0, 4, 0, 0, 0],
                        [8, 0, 9, 0, 0, 0, 1, 0, 6],
                        [0, 6, 0, 0, 0, 0, 0, 5, 0],
                        [7, 0, 2, 0, 0, 0, 4, 0, 9],
                        [0, 0, 0, 5, 0, 9, 0, 0, 0],
                        [9, 0, 4, 0, 8, 0, 7, 0, 5],
                        [6, 0, 0, 1, 0, 7, 0, 0, 3] ]"""
        self.grid = [[0 for i in range(9)] for j in range(9)]
        self.emptySpaces = []
        self.rowDensity = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}#Rows/Cols with higher densities would be filled up first,
        self.colDensity = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}# in the heuristic solve function

    def show_grid(self):
        for i in self.grid:
            for j in i:
                print(j, end = "  ")
            print()
        print()


    def insert(self, row, col, n):
        self.grid[row][col] = n
        

    def find_Empty_Space(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return (row, col)
                
    def find_Empty_Spaces(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    if not( (row, col) in self.emptySpaces ):
                        self.emptySpaces.append( (row, col) )
                else:
                    rowDensity[row] += 1
                    colDensity[col] += 1

            

    def check(self, row, col, num):#return false if there are any mistakes
        """COMPLETE"""
        if num in self.grid[row]:
            return False
        
        for i in range(9):
            if num == self.grid[i][col]:
                return False
        
        boxRow = row // 3 * 3
        boxCol = col // 3 * 3

        for i in range(boxRow, boxRow+3):
            for j in range(boxCol, boxCol+3):
                if num == self.grid[i][j]:
                    return False

        return True


    def solve(self):
        """COMPLETE"""
        #x = input()#used as next button as to slow down and inspect algorithm
        
        pos = self.find_Empty_Space()
        if pos == None:
            return True
    

        row, col = pos[0], pos[1]

        self.show_grid()
        print(f"Pos: {pos}")
        print()

        for n in range(1, 10):

            if self.check(row, col, n):
                self.insert(row, col, n)
                
                if self.solve():
                    return True
                
                self.insert(row, col, 0)#if a solve does not happen then position goes back to zero in case further backtracking needed

        return False
    

    def solveH(self):#Heuristic approach to solve

        #x = input()#used as next button as i am testign right now
        
        pos = self.find_Empty_Space()
        if pos == None:
            return True
    

        row, col = pos[0], pos[1]

        self.show_grid()
        print(f"Pos: {pos}")
        print()

        for n in range(1, 10):

            if self.check(row, col, n):
                self.insert(row, col, n)
                
                if self.solveH():
                    return True
                
                self.insert(row, col, 0)#if a solve does not happen then position goes back to zero in case further backtracking needed

        return False

    def generate(self):
        pass



puzzle1 = puzzle()
puzzle1.find_Empty_Space()
puzzle1.show_grid()
puzzle1.solve()
puzzle1.show_grid()