import csv, random

def generate_random_items(path, n=500):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name','weight','rating'])
        for i in range(1, n+1):
            w = round(random.uniform(1, 20), 1)
            r = round(random.uniform(1, 100), 1)
            writer.writerow([f'Item{i}', w, r])

if __name__ == '__main__':
    generate_random_items('data/random_items.csv', n=1000)
