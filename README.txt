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
Step11. Create a unit file test_calculator.py  for Unit testing with pytest.  Note the prefix "test" is very important that how pytest will know/find the file that contain unit test.
Step 12: Run  >>>> pytest -v  --cov=calculator   this shows more details 
                        >>> pytest test_calculator.py
                        >>> pytest  --cov=calculator
 
Step 13 : push your changes back to the remote as necessary
Step 14 : Create a folder extension .circleci for your build automation
Step 15 : Create a config.yml file inside the folder extension in step 14
            See config.yml for configuration write up
Step 16 : Commit your update to repo.
Step 17: Create account with circleci with your git/bitbucket account
Step 18 : look for your project folder on circleci and setup project.


NOTE  : Git Workflows is specific to Different team within an Organization  read more => Git Flow
            : Conda or Pipenv for Dependency and environment management 
            : Testing  => Video on getting Start with Test Guide
            : Continous Development  (CI/CD) => These are deployable artifacts that can used  by other users or used  in other projects => Benefits  
