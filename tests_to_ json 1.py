import json

def count_tests(test_data):
    categories = list(set(category for _, category, _ in test_data))
    passed_tests = {category: sum(1 for _, cat, result in test_data if result == 'PASS' and cat == category) for category in categories}
    failed_tests = {category: sum(1 for _, cat, result in test_data if result == 'FAIL' and cat == category) for category in categories}
    skipped_tests = {category: sum(1 for _, cat, result in test_data if result == 'SKIP' and cat == category) for category in categories}

    return passed_tests, failed_tests, skipped_tests

test_data = [
    ("0001_internal_deposit", "Deposit", "PASS"),
    ("0002_internal_deposit", "Deposit", "SKIP"),
    ("0003_external_deposit", "Deposit", "PASS"),
    ("0004_invalid_external_deposit", "Deposit", "FAIL"),
    ("0001_dump_in_withdrawal", "Withdrawal", "PASS"),
    ("0002_dump_in_withdrawal", "Withdrawal", "FAIL"),
    ("0003_withdrawal_internal_4ep", "Withdrawal", "FAIL"),
    ("0004_withdrawal_internal_4ep", "Withdrawal", "SKIP"),
]

passed_tests, failed_tests, skipped_tests = count_tests(test_data)

print('Passed tests per category:')
for category, count in passed_tests.items():
    print(f'{category}: {count}')

print('\nFailed tests per category:')
for category, count in failed_tests.items():
    print(f'{category}: {count}')

print('\nSkipped tests per category:')
for category, count in skipped_tests.items():
    print(f'{category}: {count}')

results_dict = {
    'passed_tests': passed_tests,
    'failed_tests': failed_tests,
    'skipped_tests': skipped_tests
}

output_file = 'results_1.json'
with open(output_file, 'w') as file:
    json.dump(results_dict, file, indent=4)

print(f'\nResults saved to {output_file}')
