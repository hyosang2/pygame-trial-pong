# Pong Game with Pygame

Welcome to the Pong Game project! This is a simple implementation of the classic Pong game using Python and the Pygame library. The code is designed to be beginner-friendly and demonstrates key programming concepts such as Object-Oriented Programming (OOP) and the use of external libraries.

## Project Structure

- **main.py**: The main file that contains all the game logic. It uses OOP principles, with each game object (like paddles and the ball) defined as a class. The game loop handles input, updates the game state, and draws everything to the screen using Pygame's Sprite system.

## What You'll Learn

- How to set up and run a Python project locally.
- Basics of Object-Oriented Programming (OOP) in Python.
- How to use Pygame for creating simple games.

## Prerequisites

- **Python 3**: Make sure you have Python 3 installed. On macOS, you can check by running `python3 --version` in your terminal.
- **Pygame**: You will need to install the Pygame library.
- **VSCode**: This guide assumes you are using Visual Studio Code as your code editor.

## Setup Instructions

### 1. Install Python 3
- Download and install Python 3 from [python.org](https://www.python.org/downloads/) if you don't already have it.
- Confirm installation with:
  ```sh
  python3 --version
  ```

### 2. Install Pygame
- Open your terminal and run:
  ```sh
  pip3 install pygame
  ```

### 3. Open the Project in VSCode
- Open VSCode.
- Use `File > Open Folder...` and select the `pygame-trial` project directory.

### 4. Select the Python 3 Interpreter in VSCode
- Click on the Python version shown in the bottom-left or bottom-right of VSCode.
- Select a Python 3 interpreter (e.g., `/usr/bin/python3`).

### 5. Fixing the "python: command not found" Issue
- If you use the play (▶️) button or the Code Runner extension in VSCode and see `/bin/sh: python: command not found`, it means VSCode is trying to use `python` instead of `python3`.
- To fix this:
  1. Open VSCode settings (press `Cmd + ,`).
  2. Search for `code runner executor map`.
  3. Click `Edit in settings.json`.
  4. Add or update the following line:
     ```json
     "code-runner.executorMap": {
         "python": "python3 -u"
     }
     ```
  5. Save the file and try running your code again.

### 6. Run the Game
- Open `main.py`.
- Press the play (▶️) button in the top right, or right-click the file and select `Run Python File in Terminal`.
- The Pong game window should appear!

## Additional Resources
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python OOP Tutorial](https://realpython.com/python3-object-oriented-programming/)

---

Enjoy learning and have fun modifying the Pong game!
