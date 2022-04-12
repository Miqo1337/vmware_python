while True:
	try:
		year = int(input("Enter a number\n"))
		break;
	except ValueError:
		print("Wrong input")
		continue

def solution(year):
	if year % 100 == 0:
		print((year // 100) - 1)
	else:
		print(year // 100)

solution(year)
