with open('source.csv') as csv:
    out = open('timeline.csv', 'w')
    line = csv.readline()
    while line != '':
        args = line.split(',')
        try:
            args[0] = str(float(args[0]) / 1268.6)
            print(args)
        except ValueError as e:
            print(e)
        out.write(','.join(args))
        line = csv.readline()
    out.close()