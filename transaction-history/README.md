# Transaction History

Implementation for the Transaction_History project.

## Category Filtering

`src/transaction_history/transaction_history.py` provides a dependency-free transaction model and filtering API:

- `available_categories(transactions)` returns unique category options for a selector.
- `filter_transactions(transactions, category=...)` matches categories without regard to capitalization or punctuation.
- Omit `category` or pass `None` to clear the category filter.
- Pass `start_date` and `end_date` to compose date and category filters.

Run the focused tests from this folder:

```powershell
$env:PYTHONPATH = "src"
py -m unittest discover -s src/tests -v
```
