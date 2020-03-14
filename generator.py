compNA = "@✨NA Comp Team A✨"
#compSIN = "@✨SIN Comp Team✨" unused for now
compRES = "@✨Comp Reserve✨"
one = "1 vs. 1"
two = "2 vs. 2"
three = "3 vs. 3"
four = "4 vs. 4"

postedTime = input("When will this announcement be posted? - ")

def printPings(a,b):
	print(a,b)

targetPings = input("Who will participate? (NA-A / NA-B)")

def askMainAgain():
	global targetPings
	targetPings = input("Who will participate? (NA / SIN) - ")

compReserve = input("Let @CompReserve know? (Y / N) - ")

def askReserveAgain():
	global compReserve
	compReserve = input("Let @CompReserve know? (Y / N) - ")

if targetPings.lower() == "na":
	mainPing = compNA
elif targetPings.lower() == "sin":
	mainPing = compSIN
else:
	print("Please enter either NA or SIN.")
	askMainAgain()

if compReserve.lower() == "y":
	reserve = " " + compRES
elif compReserve.lower() == "n":
	reserve = ""
else:
	print("Please enter either Y or N.")
	askReserveAgain()
	
opponent = input("Opponent clan? ")

def printHeader(text):
	print("Scrim with " + text)

def alternateName():
	global enemyClan
	altNameExists = input("Does the opponent have an alternate name? (Y / N) - ")
	if altNameExists.lower() == "y":
		altName = "(aka __" + input("What is the alternate name? - ") + "__)"
		enemyClan = "**" + opponent + "**" + " " + altName
	elif altNameExists.lower() == "n":
		enemyClan = "**" + opponent + "**"
	else:
		print("Please enter either Y or N.")
		alternateName()

alternateName()

scrimTypeAns = input("Is the scrim official or unofficial? (O / U) - ")

def askScrimTypeAgain():
	global scrimTypeAns
	scrimTypeAns = input("Is the scrim official or unofficial? (O / U) - ")

if scrimTypeAns.lower() == "o":
	scrimType = "**Official**"
elif scrimTypeAns.lower() == "u":
	scrimType = "**Unofficial**"
else:
	print("Please enter either O or U.")
	askScrimTypeAgain()

region = input("Please enter a region. - ")

def askTeamSizeAgain():
	global teamSize
	teamSize = input("Enter 'one', 'two', 'three' or 'four' for team sizes. - ")

teamSize = input("Enter 'one', 'two', 'three' or 'four' for team sizes. - ")

if teamSize.lower() == "one":
	teamSize = one
elif teamSize.lower() == "two":
	teamSize = two
elif teamSize.lower() == "three":
	teamSize = three
elif teamSize.lower() == "four":
	teamSize = four
else:
	print("Please enter a valid team size from the selections.")
	askTeamSizeAgain()

timeAndDate = input("Enter a scheduled date and time. If not decided yet, enter TBA. - ")

additionalNotes = input("Anything else you want to add? Enter TBA if none. - ")

print("")
print("")
print("-------------------------------------------")
print("")
print("(Posted " + postedTime + ")")
printPings(mainPing,reserve)
print("")
printHeader(enemyClan)
print("Scrim Type: " + scrimType)
print("Region: **" + region.upper() + "**")
print("Game type: **" + teamSize + "**")
if timeAndDate.lower() == "tba":
	print("Scrim date: *`TBA`*")
else:
	print("Scrim date: **" + timeAndDate + "**")
print("")
print("Additional Notes:")
if additionalNotes.lower() == "tba":
	print("`TBA`")
else:
	print(additionalNotes)
print("")
print("***ROSTER:***")
print("*`No one has signed up yet.`*")
print("")
print("-------------------------------------------")
