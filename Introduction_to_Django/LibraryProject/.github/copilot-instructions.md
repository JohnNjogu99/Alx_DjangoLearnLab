## What this project is

This is a small Django project (created with Django 5.2.6) named `LibraryProject` with a single app `bookshelf`.

- Project root: `manage.py` lives at the repository root. Use `python manage.py <command>` for project-level actions.
- App: `bookshelf` (models in `bookshelf/models.py`, admin in `bookshelf/admin.py`, migrations in `bookshelf/migrations/`).
- Database: SQLite by default; settings point to `BASE_DIR / 'db.sqlite3'` in `LibraryProject/settings.py`.

## Big-picture architecture and where to look

- `LibraryProject/` — Django project settings and URL config (`LibraryProject/settings.py`, `LibraryProject/urls.py`).
- `bookshelf/` — single application containing models, views, migrations and admin. Example model: `Book` in `bookshelf/models.py` (fields: `title`, `author`, `publication_year`).
- `bookshelf/migrations/0001_initial.py` — canonical source of the DB schema created by makemigrations.

Why it is structured this way: this is the standard Django startproject/startapp layout. `bookshelf` is the single domain app and is registered in `INSTALLED_APPS`.

## Developer workflows (commands you should run)

- Run development server: `python manage.py runserver` (from the repository root where `manage.py` is located).
- Create migrations for changes in models: `python manage.py makemigrations bookshelf`.
- Apply migrations: `python manage.py migrate`.
- Run tests: `python manage.py test` (tests currently placeholder in `bookshelf/tests.py`).
- Create admin user: `python manage.py createsuperuser` and then visit `/admin/` (there is currently no model registered in `bookshelf/admin.py`).

Notes: there's no requirements.txt or Pipfile in the repository; the code comments indicate Django 5.2.6 was used to generate files. The agent should assume a virtualenv with Django installed (or ask if an environment file should be added).

## Project-specific conventions and patterns

- App registration: the app name `bookshelf` is added to `INSTALLED_APPS` in `LibraryProject/settings.py` — any new apps must be added here.
- URL routing: `LibraryProject/urls.py` currently only exposes `admin/`. To add app routes, add an `include('bookshelf.urls')` line and create `bookshelf/urls.py`.
- Templates: `TEMPLATES['DIRS']` is empty and `APP_DIRS=True` — prefer placing templates inside `bookshelf/templates/<app>/`.
- Admin: models are not auto-registered. Example quick action: register `Book` in `bookshelf/admin.py` via `from .models import Book` and `admin.site.register(Book)`.

## Integration points & cross-component notes

- Database: `sqlite3` file at `db.sqlite3` — migrations are the canonical source of schema changes.
- No external APIs or services are referenced in code; any integration should be done through new app modules.
- Static files: default `STATIC_URL = 'static/'` — no custom static configuration present.

## Editing and PR guidance for AI agents (concrete examples)

- If adding a view, create `bookshelf/urls.py`, register paths in `LibraryProject/urls.py` with `include()`. Example: `path('', include('bookshelf.urls'))`.
- If changing models, run `makemigrations` and `migrate`. Keep migrations committed (see `bookshelf/migrations/0001_initial.py`).
- To expose `Book` in the admin: add to `bookshelf/admin.py`:

- To run quick local sanity checks use `python manage.py runserver` then inspect `/admin/` or any added routes.

## Files to reference for behavior examples

- `bookshelf/models.py` — domain model (Book).
- `bookshelf/migrations/0001_initial.py` — created migration and schema.
- `LibraryProject/settings.py` — project configuration (DB, INSTALLED_APPS, TEMPLATES).
- `LibraryProject/urls.py` — current URL map (only admin).

## When to ask the maintainer

- If a dependency manifest (requirements.txt or pyproject.toml) is needed — none present.
- If you plan to change project structure (add apps, change DB engine), ask before making large migrations or updating settings.

If anything in this file is unclear or you'd like more automation (e.g. add a `requirements.txt`, register `Book` in admin, or scaffold `bookshelf/urls.py`), tell me which task to perform next.
