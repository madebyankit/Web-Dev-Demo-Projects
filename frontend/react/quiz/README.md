# React Quiz

A timed React quiz app built with Vite. Users answer multiple-choice React questions, get immediate feedback, and receive a final summary showing skipped, correct, and incorrect answers.

## Features

- Multiple-choice quiz questions loaded from `questions.js`
- Timed question flow with automatic skip on timeout
- Answer states for selected, correct, and wrong responses
- Per-question feedback delay before moving forward
- Final results summary with percentages
- Review list showing every question and the user's answer

## Technologies Used

- React with hooks
- Vite build tool
- JavaScript modules
- CSS animations and progress styling

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn

### Installation

```bash
cd frontend/react/quiz
npm install
npm run dev
```

Open the local dev server shown in the terminal, typically `http://localhost:5173`.

## Usage

- Choose one answer before the timer runs out
- If no answer is selected, the question is marked as skipped
- After selecting an answer, the app briefly highlights the choice and then shows whether it was correct
- After the last question, the summary screen shows the final score breakdown

## Project Structure

```text
quiz/
├── public/
│   └── quiz-logo.png
├── src/
│   ├── assets/
│   │   └── quiz-complete.png
│   ├── components/
│   │   ├── Answers.jsx
│   │   ├── Header.jsx
│   │   ├── Question.jsx
│   │   ├── QuestionTimer.jsx
│   │   ├── Quiz.jsx
│   │   └── Summary.jsx
│   ├── App.jsx
│   ├── main.jsx
│   ├── index.css
│   └── questions.js
├── index.html
├── package.json
└── vite.config.js
```

## Learning Focus

This project demonstrates component composition, `useState`, `useCallback`, timers with side effects, conditional rendering, and deriving summary data from state.
