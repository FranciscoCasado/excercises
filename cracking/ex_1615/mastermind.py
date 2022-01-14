

def hits(solution: str, guess: str) -> dict:
    count = {'hits': 0, 'pseudo': 0} 
    guess = list(guess)
    solution = list(solution)
    
    for idx, symbol in enumerate(guess):
        if solution[idx] == symbol:
            count['hits'] += 1
            solution[idx] = None
            guess.remove(symbol)
            
    
    for symbol in guess:
        if symbol in solution:
            count['pseudo'] += 1
            solution.remove(symbol)
            

    return count