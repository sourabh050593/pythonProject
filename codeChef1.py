# Input Format
# The first and only line of input will contain a single integer X, the current IQ of Chef.
# Output Format
# For each testcase, output in a single line "Yes" or "No"
# You may print each character of the string in either uppercase or lowercase (for example, the strings yEs, yes, Yes, and YES will all be treated as identical).

x = int(input())
if (x+7)>170:
    print('YES')
else:
    print('NO')