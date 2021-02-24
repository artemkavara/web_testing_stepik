## GIT repository for stepik course "Web automation with Selenium and Python"

To run the test files in ```.py``` format run command ```python3 <test>.py```.

To run the test files in ```.ipynb``` format:
+ install jupyter notebook running command ```pip install notebook```
+ in terminal run command ```jupyter-notebook```
+ open desired file
+ run all cells

To run tests from ```test_<name>``` files:
+ install pytest running command ```pip install pytest==5.1.1```
+ download test file
+ run command ```pytest <file_name>``` with the list of parameters

To run tests from ```test_locale``` folder:
+ download files ```conftest.py```, ```list_lang.txt``` and ```test_items.py```
+ run command ```pytest -s --language=<lang> test_items.py```
All available languages are located in file ```list_lang.txt```, so it is an obligatory
to download it before running test. The list of languages was parsed in file ```parse_lang.py```.