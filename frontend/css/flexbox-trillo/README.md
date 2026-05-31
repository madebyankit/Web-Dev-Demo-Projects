# Trillo

A responsive hotel booking application interface built with CSS Flexbox. Features a modern, clean design for travel booking.

## Features

- **Flexbox Layout**: Comprehensive use of CSS Flexbox for complex layouts
- **Responsive Design**: Adapts to different screen sizes
- **Modern UI**: Clean, professional booking interface
- **Component-Based**: Modular CSS architecture
- **SASS Compilation**: Organized development workflow

## Technologies Used

- **CSS Flexbox**: Advanced flexbox techniques for layout
- **SASS/SCSS**: CSS preprocessor for better organization
- **HTML5**: Semantic markup
- **npm scripts**: Build automation

## Getting Started

### Prerequisites

- Node.js (for npm scripts)
- A web browser

### Installation

1. Navigate to the project directory:

   ```bash
   cd CSS/FLEXBOX_(Trillo Project)
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Compile SASS and start development:
   ```bash
   npm run start
   ```

### Manual Build

For production build:

```bash
npm run build:css
```

## Available Scripts

- `npm run watch:sass` - Watch SASS files and compile on changes
- `npm run devserver` - Start live server for development
- `npm run start` - Run both watch and dev server in parallel
- `npm run compile:sass` - Compile SASS to CSS
- `npm run prefix:css` - Add vendor prefixes
- `npm run compress:css` - Compress CSS for production
- `npm run build:css` - Full build pipeline

## Project Structure

```
├── index.html          # Main HTML file
├── css/
│   └── style.css       # Compiled CSS
├── sass/
│   ├── main.scss       # Main SASS file
│   └── abstracts/      # Variables, mixins
│   └── base/          # Reset, typography
│   └── components/    # Buttons, forms, etc.
│   └── layout/        # Header, navigation, grid
├── img/               # Images and assets
└── package.json       # Dependencies and scripts
```

## CSS Flexbox Features

- **Flexible Navigation**: Responsive header with search
- **Card Layouts**: Hotel and activity cards
- **Sidebar Layout**: Main content with sidebar
- **Footer Layout**: Multi-column footer
- **Responsive Grids**: Flexbox-based grid systems

## Learning Objectives

This project demonstrates:

- Advanced CSS Flexbox techniques
- Responsive web design with flexbox
- SASS/SCSS organization
- Component-based CSS architecture
- Modern layout patterns
