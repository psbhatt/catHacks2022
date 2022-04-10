import wordleSolver


def main():
    counter = 0

    for i in range(1000):
        result = wordleSolver.main()
        if result:
            counter += 1

    counter = counter/1000

    print(f"Accuracy was {counter} ")


if __name__ == '__main__':
    main()