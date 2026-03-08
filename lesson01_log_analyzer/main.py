countInfo = 0
countWarning = 0
countError = 0
countDict = dict()
errorlines = list()

with open('training_logs.txt') as f:
    for lines in f:
        lines = lines.strip()
        if lines.startswith('INFO'):
            countInfo += 1
        elif lines.startswith('WARNING'):
            countWarning += 1
        elif lines.startswith('ERROR'):
            countError += 1
            errorlines.append(lines)

countDict['INFO'] = countInfo
countDict['WARNING'] = countWarning
countDict['ERROR'] = countError

for k, v in countDict.items():
    print(f'{k}: {v}')

print(f'Total log entries: {countError + countInfo + countWarning}')

print("System status - ")
if countError > 0:
    print("System has critical issues")
else:
    print("System healthy")


print("Error lines - ")
for i in errorlines:
    print(i)
        
            