
const guessInput = document.getElementById("guess");
const guessButton = document.getElementById("guess-button");
const restartButton = document.getElementById("restart");
const message = document.getElementById("message");
const attemptsDisplay = document.getElementById("attempts");

const computerStatus = document.getElementById("computer-status");
const computerAttemptsDisplay = document.getElementById("computer-attempts");
const computerSteps = document.getElementById("computer-steps");
const duelResult = document.getElementById("duel-result");

let secretNumber;
let attempts;
let gameFinished;

function startGame() {
    secretNumber = Math.floor(Math.random() * 100) + 1;
    attempts = 0;
    gameFinished = false;

    attemptsDisplay.textContent = attempts;
    message.textContent = "Жду твою догадку…";
    guessInput.value = "";
    guessInput.disabled = false;
    guessButton.disabled = false;

    computerStatus.textContent = "Жду, пока ты найдёшь число…";
    computerAttemptsDisplay.textContent = "—";
    computerSteps.replaceChildren();
    duelResult.hidden = true;
    duelResult.replaceChildren();

    guessInput.focus();
}

function runComputerSearch() {
    let low = 1;
    let high = 100;
    let computerAttempts = 0;

    const searchSteps = [];

    while (low <= high) {
        const middle = Math.floor((low + high) / 2);
        computerAttempts += 1;

        const word = computerAttempts === 1 ? "Попытка" : "попытка";
        searchSteps.push(`${word} ${computerAttempts}: ${middle}`);

        if (middle === secretNumber) {
            break;
        }

        if (middle < secretNumber) {
            low = middle + 1;
        } else {
            high = middle - 1;
        }
    }

    computerSteps.textContent = searchSteps.join(", ");

    computerAttemptsDisplay.textContent = computerAttempts;
    computerStatus.textContent =
        `Нашёл число ${secretNumber} бинарным поиском!`;

    duelResult.hidden = false;

    const title = document.createElement("h3");
    title.textContent = "🏆 Результаты соревнования";

    const humanResult = document.createElement("p");
    humanResult.textContent = `Ты: ${attempts} попыток`;

    const computerResult = document.createElement("p");
    computerResult.textContent =
        `Компьютер: ${computerAttempts} попыток`;

    const conclusion = document.createElement("p");

    if (attempts < computerAttempts) {
        conclusion.textContent = "В этот раз ты оказался быстрее!";
    } else if (attempts > computerAttempts) {
        conclusion.textContent =
            "В этот раз компьютер нашёл число за меньшее количество попыток!";
    } else {
        conclusion.textContent = "Ничья по количеству попыток!";
    }

    duelResult.append(title, humanResult, computerResult, conclusion);
}

function checkGuess() {
    if (gameFinished) {
        return;
    }

    const guess = Number(guessInput.value);

    if (
        guessInput.value.trim() === ""
        || !Number.isInteger(guess)
        || guess < 1
        || guess > 100
    ) {
        message.textContent = "Введи целое число от 1 до 100.";
        return;
    }

    attempts += 1;
    attemptsDisplay.textContent = attempts;

    if (guess === secretNumber) {
        message.textContent =
            `Угадал! Это число ${secretNumber}!`;
        gameFinished = true;
        guessInput.disabled = true;
        guessButton.disabled = true;

        runComputerSearch();
        return;
    }

    if (guess < secretNumber) {
        message.textContent = "Загаданное число больше ↑";
    } else {
        message.textContent = "Загаданное число меньше ↓";
    }

    guessInput.value = "";
    guessInput.focus();
}

guessButton.addEventListener("click", checkGuess);

guessInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        checkGuess();
    }
});

restartButton.addEventListener("click", startGame);

startGame();