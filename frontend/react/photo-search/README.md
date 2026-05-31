# Photo Search App

A React application that allows users to search for high-quality photos using the Unsplash API. Features a responsive masonry grid layout for displaying search results.

## Features

- **Photo Search**: Search for photos using keywords through the Unsplash API
- **Masonry Grid Layout**: Responsive grid that adjusts image heights dynamically
- **Semantic UI Styling**: Clean, modern interface using Semantic UI components
- **Real-time Search**: Instant search results as you submit queries

## Technologies Used

- **React**: Frontend framework with class components
- **Axios**: HTTP client for API requests
- **Unsplash API**: Photo database and search functionality
- **Semantic UI**: CSS framework for styling
- **CSS Grid**: Modern layout system for masonry effect

## Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn
- Unsplash API key (get one from [Unsplash Developers](https://unsplash.com/developers))

### Installation

1. Navigate to the project directory:

   ```bash
   cd "frontend/react/Photo Search"
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Create a `.env` file in the root directory and add your Unsplash API key:

   ```
   REACT_APP_unsplashID=your_unsplash_access_key_here
   ```

4. Start the development server:

   ```bash
   npm start
   ```

5. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

```
src/
├── api/
│   └── unsplash.js          # Axios configuration for Unsplash API
├── components/
│   ├── App.js               # Main application component
│   ├── SearchBar.js         # Search input component
│   ├── ImageList.js         # Grid container for images
│   ├── ImageCard.js         # Individual image component
│   └── ImageList.css        # Grid layout styles
├── index.js                 # Application entry point
└── index.css                # Global styles
```

## How It Works

1. **Search**: Users enter search terms in the search bar
2. **API Call**: App makes a request to Unsplash API with the search query
3. **Display**: Results are displayed in a responsive masonry grid
4. **Dynamic Sizing**: Images are sized based on their aspect ratios for optimal layout

## API Configuration

The app uses the Unsplash API for photo search. You'll need to:

1. Sign up for a free Unsplash developer account
2. Get your access key
3. Add it to your `.env` file as `REACT_APP_unsplashID`

## Available Scripts

- `npm start` - Runs the app in development mode
- `npm test` - Launches the test runner
- `npm run build` - Builds the app for production
- `npm run eject` - Ejects from Create React App (irreversible)

## Features in Detail

### Masonry Layout

The app uses CSS Grid with dynamic row spans to create a Pinterest-style masonry layout. Each image calculates its required grid rows based on its height, ensuring a visually balanced display.

### Responsive Design

The grid automatically adjusts to different screen sizes using `repeat(auto-fill, minmax(250px, 1fr))`, making it work well on both desktop and mobile devices.

### Semantic UI Integration

The search bar uses Semantic UI form components for a polished, accessible interface.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Acknowledgments

- [Unsplash](https://unsplash.com/) for providing the photo API
- [Semantic UI](https://semantic-ui.com/) for the UI framework
