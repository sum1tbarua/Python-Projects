# Lesson 5 – Movie Ratings Analyzer (Python Comprehensions)

This project is part of my **Python learning repository**, where I build small projects lesson-by-lesson to practice practical programming concepts.

Lesson 5 focuses on **Python comprehensions**, which provide a concise and expressive way to transform and filter data.

The program analyzes a small dataset of movie ratings and computes useful statistics such as average ratings and top-rated movies.

---

## Concepts Practiced

- List comprehensions
- Set comprehensions
- Filtering data using comprehensions
- Data aggregation using dictionaries
- Writing reusable utility functions
- Clean Pythonic data transformations

Comprehensions are widely used in **real Python codebases**, including data science pipelines, backend services, and machine learning workflows.

---

## Dataset Format

The dataset is stored in `ratings_data.py`.

Each record follows this format:
```brew
(user, movie, rating)
```

Example:
```brew
("Alice", "Inception", 9)
```


Example dataset:

```python
ratings = [
    ("Alice", "Inception", 9),
    ("Bob", "Inception", 8),
    ("Charlie", "Interstellar", 10),
    ("Alice", "Interstellar", 9),
    ("Bob", "The Dark Knight", 10),
    ("Charlie", "Inception", 9),
    ("Alice", "The Dark Knight", 8),
    ("David", "Inception", 7)
]
```
---
## Project Structure
```brew
lesson05_movie_ratings_analyzer
│
├── main.py
├── utilities.py
├── ratings_data.py
└── README.md
```

## File Descriptions

1. ratings_data.py - Contains the dataset of movie ratings.
2. utilities.py - Contains reusable functions used to analyze the dataset:
```python
get_unique_users

get_unique_movies

get_movie_ratings

average_rating_per_movie

highest_rated_movie

high_ratings
```

These functions demonstrate the use of Python comprehensions and dictionary aggregation.

3. main.py - Entry point of the program that loads the dataset and prints analysis results.

## Features

The analyzer performs the following operations:

1. Finds unique users who submitted ratings

2. Identifies unique movies in the dataset

3. Retrieves ratings for a specific movie

4. Computes average rating per movie

5. Determines the highest rated movie

6. Filters ratings above a specified threshold

## Example Output
```python
=== Movie Ratings Analyzer ===

Unique users:
- Alice
- Bob
- Charlie
- David

Unique movies:
- Inception
- Interstellar
- The Dark Knight

Ratings for Inception:
[9, 8, 9, 7]

Average rating per movie:
- Inception: 8.25
- Interstellar: 9.5
- The Dark Knight: 9.0

Highest rated movie:
- Interstellar

Ratings >= 9:
- Charlie | Interstellar | 10
- Bob | The Dark Knight | 10
```

## How to Run

From the project directory:
```brew
python main.py
```

## Learning Goal

The purpose of this project is to practice Python comprehensions and cleaner data transformations.

Comprehensions allow Python programmers to write concise and expressive data processing code that replaces many traditional loops.

These patterns are commonly used in:

1. data science workflows

2. machine learning pipelines

3. backend data processing

4. algorithmic problem solving

## Author

Sumit Barua

MS Computer Science

Western Michigan University