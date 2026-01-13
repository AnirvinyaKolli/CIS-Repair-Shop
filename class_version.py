
import os

class RepairReceipt:
    def __init__(self, repair_request, part_costs, computer_model, repairer):
        self.repair_request = repair_request
        self.part_costs = part_costs
        self.computer_model = computer_model
        self.repairer = repairer

    def __str__(self):
       return f'Repair requirements:\n{self.repair_request}\nPart costs:\n${self.part_costs:.2f}\nComputer model:\n{self.computer_model}\nRepairer:\n{self.repairer}\n'

def get_receipt():
    repair_request = input('What needs repair: ')
    part_costs = float(input("Enter cost: $"))
    computer_model = input('Enter the model of computer: ')
    repairer = input("Enter repairer name: ")
    return RepairReceipt(repair_request, part_costs, computer_model, repairer)

def main():
    os.system('cls')
    receipt = get_receipt()
    os.system('cls')
    print(receipt)
if __name__ == "__main__": 
    main()
