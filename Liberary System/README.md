# Mini Library Management System (Python)

This project is a simple Mini Library Management System implemented in Python using **lists**, **dictionaries**, **tuples**, and **functions**.  
It allows users to **add, search, update, delete, borrow, and return** books.


## Features

- Add new books and members  
- Search books by title or author  
- Update book or member information  
- Borrow and return books (up to 3 books per member)  
- Prevent borrowing if no copies are available  
- Validation for unique IDs and valid genres  

---

## Project Structure

    MiniLibrarySystem/
│
├── operations.py # Core functions (CRUD + borrow/return)
├── demo.py # Demonstration script
├── tests.py # Unit tests using assert
├── UML.png # UML diagram (hand-drawn or generated)
├── DesignRationale.pdf # Explanation of data structure choices
└── README.md # Project overview and usage guide


---

##    How to Run

1. **Clone or Download** the project.
2. Open a terminal or IDE inside the project folder.
3. Run the demo script:

   ```bash
   python demo.py
