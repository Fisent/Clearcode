class Launch(object):
    def __str__(self, *args, **kwargs):
        return str(self.month) + "." + str(self.year) + ", succ: " + str(self.succ)

    def __init__(self, year, month, succ):
        self.year = year
        self.month = month
        self.succ = succ


def read(stream):
    out = set()
    stream.__next__()
    stream.__next__()
    for line in stream:
        splitted = line.split("  ")
        splitted = [s.strip(" ") for s in splitted if s != ""]
        if len(splitted) > 7:
            ym = splitted[1]
            succ = splitted[-2]
            date_splitted = ym.split(" ")
            year = date_splitted[0]
            month = date_splitted[1]
            out.add(Launch(year, month, succ=="S"))
    return out




def group_by(stream, field, succ):
    launches = read(stream)
    dictionary = {}
    for launch in launches:
        key = ""
        if field=="month":
            key = launch.month
        elif field=="year":
            key = launch.year
        else:
            return -1
        if(launch.succ == succ):
            if key in dictionary.keys():
                dictionary[key] += 1
            else:
                dictionary[key] = 1
    return dictionary

print(group_by(open("launchlog.txt"), "month", False))
print(group_by(open("launchlog.txt"), "year", False))
