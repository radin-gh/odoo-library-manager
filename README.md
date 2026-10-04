# Library Manager (Odoo Module)

A simple Odoo module for managing a library's books and loans.
Built with Python and PostgreSQL on Odoo 19.

## Features
- Book catalog (title, author, ISBN, availability)
- Loan management linked to books and contacts (res.partner)
- "Mark as Returned" button that updates loan status and book availability
- Computed late-days field
- Validation preventing loans of books that are already borrowed

## Installation
1. Clone Odoo 19.0 and set up Python 3.12 and PostgreSQL.
2. Copy this folder into your custom addons directory and add it to `addons_path`.
3. Restart Odoo, enable Developer Mode, and click "Update Apps List".
4. Install **Library Manager** from Apps.

## Project Structure
- `models/` - book and loan models
- `views/` - list/form views, actions, and menus
- `security/` - access rules

## Screenshots
(add screenshots here)