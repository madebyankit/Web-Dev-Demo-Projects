# Fancy To-Do List

A modern to-do list manager built with React, Material UI, and IndexedDB for persistent local storage. Supports multiple lists with custom icons.

## Features

- **Multiple Lists**: Create and manage multiple to-do lists (not just one)
- **Custom Icons**: Choose from Material UI icons when creating new lists
- **Add Items**: Add tasks to any list
- **Complete Items**: Toggle tasks as done/undone with visual feedback
- **Delete Items**: Remove tasks from lists
- **Edit List Names**: Rename lists inline
- **Persistent Storage**: All data saved locally using IndexedDB (via Dexie)
- **Optimistic Updates**: Fast UI responses with SWR

## Technologies Used

- **React**: Frontend framework with hooks and context
- **Vite**: Build tool and development server
- **Material UI (MUI)**: Component library for modern UI
- **Dexie**: Wrapper for IndexedDB for local data persistence
- **SWR**: Data fetching and caching with optimistic UI updates
- **Emotion**: CSS-in-JS styling (MUI default)

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn

### Installation

1. Navigate to the project directory:

   ```bash
   cd frontend/react/fancy-todo-list
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:

   ```bash
   npm run dev
   ```

4. Open [http://localhost:5173](http://localhost:5173) in your browser.

## Project Structure

```
fancy-todo-list/
├── src/
│   ├── components/
│   │   ├── AllTodoLists.jsx      # Sidebar with all lists
│   │   ├── App.jsx              # Main app component
│   │   ├── AppHeader.jsx        # Top app bar
│   │   ├── CurrentTodoList.jsx  # Main content area
│   │   └── NewListDialog.jsx    # Dialog for creating new lists
│   ├── hooks/
│   │   ├── useTodoList.js       # Hook for single list operations
│   │   └── useTodoLists.js      # Hook for list management
│   ├── providers/
│   │   └── AppState.jsx         # React context for app state
│   ├── utils.js                 # Dexie DB + API utilities
│   └── main.jsx                 # Entry point
├── index.html
├── package.json
└── vite.config.js
```

## Usage

- Click the **+** button in the header to create a new list
- Select a list from the sidebar to view its items
- Type in the input field and press Enter (or click the send icon) to add a new task
- Click the **checkbox** to mark a task as complete
- Click the **delete** icon to remove a task
- Click the list name to rename it
