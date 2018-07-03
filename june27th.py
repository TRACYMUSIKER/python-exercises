for student in today_seats:
    print student

IS EQUIVALENT TO


i = 0 
while i < len(today_seats):
    print today_seats[i]
    i = i + 1

IS EQUIVALENT TO



For i in range(0, len(today_seats):
	print today_seats[i]

IS EQUIVALENT TO

for i in range(len(today_seats)):
    print today_seats[i]

for i in range(len(today_seats)):
    if today_seats[i] == yesterday_seats[i]:
        print 'Move!'

or I in range(height):
	for j in range(width)
		if I == 0 or I - 1 == height or
