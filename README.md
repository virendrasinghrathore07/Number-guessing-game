# 🎯 Number Guessing Game

A simple and interactive **Number Guessing Game** built using **Python**.

In this game, the player chooses a difficulty level and tries to guess a randomly generated number within a limited number of attempts.

## 🎮 Features

* 🎯 Three difficulty levels:

  * **Easy:** Number between 1 and 100
  * **Medium:** Number between 1 and 500
  * **Hard:** Number between 1 and 1000
* 🔢 Random number generation using Python's `random` module
* ❤️ Maximum **10 attempts** per game
* 📈 Helpful hints:

  * `Too Big` if the guess is greater than the secret number
  * `Too Small` if the guess is smaller than the secret number
* 🏆 Winning message when the correct number is guessed
* 🔄 Option to play the game again
* ❌ Game ends automatically after 10 incorrect attempts

## 🛠️ Technologies Used

* **Python**
* **Random Module**
* **Loops**
* **If-Else Conditions**
* **User Input**
* **Formatted Strings (f-strings)**

## 📂 Project Structure

```text
Number-Guessing-Game/
│
├── number_guessing_game.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### 2. Go to the Project Folder

```bash
cd Number-Guessing-Game
```

### 3. Run the Python File

```bash
python number_guessing_game.py
```

## 🎯 How to Play

1. Run the program.
2. Choose your difficulty level.
3. The computer generates a random number.
4. Enter your guess.
5. The game will tell you whether your guess is:

   * **Too Big**
   * **Too Small**
   * **Correct**
6. You have a maximum of **10 attempts**.
7. After the game ends, you can choose whether to play again.

## 🖥️ Example

```text
==========NUMBER GUESSING GAME==========
Choose Your Difficulty
1. Easy  (1,100)
2. Medium  (1,500)
3. Hard  (1,1000)

Enter Your choice : 1

You choosed Easy level So guess the number between (1,100)

10 attempts left !!
Enter your guess : 50
Too Small

9 attempts left !!
Enter your guess : 75
Too Big

8 attempts left !!
Enter your guess : 63
Congratulation !! You Won the Game.

You guessed the number in 3 attempt

Do you want to play again : no

Thanks! for playing !!
```

## 📚 Concepts Practiced

This project helped practice the following Python concepts:

* Variables
* `input()`
* `print()`
* Type conversion using `int()`
* `if`, `elif`, and `else`
* `while` loops
* `break`
* `exit()`
* `random.randint()`
* f-strings
* String methods like `.lower()`

## 🔮 Future Improvements

Some features that can be added in the future:

* ⭐ Different number of attempts for each difficulty
* 🏆 Score system
* 📊 High-score tracking
* ⏱️ Timer
* 🔢 Custom number range
* 📝 Game statistics
* 🎨 GUI version using Tkinter
* 🔊 Sound effects
* 💾 Save scores to a file

## 👨‍💻 Author

**Virendra Singh Rathore**

B.Tech CSE | AI & Data Science

---

⭐ If you like this project, consider giving the repository a star!
