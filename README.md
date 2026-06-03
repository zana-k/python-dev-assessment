# Python Developer Assessment

This repository is for my developer assessment bootcamp tasks.

# Developer Assessment Tasks

This project brings together my work on practicing Python basics, using Git, writing clean code, solving data problems, handling errors, and connecting to an external API.

---

## Completed Tasks

| Feature Branch | Completed Task | Linked File |
| :--- | :--- | :--- |
| `task-1.2-git-basics` | Git Setup & Basic Settings | [README.md](./README.md) |
| `task-1.3-code-style` | Fixing Code Style and Formatting | [bad_style.py](./bad_style.py) |
| `task-2.1-dsa` | Filtering Lists and Counting Characters | [dsa_challenges.py](./dsa_challenges.py) |
| `task-2.2-oop` | Building a Book Class using Object-Oriented Python | [book_store.py](./book_store.py) |
| `task-2.3-error-debug` | Catching Code Crashes and Using the Debugger | [debug_errors.py](./debug_errors.py) |
| `task-3.1-api-interaction` | Fetching Live User Data from a REST API | [api_client.py](./api_client.py) |

---

## Execution Instructions

Make sure your virtual environment (`.venv`) is active, then run any of the files in your terminal using these commands:

```
# Run the Data Structures & Algorithms task
python dsa_challenges.py

# Run the Object-Oriented Book Class task
python book_store.py

# Run the Error Handling & Debugging task
python debug_errors.py

# Run the Live API Data task
python api_client.py

```
## Reflections

* **Most Challenging:** In `debug_errors.py` (Task 2.3), the hardest part was realizing that Python treats strings like lists of characters. When passing a string to a function expecting a list, it did not cause a TypeError like I expected. I had to learn to change the test input data type to a number to make the error handler trigger correctly.

* **Most Interesting:** I really enjoyed using the VS Code debugger in Task 2.3. Being able to pause the code, step through the logic line-by-line, and look inside the computer's memory to see exactly why the program was crashing was interesting.

* **Skill Improved:** This project helped me improve both my Git and Python skills. I gained additional practical confidence managing Git branches and merging my features back into the main code. At the same time, I grew much stronger at writing clean Python classes and safely handling live data from web APIs.


