# Investment Calculator

A React app that estimates investment growth over time using four input parameters. The calculator computes annual interest, adds annual contributions, and displays year-by-year results.

## Features

- **Initial Investment**: Starting capital for the investment plan
- **Annual Investment**: Fixed amount added each year
- **Expected Return**: Annual rate of return (percentage)
- **Duration**: Number of years to project
- **Yearly result table** with:
  - investment value at year end
  - interest earned each year
  - total interest to date
  - invested capital amount
- **Input validation** for duration greater than zero

## How It Works

The app uses a helper function to calculate investment growth each year:

- interest is calculated from the current balance
- annual contributions are added after interest is earned
- results are collected in a table for every year of the duration

## Technologies Used

- React with `useState`
- Vite build tool
- JavaScript math calculations
- `Intl.NumberFormat` for currency formatting

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn

### Installation

```bash
cd REACT/Investment-Calculator
npm install
npm run dev
```

Open the local dev server shown in the terminal, typically `http://localhost:5173`.

## Usage

- Enter the **Initial Investment** amount
- Enter the **Annual Investment** contribution
- Set the **Expected Return** percentage
- Set the **Duration** in years
- The results table updates to show how the investment grows over time

## Project Structure

```
Investment-Calculator/
├── public/                      # Static assets and images
├── src/
│   ├── components/              # UI components
│   ├── util/                    # Investment calculation helper
│   ├── App.jsx                  # Main application logic
│   ├── index.jsx                # React entry point
│   └── index.css                # Styles
├── package.json
└── vite.config.js
```
