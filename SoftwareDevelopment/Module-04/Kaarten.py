import random
Kleuren = ("Harten", "Klaveren", "Schoppen", "Ruiten")
Types = ("2","3","4","5","6","7","8","9","10", "Boer", "Vrouw", "Heer", "aas")
Deck = []
for x in range(4):
    for h in range(13):
        Deck.append(Kleuren[x] +" "+ Types[h])
    Deck.append("Joker") if x < 2 else None
random.shuffle(Deck)
for g in range(7):
    print(f"Kaart {g + 1}: "+ Deck[0])
    Deck.remove(Deck[0])
print(f"\ndeck ({len(Deck)} kaarten): {', '.join(Deck)}")