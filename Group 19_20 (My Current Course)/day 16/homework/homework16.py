# 1) თქვენი დავალებაა for loop ების დახმარებით დაპრინტოთ 120 დან 500 მდე ყოველი მესამე ციფრი
# და გამირკვიეთ იყოფა თუ არა ეს ციფრები 3 ზე, 5 ზე, 7 ზე  და დამიპრინტეთ სათითადო ეც ფიფრები. 
# მიაწერეთ, რომ იყფა ეს ციფრი, კონკრეტულად 3ზე, 5ზე და7ზე

for i in range(120, 500, 3):
    if i % 3 == 0:
        print(i , "- ეს ციფრი იყოფა 3-ზე")
        if i % 5 == 0:
            print(i, "- ეს ციფრი იყოფა 5-ზე")
            if i % 7 == 0:
                print(i, "- ეს ციფრი იყოფა 7-ზე")
                
                
                #i think its done
