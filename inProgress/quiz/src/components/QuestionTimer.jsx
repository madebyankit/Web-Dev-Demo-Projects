import { useState, useEffect } from "react";

export default function QuestionTimer({ timeout, onTimeout }) {
  const [remainingTime, setRemainingTime] = useState(timeout);

  useEffect(() => {
    const timer = setTimeout(() => {
      onTimeout();
    }, timeout);

    return () => {
      clearTimeout(timer);
    };
  }, [timeout, onTimeout]);

  useEffect(() => {
    const interval = setInterval(() => {
      setRemainingTime((prevRemainingTime) => prevRemainingTime - 100);
    }, 100);

    return () => {
      clearInterval(interval);
    };
  }, []);

  return <progress id="question-time" max={timeout} value={remainingTime} />;
}

// If useEffect depends on a function or objects which are stored differently from variables:
//
// useEffect(..., [someFunction])
//
// and inside effect we update state:
//
// setState(...)
//
//
// Then:
//
// state update
// -> component re-renders
// -> function gets recreated in memory
// -> dependency looks changed
// -> useEffect runs again
// -> state updates again
//
// This can accidentally create infinite render loops.

// A workaround this is to wrap functions that work on state in useCallback.
