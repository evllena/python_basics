class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date(cls, date):
        num = date.split('-')
        if Date.check_date(date):
            day = int(num[0])
            month = int(num[1])
            year = int(num[2])
            return f"Введенная дата: {day:02}.{month:02}.{year:04}"

    @staticmethod
    def check_date(date):
        date = date.split('-')
        return True if int(date[0]) in range(1, 32) and int(date[1]) in range(1, 13) else False


date1 = Date("07-05-1992")
print(date1.date)
print(Date.get_date("07-05-1992"))
print(Date.check_date("1-12-1992"))