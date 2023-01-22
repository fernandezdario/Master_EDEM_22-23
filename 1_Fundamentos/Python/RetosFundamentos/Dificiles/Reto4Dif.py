def programLanguage(listLanguages: list) -> dict:

    listUser: dict = dict.fromkeys(listLanguages, '')

    for i in listLanguages:

        while True:
            
            yesNoLanguage = input(f'¿Conoces el lenguaje de programación {i}? (si / no) ')
            
            if yesNoLanguage != 'si' and yesNoLanguage != 'no':
                print('Lo siento, no te he entendido. Prueba otra vez')
            
            else:
                listUser[i] = yesNoLanguage
                break
        
    return listUser