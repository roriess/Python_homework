# Complexity assessment for solutions

**enumeration.py**: _O(n!)_, because permutations are used here, and the number of permutations is given by the formula P(n) = n!

**recursion.py**: _O(n**n)_, because we have 'n' options on each line, the recursion is repeated 'n' times

**the_fastest_solution.py**: also _O(n**n)_, but it's faster and more memory-efficient, because we don't keep full boards, we only increase the solution counter
