import json
import os


test_data = [
    '0001_internal_deposit, Deposit, PASS',
    '0001_dump_in_withdrawal, Withdrawal, SKIP'
]

counts = {}

for test in test_data:
    _, category, result = test.split(',')
    category = category.strip()
    result = result.strip()

    if category not in counts:
        counts[category] = {'PASS': 0, 'FAIL': 0, 'SKIP': 0}
    counts[category][result] += 1

print('Results per Category:')
for category, results in counts.items():
    print(f'{category}:')
    for result, count in results.items():
        print(f'{result}: {count}')
    print()

output_file = 'results.json'
output_path = os.path.join(os.getcwd(), output_file)
with open(output_path, 'w') as file:
    json.dump(counts, file, indent=4)

print(f'Test results saved to : {output_file}.')
