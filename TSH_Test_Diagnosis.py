# TSH_Test_Diagnosis.py


def main():
    sort_data()


def sort_data():
    with open("test_data.txt", "r") as TSH_Contents:

        names = []
        ages = []
        genders = []
        # values = []
        # numbers = []

        count = 0  # where in the file we are
        entry = 0  # the first line we want to access

        for line in TSH_Contents:
            if line == "END":
                break
            if count == entry:
                TSH_names(line, names)
            elif count == entry + 1:
                TSH_ages(line, ages)
            elif count == entry + 2:
                TSH_genders(line, genders)
            elif count == entry + 3:
                diagnosis = TSH_diagnosis(line)
                entry += 4
            count += 1


def TSH_names(line, names):
    name = line.strip()
    names.append(name)


def TSH_ages(line, ages):
    age = line.strip()
    ages.append(age)


def TSH_genders(line, genders):
    gender = line.strip()
    genders.append(gender)


def TSH_diagnosis(line):
    TSH_results = line.strip()
    # values.append(TSH_results)
    TSH_line = [s for s in TSH_results.split(",")]
    TSH_numbers = [float(s) for s in TSH_line[1:]]
    # numbers.append(TSH_numbers)

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
        print("The patient has hypothyroidism")
    if hyper:
        diagnosis = "hyperthyroidism"
        print("The patient has hyperthyroidism")
    if normal:
        diagnosis = "normal thyroid function"
        print("The patient has normal thyroid function")
    return diagnosis

if __name__ == "__main__":
    main()
