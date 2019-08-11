class AdaptLog:

    def __init__(self):
        self.logfile = open("out.log", "w")
        self.logfile.write("Adaptation Log")
        self.logfile.close()

    def open(self):
        self.logfile = open("out.log", "w+")

    def close(self):
        self.logfile.close()

    def write(self, message):
        self.logfile.write("{}\n".format(message))
