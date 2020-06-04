import sys

def get_num_flips(s):
    if len(s) == 1:
        if s[0] == '-':
            return 1
        else:
            return 0

    count = 0
    i = 0
    j = 1

    while(True):
        if s[i] != s[j]:
            count = count + 1
            i = j

        if j == len(s) - 1:
            if s[j] == '-':
                count = count + 1
            break

        j = j + 1

    return count


def main():
    with open(sys.argv[1]) as f:
        num_tests = f.readline()
        tests = f.read()

    for i, test in enumerate(tests.split()):
        print('Case #%s: %s' % (i+1, get_num_flips(test)))

if __name__ == "__main__":
    # execute only if run as a script
    main()
