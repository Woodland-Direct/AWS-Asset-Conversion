def read_file(file_path):
    try:
        file = open(file_path, "r")
        for item in file:
            print(item)
        file.close()
    except Exception as e:
        print("Could not read file", e)
