geeljanee = input("Is de kaas geel?").lower()

if geeljanee == "ja":
    gatenjanee = input("Zitten er gaten in?").lower()
    if gatenjanee == "ja":
        hardalssteen = input("Is de kaas hard als steen?").lower()
        if hardalssteen == "ja":
            print("Parmigiano Reggiano")
        elif hardalssteen == "nee":
            print("Goudse Kaas")

    if gatenjanee == "nee":
        veelTeDuur = input("Is de kaas veel te duur?")
        if veelTeDuur == "ja":
            print("Emmenthaler")
        elif veelTeDuur == "nee":
            print("Leerdammer")

if geeljanee == "nee":
    BlauweSchimmel = input("Heeft de kaas blauweSchimmel?")
    if BlauweSchimmel == "ja":
        Ja_enmeschienkorst = input("Heeft de kaas een korst")
        if Ja_enmeschienkorst == "nee":
            print("Foume d ambert")
        elif Ja_enmeschienkorst == "ja":
            print("Blue de Rochbaron")

    elif BlauweSchimmel == "nee":
        nee_en_meschienkorst = input("Heeft de kaas een korst")
        if nee_en_meschienkorst == "nee":
            print("Mozzarella")
        elif nee_en_meschienkorst == "ja":
            print("Cammenbert")