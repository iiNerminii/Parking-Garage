class gar_Park():

    def __init__(self, capacity):
        self.tickets = []
        self.currentTicket = {}
        self.capacity = capacity

    def hello_cust(self):
        print("Hello and welcome to the world famous Parking Garage famous for... parking!!!")

    # This is where we recieve the ticket or see if there are any available spaces
    def my_ticket(self):
        print("We have parking available!")
        self.length_stayed = input("How long would you like to stay we have 4 options: 1, 2, 5, or 24 hours? ")
        if int(self.length_stayed) == 1 or int(self.length_stayed) == 2 or int(self.length_stayed) == 5 or int(self.length_stayed) == 24:
            choice = input(f"You have chosen to reserve a space for {self.length_stayed} hours is this correct? ")
            if choice.lower() == 'yes':
                self.tickets.append(1)
                print(f"Here, your ticket number is {self.tickets[0]}. We will reserve the space for {self.length_stayed} hours thank you!")
                self.currentTicket = {"Current Ticket" : "1 Not Paid"}
                    
            else:
                print("Sorry for the error, please select the amount of time you would like to reserve the space for again... ")
                self.my_ticket()
        else:
            print("Sorry that input is incorrect... try again! ")
            self.my_ticket()

        # This is where we Pay for Parking
    def time_to_Pay(self):
        if self.tickets == False:
            print("There are no tickets reserved please reserve a ticket first!")
            run()
        else: 
            ticket_num = input("What is your ticket number? Or if you don't have a ticket number or this is the wrong garage input 'Quit' ")
            if ticket_num.lower() == 'quit':
                print("Sorry we couldn't help any further have a great day! ")
            elif ticket_num == str(self.tickets[0]):
                print("Thank you! Processing...")
                print(f"Since your space was resereved for {self.length_stayed} hours, a payment of ${int(self.length_stayed) * 2} dollars is required.")
                self.payment = input("Please input the payment amount...   ")
                if int(self.payment) == int(self.length_stayed) * 2:
                    print("Thank you for your payment")
                    update1 = {"Current Ticket" : "1 Paid"}
                    self.currentTicket.update(update1)
                    self.leaving()
                else:
                    print("Sorry that is not the right payment amount try again... ")
                    self.time_to_Pay()
            elif ticket_num != str(self.tickets[0]):
                print("This is not an assigned ticket please try again or try another Parking Garage.")
                self.time_to_Pay()
        
        # This is us leaving the garage
    def leaving(self):
        if int(self.payment) == int(self.length_stayed) * 2:
            print("You have 15 min to leave the space you parked in, please come visit us again!")
        elif print("We need to recieve payment before you leave... "):
            print(self.payment)

            
test = gar_Park(3)


def run():
    test.hello_cust()
    n = 1
    while n == 1: 
        select_option = input("How can we help? Are you to: Pay, Reserve, or Quit: ")
        if select_option.lower() == 'reserve':
            test.my_ticket()
        elif select_option.lower() == 'pay':
            test.time_to_Pay()
        elif select_option.lower() == 'quit':
            print("...Ok have a great rest of your day!")
            n = 2 
        else:
            print("Sorry we do not understand that input please try again.")

run()