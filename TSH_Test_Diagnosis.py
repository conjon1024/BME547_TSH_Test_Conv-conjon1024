# TSH_Test_Diagnosis.py
import json


def main():
    sort_data()


def sort_data():
    '''Runs through each line in the data file and subfunctions extract information

    For each line in test_data.txt, this function determines which information
    is present and is going to be extracted by subfunctions. The data for a
    single patient is found on four consecutive lines in the following order:
    name, age, gender, TSH tests.
    '''
    with open("test_data.txt", "r") as TSH_Contents:

        count = 0  # where in the file we are
        entry = 0  # the first line we want to access

        for line in TSH_Contents:
            if line == "END":
                break
            if count == entry:
                (first, last) = TSH_names(line)
            elif count == entry + 1:
                age = TSH_ages(line)
            elif count == entry + 2:
                gender = TSH_genders(line)
            elif count == entry + 3:
                (TSH_sorted_numbers, diagnosis) = TSH_diagnosis(line)
                create_dictionary(first, last, age, gender,
                                  diagnosis, TSH_sorted_numbers)
                entry += 4
            count += 1


def TSH_names(line):
    '''Return first and last name of patient from given line

    Args:
        line (str): line containing first and last name

    Returns:
        string: first name of patient
        string: last name of patient
    '''
    name = line.strip()
    first = name.split(' ', 1)[0]
    last = name.split(' ', 1)[1]
    return (first, last)


def TSH_ages(line):
    '''Return age of patient from given line

    Args:
        line (str): line containing age

    Returns:
        string: age of patient
    '''
    age = line.strip()
    return age


def TSH_genders(line):
    '''Return gender of patient from given line

    Args:
        line (str): line containing gender

    Returns:
        string: gender of patient
    '''
    gender = line.strip()
    return gender


def TSH_diagnosis(line):
    '''Return sorted TSH test results and diagnosis of patient from given line

    This function takes a line that contains the name of test, followed by a
    comma, and then a list of test results separated by commas. It then
    extracts the test result numbers from the line and determines a diagnosis.
    "hyperthyroidism" as defined by any of their tests results being less than
    1.0, "hypothyroidism" as defined by any of their test results being greater
    than 4.0, and "normal thyroid function" as defined by all of their test
    results being between 1.0 and 4.0, inclusive.

    Args:
        line (str): line containing TSH test results

    Returns:
        list: list of ordered TSH test results (low to high)
        string: patient diagnosis based on TSH test results
    '''
    TSH_results = line.strip()
    TSH_line = [s for s in TSH_results.split(",")]
    TSH_numbers = [float(s) for s in TSH_line[1:]]
    TSH_sorted_numbers = sorted(TSH_numbers)

    hypo = False
    hyper = False
    normal = True
    for n in TSH_numbers:
        if n > 4.0:
            hypo = True
            normal = False
        if n < 1.0:
            hyper = True
            normal = False
    if hypo:
        diagnosis = "hypothyroidism"
    if hyper:
        diagnosis = "hyperthyroidism"
    if normal:
        diagnosis = "normal thyroid function"
    return (TSH_sorted_numbers, diagnosis)


def create_dictionary(first, last, age, gender, diagnosis, TSH_sorted_numbers):
    '''Create dictionary and JSON output files for each patient

    This function creates a dictionary containing the following keys and
    their corresponding values: First Name, Last Name, Age, Gender,
    Diagnosis, and TSH (containing a list of all of the test results). A
    JSON output file containing each patient's information is then returned.


    Args:
        first (str): first name of patient
        last (str): last name of patient
        age (str): age of patient
        gender (str): gender of patient
        diagnosis (str): patient diagnosis
        TSH_sorted_numbers (list): list of all TSH test results (low to high)

    Returns:
        file: JSON file for each patient containing their information
    '''
    new_dictionary = {"First Name": first,
                      "Last Name": last,
                      "Age": age,
                      "Gender": gender,
                      "Diagnosis": diagnosis,
                      "TSH": TSH_sorted_numbers}
    out_file = open("{}-{}.json".format(first, last), "w")
    json.dump(new_dictionary, out_file)
    out_file.close()

if __name__ == "__main__":
    main()
