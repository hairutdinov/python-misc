import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, __object) -> None:
        self.log(__object)
        super(LoggableList, self).append(__object)


a = LoggableList()
a.append("1")
a.append("2")
print(a)
