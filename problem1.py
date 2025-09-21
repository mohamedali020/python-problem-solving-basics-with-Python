"""
Problem Definition:
Write a program that reads integer N and Print the sum from 1 to N
Requirements:
1- Print the sum from 1 to N
2- Do not use if condition and loops.
Problem analysis:
Input ==> reads N of integers
Output ==> Sum from 1 to N
-- I need to find a simple 1 line formula to solve the problem :)

Implementation to coding:
- Be careful, programmer
1- Important Code Tracing
2- Do good testing for your code
Notes:
Good Testing = a mindset, not a single technique, and the importance of test cases
"""

N = int(input())
out = (N * (N + 1)) / 2
print(out)

"""
Why such equation?
Here is an intuition for N = 8
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

Let's arrange as following
1 8   2 7    3 6     4 5       [first number and last number]   [2nd number, and 2nd from back] ...

What is the value of each pair? 9 = n+1
How many pairs? 4 = n/2

So n/2 pair, each has value n+1
So total sum is (n * (n+1))/2  ==> This is known as the Gauss Formula.

Now, this works for even N
Your turn: why works for odd N

More readings: http://mathcentral.uregina.ca/qq/database/qq.02.06/jo1.html
               https://medium.com/@krunalpatel1992/gausss-genius-the-elegant-proof-behind-1-2-n-bf793ff86ec7
"""