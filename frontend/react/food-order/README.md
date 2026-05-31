# React Food Order

A React food ordering app built with Vite and a small Express backend. Users can browse available meals, add items to a cart, adjust quantities, open a checkout modal, and submit an order to the local backend.

## Features

- Meal catalog loaded from the backend `GET /meals` endpoint
- Cart state managed with React context and a reducer
- Cart modal with quantity increase/decrease controls
- Checkout modal with customer details form
- Order submission to the backend `POST /orders` endpoint
- Loading, success, and error states handled through a reusable HTTP hook

## Technologies Used

- React with hooks, context, reducer state, and `useActionState`
- Vite build tool
- Express backend with JSON file storage
- Fetch API for frontend/backend communication
- Global CSS through `src/index.css`

## Getting Started

### Prerequisites

- Node.js
- npm

### Installation

Install frontend dependencies:

```bash
cd frontend/react/food-order
npm install
```

Install backend dependencies:

```bash
cd frontend/react/food-order/backend
npm install
```

### Running the App

Start the backend API in one terminal:

```bash
cd frontend/react/food-order/backend
npm start
```

The backend listens on `http://localhost:3000`.

Start the frontend in a second terminal:

```bash
cd frontend/react/food-order
npm run dev
```

Open the local Vite URL shown in the terminal, typically `http://localhost:5173`.

## Usage

1. Browse meals on the home screen.
2. Click `Add to Cart` to add meals.
3. Open the cart from the header to review quantities and the total.
4. Continue to checkout and fill in the customer form.
5. Submit the order. Valid orders are written to `backend/data/orders.json`.

## API Overview

- `GET /meals`
  - Reads `backend/data/available-meals.json`
  - Returns the list of meals rendered by `Meals.jsx`
- `POST /orders`
  - Accepts an order with `items` and `customer` data
  - Validates customer fields and cart contents
  - Adds a generated ID and stores the order in `backend/data/orders.json`

## Project Structure

```text
food-order/
├── backend/
│   ├── app.js
│   ├── data/
│   │   ├── available-meals.json
│   │   └── orders.json
│   ├── public/
│   │   └── images/
│   └── package.json
├── public/
│   └── logo.jpg
├── src/
│   ├── assets/
│   │   └── logo.jpg
│   ├── components/
│   │   ├── UI/
│   │   │   ├── Button.jsx
│   │   │   ├── Input.jsx
│   │   │   └── Modal.jsx
│   │   ├── Cart.jsx
│   │   ├── CartItem.jsx
│   │   ├── Checkout.jsx
│   │   ├── Error.jsx
│   │   ├── Header.jsx
│   │   ├── MealItem.jsx
│   │   └── Meals.jsx
│   ├── hooks/
│   │   └── useHttp.js
│   ├── store/
│   │   ├── CartContext.jsx
│   │   └── UserProgressContext.jsx
│   ├── util/
│   │   └── formatting.js
│   ├── App.jsx
│   ├── index.css
│   └── main.jsx
├── index.html
├── package.json
└── vite.config.js
```

## Code Flow

- `main.jsx` renders the React app into the page.
- `App.jsx` wraps the UI with `UserProgressContextProvider` and `CartContextProvider`, then renders the header, meal list, cart modal, and checkout modal.
- `Meals.jsx` uses `useHttp` to fetch meals from `http://localhost:3000/meals` and renders each one through `MealItem.jsx`.
- `MealItem.jsx` adds selected meals to the cart through `CartContext`.
- `CartContext.jsx` owns cart items and exposes `addItem`, `removeItem`, and `clearCart`.
- `UserProgressContext.jsx` tracks whether the user is viewing the cart, checkout, or normal page state.
- `Cart.jsx` reads cart data, calculates the total, and moves the user to checkout.
- `Checkout.jsx` submits the final order through `useHttp` and clears the cart after a successful order.
- `backend/app.js` serves meal data, validates submitted orders, and writes successful orders to the JSON data file.

## Learning Focus

This project demonstrates React context for shared state, reducer-based cart updates, reusable custom hooks for HTTP requests, modal-driven user flow, form submission with `useActionState`, and a simple frontend-to-backend integration.
