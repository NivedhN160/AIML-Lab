'''You Are Designing an AI module for a security testing tool. a smart padlock uses a 4 digit number pin
(0000-9999). However, you have some "heuristic" clues about the owner habits that can help you generate better guesses rather than just searching from 0000 upwards
The Clues
Pin in made of even numbers (02468)
the sum of 4 digits is exactly 16'''
data=[0,2,4,6,8]
pins=[]
for a in data:
    for b in data:
        for c in data:
            for d in data:
                if a+b+c+d==16:
                    e=f"{a},{b},{c},{d}"
                    pins.append(e)
print ("valid pins:")
for e in pins:
    print(e)