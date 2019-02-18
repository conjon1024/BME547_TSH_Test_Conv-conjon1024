# BME547_TSH_Test_Conv-conjon1024

TSH_Test_Diagnosis.py is a script that initially reads in test_data.txt, a text file that contains patient data with TSH test results. The data for a single patient is found on four consecutive lines in the following order: name, age, gender, and TSH test results. The code runs through each line in test_data.txt and four different subfunctions are executed, one for each line type. The code runs until reaching the "END" line. The TSH_Test_Diagnosis.py code is compiled in Python by accessing the repository and typing "python3 TSH_Test_Diagnosis.py".

For each line containing a patient name, the code pulls the line out and returns the first and last name, which are separated by a space.

For each line containing a patient age, the code pulls the line out and returns the age.

For each line containing a patient gender, the code pulls the line out and returns the gender.

For each line containing TSH test results, the code first pulls the line out. The line contains the name of a test, followed by a comma, and then a list of test results separated by commas. The list of numbers from the line is then extracted and sorted from lowest to highest. These numbers are used to determine a diagnosis. "Hyperthyroidism" as defined by any of their tests results being less than 1.0, "hypothyroidism" as defined by any of their test results being greater than 4.0, and "normal thyroid function" as defined by all of their test results being between 1.0 and 4.0, inclusive. Initially, the hypo and hyper states are set as False and normal as True. If any number is greater than 4, the hypo state changes to True and normal changes to False. Alternatively, if any number is less than 1, the hyper state changes to True and normal state changes to False. The code returns the sorted list of test values and patient diagnosis.

The create_dictionary() function creates a dictionary containing the following keys and their corresponding values from the subfunctions: First Name, Last Name, Age, Gender, Diagnosis, and TSH (containing a list of all of the test results). From this dictionary, information was created and output in the form of a JSON file for each patient. Therefore, ten JSON files were created.

A virtual environment called TSH_Env was used for the project, and the requirements.txt file contains the pytest and pytest-pep8 packages.

Several unit tests were written in test_TSH_Test_Diagnosis.py to test the ability of the TSH_Test_Diagnosis.py script to take a string of TSH values and correctly order the test results from low to high and output the correct diagnosis. A string corresponding to a normal, hyperthyroid, and hypothyroid state were written. The output of the function is compared with the asserted answer using the assert command. The tests can be run with the command, "pytest -v".

To check if the modules comply with PEP-8 Style Guide, the command "pytest -v --pep8" can be typed into the terminal. TravisCI was enabled and used in the repository, and feature branches were merged with the master branch only after TravisCI reported a passing status.
