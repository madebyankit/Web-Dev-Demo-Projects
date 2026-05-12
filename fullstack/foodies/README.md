# Foodies

Foodies is a Next.js meal-sharing community built with SQLite. It lets users browse recipes, view meal details, and submit new meals with an image, summary, and recipe instructions.

## Features

- Browse shared meals on the home page
- See full meal details and creator contact info
- Share a new recipe through a submission form
- Save recipe data in SQLite via `better-sqlite3`
- Sanitize user input with `xss`
- Generate URL-friendly slugs for meals

## Getting Started

```bash
cd fullstack/foodies
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## Database

The project stores meals in `meals.db` and includes `initdb.js` to seed initial recipe data.

To initialize the database manually:

```bash
node initdb.js
```

## Project Structure

- `app/` — Next.js app routes and pages
- `lib/` — backend helpers for database access and form actions
- `meals.db` — SQLite database used by the app
- `public/` — static assets and uploaded meal images

## Notes

This app is a good example of a small full-stack Next.js project with server-side data handling and form submission support.
