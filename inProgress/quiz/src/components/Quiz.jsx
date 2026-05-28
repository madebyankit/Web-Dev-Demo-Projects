import { useState, useCallback } from "react";
import QUESTIONS from "../questions.js";
import quizCompleteImg from "../assets/quiz-complete.png";
import QuestionTimer from "./QuestionTimer.jsx";

export default function Quiz() {
  const [userAnswers, setUserAnswers] = useState([]);
  const activeQuestionIndex = userAnswers.length;

  const isQuizComplete = activeQuestionIndex === QUESTIONS.length; //checks if all questions answered

  const handleSelectAnswer = useCallback(function handleSelectAnswer(
    selectedAnswer,
  ) {
    setUserAnswers((prevAns) => {
      return [...prevAns, selectedAnswer];
    });
  }, []);

  const handleSkipAnswer = useCallback(
    () => handleSelectAnswer(null),
    [handleSelectAnswer],
  ); //read comment in QuestionTimer as to why we did this

  if (isQuizComplete) {
    return (
      <div id="summary">
        <img src={quizCompleteImg} alt="Quiz Completed Image" />
        <h2>Quiz Completed</h2>
      </div>
    );
  }
  //Logic only if quiz is incomplete, otherwise if quiz complete and this logic written before it breaks app
  const shuffledAnswers = [...QUESTIONS[activeQuestionIndex].answers];
  shuffledAnswers.sort(() => Math.random() - 0.5); //creating the actual shuffle

  return (
    <div id="quiz">
      <div id="questions">
        <QuestionTimer
          key={activeQuestionIndex}
          // Without key={activeQuestionIndex},
          // React reuses the same QuestionTimer component between questions.
          //
          // So timer state/effects continue instead of resetting.
          //
          // Changing the key forces React to recreate the component,
          // which resets the timer for every new question.
          timeout={10000}
          onTimeout={handleSkipAnswer} //if nothing selected timer runs out, we add null
        />
        <h2>{QUESTIONS[activeQuestionIndex].text}</h2>
        <ul id="asnwers">
          {shuffledAnswers.map((answer) => (
            <li key={answer} className="answer">
              <button onClick={() => handleSelectAnswer(answer)}>
                {answer}
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
