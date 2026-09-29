"""Filtering utilities for transaction history records."""

from dataclasses import dataclass
from datetime import date
import re
from typing import Iterable


@dataclass(frozen=True)
class Transaction:
    """A transaction record that can be filtered by date and category."""

    date: date
    description: str
    amount: float
    category: str | None = None


def normalize_category(category: str | None) -> str | None:
    """Return a case- and formatting-insensitive category key."""
    if category is None:
        return None

    normalized = re.sub(r"[^a-z0-9]+", " ", category.casefold()).strip()
    return normalized or None


def available_categories(transactions: Iterable[Transaction]) -> list[str]:
    """Return unique, display-ready category options in alphabetical order."""
    categories: dict[str, str] = {}
    for transaction in transactions:
        key = normalize_category(transaction.category)
        if key is not None and key not in categories:
            categories[key] = transaction.category.strip()

    return [categories[key] for key in sorted(categories)]


def _parse_date(value: date | str | None) -> date | None:
    if value is None or isinstance(value, date):
        return value
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(f"Invalid date: {value!r}; use YYYY-MM-DD") from error


def filter_transactions(
    transactions: Iterable[Transaction],
    *,
    category: str | None = None,
    start_date: date | str | None = None,
    end_date: date | str | None = None,
) -> list[Transaction]:
    """Filter transactions by category and inclusive date bounds.

    A missing category or an empty category selection clears the category filter.
    Category matching ignores capitalization, whitespace, and punctuation.
    """
    start = _parse_date(start_date)
    end = _parse_date(end_date)
    if start is not None and end is not None and start > end:
        raise ValueError("start_date must be before or equal to end_date")

    category_key = normalize_category(category)
    return [
        transaction
        for transaction in transactions
        if (category_key is None or normalize_category(transaction.category) == category_key)
        and (start is None or transaction.date >= start)
        and (end is None or transaction.date <= end)
    ]
