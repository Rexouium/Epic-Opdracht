import math
import time
from termcolor import colored
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_TENT_GOLD_PER_WEEK
from data import COST_HORSE_SILVER_PER_DAY
from data import JOURNEY_IN_DAYS
from data import COST_INN_HUMAN_SILVER_PER_NIGHT
from data import COST_INN_HORSE_COPPER_PER_NIGHT


# #################### M04.D02.O2 #####################


def copper2silver(amount: int) -> float:
    return amount / 10


def silver2gold(amount: int) -> float:
    return amount / 5


def copper2gold(amount: int) -> float:
    silver = copper2silver(amount)
    return silver2gold(silver)


def platinum2gold(amount: int) -> float:
    return amount * 25


def getPersonCashInGold(personCash: dict) -> float:
    gold = personCash['gold']
    gold += copper2gold(personCash['copper'])
    gold += silver2gold(personCash['silver'])
    gold += platinum2gold(personCash['platinum'])
    return gold


# #################### M04.D02.O4 #####################


def getJourneyFoodCostsInGold(people: int, horses: int) -> float:
    copperCosts = JOURNEY_IN_DAYS * (people * COST_FOOD_HUMAN_COPPER_PER_DAY)
    gold = copper2gold(copperCosts)
    copperCosts = JOURNEY_IN_DAYS * (horses * COST_FOOD_HORSE_COPPER_PER_DAY)
    gold += copper2gold(copperCosts)
    return round(gold, 2)


# #################### M04.D02.O5 #####################


def getFromListByKeyIs(list: list, key: str, value: any) -> list:
    lijstje = []
    for x in list:
        if x[key] == value:
            lijstje.append(x)
    return lijstje


def getAdventuringPeople(people: list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)


def getShareWithFriends(friends: list) -> int:
    return getFromListByKeyIs(friends, "shareWith", True)


def getAdventuringFriends(friends: list) -> list:
    Friendlist = []
    adv = getAdventuringPeople(friends)
    share = getShareWithFriends(friends)
    for x in adv:
        if x['adventuring'] and x['shareWith'] and x not in Friendlist:
            Friendlist.append(x)
    for y in share:
        if y['adventuring'] and y['shareWith'] and y not in Friendlist:
            Friendlist.append(y)
    return Friendlist


# #################### M04.D02.O6 #####################


def getNumberOfHorsesNeeded(people: int) -> int:
    return math.ceil(people / 2)


def getNumberOfTentsNeeded(people: int) -> int:
    return math.ceil(people / 3)


def getTotalRentalCost(horses: int, tents: int) -> float:
    tentvariable = math.ceil(JOURNEY_IN_DAYS / 7) * (tents * COST_TENT_GOLD_PER_WEEK)
    horsevariable = horses * (JOURNEY_IN_DAYS * COST_HORSE_SILVER_PER_DAY)
    return tentvariable + silver2gold(horsevariable)


# #################### M04.D02.O7 #####################


def getItemsAsText(items: list) -> str:
    item_gear_Text = []
    for item in items:
        item_gear_Text.append(f"{item['amount']}{item['unit']} {item['name']}")
    return ', '.join(item_gear_Text)


def getItemsValueInGold(items: list) -> float:
    value = float()
    for item in items:
        aantal = item['amount']
        PrijsSoort = item['price']['type']
        prijs = item['price']['amount']

        if PrijsSoort == 'copper':
            value += aantal * copper2gold(prijs)
        elif PrijsSoort == 'silver':
            value += aantal * silver2gold(prijs)
        elif PrijsSoort == 'platinum':
            value += aantal * platinum2gold(prijs)
        else:
            value += aantal * prijs
    return value


# #################### M04.D02.O8 #####################


def getCashInGoldFromPeople(people: list) -> float:
    totalCashingold = 0
    for person in people:
        totalCashingold += person['cash']['gold']
        totalCashingold += platinum2gold(person['cash']['platinum'])
        totalCashingold += silver2gold(person['cash']['silver'])
        totalCashingold += copper2gold(person['cash']['copper'])
    return totalCashingold


# #################### M04.D02.O9 #####################


def getInterestingInvestors(investors: list) -> list:
    Invertorlist = []
    for investor in investors:
        if investor['profitReturn'] <= 10:
            Invertorlist.append(investor)
    return Invertorlist


def getAdventuringInvestors(investors: list) -> list:
    investors = getInterestingInvestors(investors)
    JoiningInvestor = []
    for investor in investors:
        if investor['adventuring']:
            JoiningInvestor.append(investor)
    return JoiningInvestor


def getTotalInvestorsCosts(investors: list, gear: list) -> float:
    total = 0
    investors = getAdventuringInvestors(investors)
    for investor in range(len(investors)):
        total += getItemsValueInGold(gear)
    total += getJourneyFoodCostsInGold(len(investors), len(investors))
    total += getTotalRentalCost(len(investors), len(investors))
    print(total)
    return total


# #################### M04.D02.O10 #####################


def getMaxAmountOfNightsInInn(leftoverGold: float, people: int, horses: int) -> int:
    Mensencosten = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    Pardencosten = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    return int(leftoverGold / (Pardencosten + Mensencosten))


def getJourneyInnCostsInGold(nightsInInn: int, people: int, horses: int) -> float:
    mensengoudpernacht = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    paardengoudpernacht = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    return round((mensengoudpernacht + paardengoudpernacht) * nightsInInn, 2)


# #################### M04.D02.O12 #####################


def getInvestorsCuts(profitGold: float, investors: list) -> list:
    shares = []
    investors = getInterestingInvestors(investors)
    for investor in investors:
        shares.append(round(investor['profitReturn'] / 100 * profitGold, 2))
    return shares


def getAdventurerCut(profitGold: float, investorsCuts: list, fellowship: int) -> float:
    totalShares = 0
    for sharedcash in investorsCuts:
        totalShares += sharedcash
    return round((profitGold - totalShares) / fellowship, 2)


# #################### M04.D02.O13 #####################


def getEarnigs(profitGold: float, mainCharacter: dict, friends: list, investors: list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(interestingInvestors)
    investorsCuts = getInvestorsCuts(profitGold, interestingInvestors)
    goldshare = getAdventurerCut(profitGold, investorsCuts, len(adventuringFriends) + len(adventuringInvestors) + 1)

    for person in people:
        BeginGoud = getPersonCashInGold(person['cash'])
        eindgoud = BeginGoud

        if person == mainCharacter:
            eindgoud += goldshare + round(len(adventuringFriends) * 10, 2)
        elif person in adventuringInvestors:
            eindgoud += goldshare
        elif person in adventuringFriends:
            eindgoud += goldshare - 10
        if person in interestingInvestors:
            eindgoud += round(profitGold * person['profitReturn'] / 100, 2)

        earnings.append({
            'name': person['name'],
            'start': round(BeginGoud, 2),
            'end': round(eindgoud, 2)
        })
    return earnings


# #################### view functions #####################


def print_colorvars(txt: str = '{}', vars: list = [], color: str = 'yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']), vars)
    print(txt.format(*vars))


def print_title(name: str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')


def print_chapter(number: int, name: str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')


def nextStep(secwait: int = 1) -> None:
    print('')
    time.sleep(secwait)


def ifOne(amount: int, yes: str, no: str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()
