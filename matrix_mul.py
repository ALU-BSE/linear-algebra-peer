# Example arrays
Prices = [[300, 500],  
          [1000, 120.85]]  

Array2 = [200, 100]

# Calculate the result
Ans = []

for i in range(len(Prices)):
    row_sum = 0 
    for j in range(len(Prices[0])):  
        row_sum += Prices[i][j] * Array2[j]  # Multiply each price with corresponding quantity and sum them up
    Ans.append(row_sum)  # Append the total cost of the row to the answer list

# Print the result
print("Total cost for each row:", Ans)
