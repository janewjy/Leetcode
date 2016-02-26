def sorting(s):
    tokens = s.split('5')
    output = []
    for i in xrange(len(tokens)):
        if tokens[i]:
            output.append(int(tokens[i]))
    output.sort()
    output = [str(i) for i in output]

    return ' '.join(output)

