# Asteroids - Pygame Implementation

This project is a clone of the classic arcade game Asteroids, implemented using Python and the Pygame library. It serves as a demonstration of object-oriented programming principles and game 
development skills.  This project was a great learning experience, allowing me to solidify my understanding of several key concepts in Python game development.

## Table of Contents

- [Introduction](#introduction)
- [Gameplay](#gameplay)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Object-Oriented Programming](#object-oriented-programming)
- [Challenges and Lessons Learned](#challenges-and-lessons-learned)
- [Future Improvements](#future-improvements)
- [Acknowledgements](#acknowledgements)


## Introduction

Asteroids is a classic arcade space shooter where the player controls a spaceship and must destroy asteroids by shooting them while avoiding collisions. This project aims to recreate the 
core mechanics and feel of the original game using Python and the Pygame library. It's a personal project intended to enhance my game development skills and showcase my understanding of 
object-oriented programming.

## Gameplay

The player controls a spaceship that can rotate, accelerate, and fire projectiles. Asteroids of varying sizes populate the game world.  Larger asteroids break into smaller ones when hit, 
adding a layer of increasing difficulty. The goal is to survive as long as possible by destroying all the asteroids.  The game ends when the player's ship collides with an asteroid.

## Features

*   **Object-Oriented Design:**  The game utilizes OOP principles to manage game entities like the player, asteroids, and projectiles.
*   **Collision Detection:**  Accurate collision detection between the player, asteroids, and projectiles.
*   **Score Tracking:**  Keeps track of the player's score based on destroyed asteroids.
*   **Level Progression:** As the player progresses, more asteroids are added, increasing the difficulty.
*   **Classic Asteroids Movement:**  The spaceship and asteroids wrap around the screen edges.
*   **Sound Effects:**  Implements sound effects for shooting and explosions (if implemented, mention specific sounds used).
*   **Responsive Controls:**  Smooth and responsive controls for ship movement and shooting.

## Technologies Used

*   **Python:** The core programming language used for the game's logic and structure.
*   **Pygame:** A cross-platform Python library used for creating games and multimedia applications.  It provides modules for handling graphics, sound, and user input, which were essential 
for this project.  I learned a lot about using Pygame's sprite system, collision detection, and event handling.
*   **(Optional) Other Libraries:** If used any, list and describe the purpose.  For example:
    *   `math`: For trigonometric calculations related to ship movement and projectile trajectories.
    *   `random`: For generating random asteroid positions and movement.

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/juanezamudio/asteroids.git](https://github.com/juanezamudio/asteroids.git)
    ```

2.  **Navigate to the Directory:**
    ```bash
    cd asteroids
    ```

3.  **Install Dependencies:**  It's highly recommended to use a virtual environment to manage dependencies.
    ```bash
    python3 -m venv .venv  # Create a virtual environment
    source .venv/bin/activate  # Activate the environment (Linux/macOS)
    .venv\Scripts\activate  # Activate the environment (Windows)
    pip install -r requirements.txt # Install project dependencies (create requirements.txt if needed)
    ```

4.  **Run the Game:**
    ```bash
    python main.py
    ```

## How to Play

*   **Up Arrow:** Accelerate the spaceship.
*   **Left Arrow:** Rotate the spaceship counter-clockwise.
*   **Right Arrow:** Rotate the spaceship clockwise.
*   **Spacebar:** Fire projectiles.
*   **(Optional) Other Controls:**  Mention any other controls implemented.

## Project Structure

asteroids/
├── main.py          # Main game file
├── player.py        # Player class and logic
├── asteroid.py      # Asteroid class and logic
├── projectile.py    # Projectile class and logic
├── game_utils.py   # Helper functions and game constants
├── assets/          # Sprites, sounds, and other media
│   ├── ...
├── requirements.txt # Project dependencies
└── README.md        # This file

## Object-Oriented Programming

This project heavily utilizes object-oriented programming principles:

*   **Classes:** The game is built around classes representing different game entities (Player, Asteroid, Projectile). This makes the code modular and easier to maintain.
*   **Inheritance:**  (If used) Explain how inheritance is used, for example, if different types of asteroids inherit from a base Asteroid class.
*   **Encapsulation:** Data and methods are encapsulated within classes, protecting them from direct external access and promoting code organization.
*   **Polymorphism:** (If used) Explain how polymorphism is used, e.g., if different game entities have a common `update()` method that behaves differently for each entity.

## Challenges and Lessons Learned

*   **Collision Detection:**  Implementing accurate and efficient collision detection was a key challenge. I learned about different collision detection methods and how to optimize them for game performance.
*   **Game Loop Management:**  Understanding and managing the game loop, including event handling, updating game state, and rendering, was crucial.
*   **Pygame's Sprite System:**  I gained significant experience with Pygame's sprite system, which simplifies the management of game entities.
*   **(Add your personal challenges and what you learned from them)**  For example, "Balancing the game difficulty was challenging. I learned how to adjust parameters like asteroid speed and spawn rate to create a fun and engaging experience."

## Future Improvements

*   **More Game Modes:**  Adding different game modes, such as a survival mode or a timed mode.
*   **Power-ups:**  Implementing power-ups for the player, such as shields or rapid fire.
*   **Improved Graphics and Sound:**  Enhancing the visuals and sound effects to create a more immersive experience.
*   **AI Opponents:** Adding enemy spaceships to challenge the player.
*   **Leaderboard:** Implementing a leaderboard to track high scores.

## Acknowledgements

*   Pygame Library:  This project would not have been possible without the Pygame library.
*   Inspiration:  Inspired by the original Asteroids arcade game.
*   (Optional) Any other resources or tutorials that helped you.

Thank you for checking out my Asteroids project!  I hope you enjoy playing it.  Feel free to contribute or provide feedback.