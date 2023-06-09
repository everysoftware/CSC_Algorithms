from heapify import *
from parallel import *
from sets import *
from table_union import *
from auto_analysis import *
from contact_book import *


def test_heapify():
    n = int(input())
    a = list(map(int, input().split()))
    swaps = heapify(n, a)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


def test_parallel():
    n, m = list(map(int, input().split()))
    time = list(map(int, input().split()))
    for x in parallel(n, m, time):
        print(*x)


def test_naive_set():
    s = NaiveSet(10)
    for i in range(1, 10):
        s.make_set(i)
    for x in [3, 2, 4, 7]:
        s.union(9, x)
        assert s.find(9) == s.find(x)
    assert s.find(5) != s.find(9)
    assert s.find(5) != s.find(6)
    for x in [1, 8]:
        s.union(6, x)
        assert s.find(6) == s.find(x)
    print(f'Smallest: {s.smallest}')


def test_tree_set():
    def test1():
        s = TreeSet(10)
        for i in range(1, 10):
            s.make_set(i)
        for x in [3, 2, 4, 7]:
            s.union(9, x)
            assert s.find(9) == s.find(x)
        assert s.find(5) != s.find(9)
        assert s.find(5) != s.find(6)
        for x in [1, 8]:
            s.union(6, x)
            assert s.find(6) == s.find(x)
        print(f'Parent: {s.parent}')
        print(f'Rank: {s.rank}')

    def test2():
        s = TreeSet(6)
        for i in range(1, 7):
            s.make_set(i)
        for x, y in [(2, 4), (5, 2), (3, 1), (2, 3), (2, 6)]:
            s.union(x, y)
            assert s.find(x) == s.find(y)
        print(f'Parent: {s.parent}')
        print(f'Rank: {s.rank}')

    print('Test #1')
    test1()
    print('Test #2')
    test2()


def test_table_union():
    n, m = list(map(int, input().split()))
    sizes = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(m)]
    print(*table_union(n, m, sizes, queries), sep='\n')


def test_auto_analysis():
    n, e, d = list(map(int, input().split()))
    equals = [list(map(int, input().split())) for _ in range(e)]
    not_equals = [list(map(int, input().split())) for _ in range(d)]
    print(1 if auto_analysis(n, e, d, equals, not_equals) else 0)


def test_contact_book():
    n = int(input())
    queries = [input().split() for _ in range(n)]
    print(*contact_book(n, queries), sep='\n')


def main():
    f = [
        ('Task #1. Heapify', test_heapify),
        ('Task #2. Parallel processing', test_parallel),
        ('Naive set', test_naive_set),
        ('Tree set', test_tree_set),
        ('Task #3. Table union', test_table_union),
        ('Task #4. Auto analysis', test_auto_analysis),
        ('Task #5. Contact book', test_contact_book)
    ]
    for i, x in enumerate(f):
        print(f'{i + 1}. {x[0]}')
    n = int(input())
    if n > len(f):
        print('Unknown command')
    else:
        f[n - 1][1]()


main()
