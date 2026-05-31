# To-Do App

A modern, animated To-Do application built with React, Redux Toolkit, and Framer Motion.

## Features

- **Add Todos**: Create new to-do items with a simple input field
- **Edit Todos**: Double-click or use the edit button to modify existing todos
- **Complete Todos**: Mark todos as completed with a checkmark
- **Remove Todos**: Delete todos with the remove button
- **Filter Todos**: View active, completed, or all todos with filter buttons
- **Smooth Animations**: Beautiful animations powered by Framer Motion
- **Responsive Design**: Works on desktop and mobile devices

## Technologies Used

- **React**: Frontend framework for building the user interface
- **Redux Toolkit**: State management for handling todo data
- **Framer Motion**: Animation library for smooth UI transitions
- **React Icons**: Icon library for buttons and UI elements
- **CSS**: Custom styling with gradients and modern design

## Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn

### Installation

1. Navigate to the project directory:

   ```bash
   cd frontend/react/To-Do
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:

   ```bash
   npm start
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

```
src/
├── components/
│   ├── Todos.js          # Input component for adding new todos
│   ├── DisplayTodos.js   # Container for displaying and filtering todos
│   └── TodoItem.js       # Individual todo item component
├── redux/
│   ├── store.js          # Redux store configuration
│   └── reducer.js        # Todo state management logic
├── css/
│   └── main.css          # Main stylesheet
├── App.js                # Main application component
└── index.js              # Application entry point
```

## Available Scripts

- `npm start` - Runs the app in development mode
- `npm test` - Launches the test runner
- `npm run build` - Builds the app for production
- `npm run eject` - Ejects from Create React App (irreversible)

## Usage

1. **Adding a Todo**: Type in the input field and click the + button or press Enter
2. **Editing a Todo**: Click the edit icon or double-click the text to edit inline
3. **Completing a Todo**: Click the green checkmark to mark as completed
4. **Removing a Todo**: Click the red X to delete the todo
5. **Filtering Todos**: Use the Active, Completed, or All buttons to filter the view

## State Management

The app uses Redux Toolkit for state management with the following actions:

- `addTodos`: Adds a new todo to the state
- `removeTodos`: Removes a todo by ID
- `updateTodos`: Updates a todo's text
- `completeTodos`: Marks a todo as completed

## Animations

Framer Motion is used throughout the app for:

- Page entrance animations
- Button hover and tap effects
- Todo item slide-in/out animations
- Filter button interactions

## Styling

The app features:

- Gradient background (green to dark green)
- Custom font (RocknRoll One)
- Card-based layout for todos
- Responsive design
- Dark theme with light text

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Notes

This app was created with Create React App, so it uses `npm start` for local development instead of Vite's `npm run dev`.
