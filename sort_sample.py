# coding=utf-8
import random

# 写経元　https://qiita.com/suecharo/items/30f5d817da4c948c3be6

# 隣り合う要素の大小を比較しながら整列させること。最悪計算時間がO(n2)と遅いが、アルゴリズムが単純で実装が容易なため、また並列処理との親和性が高いことから、しばしば用いられる。安定な内部ソート。基本交換法、隣接交換法ともいう
# https://ja.wikipedia.org/wiki/%E3%83%90%E3%83%96%E3%83%AB%E3%82%BD%E3%83%BC%E3%83%88
def bubbel_sort(arr):
    change = True
    while change:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
                
            print(f'{i}:{arr}')
    return arr

# 配列された要素から、最大値やまたは最小値を探索し配列最後の要素と入れ替えをおこなう
# https://ja.wikipedia.org/wiki/%E9%81%B8%E6%8A%9E%E3%82%BD%E3%83%BC%E3%83%88
def select_sort(arr):
    for i, elem in enumerate(arr):
        min_index = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[min_index] = arr[min_index], elem
        print(f'{i}:{arr}')
    return arr

# 整列してある配列に追加要素を適切な場所に挿入する
# https://ja.wikipedia.org/wiki/%E6%8C%BF%E5%85%A5%E3%82%BD%E3%83%BC%E3%83%88
def insert_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        elem = arr[i]
        while arr[j] > elem and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
        print(f'{i}:{arr}')
    return arr

def create_random_arr():
    arr = list(range(1,10))
    random.shuffle(arr)
    print(f'生成した配列 {arr}');
    return arr

def main():
    print(f'bubble_sort {bubbel_sort(create_random_arr())}')

    print(f'select_sort {select_sort(create_random_arr())}')

    print(f'insert_sort {insert_sort(create_random_arr())}')

main()
