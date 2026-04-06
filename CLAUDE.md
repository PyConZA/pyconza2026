# virtual environment 

This project uses uv for dependency management. Dependencies are defined in pyproject.toml.

uv sync

# Tailwind 
- Input css file: static/css/main.css
- Use our tailwind utility classes whenever possible. For example `class="btn"`
- Focus on reusability and DRY code. If some visual element is used in multiple places, then define it in the tailwind_input.css class
- Make sure that the website is responsive. It should look good on screens of all sizes


# Core Values

- Community-First: Emphasize collaboration and inclusivity
- South African Excellence: Celebrate South African tech talent and innovation
- Python Passion: Maintain connection to global Python community
- Accessibility: Design for all users, regardless of ability or connection speed


# Design
The PyConZA visual identity merges Python's established brand elements with vibrant South African design sensibilities. Our approach balances professionalism with warmth, technical precision with creative expression, and global standards with local flavor.


## Design Implementation Guidelines

### Micro-interactions & Animations
- **Hover states**: Subtle color shifts and slight scale transforms
- **Focus states**: Clear sage-colored focus rings for accessibility
- **Loading states**: Skeleton screens with subtle pulse animation
- **Transitions**: 200-300ms duration for smooth, professional feel
- **Scroll reveals**: Fade-in with subtle upward movement for content sections

### Best Practices Checklist
- [ ] Every interactive element has hover and focus states
- [ ] Text has sufficient contrast (WCAG AA minimum)
- [ ] Components are responsive across all breakpoints
- [ ] Images have descriptive alt text
- [ ] Loading states are implemented for dynamic content
- [ ] Cotton components are self-contained and reusable
- [ ] Partials handle HTMX updates gracefully
- [ ] Typography maintains readability (line length, spacing)
- [ ] The Sage archetype is reflected in design choices

## Error Prevention
- Always use `{% load static %}` when referencing static files
- Include CSRF tokens in forms: `{% csrf_token %}`
- Use Django's `|safe` filter only when absolutely necessary
- Escape user content by default (Django does this automatically)
- Test responsive breakpoints: mobile, tablet, desktop
- Ensure Cotton components have sensible defaults
- Validate that Tailwind classes exist (no arbitrary values without config)