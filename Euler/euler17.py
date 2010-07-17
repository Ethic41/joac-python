def inWords(number):
    table = {'0':'','1':'one','2':'two','3':'three', '4':'four', '5':'five','6':'six', '7':'seven', '8':'eigth', '9':'nine', '10':'ten','11':'eleven', '12':'twelve','13':'thirteen', '14':'fourteen','15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen', '20':'twenty', '30':'thirty', '40':'forty','50':'fifty', '60':'sixty', '70':'seventy', '80':'eighty', '90':'ninety'}
    snumber = str(number)
    if number <=  20:
        return table[snumber]
    elif number < 100:
        return table[snumber[0]+'0']+table[snumber[1]]
    elif number < 1000:
        if int(snumber[1:]):
            return table[snumber[0]]+'hundredand'+inWords(int(snumber[1:]))
        else:
            return table[snumber[0]]+'hundred'
    elif number == 1000:
        return 'onethousand'
    else:
        return 'something wrong'
