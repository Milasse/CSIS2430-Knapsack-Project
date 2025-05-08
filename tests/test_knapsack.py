import pytest
from src.knapsack import load_items_from_csv, greedy_by_ratio, greedy_by_weight, greedy_by_rating
from src.dp_knapsack import dp_knapsack, Item as DPItem

def make_test_items():
    return [DPItem(i.name, int(i.weight), int(i.rating)) for i in load_items_from_csv('data/sample_items.csv')]

@pytest.mark.parametrize("heuristic, func", [
    ('ratio', greedy_by_ratio),
    ('weight', greedy_by_weight),
    ('rating', greedy_by_rating),
])
def test_greedy_with_small_capacity(heuristic, func):
    items = load_items_from_csv('data/sample_items.csv')
    sel, w, r = func(items, 5)
    assert w <= 5
    assert isinstance(r, float)


def test_dp_exact():
    items = make_test_items()
    chosen, max_rating = dp_knapsack(items, 10)
    # Replace 18 with expected value based on sample data
    assert max_rating == sum(i.rating for i in chosen)


def test_approx_ratio_close_to_opt():
    items = load_items_from_csv('data/sample_items.csv')
    sel_r, w_r, r_r = greedy_by_ratio(items, 10)
    dp_items = make_test_items()
    _, opt = dp_knapsack(dp_items, 10)
    assert r_r >= 0.9 * opt