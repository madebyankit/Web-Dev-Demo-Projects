# Natours

A responsive landing page for a fictional adventure tour company, built with advanced CSS, SASS, and animations.

## Features

- **Modern Design**: Clean, professional layout for a tour booking website
- **SASS Architecture**: Organized SCSS files with partials and variables
- **CSS Animations**: Smooth animations and transitions throughout
- **Responsive Layout**: Mobile-first design that works on all devices
- **Custom Icons**: Icon font for consistent visual elements
- **Advanced CSS**: Float layouts, transforms, and modern techniques

## Technologies Used

- **SASS/SCSS**: CSS preprocessor for better organization
- **CSS**: Advanced selectors, animations, and layouts
- **HTML5**: Semantic markup
- **npm scripts**: Build process for SASS compilation

## Getting Started

### Prerequisites

- Node.js (for npm scripts)
- A web browser

### Installation

1. Navigate to the project directory:

   ```bash
   cd CSS/SASS_Animations_FloatLayout_(Natours project)
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Compile SASS and start development:
   ```bash
   npm run start
   ```

This will watch for SASS changes and compile them automatically.

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
- `npm run concat:css` - Concatenate CSS files
- `npm run prefix:css` - Add vendor prefixes
- `npm run compress:css` - Compress CSS for production
- `npm run build:css` - Full build pipeline

## Project Structure

```
├── index.html          # Main HTML file
├── css/
│   ├── style.css       # Compiled CSS
│   └── icon-font.css   # Custom icon font
├── sass/
│   ├── main.scss       # Main SASS file
│   └── abstracts/      # Variables, mixins, functions
│   └── base/          # Reset, typography
│   └── components/    # Buttons, cards, etc.
│   └── layout/        # Header, footer, grid
│   └── pages/         # Page-specific styles
├── img/               # Images and assets
└── package.json       # Dependencies and scripts
```

## Features Demonstrated

- **SASS Architecture**: 7-1 pattern with organized partials
- **CSS Animations**: Keyframe animations and transitions
- **Float Layouts**: Traditional CSS layout techniques
- **Responsive Design**: Media queries and flexible layouts
- **CSS Transforms**: Scale, rotate, and translate effects
- **Custom Properties**: CSS variables for theming

## Browser Support

Works in all modern browsers. Uses Autoprefixer for vendor prefixes.

## Learning Objectives

This project demonstrates:

- Advanced CSS techniques and animations
- SASS/SCSS organization and compilation
- Build processes with npm scripts
- Responsive web design principles
- CSS architecture patterns
