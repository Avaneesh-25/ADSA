def pairInSortedRotated(arr, target):
    n = len(arr)
    if n < 2:
        return False

    # Find the pivot element (index of the largest element)
    pivot = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            pivot = i
            break

    # l is index of smallest element, r is index of largest element
    l = (pivot + 1) % n
    r = pivot

    # Two-pointer traversal using modulo arithmetic
    while l != r:
        current_sum = arr[l] + arr[r]
        if current_sum == target:
            return True

        if current_sum < target:
            l = (l + 1) % n
        else:
            r = (r - 1 + n) % n

    return False


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    target = int(input())
    print(pairInSortedRotated(arr, target))