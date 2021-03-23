import json
# opening and reading 
file = open("airlines.csv",'r')

# finding unique airports
airports = []
airport_data = {}
count = 0
firstLine = True
for line in file:
    if firstLine:       #removing header line of file
        firstLine = False
        continue
    airports.append(line.split('"')[1])

unique_airports = set(airports) #finding unique elements of airports
for i in unique_airports:
    for j in airports:
        if(i == j):
            count+=1

    airport_data[i] = count
    count = 0

json_val = eval(json.dumps(airport_data)) #converting data into json
a = json.dumps(json_val,indent = 4) #prints the data in json format with indent
print(a)

#max value without using max()
most_mentioned = 0
for value in json_val:
    if json_val[value] > most_mentioned:
        most_mentioned = json_val[value]
        most_mentioned_key = value
print(most_mentioned_key,most_mentioned)

#minimum value without using min()
least_mentioned = most_mentioned
for value in json_val:
    if json_val[value] < least_mentioned:
        least_mentioned = json_val[value]
        least_mentioned_key = value
print(least_mentioned_key,least_mentioned)
