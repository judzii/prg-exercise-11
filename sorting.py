import random
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(spisok):
    novy_spisok = spisok.copy()
    dlina = len(novy_spisok)

    for i in range(dlina):
        indeks_min = i

        for j in range(i + 1, dlina):
            if novy_spisok[j] < novy_spisok[indeks_min]:
                indeks_min = j

        novy_spisok[i], novy_spisok[indeks_min] = novy_spisok[indeks_min], novy_spisok[i]

    return novy_spisok

def bubble_sort(spisok):
    novy_spisok = spisok.copy()
    dlina = len(novy_spisok)

    plt.ion()
    plt.show()

    for i in range(dlina):
        for j in range(0, dlina - i - 1):

            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(novy_spisok)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(novy_spisok)), novy_spisok, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if novy_spisok[j] > novy_spisok[j + 1]:
                novy_spisok[j], novy_spisok[j + 1] = novy_spisok[j + 1], novy_spisok[j]

    plt.ioff()
    plt.show()

    return novy_spisok

def main():
    # test_spisok = [8, 11, 4, 16, 6]
    # print("puvodni:", test_spisok)
    # print("serazeny:", selection_sort(test_spisok))
    # print("bubble:", bubble_sort(test_spisok))

    random_spisok = random_numbers(20)
    print("nahodny:", random_spisok)
    print("serazena:", selection_sort(random_spisok))
    print("buble:", bubble_sort(random_spisok))


if __name__ == "__main__":
    main()