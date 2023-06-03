def count_tests(test_data):
    # Process the test data and extract test information
    tests = [test for test in test_data]
    categories = set(test[1] for test in tests)

    results = {}
    for category in categories:
        passed = sum(1 for test in tests if test[1] == category and test[2] == 'PASS')
        failed = sum(1 for test in tests if test[1] == category and test[2] == 'FAIL')
        skipped = sum(1 for test in tests if test[1] == category and test[2] == 'SKIP')
        results[category] = {'Passed': passed, 'Failed': failed, 'Skipped': skipped}

    return results

# sample data

test_data = [
    ["0001_internal_deposit", "Deposit", "PASS"],
    ["0002_internal_deposit", "Deposit", "SKIP"],
    ["0003_external_deposit", "Deposit", "PASS"],
    ["0004_invalid_external_deposit", "Deposit", "FAIL"],
    ["0001_dump_in_withdrawal", "Withdrawal", "PASS"],
    ["0002_dump_in_withdrawal", "Withdrawal", "FAIL"],
    ["0003_withdrawal_internal_4ep", "Withdrawal", "FAIL"],
    ["0004_withdrawal_internal_4ep", "Withdrawal", "SKIP"]
]

test_results = count_tests(test_data)

for category, counts in test_results.items():
    print(f"Category: {category}")
    print(f"Passed: {counts['Passed']}")
    print(f"Failed: {counts['Failed']}")
    print(f"Skipped: {counts['Skipped']}")
    print()
