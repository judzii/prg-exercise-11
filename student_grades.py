from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        body = self.scores[index]
        if body >= 90:
            return "A"
        elif body >= 80:
            return "B"
        elif body >= 70:
            return "C"
        elif body >= 60:
            return "D"
        elif body >= 50:
            return "E"
        else:
            return "F"

    def find(self, hledane_body):
        indexy = []

        for index in range(len(self.scores)):
            if self.scores[index] == hledane_body:
                indexy.append(index)

        return indexy

    def get_sorted(self):
        novy_spisok = self.scores.copy()
        dlina = len(novy_spisok)

        for i in range(dlina):
            for j in range(0, dlina - i -1):
                if novy_spisok[j] > novy_spisok[j + 1]:
                    novy_spisok[j], novy_spisok[j + 1] = novy_spisok[j + 1], novy_spisok[j]

        return novy_spisok


def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print("pocet studentu:", results.count())
    print()

    for index