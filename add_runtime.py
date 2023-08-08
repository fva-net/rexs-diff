import time
def add_runtime(outputfile: str, line5: str, line1: str, line2: str):
    with open(outputfile, "r") as file:
        original_output = file.read()
    with open(outputfile, "w") as file:
        file.write(line5)
        file.write("\n")
        file.write("\n")
        file.write(line1)
        file.write("\n")
        file.write(line2)
        file.write("\n")
        file.write(original_output)
