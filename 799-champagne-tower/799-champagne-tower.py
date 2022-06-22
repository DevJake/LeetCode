class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[poured]]
        
        for i in range(query_row):
            c_row = tower[i]
            n_row = [0] * (len(c_row)+1)
            
            for j in range(len(c_row)):
                fill_amount = min(1, c_row[j])
                overflow_amount = max(0, c_row[j] - 1)
                n_row[j] = n_row[j] + (overflow_amount / 2)
                
                n_row[j+1] = n_row[j+1] + (overflow_amount / 2)
                
                c_row[j] = fill_amount
                
            tower.append(n_row)
        
        return min(1, tower[query_row][query_glass])
        
        
