# Meal Time

Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

In `meal.py`, implement a program that prompts the user for a time and outputs whether it’s `breakfast time`, `lunch time`, or `dinner time`. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as `#:##` or `##:##`. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein `convert` is a function (that can be called by `main`) that converts `time`, a `str` in 24-hour format, to the corresponding number of hours as a `float`. For instance, given a `time` like `"7:30"` (i.e., 7 hours and 30 minutes), `convert` should return `7.5` (i.e., 7.5 hours).
```py
def main():
    ...


def convert(time):
    ...


if __name__ == "__main__":
    main()
```
??? Hints
    - Recall that a `str` comes with quite a few methods, per <https://docs.python.org/3/library/stdtypes.html#string-methods>, including `split`, which separates a `str` into a sequence of values, all of which can be assigned to variables at once. For instance, if `time` is a `str` like `"7:30"`, then
    ```
		hours, minutes = time.split(":")
    ```
    will assign `"7"` to `hours` and `"30"` to `minutes`.

    - Keep in mind that there are 60 minutes in 1 hour.

## Before You Begin
From the root of your repository execute `cd conditionals` So your current working directory is ...		
```
/conditionals $:
```
Next execute
```
code meal.py
```
to make a file called `meal.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually. At the `meal/ $` prompt in your terminal: :

1. Run your program with `python meal.py`. Type `7:00` and press Enter. Your program should output: 
```
breakfast time
```
2. Run your program with `python meal.py`. Type `7:30` and press Enter. Your program should output:
```
breakfast time
```
3. Run your program with `python meal.py`. Type `12:42` and press Enter. Your program should output:
```
lunch time
```
4. Run your program with `python meal.py`. Type `18:32` and press Enter. Your program should output:
```
dinner time
```
5. Run your program with `python meal.py`. Type `11:11` and press Enter. Your program should output:
```
nothing
```

### Pytest 
You can execute the below to check your code using `pytest` from the root directory.

```
pytest .\tests\conditionals\test_meal.py
```

A green output from running the test means it was successful. A red output means there is a bug in your code that you need to fix.

## How to Submit

From github desktop or the command line, commit your changes and push them to your repository.

### Codespaces
If you are using codespaces, you can commit your changes directly from the Codespace interface. Click on the Source Control icon in the left sidebar, then click on the "..." button and select "Commit to main". Enter a commit message and click "Commit".

#### Codespace terminal or your local terminal. 

!!! Note
    You will need to have installed `git-scm` for this to work locally

At the `/conditionals/meal $` prompt in your terminal:
```
git add -A 
```
Add all changed files in the repository to be committed
```
git commit -m "Upload completed meal.py"
```
Commit all changes in the REPO with the comment “Upload completed meal.py“ note: If the file is not complete, adjust the comment to describes what is being committed
```
git push 
```
Push all changes to the repo.