import sys

# NOTE: this can be done recursively but the
#   call stack for long strings might overflow
#   the spec says the  limit is 100, so it should be ok
#       The iterative approach is also faster, so I am
#       using that one. I am leaving this here for refrence
#       because it very clear
def n_flips_recurse(s):
    if len(s) == 1:
        return 1 if s[0] == '-' else 0

    if s[0] != s[1]:
        return n_flips_recurse(s[1:]) + 1
    return n_flips_recurse(s[1:])


def n_flips(s):
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
        f.readline()  # read the first line, but we don't use it
        tests = f.read()

    for i, test in enumerate(tests.split()):
        print('Case #%d: %d' % (i+1, n_flips(test)))


if __name__ == "__main__":
    main()
