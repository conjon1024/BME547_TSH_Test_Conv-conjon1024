# test_TSH_Test_Diagnostics.py


def test_TSH_diagnosis_normal():
    from TSH_Test_Diagnosis import TSH_diagnosis

    line = "TSH,2.4,3.4,1.4,1.8,3.1,2.7,1.9,2.5"
    diagnosis = TSH_diagnosis(line)

    assert diagnosis == "normal thyroid function"


def test_TSH_diagnosis_hyper():
    from TSH_Test_Diagnosis import TSH_diagnosis

    line = "TSH,1.5,2.7,3.2,3.4,0.7,3.0,0.5,2.4,2.7,3.4"
    diagnosis = TSH_diagnosis(line)

    assert diagnosis == "hyperthyroidism"


def test_TSH_diagnosis_hypo():
    from TSH_Test_Diagnosis import TSH_diagnosis

    line = "TSH,3.7,4.2,3.6,3.2,4.3,5.2,3.4,3.6,4.2,3.6,3.2"
    diagnosis = TSH_diagnosis(line)

    assert diagnosis == "hypothyroidism"
