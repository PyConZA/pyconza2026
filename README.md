# PyCon Africa 2025 Conference Website

Based on the [PyConZA 2024](https://github.com/PyConZA/pyconza2024/) website, which is based on [wafer](https://github.com/CTPUG/wafer).
Based on the [PyConAfrica/PyConZA 2025](https://github.com/PyConZA/pyconza2025) website, which is based on [wafer](https://github.com/CTPUG/wafer).

# Local development 

## Installation

We are using Python 3.13.12

Install Python dependencies:

```
pip install -r requirements.txt
```

Set up the database and cache tables:

```
python manage.py migrate
python manage.py createcachetable wafer_cache_table
```

Set up the default auth groups:

```
python manage.py wafer_add_default_groups
```

Set up the pages by loading up the various Markdown files:

```
python manage.py load_md_content
```

Install Javascript dependencies:

```
npm install
```

Generate main css file:

```
npm run tailwind
```

Run the development server

```
python manage.py runserver
```

## Tailwind 

We are using TailwindCSS for styling. If you make any changes to `static/css/main.css` or the tailwind classes used in any html file then you will need to rebuild the main tailwind file using `npm run tailwind`.

If you are developing and want to automatically rebuild the css when changes are detected, use `npm run tailwind-w`.

# Deployment 

Make use of `settings_prod.py` when deploying to production. 

To generate and collect static files, do the following:

```
npm install
npm run tailwind
python manage.py collectstatic
```