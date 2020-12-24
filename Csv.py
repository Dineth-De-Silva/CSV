import os


class csv:
    def __init__(self, FileName):
        self.FileName = FileName

    def write(self, Data):
        File = open(self.FileName + ".csv", "w")
        if isinstance(Data, list):
            for Element in Data:
                if isinstance(Element, list):
                    for Subelement in Element:
                        File.write(Subelement + ", ")
                    File.write("\n")
                else:
                    File.write(Element + "\n")
        else:
            File.write(Data + "\n")
        File.close()

    def read(self):
        File = open(self.FileName + ".csv", "r")
        Lines = File.readlines()
        Return = []
        for Line in Lines:
            if "," in Line:
                SubReturn = []
                Start = 0
                CreatedStr = ""
                End = False
                while not End:
                    if Start <= len(Line):
                        RemainingStr = Line[Start:]
                        for char in RemainingStr:
                            if char == ",":
                                SubReturn.append(CreatedStr)
                                Start += len(CreatedStr) + 2
                                CreatedStr = ""
                                End = True
                            else:
                                CreatedStr += char
                    else:
                        End = True
                Return.append(SubReturn)
            else:
                Return.append(Line[0:len(Line) - 1])
        File.close()
        return Return

    def close(self):
        os.remove(self.FileName + ".csv")
