MBO_Diploma_4 = input("Heeft u een MBO 4 diploma? J/N")
Geldig_vrachtwagen_rijbewijs = input("Heeft u een geldig vrachtwagen rijbewijs J/N")
In_bezit_van_hoge_hoed = input("Bezit u een hoge hoed J/N")
Hoe_lang_bent_u = int(input("Hoe Lang bent u"))
Hoe_zwaar_bent_u = int(input("Hoe zwaar bent u"))
Certificaat_overleven = input("Heeft u het Certificaat “Overleven met gevaarlijk personeel J/N")
Dressuur = int(input("Hoe veel jaar Dressuur"))
Jongleren = int(input("Hoe veel jaar jongleren"))
Acteren = int(input("Hoe veel jaar Acrobatiek"))
Gender = input("Man of Vrouw?")
if Gender == "Man":
    Heeft_snor = input("Heeft u een snor?")
    Hoe_Breed = int(input("Hoe breed is de snor"))
    Gender_ok = Heeft_snor == "J" and Hoe_Breed >= 10
elif Gender == "Vrouw":
    Haar_kleur = input("Wat is uw haar kleur")
    Hoe_lang_haar = int(input("Hoe lang is uw haar"))
    Gender_ok = Haar_kleur == "Rood" and Hoe_lang_haar >= 20
if MBO_Diploma_4 == "J" and Geldig_vrachtwagen_rijbewijs == "J" and In_bezit_van_hoge_hoed == "J" and Gender == "Man" and Gender_ok == True and (Hoe_lang_bent_u >= 150 and Hoe_lang_bent_u <= 220) and (Hoe_zwaar_bent_u >= 90 and Hoe_zwaar_bent_u <= 120) and (Dressuur >= 4 or Jongleren >= 5 or Acteren >= 3):
    print("U bent ge accepteerd voor een gesprek")
else:
    print("Heenlaas u heeft het niet gehaald")