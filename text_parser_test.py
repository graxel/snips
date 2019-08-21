
raw_text = """13.45 trash bags and tp
8.45 Dishwasher Detergent

Apostales yerba mate gin

Explain my background story

cover letter, touch on whats 



lions mane 5-20g
psilocybe 0.1-1g
vit b3 100-200mg

Customer Success Mgr 

Professional Services and Implementation 


Ron Zacapa

Word Cloud color changes with age-weather radar colors 

Wild Side West - Bernal Heights bar


SAP North Carolina 

yoga
improv
Bay area myco
kickball

twist
karl_rockwell@hotmail


noc noc bar

Laundry and clean up room


ODC
Dance mission theatre
smok



Peggy Sue got Married 



Outer ring for rotary woofer? or maybe several rings. Rings could even be connected together for stiffness. Like a spiderweb
or just very stiff, sturdy vanes

Small blade angles with most likely give a less distorted sound, however, would require a faster rotation.

Why not increase size? Size is the limiting parameter. Sell different diameters and that will be the different product offerings / power limitations. 

How to damp turbulence noise? maybe some kind of stuffing or an air distributor, like a showerhead? 

What is the ideal flow profile? Turbulent, Laminar Quadratic or flat? Laminar isnt possible with the vanes whizzing by. ill have to look into fan or turbine design. variable attack angle, variable pie slice, straight parallel blades. 



Music recommendations 

The Reflex
rayko
Fantastic voyage lakeside

art bazzle Miami 

u wish it would rain temptations
i can't help myself 4 tops

position
Congratulations on using meditation to control emotion through self reflection 

Amnesia Mission jazz on Weds

Yall definitely gon be wanting to be suckin on Rick Black (brand cigars) 

vreatest weakness 
curiosity. Now you might be thinking that I'm taking the cop out giving a strenth as a weakness, but here me out. The curiosity manifests as rebellion if stifled with a response from authority of "because I said so" ot "That's just the way things are" 


faahion show girl Angelica Janice naro 5102219668 cake.angel007@gmail.com
a
In addition Salesforce's Ohana company culture, I am most interested in working for Salesforce due to tthe huge pgrowth potential Salesforce offers. This Sale analyst position is the perfect mix of client-facing sales and data analysis 
As a mix of data analysis and sales, this position highly interests me


The National - band 
mushrooms bbc documentary
Thw hunt - David Attenborough

Almost any problem boils down to alack of education 
The vast majority of problems can be solved through education 


isnt mindfulness the same thing constantly questioning everything you do? 

3882.06

the youngest truffle dealer in NY

writers' club / book club


mario lopez



Arbitrage bot: 

Ventanillas de exchange currency pairs


Compulsive ____ to improve efficiency 

attention to 



Three phone state shortcuts:

Concentration 
Calls, alarms, and calendar appointments at low volume
all other notifications off

Out (Loud)  
All high volume + vibrate

Home 
All medium volume

smoke stqck dogpatch

"""



#raw_text = input("Enter some text:")

words=dict()

text = raw_text

#replace all uppercase with lowercase
alphabet = []
for a in range(26):
    alphabet.append([chr(65+a),chr(97+a)])

for letter in alphabet:
    text = text.replace(letter[1] , letter[0])

#replace all punctuation with spaces
punct_list = [',', '.', ':', '-', '(', ')',
             '\"', '\'', '/', '\n', '?', '!']
for punct in punct_list:
    text = text.replace(punct, ' ')

i = text.find(" ")
while i > -1:
    word = text[:i]
    if len(word) > 0:
        words.append(word)
    text = text[i+1:]
    #print("|", word, "|", sep="")
    i = text.find(" ")
    
last_word = text    
if len(last_word) > 0:
    words.append(last_word)
#print("_", last_word, "_", sep="")

print(words) 
words.sort()
print(words)

word_freq = []
prev = ""
for word in words:
    if word == prev:
        word_freq[len(word_freq)-1][1] = 1 +\
        word_freq[len(word_freq)-1][1] 
        print("+1")
    else:
        word_freq.append([word, 1])
        print(word_freq[len(word_freq)-1][0],
        '\t', word_freq[len(word_freq)-1][1])
        
    prev = word

print(word_freq)

