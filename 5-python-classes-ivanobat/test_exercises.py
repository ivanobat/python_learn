from exercises import *
import pytest

def test_patient_constructor():
    patient = Patient('Foo', ['cough'])
    assert patient.name == 'Foo'
    assert patient.symptoms == ['cough']

def test_patient_add_test_exists():
    patient = Patient('Foo', ['cough'])

    patient.add_test('sars', False)
    patient.add_test('covid', False)

def test_patient_has_covid():
    patient = Patient('Foo', ['cough'])
    patient.add_test('covid', False)
    patient.add_test('sars', False)
    assert patient.has_covid() == 0.01

    patient = Patient('Foo', ['cough'])
    patient.add_test('covid', True)
    patient.add_test('sars', False)
    assert patient.has_covid() == 0.99

    patient = Patient('Foo', ['happy'])
    assert round(patient.has_covid(), 5) == 0.05

    patient = Patient('Foo', ['cough', 'dizzy'])
    assert round(patient.has_covid(), 5) == 0.15

    patient = Patient('Foo', ['cough', 'fever', 'anosmia'])
    assert round(patient.has_covid(), 5) == 0.35


def test_encoder_constructor():
    encoder = Encoder()
    assert encoder

def test_encoder_encode_decode():
    encoder = Encoder()

    data = [['foo', 'bar', 'foo', 'baz'],
            ['qux', 'foo', 'baz', 'qux']]

    res = [encoder.encode(d) for d in data]

    for r in res:
        for i in r:
            assert isinstance(i, int)

    decoded = [encoder.decode(r) for r in res]

    assert decoded == data


#################################################
# BONUS QUESTIONS
################################################

def test_encoder_export_import_mapping():
    encoder_a = Encoder()

    data = [['foo', 'bar', 'foo', 'baz'],
            ['qux', 'foo', 'baz', 'qux']]

    res_a = [encoder_a.encode(d) for d in data]
    mapping = encoder_a.export_mapping()

    encoder_b = Encoder()
    encoder_b.import_mapping(mapping)

    res_b = [encoder_b.encode(d) for d in [data[1], data[0]]]
    assert res_b[0] == res_a[1]
    assert res_b[1] == res_a[0]


def test_encode_raises_on_bad_input():
    encoder = Encoder()
    with pytest.raises(Exception) as e:
        assert encoder.encode(['foo', [1,2,3], 'bar'])
    assert str(e.value) == 'Encoder.encode() was passed elements that it cannot encode'


def test_decode_raises_on_bad_input():
    encoder = Encoder()
    with pytest.raises(Exception) as e:
        assert encoder.decode([0,1.2,2])
    assert str(e.value) == 'Encoder.decode() was passed integers that it cannot decode'
