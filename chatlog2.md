Yes, that's correct! When you run:
```
python -m unittest
```
Python’s unittest framework will:

- Search the current directory and subdirectories for any files named `test*.py` (like test_main.py).
- In those files, it looks for classes that inherit from `unittest.TestCase`.
- It then runs any methods in those classes whose names start with `test_`.

You don’t need to specify the file or class—unittest will automatically discover and run all matching tests it finds in your project. If you want to run a specific test file, you can do:
```
python -m unittest test_main.py
```
Or even a specific test class or method:
```
python -m unittest test_main.TestWeatherAPI
python -m unittest test_main.TestWeatherAPI.test_monthly_average_spain
```

Let me know if you want more details or tips on writing more tests!