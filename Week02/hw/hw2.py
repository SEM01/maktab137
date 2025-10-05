import json

class InvalidConfigError(Exception):
    pass
class api_key_error(InvalidConfigError):
    pass
class database_url_error(InvalidConfigError):
    pass
class mode_error(InvalidConfigError):
    pass

def load_config(filepath):
    try:
        with open(filepath, 'r') as file:
            f = json.load(file)
            try:
                if 'api_key' not in f:
                    raise api_key_error
            except api_key_error:
                print("not api")
            try:
                if 'database_url' not in f:
                    raise database_url_error
            except database_url_error:
                print("Database URL is not Defiend")
            try: 
                if 'mode' not in f:
                    raise mode_error
            except mode_error:
                print("Mode key isn't Defiend")
            try:
                if ((f["mode"]) != "debug") and ((f["mode"]) != "production"):
                    raise InvalidConfigError
            except InvalidConfigError:
                print("False Value for Mode")
            
    except FileNotFoundError:
        print("File not Found")
    except json.JSONDecodeError:
        print("JSON File Structure is Incrorrect")   

