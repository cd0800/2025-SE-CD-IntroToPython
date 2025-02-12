# Overview

This is an adaptation of the CS50 Introduction to Python course from Harvard. The course covers the basics of Python programming, including data types, control structures, functions, and more.

## Getting Started

!!! Note "Different Operating Systems"
    Depending on which operating system you are using, the terminal or command prompt may look different.

    - On Windows, you may see `C:\Users\username\github\IntroToPython>`.
    - On Linux or Mac, you may see `$` or `%`.

    In all examples I will not use a prompt to make it easier to copy the command.

To get started with the course, follow these steps:

1. Fork this repository on GitHub. 

    !!! success "Naming Convention for Repositories"
        - Follow the naming convention `<year>-<subject>-<your_initials>-IntroToPython` for your forked repository.
        - For example, `2025-11SEO4-AB-IntroToPython`

    `need images`

2. Clone your new repository to you local machine using GitHub Desktop or the command line.

    `need images`

3. Ensure that you have python installed on your local machine. You can download it from [python.org](https://www.python.org/downloads/).

4. Open a terminal or command prompt and navigate to the root directory of your repository and type:

```
pip install -r requirements.txt
```

## Structure of the Repository

The repository is structured as follows:

- `README.md`: This file contains an overview of the course and installation instructions.
- `docs/`: This directory contains the course materials, including lectures, assignments, and solutions.
- `requirements.txt`: This file lists the Python packages required for the course.
- `src/`: This directory contains any source code or scripts that are part of the course. **Your solutions should go here**
- `tests/`: This directory contains any test files for the course.

## Course Basics

The intention is for you to start from [Lesson 0](./Functions_Variables/index.md) and work through each lesson in order. Each lesson will have a corresponding set of exercises or problems that you should complete. The solutions to these exercises should be placed in the `src/` directory. As an example, if you are working on the Indoor voice problem from [Lesson 0](./Functions_Variables/Exercises/problem1.md), your solutions should be placed in `src/lesson_0/indoor.py`.

## Submission

- To submit your work, simply push it to your GitHub repository. 
- To receive feedback on your work, please email your teacher.

If you want to confirm that your code is working correctly, you can run the tests in the `tests/` directory using the following command from the root directory.

For example, if you want to check that your code is working correctly for the `indoor()` method from [Lesson 0](./Functions_Variables/Exercises/problem1.md), you can run:

```bash
pytest -k "indoor"
```




















