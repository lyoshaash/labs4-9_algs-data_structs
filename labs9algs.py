def lab9():
    def merge(arr, lf, mid, rg):
        result = []
        i, j = lf, mid
        while i < mid and j < rg:
            if arr[i] <= arr[j]:
                result.append(arr[i])
                i += 1
            else:
                result.append(arr[j])
                j += 1
        result.extend(arr[i:mid])
        result.extend(arr[j:rg])
        arr[lf:rg] = result

    def merge_sort(arr, lf, rg):
        if rg - lf <= 1:
            return
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        merge(arr, lf, mid, rg)

    print("введите массив целых чисел через пробел:")
    arr = list(map(int, input().split()))
    print("введите два индекса: ")
    lf, rg = map(int, input().split())

    merge_sort(arr, lf, rg)
    print("lab9 (результат):", arr)


if __name__ == '__main__':
    lab9()

path = Path("/mnt/data/labs_4_9_lab9_input.py")
path.write_text(lab9_input_version, encoding="utf-8")
str(path)
