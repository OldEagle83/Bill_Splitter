import random

msg00 = 'Enter the number of friends joining (including you):'
msg01 = 'Enter the name of every friend (including you), ' \
        'each on a new line:'
msg02 = 'Enter the total bill value:'
msg03 = 'Do you want to use the "Who is lucky?" feature? Write Yes/No'
msg_lucky = '{} is the lucky one!'
msg_no_luck = 'No one is going to be lucky'
msg_sad = 'No one is joining for the party'


class Party:
    def __init__(self):
        self.attendants = dict()
        self.rsvp_count = 0
        self.bill = 0
        self.lucky_person = None

    def add_people(self, number):
        print(msg01)
        for _ in range(number):
            name = input()
            self.attendants[name] = 0

    def invite(self):
        print(msg00)
        number = int(input())
        if number > 0:
            self.rsvp_count += number
            self.add_people(number)

    def rsvp(self):
        if self.rsvp_count == 0:
            print(msg_sad)

    def take_bill(self):
        print(msg02)
        self.bill = int(input())

    def split_bill(self, bill, lucky=None):
        if self.rsvp_count > 0:
            if lucky is None:
                bill_split = round(bill / self.rsvp_count, 2)
                for person in self.attendants.keys():
                    self.attendants[person] += bill_split
            else:
                bill_split = round(bill / (self.rsvp_count - 1), 2)
                payers = list(self.attendants.keys())
                payers.remove(self.lucky_person)
                for person in payers:
                    self.attendants[person] += bill_split
        else:
            return
        print(self.attendants)

    def lucky(self):
        print(msg03)
        lucky = input()
        if lucky == 'Yes':
            self.lucky_person = random.choice(list(self.attendants.keys()))
            print(msg_lucky.format(self.lucky_person))
        else:
            print(msg_no_luck)


party01 = Party()
party01.invite()
party01.rsvp()
if party01.rsvp_count > 0:
    party01.take_bill()
    party01.lucky()
    party01.split_bill(party01.bill, party01.lucky_person)
