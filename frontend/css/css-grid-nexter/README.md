# Nexter

A modern real estate website built with CSS Grid, showcasing advanced layout techniques and responsive design.

## Features

- **CSS Grid Layout**: Comprehensive use of CSS Grid for complex layouts
- **Responsive Design**: Adapts beautifully to all screen sizes
- **Modern UI**: Clean, professional real estate interface
- **Gallery Layouts**: Grid-based image galleries
- **SASS Architecture**: Organized SCSS with build process

## Technologies Used

- **CSS Grid**: Advanced grid techniques for layout
- **SASS/SCSS**: CSS preprocessor for organization
- **HTML5**: Semantic markup
- **npm scripts**: Build automation

## Getting Started

### Prerequisites

- Node.js (for npm scripts)
- A web browser

### Installation

1. Navigate to the project directory:

   ```bash
   cd CSS/CSS_GRID_(Nexter Project)
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
│   └── components/    # Cards, buttons, etc.
│   └── layout/        # Grid, sidebar, header
├── img/               # Property images and assets
└── package.json       # Dependencies and scripts
```

## CSS Grid Features

- **Complex Layouts**: Multi-area grid layouts
- **Responsive Grids**: Grid that adapts to screen size
- **Image Galleries**: Grid-based photo galleries
- **Content Areas**: Grid for main content and sidebar
- **Card Layouts**: Property cards in grid format

## Learning Objectives

This project demonstrates:

- Advanced CSS Grid techniques
- Responsive grid layouts
- SASS/SCSS organization
- Modern CSS layout patterns
- Grid-based design systems
