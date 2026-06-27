t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
 
    # Count W in the first window of size k
    w_count = s[:k].count('W')
    ans = w_count
 
    # Slide the window
    for i in range(k, n):
        # Remove leftmost element
        if s[i-k] == 'W':
            w_count -= 1
        # Add new rightmost element
        if s[i] == 'W':
            w_count += 1
        ans = min(ans, w_count)
 
    print(ans)