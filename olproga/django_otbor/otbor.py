"""ans = []
with open('input.txt', 'r') as fp:
    for i in range(int(input()) + 1):
        ans.append(bin(i)[2:].count('1'))

with open('output.txt', 'w') as o:
    for a in ans:
        o.write(a)"""


"""def main():
    return 'что-то'

if __name__ == '__main__':
    main()"""

"""import typing
import itertools as i


def find_summ_triple(itr: typing.Iterable[int]) -> typing.Optional[int]:
    if len(itr) < 3:
        return None
    return len(list(i.permutations(itr, 3)))


a = list(map(int, input().split()))
print(find_summ_triple(a))"""

"""import cluster


class Cluster:
    def __init__(self):
        self.slots = []
        self.jobs = []
        self.cpu = 0
        self.ram = 0
        self.disk = 0
        self.free_cpu = 0
        self.free_ram = 0
        self.free_disk = 0
    
    def __iadd__(self, other):
        if isinstance(other, cluster.Slot):
            self.slots.append(other)
            self.cpu += other.cpu
            self.ram += other.ram
            self.disk += other.disk
            self.free_cpu += other.cpu
            self.free_ram += other.ram
            self.free_disk += other.disk
        elif isinstance(other, cluster.Job):
            if other.cpu > self.free_cpu or other.ram > self.free_ram or other.disk > self.free_disk:
                raise cluster.NotEnoughResources()
            self.jobs.append(other)
            self.free_cpu -= other.cpu
            self.free_ram -= other.ram
            self.free_disk -= other.disk
        else:
            raise TypeError('Job and Slot allowed')
        return self

    def __iter__(self):
        return iter(self.slot)  

    def __contains__(self, item):
        if isinstance(item, cluster.Slot):
            return item in self.slots
        elif isinstance(item, cluster.Job):
            return item in self.jobs
        return False
    
    
    def __str__(self):
        RAM = f'{self.ram - self.free_ram}/{self.ram}'
        CPU = f'{self.cpu - self.free_cpu}/{self.cpu}'
        DISK = f'{self.cpu - self.free_cpu}/{self.cpu}'
        return f'RAM: {RAM} CPU: {CPU} DISK: {DISK} SLOTS: {len(self.slots)} JOBS: {len(self.jobs)}'"""

"""with open('input.txt', 'r') as fp:
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    mx = 0
    for i in range(min(len(a), len(b)) - 1):
        for j in range(min(len(a), len(b)) - 1):
            #print(3 * (a[i] - b[j]) + 3 * (a[i + 1] - b[j + 1]))
            mx = max(mx, 3 * (a[i] - b[j]) + 3 * (a[i + 1] - b[j + 1]))
with open('output.txt', 'w') as o:
    o.write(str(mx))"""


"""import typing


def gen_triplets(lst):
    if len(lst) < 3:
        return None
    if len(lst) == 3:
        return [list(lst)]
    first = lst[0]
    rest = lst[1:]
    result = []
    for i in range(len(rest)):
        for j in range(i + 1, len(rest)):
            result.append([first, rest[i], rest[j]])
    return result


def find_summ_triple(itr: typing.Iterable[int]) -> typing.Optional[int]:
    triplets = gen_triplets(list(itr))
    if triplets is None:
        return None
    s = 0
    for t in triplets:
        s += (t[0] * t[1] * t[2])
    return s"""


"""import sqlite3


def get_result(db_name: str, timestamp: int) -> list[tuple[int, str]]:
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    q = 
    WITH MarketSavings AS (
        SELECT 
            p.market_id,
            MAX(p.price * d.discount / 100.0) as max_saving
        FROM Products p
        JOIN Deals d ON p.market_id = d.market_id
        WHERE d.start <= ? AND d.end >= ?
        GROUP BY p.market_id
        HAVING max_saving > 0
        ORDER BY max_saving DESC
        LIMIT 5
    )
    SELECT m.id, m.name
    FROM Markets m
    JOIN MarketSavings ms ON m.id = ms.market_id
    ORDER BY m.name ASC, m.id ASC

    cur.execute(q, (timestamp, timestamp, timestamp, timestamp))
    res = cur.fetchall()

    conn.close()
    return res"""


import typing
import itertools as i


def gen_triplets(lst):
    lst = list(lst)
    if len(lst) < 3:
        return None
    if len(lst) == 3:
        return [list(lst)]
    return list(set(list(i.combinations(lst, 3))))
    


def find_summ_triple(iterable: typing.Iterable[int]) -> typing.Optional[int]:
    itr = iterable
    triplets = gen_triplets(itr)
    if triplets is None:
        return None
    s = 0
    for t in triplets:
        s += (t[0] * t[1] * t[2])
    return s


a = list(map(int, input().split()))
print(find_summ_triple(a))