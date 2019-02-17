# test_TSH_Test_Diagnostics.py


def test_TSH_diagnosis_normal():
    from TSH_Test_Diagnosis import TSH_diagnosis

    line = "TSH,2.4,3.4,1.4,1.8,3.1,2.7,1.9,2.5"
    (TSH_sorted_numbers, diagnosis) = TSH_diagnosis(line)

    assert diagnosis == "normal thyroid function"
    assert TSH_sorted_numbers == [1.4, 1.8, 1.9, 2.4, 2.5, 2.7, 3.1, 3.4]


def test_TSH_diagnosis_hyper():
    from TSH_Test_Diagnosis import TSH_diagnosis

    line = "TSH,1.5,2.7,3.2,3.4,0.7,3.0,0.5,2.4,3.4"
    (TSH_sorted_numbers, diagnosis) = TSH_diagnosis(line)

    assert diagnosis == "hyperthyroidism"
    assert TSH_sorted_numbers == [0.5, 0.7, 1.5, 2.4, 2.7, 3.0, 3.2, 3.4, 3.4]


def test_TSH_diagnosis_hypo():
    from TSH_Test_Diagnosis import TSH_diagnosis

    line = "TSH,3.7,3.2,4.3,5.2,3.4,3.6,4.2,3.6,3.2"
    (TSH_sorted_numbers, diagnosis) = TSH_diagnosis(line)

    assert diagnosis == "hypothyroidism"
    assert TSH_sorted_numbers == [3.2, 3.2, 3.4, 3.6, 3.6, 3.7, 4.2, 4.3, 5.2]
