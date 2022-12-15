T = int(input())
for t in range(T):
    def get_permutation(arr, n):

        # Sort the given array
        arr = sorted(arr)

        # To store the required minimum
        # number of operations
        result = 0

        # Find the operations on each step
        for i in range(n):
            result += abs(arr[i] - (i + 1))

        # Return the answer
        return result

    N = int(input())
    arr = list(map(int, input().strip().split(' ')))[:N]

    # Function call
    print(get_permutation(arr, N))
