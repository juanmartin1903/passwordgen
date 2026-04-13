# huvudfil för lösenordsgeneratorn

def show_menu():
    print("\n=== Lösenordsgenerator ===")
    print("1. Generera lösenord")
    print("2. Avsluta")

def main():
    while True:
        show_menu()
        choice = input("Välj en alternativ: ")

        if choice == "1":
            print("Lösenord genererator är inte klart ännu.")
        elif choice == "2":
            print("Hej då!")
            break
        else:
            print("Felaktigt alternativ.")

if __name__ == "__main__":
    main()