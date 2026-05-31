# Web-Dev-Demo-Projects

This repository documents my hands-on learning across various web development concepts and technologies.
While the implementations are my own, designs and concepts are based on course material and are not claimed as original work.

## Projects

### Backend

Backend applications with Express.js, MongoDB, and FastAPI.

- **Express**
  - **auth-demo**
    - User authentication demo with login/register functionality using Express, MongoDB, and EJS.
  - **blog-site**
    - Full-stack blog app with RESTful CRUD operations, MongoDB, and EJS templating.
  - **yelp-camp**
    - Campground review site with user authentication, reviews, and image uploads using Express, MongoDB, and EJS.
- **FastAPI**
  - **books-api**
    - FastAPI book collection API with filterable routes and JSON create/update/delete operations.
  - **todo-db-auth**
    - Database-backed to-do app with JWT authentication, protected user routes, admin routes, Jinja pages, PostgreSQL, Alembic, and tests.

### Frontend

Frontend applications and static templates.

- **CSS**
  - **css-grid-nexter**
    - Real estate site showcasing CSS Grid layouts.
  - **flexbox-trillo**
    - Hotel booking interface using CSS Flexbox.
  - **sass-animations-float-layout-natours**
    - Tour company landing page with SASS and CSS animations.

- **React**
  - **fancy-todo-list**
    - Multi-list to-do manager with Material UI, custom icons, and IndexedDB persistence via Dexie + SWR.
  - **food-order**
    - Food ordering app with a Vite React frontend, cart and checkout modals, custom HTTP hook, and local Express API for meals and orders.
  - **quiz**
    - Timed React quiz app with answer feedback, automatic skips, and a final score summary.
  - **tic-tac-toe**
    - Classic two-player board game with turn-based play, win/draw detection, editable player names, and reset functionality.
  - **to-do**
    - Task manager with Redux Toolkit, featuring animations and filtering.

### Fullstack

Full-stack applications combining frontend and backend.

- **foodies**
  - Recipe sharing community built with Next.js and SQLite, featuring meal browsing, recipe submission, and image upload.

### In Progress

Experimental or unfinished projects.

- **in-progress/yelp-camp-react**
  - Work-in-progress React version of the YelpCamp campground review app.

### Resources

Quick reference materials and cheatsheets.

- **Cheatsheets**
  - **hint.css**
    - CSS library for tooltips.
  - **React.js**
    - Reference guide for React concepts.

## Technologies Covered

- **Frontend**: React, Redux Toolkit, Framer Motion, CSS, SASS, Next.js
- **Backend**: Express.js, MongoDB, Mongoose, FastAPI, Python, PostgreSQL, SQLite
- **Styling**: CSS, SASS, Material UI
- **Tools**: Node.js, npm, Vite, live-server, uvicorn, Alembic, Pytest

## Getting Started

Each project has its own setup. Generally:

1. Go to the project folder
2. Run `npm install` (if package.json exists)
3. Run the script listed in that project's README, commonly `npm run dev`, `npm start`, or `node index.js`
4. For FastAPI projects, create the shared virtual environment in `backend/fastapi` and run `uvicorn main:app --reload` from the app folder

Check individual project READMEs for details.

## Repository Structure

```
Web-Dev-Demo-Projects/
├── backend/
│   ├── express/
│   │   ├── auth-demo/
│   │   ├── blog-site/
│   │   └── yelp-camp/
│   └── fastapi/
│       ├── books-api/
│       └── todo-db-auth/
├── frontend/
│   ├── css/
│   │   ├── css-grid-nexter/
│   │   ├── flexbox-trillo/
│   │   └── sass-animations-float-layout-natours/
│   └── react/
│       ├── fancy-todo-list/
│       ├── food-order/
│       ├── quiz/
│       ├── tic-tac-toe/
│       └── to-do/
├── fullstack/
│   └── foodies/
├── in-progress/
│   └── yelp-camp-react/
├── resources/
│   └── cheatsheets/
│       ├── React.js
│       └── hint.css
└── README.md
```

## Learning Focus

These projects demonstrate:

- Modern JavaScript frameworks
- RESTful API design
- Database integration
- Advanced CSS techniques
- Full-stack development

Feel free to explore and use as learning references!
