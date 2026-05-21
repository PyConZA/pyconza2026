# Stack 


# virtual environment 

This project uses uv for dependency management. Dependencies are defined in pyproject.toml.

uv sync

# Tailwind 
- Input css file: static/css/main.css
- Use our tailwind utility classes whenever possible. For example `class="btn"`
- Focus on reusability and DRY code. If some visual element is used in multiple places, then define it in the tailwind_input.css class
- Make sure that the website is responsive. It should look good on screens of all sizes

## Error Prevention
- Always use `{% load static %}` when referencing static files
- Include CSRF tokens in forms: `{% csrf_token %}`
- Use Django's `|safe` filter only when absolutely necessary
- Escape user content by default (Django does this automatically)
- Test responsive breakpoints: mobile, tablet, desktop
- Ensure Cotton components have sensible defaults
- Validate that Tailwind classes exist (no arbitrary values without config)

## DO NOT

- Don't add placeholder links and buttons that don't do anything. Everything should work.  