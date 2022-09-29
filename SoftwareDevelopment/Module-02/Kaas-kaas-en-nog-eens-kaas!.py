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
        veelTeDuur = input("Is de kaas veel te duur?").lower()
        if veelTeDuur == "ja":
            print("Emmenthaler")
        elif veelTeDuur == "nee":
            print("Leerdammer")

if geeljanee == "nee":
    BlauweSchimmel = input("Heeft de kaas blauweSchimmel?").lower()
    if BlauweSchimmel == "ja":
        Ja_enmeschienkorst = input("Heeft de kaas een korst").lower()
        if Ja_enmeschienkorst == "nee":
            print("Foume d ambert")
        elif Ja_enmeschienkorst == "ja":
            print("Blue de Rochbaron")

    elif BlauweSchimmel == "nee":
        nee_en_meschienkorst = input("Heeft de kaas een korst").lower()
        if nee_en_meschienkorst == "nee":
            print("Mozzarella")
        elif nee_en_meschienkorst == "ja":
            stinkt_de_kaas = input("Stinkt de kaas?")
            if stinkt_de_kaas == "ja":
                print("Cammenbert")
            elif stinkt_de_kaas == "nee":
                print("Brie")