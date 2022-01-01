class Category:


    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.total_amount = 0
        self.total_withdrawal = 0
        self.only_deposit = 0



    def __str__(self):
        checkToDisplay = []

        line_length = 30
        starsNumber = int((line_length - len(self.category)) / 2)
        title = starsNumber * '*' + self.category + starsNumber * '*'
        checkToDisplay.append(title+"\n")


        for item in self.ledger:
            description = item['description'][:23]
            amount = '{0:.2f}'.format(float(item['amount']))
            space = " " * (line_length - (len(description) + len(str(amount))))
            item_to_display = description + space + amount[:7]
            checkToDisplay.append(item_to_display+"\n")

        total = 'Total: {0:.2f}'.format(float(self.total_amount))
        checkToDisplay.append(total)

        return str("".join(checkToDisplay))



    def deposit(self, amount_of_deposit, description=""):
        self.to_deposit = {"amount": amount_of_deposit, "description": description}
        self.ledger.append(self.to_deposit)
        self.total_amount += amount_of_deposit
        self.only_deposit += amount_of_deposit



    def withdraw(self, amount_of_withdraw, description=""):
        self.amount_of_withdraw = -amount_of_withdraw
        if self.check_funds(amount_of_withdraw):
            self.withdrawal = {"amount": self.amount_of_withdraw, "description": description}
            self.ledger.append(self.withdrawal)
            self.total_amount += self.amount_of_withdraw
            self.total_withdrawal -= self.amount_of_withdraw
            return True
        return False



    def transfer(self, amount_to_transfer, transfer_to_category):
        self.amount_to_transfer = -amount_to_transfer
        if self.check_funds(amount_to_transfer):
            self.withdraw(amount_to_transfer, 'Transfer to ' + transfer_to_category.category)
            transfer_to_category.deposit(amount_to_transfer, 'Transfer from ' + self.category)
            return True
        return False



    def check_funds(self, amount):
        self.balance = self.total_amount - amount
        if self.balance >= 0:
            return True
        else:
            return False



    def get_balance(self):
        return self.total_amount



def create_spend_chart(categories):

    to_display = []
    list_of_name = []
    stakeList = []
    problems = []

    to_display.append("Percentage spent by category\n")

    for scale_number in reversed(range(110)):
        if scale_number % 10 == 0:
            if len(str(scale_number)) == 2:
                scale_number = " " + str(scale_number) + "|"
            elif len(str(scale_number)) == 1:
                scale_number = "  " + str(scale_number) + "|"
            else:
                scale_number = str(scale_number) + "|"
            stakeList.append(scale_number)

    problems.append(stakeList)
    all_category_withdrawal = 0
    number_of_categories = 0
    longest_category_name = 0

    for cat in categories:
        all_category_withdrawal += cat.total_withdrawal
        if len(cat.category) > longest_category_name:
            longest_category_name = len(cat.category)

    for cat in categories:
        category = cat.category
        if len(category) < longest_category_name:
            remaning_length = (longest_category_name - len(category)) * " "
            category = category + remaning_length
        splitted_category = list(category)
        list_of_name.append(splitted_category)
        number_of_categories += 1


        q = cat.total_withdrawal / all_category_withdrawal
        percent = round(q * 100)
        if percent < 10:
            percent =  0
        percentRounded = round(percent/10)*10



        charStack = int(1+ (int(percentRounded)) / 10) * ':o '
        spaces = 11 - (len(charStack) / 3)
        stake = (int(spaces) * ':  ') + charStack
        stakeToAdd = stake.split(":")

        if percentRounded == 100 or len(stakeToAdd) == 12:
            del stakeToAdd[0]
        else:
            stakeToAdd[0] = "  "
        problems.append(stakeToAdd)

    
    for i in range(len(stakeList)):
        for x in problems:
            to_display.append(x[i] + ' ')
        to_display.append('\n')


    underline = 4 * " " + 3 * (number_of_categories * "-") + "-"
    to_display.append(underline + '\n')


    for letter in range(longest_category_name):
        to_display.append("   ")
        for word in list_of_name:
            line = "  " +word[letter]
            to_display.append(line)
        to_display.append("  \n")

    to_display[-1] = '  '
    to_display = "".join(to_display)

    return to_display


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)




create_spend_chart([business, food, entertainment])