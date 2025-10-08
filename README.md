# 🎬 Mini Assignment – Movie Booking System

A simple command-line Python project that simulates a movie ticket booking system. This project is designed as a mini-assignment to demonstrate the use of object-oriented programming concepts in Python.

## 🧠 Features

- Add new movies with details like name, genre, and available seats
- Display all available movies
- Book tickets for a selected movie
- View booking confirmations
- Basic menu-driven interface for user interaction

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Paradigm**: Object-Oriented Programming (OOP)
- **Interface**: CLI (Command Line Interface)

## 📁 Project Structure

mini-assignment/
│
├── main.py # Main entry point with the menu logic
├── movie.py # Movie class definition
└── README.md # Project documentation


### `movie.py`

Contains the `Movie` class, which stores information about a movie, such as:
- Title
- Genre
- Number of available seats

Includes methods to:
- Book seats
- Display movie information

### `main.py`

Implements a simple menu system that allows users to:
- Add a new movie
- Display list of movies
- Book a ticket
- Exit the program

## 🚀 Getting Started

### Prerequisites

Make sure Python 3 is installed. You can check with:
python3 --version

## Run the program

Clone the repository and run:

git clone https://github.com/NonLulz/mini-assignment.git
cd mini-assignment
python3 main.py

📌 Example Interaction
==== Movie Booking System ====
1. Add a new movie
2. Display available movies
3. Book a ticket
4. Exit
Enter your choice:

🔧 Future Improvements (Suggestions)

Save movies and bookings to a file (persistence)

Add seat maps for individual movie screens

Include user authentication

Build a GUI version using Tkinter or PyQt

🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to open an issue or submit a pull request.

📄 License

This project is licensed under the MIT License. See the LICENSE
 file for details.

Made with ❤️ by NonLulz
