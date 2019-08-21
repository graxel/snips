import random
import datetime
COCONUTs = 0
TUNOCOCs = 0
for attempt in range(20):
    counter = 0
    garble = str()
    print(f'Round {attempt}:\nSearching',sep='',end='')
    while (('COCONUT' not in garble) and ('TUNOCOC' not in garble)):
        mult = 100
        counter += mult
        garble = garble[-6:] + ''.join([chr(random.randint(65,90)) for _ in range(mult)])
        if (counter%10_000_000)<mult:
            # clock = datetime.datetime.now()
            # print(f'{clock}\t{counter:,} letters typed...')
            print('.',sep='',end='',flush=True)
    # print('...')
    print(f'\nFound {garble} after {counter} letters')
    if 'COCONUT' in garble:
        COCONUTs += 1
    if 'TUNOCOC' in garble:
        TUNOCOCs += 1
    print(f'Score:   COCONUTs {COCONUTs}   TUNOCOCs {TUNOCOCs}\n')
print(f'Final score:   COCONUTs {COCONUTs}   TUNOCOCs {TUNOCOCs}')