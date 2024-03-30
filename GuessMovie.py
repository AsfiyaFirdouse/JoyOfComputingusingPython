import random

movies = ['anand', 'drishyam', 'golmaal', 'black friday', 'dangal', 'vikram vedha', 'taare zameen par']


def create_question(movies):
    n = len(movies)
    letter = list(movies)
    temp = []
    for i in range(n):
        if letter[i] == ' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn = ''.join(str(x) for x in temp)
    return qn


def is_present(letter, movies):
    c = movies.count(letter)
    if c == 0:
        return False
    else:
        return True


def unlock(qn, movies, letter):
    ref = list(movies)
    qn_list = list(qn)
    temp = []
    n = len(movies)
    for i in range(n):
        if ref[i] == ' ' or ref[i] == letter:
            temp.append(ref[i])
        else:
            if qn_list[i] == '*':
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new = ''.join(str(x) for x in temp)
    return qn_new


def play():
    p1name = input('Player 1 enter ur name:')
    p2name = input('Player 2 enter ur name:')
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True
    while willing:
        if turn % 2 == 0:
            # player1
            print(p1name, 'Your Turn')
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input('Your Letter:')
                if (is_present(letter, picked_movie)):
                    # unlock
                    modified_qn = unlock(modified_qn, picked_movie, letter)
                    print(modified_qn)
                    d = int(input('Press 1 to guess movie or 2 unlock another letter:'))
                    if d == 1:
                        ans = input('Your answer:')
                        if ans == picked_movie:
                            pp1 += 1
                            print('Answer is correct')
                            not_said = False
                            print(p1name, 'Your Score', pp1)
                        else:
                            print('Wrong Answer,Try again')


                else:
                    print(letter, ' not found')
            c = input('Press 1 to continue n 0 to quit')
            if c == 0:
                print(p1name, 'Your Score:', pp1)
                print(p2name, 'Your Score:', pp2)
                print('Thanks for playing')
                print('Have a nice day.')
                willing = False
        else:
            # player2
            print(p2name, 'Your Turn')
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input('Your Letter:')
                if (is_present(letter, picked_movie)):
                    # unlock
                    modified_qn = unlock(modified_qn, picked_movie, letter)
                    print(modified_qn)
                    d = int(input('Press 1 to guess movie or 2 unlock another letter:'))
                    if d == 1:
                        ans = input('Your answer:')
                        if ans == picked_movie:
                            pp2 += 1
                            print('Answer is correct')
                            not_said = False
                            print(p2name, 'Your Score', pp2)
                        else:
                            print('Wrong Answer,Try again')


                else:
                    print(letter, ' not found')
            c = input('Press 1 to continue n 0 to quit')
            if c == 0:
                print(p1name, 'Your Score:', pp1)
                print(p2name, 'Your Score:', pp2)
                print('Thanks for playing')
                print('Have a nice day.')
                willing = False
        turn += 1


play()

