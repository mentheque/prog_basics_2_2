class Time:
    def __init__(self, hours = 0, minutes = 0):
        self.hours = hours%24
        self.minutes = minutes%60

        self._HOUR_ = 60
        self._MINUTE_ = 1

        self._EVENING_NIGHT_ = 23*self._HOUR_ + 11*self._MINUTE_
        self._NIGHT_MORNING_ = 5*self._HOUR_ + 30*self._MINUTE_
        self._MORNING_DAY_ = 11*self._HOUR_ + 23*self._MINUTE_
        self._DAY_EVENING_ = 18*self._HOUR_ + 0*self._MINUTE_

    def show(self):
        return f"{self.hours//10}{self.hours%10}:{self.minutes//10}{self.minutes%10}"

    def absTime(self):
        return self.hours*60 + self.minutes
    def add(self, increment = 1):
        self.minutes, self.hours = (self.absTime() + increment)%60, ((self.absTime() + increment)//60)%24

    def isMorning(self):
        if self.absTime() >= self._NIGHT_MORNING_ and self.absTime() <= self._MORNING_DAY_:
            return True
        return False
    def isDay(self):
        if self.absTime() >= self._MORNING_DAY_ and self.absTime() <= self._DAY_EVENING_:
            return True
        return False
    def isEvening(self):
        if self.absTime() >= self._DAY_EVENING_ and self.absTime() <= self._EVENING_NIGHT_:
            return True
        return False
    def isNight(self):
        if self.absTime() >= self._EVENING_NIGHT_ or self.absTime() <= self._NIGHT_MORNING_ :
            return True
        return False

    def sayHello(self):
        if self.isMorning():
            return "Доброе утро"
        if self.isDay():
            return "Добрый день"
        if self.isEvening():
            return "Добрый вечер"
        return "Добрая ночь"
        #Note: Граничные значения принадлежат обоим промежуткам,
        #           но этот метод фактически определяет их принадлежащими Утро-Утро-День-Вечер


_time = Time()
for a in range(27):
    print(_time.show())
    print(f"it's a {_time.sayHello()}, sir")
    _time.add(57)
_time.add(611)
print(_time.show())
print(f"it's a {_time.sayHello()}, sir")





