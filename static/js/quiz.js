// Quiz functionality
document.addEventListener("DOMContentLoaded", function () {
  // Initialize variables
  let currentQuestionIndex = 0;
  let score = 0;
  const questions = quizQuestions; // quizQuestions is defined in quiz_interface.html
  let selectedAnswer = null;
  let quizCompleted = false;

  // Store user answers for server submission
  const userAnswers = [];

  // DOM elements
  const questionText = document.getElementById("question-text");
  const optionA = document.getElementById("option-a");
  const optionB = document.getElementById("option-b");
  const optionC = document.getElementById("option-c");
  const optionD = document.getElementById("option-d");
  const labelA = document.getElementById("label-option-a");
  const labelB = document.getElementById("label-option-b");
  const labelC = document.getElementById("label-option-c");
  const labelD = document.getElementById("label-option-d");
  const submitButton = document.getElementById("submit-button");
  const feedbackArea = document.getElementById("feedback-area");
  const progressIndicator = document.getElementById("progress-indicator");
  const scoreArea = document.getElementById("score-area");
  const questionArea = document.getElementById("question-area");

  // Option radio buttons
  const options = document.querySelectorAll('input[name="option"]');

  // Add event listeners for option selection
  options.forEach((option) => {
    option.addEventListener("change", function () {
      selectedAnswer = this.value;
      submitButton.disabled = false;
    });
  });

  // Add event listener for the submit button
  submitButton.addEventListener("click", function () {
    if (quizCompleted) {
      // Show results at the end of the quiz
      submitQuizToServer();
      return;
    }

    if (!selectedAnswer && submitButton.textContent === "Submit Answer") {
      // Don't proceed if no answer is selected (should not happen with disabled button)
      return;
    }

    // If showing feedback, proceed to next question
    if (submitButton.textContent === "Next Question") {
      currentQuestionIndex++;
      loadQuestion();
      return;
    }

    // Check the answer
    const currentQuestion = questions[currentQuestionIndex];
    const isCorrect = selectedAnswer === currentQuestion.correct_option;

    // Store the user's answer
    userAnswers[currentQuestionIndex] = {
      question_id: currentQuestion.id,
      selected_option: selectedAnswer,
    };

    // Update score if correct (client-side, but final score will be calculated on server)
    if (isCorrect) {
      score++;
    }

    // Show feedback
    showFeedback(isCorrect, currentQuestion.explanation);

    // Change button text for next action
    if (currentQuestionIndex < questions.length - 1) {
      submitButton.textContent = "Next Question";
    } else {
      submitButton.textContent = "Show Results";
      quizCompleted = true;
    }
  });

  // Function to submit the quiz to the server
  function submitQuizToServer() {
    // Display a loading message in score area
    scoreArea.classList.remove("hidden");
    scoreArea.innerHTML = "<p>Submitting your quiz results...</p>";
    questionArea.style.display = "none";
    feedbackArea.classList.add("hidden");
    progressIndicator.style.display = "none";

    // Check if user is logged in
    if (!isLoggedIn) {
      scoreArea.innerHTML = `
        <h3>Quiz Complete!</h3>
        <p class="final-score">You scored ${score} out of ${
        questions.length
      } (${Math.round((score / questions.length) * 100)}%)</p>
        <p>Note: Log in to save your quiz results and track your progress!</p>
        <a href="javascript:location.reload()" class="retry-button">Try Again</a>
      `;
      return;
    }

    // Prepare data for submission
    const quizData = {
      answers: userAnswers,
      topic: quizTopic,
    };

    // Send the data to the server
    fetch(submitQuizUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken(), // If using CSRF protection
      },
      body: JSON.stringify(quizData),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        // Show results from server
        scoreArea.innerHTML = `
        <h3>Quiz Complete!</h3>
        <p class="final-score">You scored ${data.score} out of ${data.total_questions} (${data.percentage}%)</p>
        <p>Your result has been saved!</p>
        <p><a href="/my_progress/" class="progress-link">View All My Progress</a></p>
        <a href="javascript:location.reload()" class="retry-button">Try Again</a>
      `;
      })
      .catch((error) => {
        console.error("Error submitting quiz:", error);
        scoreArea.innerHTML = `
        <h3>Quiz Complete!</h3>
        <p class="final-score">You scored ${score} out of ${
          questions.length
        } (${Math.round((score / questions.length) * 100)}%)</p>
        <p class="error">There was an error saving your results. Please try again later.</p>
        <a href="javascript:location.reload()" class="retry-button">Try Again</a>
      `;
      });
  }

  // Helper function to get CSRF token from cookies
  function getCSRFToken() {
    const name = "csrf_token=";
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookieArray = decodedCookie.split(";");

    for (let i = 0; i < cookieArray.length; i++) {
      let cookie = cookieArray[i].trim();
      if (cookie.indexOf(name) === 0) {
        return cookie.substring(name.length, cookie.length);
      }
    }
    return "";
  }

  // Function to load a question
  function loadQuestion() {
    // Reset state
    selectedAnswer = null;
    submitButton.disabled = true;
    submitButton.textContent = "Submit Answer";
    feedbackArea.classList.add("hidden");
    feedbackArea.innerHTML = "";

    // Reset option selection and styling
    options.forEach((option) => {
      option.checked = false;
      option.parentElement.classList.remove("correct", "incorrect");
    });

    // Update progress indicator
    progressIndicator.textContent = `Question ${currentQuestionIndex + 1} of ${
      questions.length
    }`;

    // Get current question
    const question = questions[currentQuestionIndex];

    // Create options array for randomization
    const optionsArray = [
      { value: "A", text: question.option_a },
      { value: "B", text: question.option_b },
      { value: "C", text: question.option_c },
      { value: "D", text: question.option_d },
    ];

    // Randomize options order
    shuffleArray(optionsArray);

    // Update question text
    questionText.textContent = question.question_text;

    // Apply randomized options
    labelA.textContent = optionsArray[0].text;
    optionA.value = optionsArray[0].value;

    labelB.textContent = optionsArray[1].text;
    optionB.value = optionsArray[1].value;

    labelC.textContent = optionsArray[2].text;
    optionC.value = optionsArray[2].value;

    labelD.textContent = optionsArray[3].text;
    optionD.value = optionsArray[3].value;
  }

  // Helper function to shuffle an array (Fisher-Yates algorithm)
  function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

  // Function to show feedback
  function showFeedback(isCorrect, explanation) {
    feedbackArea.classList.remove("hidden");

    // Create feedback content
    const resultText = document.createElement("p");
    resultText.className = isCorrect ? "correct-answer" : "incorrect-answer";
    resultText.textContent = isCorrect ? "Correct!" : "Incorrect!";
    feedbackArea.appendChild(resultText);

    // Show correct answer if wrong
    if (!isCorrect) {
      const correctOptionText = document.createElement("p");
      correctOptionText.className = "correct-option";
      const correctOption = questions[currentQuestionIndex].correct_option;

      // Find which display position has the correct answer value
      let correctDisplayLabel = "";
      if (optionA.value === correctOption) {
        correctDisplayLabel = labelA.textContent;
      } else if (optionB.value === correctOption) {
        correctDisplayLabel = labelB.textContent;
      } else if (optionC.value === correctOption) {
        correctDisplayLabel = labelC.textContent;
      } else if (optionD.value === correctOption) {
        correctDisplayLabel = labelD.textContent;
      }

      correctOptionText.textContent = `The correct answer is: ${correctOption}. ${correctDisplayLabel}`;
      feedbackArea.appendChild(correctOptionText);
    }

    // Add explanation if available
    if (explanation) {
      const explanationText = document.createElement("p");
      explanationText.className = "explanation";
      explanationText.textContent = `Explanation: ${explanation}`;
      feedbackArea.appendChild(explanationText);
    }

    // Highlight correct/incorrect options
    // Find which option element has the correct answer value
    let correctOptionElement = null;
    if (optionA.value === questions[currentQuestionIndex].correct_option) {
      correctOptionElement = optionA;
    } else if (
      optionB.value === questions[currentQuestionIndex].correct_option
    ) {
      correctOptionElement = optionB;
    } else if (
      optionC.value === questions[currentQuestionIndex].correct_option
    ) {
      correctOptionElement = optionC;
    } else if (
      optionD.value === questions[currentQuestionIndex].correct_option
    ) {
      correctOptionElement = optionD;
    }

    if (correctOptionElement) {
      correctOptionElement.parentElement.classList.add("correct");
    }

    if (!isCorrect && selectedAnswer) {
      // Find which option element has the selected answer value
      let selectedOptionElement = null;
      if (optionA.value === selectedAnswer) {
        selectedOptionElement = optionA;
      } else if (optionB.value === selectedAnswer) {
        selectedOptionElement = optionB;
      } else if (optionC.value === selectedAnswer) {
        selectedOptionElement = optionC;
      } else if (optionD.value === selectedAnswer) {
        selectedOptionElement = optionD;
      }

      if (selectedOptionElement) {
        selectedOptionElement.parentElement.classList.add("incorrect");
      }
    }
  }

  // Load the first question
  loadQuestion();
});
