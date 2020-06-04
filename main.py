import sys

# NOTE: call stack for long strings might be a problem
#   but the limit is 100 in spec, so we are ok
def n_flips(s):
    if len(s) == 1:
        return 1 if s[0] == '-' else 0

    while(True):
        if s[0] != s[1]:
            return n_flips(s[1:]) + 1
        return n_flips(s[1:])


def get_num_flips(s):
    if len(s) == 1:
        return 1 if s[0] == '-' else 0

    count = 0
    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            count = count + 1

    if s[-1] == '-':
        count = count + 1

    return count


def main():
    with open(sys.argv[1]) as f:
        num_tests = f.readline()

        # NOTE: if the data set if large, this could overflow
        # maybe stream, and reuse the same string, pre allocated to make of 100
        #  while using less memory, this will be slower
        tests = f.read()

    for i, test in enumerate(tests.split()):
        print('Case #%s: %s %s' % (i+1, get_num_flips(test), n_flips(test)))


if __name__ == "__main__":
    # execute only if run as a script
    main()
