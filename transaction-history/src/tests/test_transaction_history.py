import unittest
from datetime import date

from transaction_history import Transaction, available_categories, filter_transactions


TRANSACTIONS = [
    Transaction(date(2026, 1, 2), "Coffee", 4.50, "Food & Dining"),
    Transaction(date(2026, 1, 5), "Bus pass", 25.00, "Transport"),
    Transaction(date(2026, 2, 1), "Groceries", 80.00, "food-dining"),
    Transaction(date(2026, 2, 4), "Salary", 2000.00, None),
]


class TransactionHistoryTests(unittest.TestCase):
    def test_available_categories_are_unique_and_displayable(self):
        self.assertEqual(
            available_categories(TRANSACTIONS),
            ["Food & Dining", "Transport"],
        )

    def test_category_filter_ignores_capitalization_and_formatting(self):
        results = filter_transactions(TRANSACTIONS, category=" food dining ")

        self.assertEqual([transaction.description for transaction in results], ["Coffee", "Groceries"])

    def test_other_categories_are_excluded(self):
        results = filter_transactions(TRANSACTIONS, category="Transport")

        self.assertEqual([transaction.description for transaction in results], ["Bus pass"])

    def test_clearing_category_restores_all_transactions(self):
        results = filter_transactions(TRANSACTIONS, category=None)

        self.assertEqual(results, TRANSACTIONS)

    def test_missing_category_is_excluded_when_category_is_selected(self):
        results = filter_transactions(TRANSACTIONS, category="Other")

        self.assertEqual(results, [])

    def test_no_matching_category_returns_empty_result(self):
        self.assertEqual(filter_transactions(TRANSACTIONS, category="Utilities"), [])

    def test_category_and_date_filters_are_applied_together(self):
        results = filter_transactions(
            TRANSACTIONS,
            category="FOOD DINING",
            start_date="2026-02-01",
            end_date="2026-02-28",
        )

        self.assertEqual([transaction.description for transaction in results], ["Groceries"])

    def test_invalid_date_range_is_rejected(self):
        with self.assertRaises(ValueError):
            filter_transactions(
                TRANSACTIONS,
                start_date="2026-03-01",
                end_date="2026-02-01",
            )


if __name__ == "__main__":
    unittest.main()