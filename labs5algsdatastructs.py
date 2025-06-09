def count_points(k, grid):
    from collections import Counter

    all_symbols = ''.join(grid)
    count = Counter(all_symbols)

    points = 0
    for t in range(1, 10):
        t_str = str(t)
        if t_str in count:
            if count[t_str] <= 2 * k:
                points += 1
    return points

if __name__ == "__main__":
    k = int(input())
    grid = [input().strip() for _ in range(4)]
    print(count_points(k, grid))
