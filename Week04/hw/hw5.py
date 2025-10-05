def file_io(input_file, output_file):
    def wrapper(func):
        def write(*args):
            with open(input_file, 'w') as input:
                input.write(*args)
            with open(output_file, 'w') as output:
                output.write(func(*args))
            func(*args)
            
        return write
    return wrapper


@file_io(input_file="input.txt", output_file="output.txt")
def process_data(data):
    return data.upper()

data = "salam"
process_data(data)
