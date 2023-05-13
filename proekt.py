from random import randint
print("привет ты попал в казино тут есть рулетка, блэкджек,слоты твой баланс 1000 ")
igra = input("во что вы хотите поиграть? (рулетка блэкджек слоты)")
balance = 1000
while igra != "выход":
    if igra == "рулетка":
        
            
        
        print("вы играете в рулетку, поставить можно на числа 0 32 15 40 4 10 8 42 67 19 94 37 46")
        cisla =[0, 32, 15, 40, 4, 10, 8, 42, 67, 19, 94, 37, 46]
        cislo = int(input("число на которое вы ставите"))
        
        if cislo in cisla:
            print("вы поставили на", cislo)
        else:
            print("такого числа нету")
            break
            
            
        stav = int(input("введите ставку"))
        

        while stav > balance:
            print("ставка больше чем ваш баланс")
            stav = int(input("введите ставку"))
            
        
        
        balance = balance - stav
        print("вы сделали ставку в ",stav,"теперь ваш баланс равен", balance)
        
        a = randint(0, 94)
        if a == cislo:
            print("поздравляю вы выйграли")
            
            balance = balance + stav * 3
            print("ваш баланс теперь",balance)
        else:
            print("выпало", a, "вы проиграли ваше число было", cislo)
            
            
            
            
            
            
            
            
            
            
    elif igra == "блэкджек":
        konec = False
        print("вы играете в блэкджек")
        
        
        
        dengi = int(input("поставьте ставку"))
        while balance < dengi:
            print("ставка больше чем ваш баланс")
            dengi = int(input("введите ставку"))
            
        player1 = randint(2,11)
            
            
        diler1 = randint(2,11)
           
        comandaBJ = input("введите команду пас взять ")
            
        print("первые очки диллера",diler1,"ваши очки",player1)
        while comandaBJ != "пас":
            konec = True
        if comandaBJ == "взять":
            player1 = player1 + randint(2,11)
            if player1 > 21:
                print("вы проиграли у вас больше 21 очка")
                break
            elif player == 21:
                konec = True
                print("у вас ровно 21 очко авто-стоп вы")
        else:
            print("вы написали команду которой не существует")
            comandaBJ = input("введите команду пас взять ")
            
        while konec != True:
            diler1 = diler1 + randint(2,11)
            print("дилер взял карту теперь у него",diler1)
            if diler1 > 21:
                print("вы выйграли")
                dengi = dengi * 2
                break
                print("теперь у вас", balance)
            elif diler1 > player1:
                print("вы проиграли")
                balance = balance - dengi
                print("теперь у вас", balance)
                break
            elif diler1 == player1:
                print("ничья, ваш баланс не изменился",balance)
                    
        

