# Photo Organizer

A small Django web app for storing photos, labelling them with tags, and finding
them again by tag. Built as an IB Computer Science Internal Assessment (CSIA)
project.

Everything runs locally: images are written to `media/` and the data lives in a
SQLite file (`db.sqlite3`) that is committed with the repo, so the app starts up
with sample images and tags already in it.

## Features

- **Home** — pick one or more tags from a multi-select list and search.
- **Gallery** — view every uploaded image with its title.
- **Add Image** — upload an image file, give it a title, and attach existing tags.
- **Create Tag** — add a new tag name that can then be used on images.
- **Admin** — the standard Django admin at `/admin/` for editing images and tags directly.

## Stack

| Piece | Version |
| --- | --- |
| Python | 3.12 |
| Django | 4.2.7 |
| Database | SQLite |
| Dependency manager | Pipenv (`Pipfile`) |

## Getting started

### 1. Install dependencies

With Pipenv (matches the committed `Pipfile.lock`):

```bash
pipenv install
pipenv shell
```

Or with a plain virtualenv:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install "django==4.2.7"
```

Pillow is required by Django's `ImageField` for upload validation. If uploading
an image raises an error about Pillow, install it too:

```bash
pip install Pillow
```

### 2. Apply migrations

The repo already ships a populated `db.sqlite3`, but run this to be sure the
schema is current:

```bash
python manage.py migrate
```

### 3. Run the server

```bash
python manage.py runserver
```

Then open http://127.0.0.1:8000/.

### 4. (Optional) Create an admin user

```bash
python manage.py createsuperuser
```

and log in at http://127.0.0.1:8000/admin/.

## How to use it

1. Go to **Create Tag** and add the labels you want to organise by (e.g. `beach`,
   `family`, `school`). Tag names must be unique and up to 20 characters.
2. Go to **Add Image**, choose a file, give it a unique title, and select any
   tags that apply. The file is saved into `media/`.
3. Go to **Gallery** to see everything you have uploaded.
4. On **Home**, select one or more tags (ctrl/cmd-click for several) and press
   **Search**. The results page shows every image carrying *any* of the selected
   tags.

## Project layout

```
CSIA/
├── manage.py              # Django entry point
├── db.sqlite3             # SQLite database (committed, contains sample data)
├── media/                 # Uploaded image files
├── gallery/               # Project package (settings, URLs, templates, CSS)
│   ├── settings.py
│   ├── urls.py            # / , /gallery , /create , /search , /tag , /admin
│   ├── static/style.css
│   └── templates/         # home.html, gallery.html, create.html, search.html, tag.html
└── photos/                # App package
    ├── models.py          # Tag and Image models
    ├── forms.py           # ImageForm, TagForm (ModelForms)
    ├── views.py           # home, gallery, create, search, tag views
    ├── admin.py
    └── migrations/
```

## Data model

- **Tag** — `name` (unique, ≤20 chars), `created_at` (set automatically).
- **Image** — `image` (the uploaded file), `title` (unique, ≤40 chars),
  `tags` (many-to-many to `Tag`, optional).

## Notes and limitations

This is a coursework project intended to be run on a local machine, not
deployed:

- `DEBUG = True` and the `SECRET_KEY` is checked into `gallery/settings.py`.
  Both would need to change before any real deployment.
- `ALLOWED_HOSTS` is empty, so the app only serves `localhost`/`127.0.0.1`.
- Media files are served by Django itself, which only works while `DEBUG` is on.
- There is no login requirement — anyone who can reach the server can upload
  images and create tags.

## Licence

MIT — see [LICENSE](LICENSE).
