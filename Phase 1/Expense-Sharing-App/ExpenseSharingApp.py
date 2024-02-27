from colorama import Fore

class TextColor:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class ExpenseManager:
    def __init__(self) -> None:
        self.members = []

    def get_members(self) -> None:
        num = int(input(Fore.LIGHTMAGENTA_EX + "Enter number of members: " + Fore.RESET))
        for i in range(1, num + 1):
            self.members.append(input(f"Enter member - {i} Name: ").capitalize())

    @staticmethod
    def show_expenses(lst, amount) -> None:
        max_name_length = max(len(name) for name in lst)
        max_amount_length = len("Amount to be Paid")

        print(Fore.LIGHTYELLOW_EX + TextColor.UNDERLINE + "\nExpenses Split Bill" + TextColor.END + Fore.RESET)
        
        print(f"\n\t {'Name':<{max_name_length}} \t\t {'Amount to be Paid':<{max_name_length}}")
        print("\t" + "-" * (max_name_length + max_amount_length + 20))
        for member in lst:
            print(f"\t {member:<{max_name_length}} \t\t ₹ {amount:<{max_name_length}}")

    def split_expenses(self, total_amount) -> None:
        if total_amount <= 0:
            exit(Fore.RED + "Exited with code 0: Amount Can't be Negative" + Fore.RESET)

        amount_per_person = total_amount / len(self.members)
        amount_per_person = round(amount_per_person, 2)

        self.show_expenses(self.members, amount_per_person)

    @staticmethod
    def show_paid_and_unpaid(paid_list, members) -> None:
        max_name_length = max(len(name) for name in members)
        max_status_length = len("Paid/Unpaid")

        print(Fore.LIGHTYELLOW_EX + TextColor.UNDERLINE + "\nList of Paid and Unpaid Members" + TextColor.END + Fore.RESET)

        print(f"\n\t {'Name':<{max_name_length}} \t\t {'Paid/Unpaid':{max_name_length}}")
        print("\t" + "-" * (max_name_length + max_status_length + 20))

        for name in members:
            status = "Paid" if name in paid_list else "Unpaid"
            print(f"\t {name:<{max_name_length}} \t\t {status:<{max_name_length}}")

    def track_payments(self) -> None:
        paid_list = []

        while True:
            paid_name = input(Fore.LIGHTMAGENTA_EX + "\nPress 0 to Exit or Enter your name if you paid: " + Fore.RESET).capitalize()

            if paid_name == '0':
                break

            if paid_name not in self.members:
                print(Fore.RED + "Invalid User Name!!!" + Fore.RESET)
            else:
                paid_list.append(paid_name)

            if sorted(self.members) == sorted(paid_list):
                break

        self.show_paid_and_unpaid(paid_list, self.members)


if __name__ == "__main__":
    print(Fore.BLUE + TextColor.BOLD + TextColor.UNDERLINE + "\n\t\t\t\t\t Expense Tracker App\n" + TextColor.END + Fore.RESET)

    app = ExpenseManager()

    # Adding Members
    app.get_members()

    # Adding and Splitting Expenses among Members
    total_amount = float(input(Fore.LIGHTMAGENTA_EX + "\nEnter Total Expenses Amount: " + Fore.RESET))
    app.split_expenses(total_amount)

    # Tracking Paid & Unpaid Members
    app.track_payments()

