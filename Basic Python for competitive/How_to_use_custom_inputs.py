# You are given a program which does the following
#
# Accepts the count of test cases - tt - in the 1st line.
# First line of each test case consists of an integer NN
# Outputs the integer which is greater than NN by 11
# Note: The Sample 1 input values are pre-populated in the Custom inputs below the IDE
# You need to do the following
#
# Replace the Custom inputs with Sample test case 2 and click Run to check the result.
# You can click the CopyCopy icon at the top-right of the sample testcases to copy easily.
# Replace the Custom inputs with your own created inputs and click Run to check the result.
# You can experiment a few more options.
# Once done, click on Submit to test your code against the Private test files
# Note - Do not forget that the 1^{st}1
# st
#   integer in the custom inputs has to be tt - the number of test cases


t = int(input())
for i in range(t):
    N = int(input())
    print(N+1)
