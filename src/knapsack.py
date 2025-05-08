import csv
import argparse
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Item:
    name: str
    weight: float
    rating: float


def greedy_by_ratio(items: List[Item], capacity: float) -> Tuple[List[Item], float, float]:
    items_sorted = sorted(items, key=lambda it: it.rating/it.weight, reverse=True)
    sel, w, r = [], 0.0, 0.0
    for it in items_sorted:
        if w + it.weight <= capacity:
            sel.append(it)
            w += it.weight
            r += it.rating
    return sel, w, r


def greedy_by_weight(items: List[Item], capacity: float) -> Tuple[List[Item], float, float]:
    items_sorted = sorted(items, key=lambda it: it.weight)
    sel, w, r = [], 0.0, 0.0
    for it in items_sorted:
        if w + it.weight <= capacity:
            sel.append(it)
            w += it.weight
            r += it.rating
    return sel, w, r


def greedy_by_rating(items: List[Item], capacity: float) -> Tuple[List[Item], float, float]:
    items_sorted = sorted(items, key=lambda it: it.rating, reverse=True)
    sel, w, r = [], 0.0, 0.0
    for it in items_sorted:
        if w + it.weight <= capacity:
            sel.append(it)
            w += it.weight
            r += it.rating
    return sel, w, r


def load_items_from_csv(path: str) -> List[Item]:
    items = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['name'].startswith('#'): continue
            items.append(Item(
                name=row['name'],
                weight=float(row['weight']),
                rating=float(row['rating'])
            ))
    return items


def main():
    parser = argparse.ArgumentParser(description="Run knapsack heuristics")
    parser.add_argument("--input", required=True, help="CSV file of items")
    parser.add_argument("--capacity", type=float, required=True)
    args = parser.parse_args()

    items = load_items_from_csv(args.input)
    for name, func in [
        ("ratio", greedy_by_ratio),
        ("weight", greedy_by_weight),
        ("rating", greedy_by_rating),
    ]:
        sel, w, r = func(items, args.capacity)
        print(f"Heuristic: {name}")
        print(f"  Total weight: {w:.2f}, Total rating: {r:.2f}")
        print("  Items:")
        for it in sel:
            print(f"    {it.name} (w={it.weight}, r={it.rating})")
        print()

if __name__ == '__main__':
    main()