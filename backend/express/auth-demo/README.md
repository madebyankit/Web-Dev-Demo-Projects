# Auth Demo

A small Express and MongoDB authentication demo. It shows how to register users, hash passwords with bcrypt, create login sessions, protect private routes, and log users out.

## Features

- Register users with username and password
- Hash passwords before saving them to MongoDB
- Validate login credentials with a custom Mongoose static method
- Store logged-in user state with `express-session`
- Protect `/secret` and `/topsecret` with a login middleware
- Render login, register, and secret pages with EJS

## Technologies Used

- Express
- MongoDB and Mongoose
- EJS
- bcrypt
- express-session

## Getting Started

### Prerequisites

- Node.js
- npm
- MongoDB running locally

### Installation

```bash
cd backend/express/auth-demo
npm install
node index.js
```

Open `http://localhost:3000` in your browser.

## Routes

- `GET /` - simple home response
- `GET /register` - registration form
- `POST /register` - create a user and start a session
- `GET /login` - login form
- `POST /login` - authenticate a user
- `POST /logout` - clear the active session
- `GET /secret` - protected EJS page
- `GET /topsecret` - protected text response

## Project Structure

```text
auth-demo/
├── models/
│   └── user.js       # User schema, password hashing, login validation
├── views/
│   ├── login.ejs
│   ├── register.ejs
│   └── secret.ejs
├── index.js          # Express app, routes, session setup
└── package.json
```

## Notes

- The app connects to `mongodb://localhost:27017/loginDemo`.
- The session secret is hardcoded for learning purposes. Use an environment variable for real applications.
- `package.json` does not define a start script, so run the app with `node index.js`.
