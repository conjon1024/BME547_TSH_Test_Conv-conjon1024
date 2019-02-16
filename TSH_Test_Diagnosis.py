# TSH_Test_Diagnosis.py


def main():
    sort_data()


def sort_data():
    with open("test_data.txt", "r") as TSH_Contents:

        names = []
        ages = []
        genders = []
        values = []

        count = 0  # where in the file we are
        entry = 0  # the first line we want to access

        for line in TSH_Contents:
            if line == "END":
                break
            if count == entry:
                name = line.strip()
                names.append(name)
            elif count == entry + 1:
                age = line.strip()
                ages.append(age)
            elif count == entry + 2:
                gender = line.strip()
                genders.append(gender)
            elif count == entry + 3:
                TSH_results = line.strip()
                values.append(TSH_results)
                entry += 4
            count += 1
        print(names, ages, genders, values)

if __name__ == "__main__":
    main()
