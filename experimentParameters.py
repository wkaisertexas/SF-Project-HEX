# this reads from the file and reads the file for all of the necessary information to complete the experiment

class parameters:
    # Defaults

    name = "Standard-HEX-Model"
    version = "000"

    # model variables
    number_of_training_iterations = 10000

    save_frequency = 1000
    printout_frequency = 100

    use_CUDA = False  # this is for gpu acceleration

    def __init__(self, file_location):  # this reads all of the parameters
        file = open(file_location, "r")

        for line in file:
            if str(line)[0] is "#":
                continue

            # this maps the test equivalent to
            mapping = {
                "number_of_training_iterations": self.number_of_training_iterations
            }

        file.close()
        return