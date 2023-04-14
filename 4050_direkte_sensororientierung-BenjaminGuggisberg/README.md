[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-8d59dc4de5201274e310e4c54b9627a8934c3b88527886e3b421487c677d23eb.svg)](https://classroom.github.com/a/dzCvhdfN)
# 4050_Direkte_Sensororientierung

**Course: 4050 - Photogrammetrie, Computer Vision & English**

The whole exercise is described in [Direkte_Sensororientierung.ipynb](Direkte_Sensororientierung.ipynb).

Complete the assignment and push the solutions back to GitHub. Your solutions will be correct if all the automatic unit tests turn green. You can see the unit tests under the actions tab in the GitHub repository.

## Unit tests

### Concept

A **unit** is a specific piece of code to be tested, such as a function or a class. **Unit tests** are then other pieces of code that specifically exercise the code unit with a full range of different inputs, including boundary and edge cases.

For example, say you have a function to validate the format of an account number that a user enters in a web form:

```python
def validate_account_number_format(account_string):
    # Return False if invalid, True if valid
    # ...
```

Unit tests are concerned only with the unit's **interface**—its arguments and return values—not with its implementation (which is why no code is shown here in the function body; often you'd be using other well-tested libraries to help implement the function). In this example, the function accepts any string and returns true if that string contains a properly formatted account number, false otherwise.

### Usage

You can use the unit tests to check your code for functionality.

#### Command line

To run the unit tests from command line, the following command from the root folder of this repository:

```bash
python -m unittest discover -v -s "tests" -p "test_*.py"
```

Dependent on your python installation you may have to use ``python3`` instead of ``python`` argument.

The meaning of the used arguments you can find in the [documentation of the unittest library](https://docs.python.org/3/library/unittest.html).


#### VS Code

Additionally you can also use [Visual Studio Code](https://code.visualstudio.com/) or any other integrated development environment (IDE) to run the unit tests.

To configure unit testing in VS Code, see the section **Configure tests** in [Python testing in Visual Studio Code](https://code.visualstudio.com/docs/python/testing).
