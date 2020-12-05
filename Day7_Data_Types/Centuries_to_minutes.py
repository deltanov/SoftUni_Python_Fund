century=int(input())

centuries=century
years=100*century
days=int(years*365.2422)
hours=int(days*24)
minutes=int(hours*60)

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")