
import os
def get_receipt():
    repair_request = input('What needs repair: ')
    part_costs = float(input("Enter cost: $"))
    computer_model = input('Enter the model of computer: ')
    repairer = input("Enter repairer name: ")
    return repair_request, part_costs, computer_model, repairer

def return_reciept(repair_request, part_costs, computer_model, /, *, repairer='Neel'):
    return f'Repair requirements:\n{repair_request}\nPart costs:\n${part_costs:.2f}\nComputer model:\n{computer_model}\nRepairer:\n{repairer}\n'

def main():
    os.system('cls')
    repair_request, part_costs, computer_model, repairer = get_receipt()
    r = return_reciept(repair_request, part_costs, computer_model, repairer)
    os.system('cls')
    print(r)
if __name__ == "__main__": 
    main()


