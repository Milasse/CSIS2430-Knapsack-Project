from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class Item:
    name: str
    weight: int    # must be integer for DP
    rating: int


def dp_knapsack(items: List[Item], capacity: int) -> Tuple[List[Item], int]:
    n = len(items)
    table = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wt, val = items[i - 1].weight, items[i - 1].rating
        for w in range(capacity + 1):
            table[i][w] = table[i - 1][w]
            if wt <= w:
                cand = table[i - 1][w - wt] + val
                if cand > table[i][w]:
                    table[i][w] = cand
    w = capacity
    chosen = []
    for i in range(n, 0, -1):
        if table[i][w] != table[i - 1][w]:
            chosen.append(items[i - 1])
            w -= items[i - 1].weight
    chosen.reverse()
    return chosen, table[n][capacity]