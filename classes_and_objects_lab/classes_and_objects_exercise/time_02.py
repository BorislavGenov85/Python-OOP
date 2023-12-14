class Time:

    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        a_second = 1
        if self.seconds + a_second > Time.max_seconds:
            self.seconds = 00
            if self.minutes + a_second > Time.max_minutes:
                self.minutes = 00
                if self.hours + a_second > Time.max_hours:
                    self.hours = 00

                else:
                    self.hours += 1

            else:
                self.minutes += 1

        else:
            self.seconds += 1

        return Time.get_time(self)


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
