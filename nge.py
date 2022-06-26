def nextGreaterElements(arr):
    N = len(arr)
    out = [-1]
    stack = [arr[-1]]
    
    for i in range(N-2, -1, -1):
        while stack and (arr[i] >= stack[-1]):
            stack.pop()

        out.append(-1 if not stack else stack[-1])
        stack.append(arr[i])

    return out[::-1]


def main():
    arr1 = [2, 7, 3, 5, 4, 6, 8]
    ans1 = nextGreaterElements(arr1)
    assert ans1 == [7, 8, 5, 6, 6, 8, -1]

    arr2 = [5, 4, 3, 2, 1]
    ans2 = nextGreaterElements(arr2)
    assert ans2 == [-1, -1, -1, -1, -1]


if __name__ == "__main__":
    main()