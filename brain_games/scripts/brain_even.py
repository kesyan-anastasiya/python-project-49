import random
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even(name):
    count = 0
    beg = 1
    end = 100

    while count < 3:
        random_integer = random.randint(beg, end)
        print(f'Question: {random_integer}')
        answer = prompt.string('Your answer: ')
        true_answer = random_integer % 2 == 0 and "yes" or "no"
        if answer == true_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{true_answer}'. "
                  f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    is_even(name)


if __name__ == '__main__':
    main()
