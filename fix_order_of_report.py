# in the rare case that you forget to replace tickers.csv here is a script that can let you salvage most of your scrapes

tickers_used = open('tickers.csv') # length should be 1 + length of report 
tickers_correct = open('tickers2.csv')
report = open('report.csv')

r_array = []
for r in report:
	r_array.append(r)

ticker_data = {}
i = 0
for tu in tickers_used:
	try:
		tus = tu.split(",")[0] # get rid of crap
		ticker_data[tus] = r_array[i]
		i += 1
	except:
		break

for tc in tickers_correct:
	tcs = tc.split("\n")[0].strip() # get rid of crap
	if tcs in ticker_data:
		try:
			print(tcs + ",", ticker_data[tcs])
		except:
			print("must be done")
			break
	else:
		print(tcs + ", did not find data for this stock")
