import random
import time
from src.knapsack import greedy_by_ratio, greedy_by_weight, greedy_by_rating, load_items_from_csv
from src.dp_knapsack import dp_knapsack, Item as DPItem

items = load_items_from_csv('data/sample_items.csv')
capacities = [50, 100, 200]

for cap in capacities:
    print(f"Capacity: {cap}")
    for name, func in [('ratio', greedy_by_ratio), ('weight', greedy_by_weight), ('rating', greedy_by_rating)]:
        start = time.time()
        sel, w, r = func(items, cap)
        print(f" {name}: rating={r:.2f}, time={time.time() - start:.6f}s")
    dp_items = [DPItem(i.name, int(i.weight), int(i.rating)) for i in items]
    start = time.time()
    _, opt = dp_knapsack(dp_items, int(cap))
    print(f" dp: optimal={opt}, time={time.time() - start:.6f}s")
    print()
