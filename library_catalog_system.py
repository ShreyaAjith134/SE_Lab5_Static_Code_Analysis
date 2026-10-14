"""Library catalog management module."""

import hashlib
import secrets

catalog = {
    "B01": {"title": "Clean Code", "copies": 3},
    "B02": {"title": "The Pragmatic Programmer", "copies": 1},
    "B03": {"title": "Design Patterns", "copies": 2},
}


def issue_book(book_id, patron, active_issues=None):
    """Issue a book to a patron if copies are available."""
    if active_issues is None:
        active_issues = []

    if book_id not in catalog or catalog[book_id]["copies"] <= 0:
        return False

    catalog[book_id]["copies"] -= 1
    active_issues.append(f"Issued book {book_id} to patron {patron}")
    return True


def return_book(book_id):
    """Return a book and increase its available copy count."""
    if book_id not in catalog:
        return False

    catalog[book_id]["copies"] += 1
    return True


def check_availability(book_id):
    """Check whether a book exists and has available copies."""
    if book_id not in catalog:
        return False

    return catalog[book_id]["copies"] > 0


def calculate_fine(days_overdue, daily_rate=2.0):
    """Calculate a fine using the overdue days and daily rate."""
    if days_overdue < 0 or daily_rate < 0:
        raise ValueError("Days overdue and daily rate must be non-negative.")

    return days_overdue * daily_rate


def generate_patron_hash(patron_id):
    """Generate a SHA-256 digest for a patron identifier."""
    return hashlib.sha256(patron_id.encode("utf-8")).hexdigest()


def generate_temp_patron_pin():
    """Generate a cryptographically secure four-digit PIN."""
    return secrets.randbelow(9000) + 1000


def export_catalog(filename="catalog_export.txt"):
    """Export the catalog to a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as catalog_file:
        catalog_file.write(str(catalog))

    print(f"Catalog backup exported to: {filename}")


def main():
    """Demonstrate the library catalog operations."""
    issue_book("B01", "P101")
    return_book("B02")
    print("Is B01 available:", check_availability("B01"))
    print("Fine accrued:", calculate_fine(4))
    print("Patron Hash:", generate_patron_hash("P101"))
    print("Temp PIN:", generate_temp_patron_pin())
    export_catalog()


if __name__ == "__main__":
    main()
