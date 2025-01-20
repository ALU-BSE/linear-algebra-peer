Prices = [[300, 500],  
          [1000, 120.85]]  

Array2 = [200, 100]

Ans = []

for i in range(len(Prices)):
    row_sum = 0 
    for j in range(len(Prices[0])):  
        row_sum += Prices[i][j] * Array2[j]  

print("Total cost for each row:", Ans)
