# PyConZA 2026 Conference Website

Based on the [PyConZA 2025 / PyCon Africa 2025](https://github.com/PyConZA/pyconza2025) website, which is based on [wafer](https://github.com/CTPUG/wafer).

# Local development 

## Installation

We are using Python 3.13.12 and UV. 

Install UV then run `./install_dev.sh` to get everything set up. 
You can also refer to the `install_dev.sh` script to see how the entire setup works. There are comments that explain everything.

## Running the development server


You can activate your virtual env then run the server like this:

```
source .venv/vin/activate # Linux
python manage.py runserver
```

If you have trouble activating your virtualenv then you can run the runserver like this:

```
uv run python manage.py runserver
```

## Tailwind 

We are using TailwindCSS for styling. If you make any changes to `static/css/main.css` or the tailwind classes used in any html file then you will need to rebuild the main tailwind file using `npm run tailwind`.

If you are developing and want to automatically rebuild the css when changes are detected, use `npm run tailwind-w`.

In this case you will have 2 terminals open: One will be running the `runserver` and the other will be running `npm run tailwind-w`

# Deployment 

Make use of `settings_prod.py` when deploying to production. 

To generate and collect static files, do the following:

```
npm install
npm run tailwind
python manage.py collectstatic
```
