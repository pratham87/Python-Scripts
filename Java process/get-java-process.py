def getApp():
    with open('/Users/Prathamesh/Desktop/ws1/github/Ruby/Fundamentals/test.txt') as f:
        for line in f.readlines():
            values = line.split()
            if len(values) >= 25:
                pid = values[1]
                #if any(x != ("Jun" and "Jul") for values[4]):
                if ":" not in values[4] and "Jul" not in values[4]:
                    date = values[4]
                    for value in values:
                        if 'DISApplicationName' in value:
                            appName = value.split("=")[1]
                        if 'Dmme.app.hostname' in value:
                            hostname = value.split("=")[1]
                    print '{:5}'.format(pid),'\t','{:5}'.format(date),'\t','{:>1}'.format(appName),'\t\t','{:>10}'.format(hostname)


def getFailures():
    print "Failures: "
    with open('/Users/Prathamesh/Desktop/ws1/github/Ruby/Fundamentals/test.txt') as f:
        for line in f.readlines():
            values = line.split()
            if 'FAILURE' in values[2]:
                print '{:>10}'.format(values[3])
                
getApp()
getFailures()        