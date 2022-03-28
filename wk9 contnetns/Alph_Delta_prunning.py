# Initial values of Alpha and Beta-representing infinity
MAX, MIN = 1000, -1000
 
# Returns optimal value for current player
def minimax(depth, nodeIndex, maximizingPlayer,
            values, alpha, beta):
  
    # Terminating condition. i.e leaf
    if depth == 3:
        return values[nodeIndex]
 
    if maximizingPlayer:
        best = MIN
 
        # Recur for left and right children
        for i in range(0, 2):
             
            val = minimax(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
 
            # Test for prunning Pruning
            if beta <= alpha:
                break
          
        return best
      
    else:
        best = MAX
 
        # Recur for left and right children
        for i in range(0, 2):
          
            val = minimax(depth + 1, nodeIndex * 2 + i,
                            True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
 
            # Test for prunning Pruning
            if beta <= alpha:
                break
          
        return best
      
# Driver Code
values = [2,3,5,9,0,1,7,5] 
print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))
