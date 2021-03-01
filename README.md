# CalculatorLibrary

CI-PROJECT- SETTING UP YOUR PYTHON CI (CONTINOUS INTEGRATION) PROJECT

Passthrough: zCX2rXXBbjgmiPB  for url :https://realpython.com/lessons/adding-unit-tests/

Step 1:  Setup your remote repo.   NOTE: add a python gitignore 
Step 2 :  Clone the repo to your local directory
Step 3: Install virtualenv if not available  >>> pip3 install virtualenv
Step 4 : Create your venv >>> virtualenv whateverName —system-site-packages
Step 5 : Activate venv >>source whateverName/bin/activate
Step 6 : We use Lintinng to look potential error >>> pip install flake8 with combines  error and PEP 8 style checks
           To perform unit tests to ensue no test is missed >> pip install pytest, pytest-cov
            To perform and calculates how much of the code is covered by units tests  >> pip install pytest-cov
Step 7 :  Because you have added depenencies to your project you will have to save them  in a requirement.txt file >>> pip freeze > requirements.txt
             This captures all the dependences used in your project in the requirement file
Step 10: As you write you code continously, you want to perform quality checks on your code with  >> flake8  - - statistics or flake8 -file.py: This check for error  and style issues.(autpep8/black for formatting)
Step11. Create a unit file test_calculator.py  for Unit testing with pytest.  Note the prefix test is very importany that how pytest will know that file contain unit test.
