class InternalDataError(Exception):
    print("InternalDataError")

def process(data_dictionary, record_id):
    try:
        return data_dictionary[record_id]
    except KeyError as ke:
        raise InternalDataError("Record not present") from ke


data = {"key":"value"}
key = "id"

retValue = process(data, key)
print(retValue)
