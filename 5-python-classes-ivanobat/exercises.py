###########################################
# PART A: Patient
###########################################

#
# In this exercise we will make an "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively

class Patient():
    tests = {} 

    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms
        self.tests = {}

    #def getName(self):
    #    return self.name

    #def getSymptom(self):
    #    return self.symptoms

#
# 2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.
    def add_test(self, testname, testresults):
        self.tests[testname] = testresults
        return None
#
# 3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']
    def has_covid(self):
        probability_covid = 0.5
        other_symptoms = ['fever','cough','anosmia']

        #probability_covid = [0.99 for k,v in self.tests.items() if k == 'covid' and v == True]
        #probability_covid = [0.01 for k,v in self.tests.items() if k == 'covid' and v == False]
        for k,v in self.tests.items():
            if k == 'covid' and v == True:
                probability_covid = 0.99
                return probability_covid
            elif k == 'covid' and v == False:
                probability_covid = 0.01
                return probability_covid
                    
        if not self.tests:
            probability_covid = 0.05
            for symptom in other_symptoms:
                print(symptom)
                if symptom in self.symptoms:
                    probability_covid += 0.1   

        return probability_covid

###########################################
# PART B: Encoder
###########################################

#
# In this exercise we will make an "Encoder" class
#
# The Encoder class should be able to encode
# a list of strings into a list of
# integers that can later be losslessly
# decoded.
#
# For example, if given a list of words:
# ['Joan', 'went', 'to', 'the', 'store']
# it might encode:
# [245, 9873, 290, 10, 209]
# and be able to decode it back again
# to the list of words.
#
#
#
# 4)
# Create a class called "Encoder."
# The constructor should have no
# parameters (besides, of course, "self")
class Encoder():

    def __init__(self):
        self.coded_dictionary = {}
        return None

#
#
# 5)
# Add two methods: "encode" and "decode"


# "encode" should have a single parameter,
# a list of strings, and returns
# a list of integers which represents the
# encoding.
    def get_int(self, key, any_dictionary):
        if key in any_dictionary:
            return any_dictionary[key]
        else:
            return int.from_bytes(key.encode('utf-8'), byteorder = 'big') 

    def encode(self, string_list):
        int_from_bytes =  []
        try:
            for item in string_list:
                coded_int = self.get_int(item, self.coded_dictionary)
                self.coded_dictionary[item] = coded_int
                int_from_bytes.append(coded_int)
                #int_from_bytes.append(int.from_bytes(item.encode('utf-8'), byteorder = 'big'))        
        except:
            raise ValueError('Encoder.encode() was passed elements that it cannot encode')
        return int_from_bytes

# "decode" should have a single parameter,
# a list of integers, and returns a list
# of strings, which should be the same as
# was passed to "encode"

    def get_str(self, value, any_dictionary):
        return list(any_dictionary.keys())[list(any_dictionary.values()).index(value)]  
    
    def decode(self, int_list):
        string_from_bytes = []
        try:
            for item in int_list:
                decoded_string = self.get_str(item, self.coded_dictionary)
                string_from_bytes.append(decoded_string)
                #string_from_bytes.append(item.to_bytes((item.bit_length() + 7) // 8, 'big').decode('utf-8'))   
        except:
            raise ValueError('Encoder.decode() was passed integers that it cannot decode')
        return string_from_bytes

##################################
# BONUS EXERCISES
##################################

# 6)
# Your encoder has learned a "mapping"
# from strings to ints in order to encode
# its input data.
#
# Imagine we want to be able to "export"
# that mapping from one encoder and load it
# into another.
#
# Create a method called "export_mapping"
# and a method called "import_mapping".
#
# "export_mapping" should have no parameters,
# and should return an object that can be
# imported into another Encoder instance
# via the "import_mapping" method and
# used to encode/decode in the same way
# as the original.
    def export_mapping(self):
        return None

    def import_mapping(self, mapping):
        return None
#
# 7)
# Modify your method "encode" so that it
# raises an exception if the input list
# has elements that cannot be encoded.
# (for example, if instead of a string,
# the list contains a nested complex data
# type, like a list or dictionary)
#
# The exception should say:
# "Encoder.encode() was passed elements that it cannot encode"

#
#
# 8)
# Modify your method "decode" so that it
# raises a helpful exception if it cannot decode
# an integer in the provided list.
#
# The exception should say:
# "Encoder.decode() was passed integers that it cannot decode"
