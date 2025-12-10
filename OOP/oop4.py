class Journal:
    def __init__(self, title, filename):
        self.title = title
        self.filename = filename
        try:
            open(self.filename, "a").close()
        except Exception as e:
            print("eror")
    def wrint(self, text):
        with open(self.filename, "a") as e:
            e.write(text + '\n')
    def rewrit(self, text):
        with open(self.filename, "w") as e:
            e.write(text + '\n')
    def read(self):
        with open(self.filename, "r") as d:
            return d.read()
        

journal = Journal("Мой дневник", "diary.txt")

journal.wrint("Сегодня я выучил классы в Python")
journal.wrint("Мне это понравилось!")

print(journal.read())

journal.rewrit("Я начал новый дневник")
print(journal.read())
