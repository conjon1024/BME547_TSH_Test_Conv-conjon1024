# TSH_Test_Diagnosis.py
import json


def main():
    sort_data()


def sort_data():
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
    name = line.strip()
    first = name.split(' ', 1)[0]
    last = name.split(' ', 1)[1]
    return (first, last)


def TSH_ages(line):
    age = line.strip()
    return age


def TSH_genders(line):
    gender = line.strip()
    return gender


def TSH_diagnosis(line):
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
