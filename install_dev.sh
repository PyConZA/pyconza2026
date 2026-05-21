#!/bin/sh

# install dependencies and set up virtual env
uv sync

# set up the database
uv run python manage.py migrate
uv run python manage.py createcachetable wafer_cache_table
uv run python manage.py wafer_add_default_groups

# create a superuser for local development
DJANGO_SUPERUSER_PASSWORD='super' uv run python manage.py createsuperuser \
  --noinput --username super --email super@email.com

# load the markdown content files in `./pages_md`
uv run python manage.py load_md_content

# install node dependencies 
npm i

# Build the tailwind styles 
npm run tailwind
# note that if you make changes static/css/main.css, or you change 
# how tailwind classes are used in any html file, then you will
# need to rebuild the tailwind css. See the note in the README.md
