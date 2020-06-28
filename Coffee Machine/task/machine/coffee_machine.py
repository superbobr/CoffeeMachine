class CoffeeMachine:

    def __init__(self, water, milk, coffee, cups, money, status=''):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        self.status = status

    def get_user_input(self, user_input):
        self.user_input = user_input
        if user_input == 'remaining':
            self.get_remaining()
        elif user_input == 'take':
            self.take()
        elif user_input == 'fill':
            inp_water = int(input('Write how many ml of water do you want to add:\n'))
            inp_milk = int(input('Write how many ml of milk do you want to add:\n'))
            inp_coffee = int(input('Write how many grams of coffee beans do you want to add:\n'))
            inp_cups = int(input('Write how many grams of coffee beans do you want to add:\n'))
            self.fill(inp_water, inp_milk, inp_coffee, inp_cups)
        elif user_input == 'buy':
            user_choice = input(
                'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
            if user_choice != 'back':
                self.buy(user_choice)
                if self.water > 0 and self.milk > 0 and self.coffee > 0 and self.cups > 0:
                    print('I have enough resources, making you a coffee!')
                else:
                    need = ''
                    needs = {'water': self.water, 'milk': self.milk, 'coffee': self.coffee, 'cups': self.cups}
                    for key, values in needs.items():
                        if values < 0:
                            need = key
                    self.return_buy(user_choice)
                    print(f'Sorry, not enough {need}!')

    def take(self):
        print('I gave you ${}'.format(self.money))
        self.money = 0

    def fill(self, w, m, c, cu):
        self.water += w
        self.milk += m
        self.coffee += c
        self.cups += cu

    def buy(self, choice):
        if choice == '1':
            self.money += 4
            self.water -= 250
            self.coffee -= 16
            self.cups -= 1
        elif choice == '2':
            self.money += 7
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.cups -= 1
        elif choice == '3':
            self.money += 6
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.cups -= 1

    def get_remaining(self):
        print(
            'The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n${} of money'.format(
                self.water, self.milk, self.coffee, self.cups, self.money))

    def return_buy(self, choice):

        if choice == '1':
            self.money -= 4
            self.water += 250
            self.coffee += 16
            self.cups += 1
        elif choice == '2':
            self.money -= 7
            self.water += 350
            self.milk += 75
            self.coffee += 20
            self.cups += 1
        elif choice == '3':
            self.money -= 6
            self.water += 200
            self.milk += 100
            self.coffee += 12
            self.cups += 1


coffee_machine_1 = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    user_input = input('Write action (buy, fill, take, remaining, exit):\n')
    if user_input == 'exit':
        break
    else:
        coffee_machine_1.get_user_input(user_input)
