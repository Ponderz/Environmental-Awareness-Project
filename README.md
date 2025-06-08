# Shipwrecked Project 1: Environmental Arcade & CO₂ Data Analysis

## Overview

This project consists of two main parts:

1. **Environmental Arcade (Python Turtle Games)**
    - **Polluted Water and Trees**: A two-player adaptation of Snakes and Ladders with an environmental theme.
    - **Hangtree**: A two-player adaptation of Hangman, using a tree instead of a hangman.

2. **CO₂ Data Analysis**
    - Analysis and visualization of CO₂ levels from the Mauna Loa Observatory dataset.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/shipwreckedProject1.git
cd shipwreckedProject1
```

### 2. Install Python

Ensure you have Python 3.8 or higher installed. Download it from [python.org](https://www.python.org/downloads/).

### 3. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Requirements

```bash
pip install -r requirements.txt
```

### 5. Running the Arcade Games

Navigate to the arcade directory and run the desired game:

```bash
cd arcade
python polluted_water_and_trees.py
# or
python hangtree.py
```

### 6. Running the CO₂ Data Analysis

Navigate to the analysis directory and run the analysis script:

```bash
cd ../analysis
python co2_analysis.py
```

---

## Project Structure

```
shipwreckedProject1/
│
├── arcade/
│   ├── polluted_water_and_trees.py
│   └── hangtree.py
│
├── analysis/
│   └── co2_analysis.py
│
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.8+
- See `requirements.txt` for Python package dependencies (e.g., `turtle`, `matplotlib`, `pandas`).

---

## License

This project is for educational purposes.
