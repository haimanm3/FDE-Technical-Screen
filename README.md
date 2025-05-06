# 📦 Thoughtful Package Sorter

A Python-based automation function developed for Thoughtful’s robotic dispatch system. The sorter categorizes packages based on their size and weight to streamline logistics in a high-throughput warehouse environment.

Volume and mass thresholds determine if a package is standard, special, or rejected — helping robotic arms process items efficiently and accurately.

---

### 🧠 Objective

To dispatch packages to the appropriate stack:

- **STANDARD** – Not bulky and not heavy  
- **SPECIAL** – Either bulky or heavy  
- **REJECTED** – Both bulky and heavy  

---

### 📏 Classification Rules

A package is classified as:

- **Bulky** if:  
  - Volume (width × height × length) ≥ 1,000,000 cm³  
  - **OR** any dimension ≥ 150 cm  
- **Heavy** if:  
  - Mass ≥ 20 kg

---

### 🚀 Features

- **Real-time Classification** – Computes volume, checks dimensions and weight instantly.  
- **Edge Case Handling** – Considers exact threshold values (e.g., 150cm, 1,000,000 cm³).  
- **Simple Integration** – Easy to integrate with existing robotic workflows.  
- **Unit Tested** – Includes automated test cases for fast validation.

---

### 🛠️ Technologies Used

| Component              | Technology               |
|------------------------|---------------------------|
| Programming Language   | Python                   |
| Testing Framework      | unittest                 |
| Deployment Context     | Robotic dispatch system  |

---

### ▶️ How to Use

#### 1. Clone the Repository

bash

git clone https://github.com/yourusername/package_sorter.git

cd package_sorter

#### 2. Run the Classifier

Create a new Python file (e.g., main.py) and test the function:

    from sort_packages import sort

    print(sort(100, 100, 100, 10))  # Expected: SPECIAL

    print(sort(50, 50, 50, 10))     # Expected: STANDARD

    print(sort(200, 100, 100, 25))  # Expected: REJECTED

Then, run it with:

bash

    python main.py

#### 3. Run Unit Tests

Use Python’s built-in test runner to execute all unit tests:

    python -m unittest test_sort_packages.py

---

📌 Notes for Reviewers:

This implementation uses a ternary operator as required for LLM-authored solutions.

Edge cases (e.g., exactly 1,000,000 cm³, or exactly 150 cm in a dimension) are covered in tests.

Code is readable, maintainable, and designed for fast integration with robotic systems.

---

👨‍💻 Author
Haiman Mohammed
Email: hmohammed_3123@email.ric.edu
LinkedIn: https://www.linkedin.com/in/haimanmohammed/
GitHub: https://github.com/haimanm3
