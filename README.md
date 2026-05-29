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

- **Bootstrap**
  - **Candy_Museum**
    - A themed website for a candy museum using Bootstrap components.
  - **Dating_Site_Homepage**
    - Homepage design for a dating site showcasing Bootstrap layouts.
  - **Image_Gallery**
    - Simple photo gallery using Bootstrap's grid system.

- **CSS**
  - **CSS_GRID_(Nexter Project)**
    - Real estate site showcasing CSS Grid layouts.
  - **FLEXBOX_(Trillo Project)**
    - Hotel booking interface using CSS Flexbox.
  - **SASS_Animations_FloatLayout_(Natours project)**
    - Tour company landing page with SASS and CSS animations.

- **React**
  - **fancy-todo-list**
    - Multi-list to-do manager with Material UI, custom icons, and IndexedDB persistence via Dexie + SWR.
  - **Investment-Calculator**
    - Financial growth calculator that projects future value using initial investment, annual contributions, expected return, and duration.
  - **Photo Search**
    - Image search app using Unsplash API and Axios, with responsive masonry grid.
  - **quiz**
    - Timed React quiz app with answer feedback, automatic skips, and a final score summary.
  - **Score-Keeper**
    - Simple score-tracking app demonstrating React basics.
  - **Tic-Tac-Toe**
    - Classic two-player board game with turn-based play, win/draw detection, editable player names, and reset functionality.
  - **To-Do**
    - Task manager with Redux Toolkit, featuring animations and filtering.

### Fullstack

Full-stack applications combining frontend and backend.

- **foodies**
  - Recipe sharing community built with Next.js and SQLite, featuring meal browsing, recipe submission, and image upload.

### In Progress

Experimental or unfinished projects.

- **inProgress/yelp-camp-react**
  - Work-in-progress React version of the YelpCamp campground review app.

### Resources

Quick reference materials and cheatsheets.

- **Cheatsheets**
  - **hint.css**
    - CSS library for tooltips.
  - **React.js**
    - Reference guide for React concepts.

## Technologies Covered

- **Frontend**: React, Redux Toolkit, Axios, Framer Motion, Bootstrap, CSS, SASS, Next.js
- **Backend**: Express.js, MongoDB, Mongoose, FastAPI, Python, PostgreSQL, SQLite
- **Styling**: CSS, SASS, Bootstrap, Material UI
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
│   ├── bootstrap/
│   │   ├── Candy_Museum/
│   │   ├── Dating_Site_Homepage/
│   │   └── Image_Gallery/
│   ├── css/
│   │   ├── CSS_GRID_(Nexter Project)/
│   │   ├── FLEXBOX_(Trillo Project)/
│   │   └── SASS_Animations_FloatLayout_(Natours project)/
│   └── react/
│       ├── fancy-todo-list/
│       ├── Investment-Calculator/
│       ├── Photo Search/
│       ├── quiz/
│       ├── Score-Keeper/
│       ├── Tic-Tac-Toe/
│       └── To-Do/
├── fullstack/
│   └── foodies/
├── inProgress/
│   └── yelp-camp-react/
├── resources/
│   └── cheatsheets/
│       ├── hint.css/
│       └── React.js/
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
