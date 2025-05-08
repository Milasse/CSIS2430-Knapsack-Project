# CSIS 2430: Programming Project 3

## Overview
Implements three greedy heuristics and an exact dynamic programming solution for the 0/1 knapsack problem. Benchmarks and compares solution quality.

## Structure
- `data/sample_items.csv`: example payload list
- `data/random_items.csv`: generated random payload list (via script)
- `src/knapsack.py`: greedy heuristics + CSV loader + CLI
- `src/dp_knapsack.py`: DP solver
- `tests/test_knapsack.py`: pytest unit tests
- `benchmarks/benchmark.py`: runtime & quality comparison
- `generate_random_items.py`: random data generator script
- `CSIS2430_Knapsack_Report.docx`: full write-up in Word format

## Requirements
- Python 3.8+
- pytest

## Usage
```bash
# Generate random data (optional)
python generate_random_items.py

# Run greedy heuristics on sample or random dataset
python src/knapsack.py --input data/sample_items.csv --capacity 50
python src/knapsack.py --input data/random_items.csv --capacity 500

# Run tests
pytest

# Benchmark
python -m benchmarks.benchmark