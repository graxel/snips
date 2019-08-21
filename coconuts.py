import random
COCONUTs = 0
TUNOCOCs = 0
for attempt in range(1):
    counter = 0
    garble = str()
    # last = garble[-7:]
    while ((garble != 'COCONUT') and (garble != 'TUNOCOC') and (counter < 10_000_000)):
        counter +=1
        garble = garble[-6:] + chr(random.randint(65,90))
        # last = garble[-7:]
        # print(garble)
        if (counter%1_000_000)==0:
            print(f'{counter:,} letters typed...')
    print(f'Round {attempt}: {garble} after {counter} letters')
    if garble == 'COCONUT':
        COCONUTs += 1
    if garble == 'TUNOCOC':
        TUNOCOCs += 1
print(f'\nFinal score:   COCONUTs {COCONUTs}   TUNOCOCs {TUNOCOCs}')