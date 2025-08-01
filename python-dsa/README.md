# Python DSA Practice

This folder contains all the Data Structures and Algorithms (DSA) problems that I am practicing using Python.

## Setup Instructions

After navigating into the `python-dsa` directory, set up your Python environment as follows:

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

Now you can test my DSA problems! I have set up automated tests, but if you want you can create a python file and set up manual testing through the CLI (though I do not know why you would do that?).

Anyways if you do want to test, then:

- Use a non-PowerShell terminal (like Git Bash) to run the test script.
- Make sure to activate your virtual environment using `source`:
  ```bash
  source .venv/bin/activate
  ```
- Then run the test script:
  ```bash
  ./Scripts/test.sh
  ```

This will collect and run all pytest tests. You can also use `-k` to filter tests:
```bash
./Scripts/test.sh -k <keyword>
```


