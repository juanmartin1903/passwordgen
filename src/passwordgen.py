# Bibliotek som används för att skapa det grafiska gränssnittet, generera säkra lösenord och hantera strängar

import tkinter as tk # Bibliotek för att skapa grafiska användargränssnitt
import secrets # Bibliotek för att generera säkra slumpmässiga tal, används här för att skapa lösenord
import string # Bibliotek som innehåller olika strängkonstanter, används här för att få tillgång till bokstäver och siffror

# Funktion för att generera ett enkelt lösenord baserat på den valda längden från skalan

def generate_simple_password():
    characters = ""

    # Konsonanter (alla bokstäver utom vokaler)

    consonants = ''.join([c for c in string.ascii_letters if c.lower() not in "aeiouåäö"])
    vowels = "aeiouåäöAEIOUÅÄÖ"
    digits = string.digits
    symbols = string.punctuation

    if checkbutton_var.get() == 1:      # Inkludera konsonanter
        characters += consonants
    if checkbutton_var2.get() == 1:     # Inkludera vokaler
        characters += vowels
    if checkbutton_var3.get() == 1:     # Inkludera siffror
        characters += digits
    if checkbutton_var4.get() == 1:     # Inkludera specialtecken
        characters += symbols

    if characters == "":
        return "Välj minst ett alternativ"

    length = scale_1.get()
    return ''.join(secrets.choice(characters) for _ in range(length))

# Funktion för att generera och visa det genererade lösenordet i output_box

def generate_and_display():
    password = generate_simple_password() # Anropar funktionen generate_simple_password för att skapa ett nytt lösenord
    output_box.delete(0, tk.END)
    output_box.insert(0, password)

def copy_to_clipboard():
    password = output_box.get()
    if password.strip() != "":
        window.clipboard_clear()
        window.clipboard_append(password)

# Huvudfunktionen som skapar det grafiska gränssnittet och hanterar användarinteraktionen

def main():
    global output_box, scale_1, window, copy_icon
    global checkbutton_var, checkbutton_var2, checkbutton_var3, checkbutton_var4    

# Skapar huvudfönstret för applikationen, sätter titel och storlek, och lägger till olika widgets (etiketter, skala, knappar och inmatningsfält) för att skapa användargränssnittet

    window = tk.Tk()
    window.title("Lösenord Generator")
    window.geometry("400x400")

    title = tk.Label(window, text="Lösenord Generator", font=("Arial", 16))
    title.pack(pady=10)

    checkbutton_var = tk.IntVar() 
    chk1 = tk.Checkbutton(window, text="Inkludera Konsonanter", variable=checkbutton_var)
    checkbutton_var.set(1)
    chk1.pack(pady=5)
    checkbutton_var2 = tk.IntVar() 
    chk2 = tk.Checkbutton(window, text="Inkludera Vokaler", variable=checkbutton_var2)
    checkbutton_var2.set(1)
    chk2.pack(pady=5)
    checkbutton_var3 = tk.IntVar()
    chk3 = tk.Checkbutton(window, text="Inkludera Siffror", variable=checkbutton_var3)
    checkbutton_var3.set(1)
    chk3.pack(pady=5)
    checkbutton_var4 = tk.IntVar()
    chk4 = tk.Checkbutton(window, text="Inkludera specialtecken", variable=checkbutton_var4)
    checkbutton_var4.set(0)
    chk4.pack(pady=5)

    scale_label = tk.Label(window, text="Välj Lösenordslängd:", font=("Arial", 12))
    scale_label.pack(pady=5)

    scale_1 = tk.Scale(window, from_=8, to=20, orient=tk.HORIZONTAL)
    scale_1.pack(pady=5)

    btn_generate = tk.Button(window, text="Generera Lösenord", command=generate_and_display)
    btn_generate.pack(pady=5)

    # Frame para colocar entry + botón en la misma fila
    output_frame = tk.Frame(window)
    output_frame.pack(pady=10, padx=20, fill="x")   

    copy_icon = tk.PhotoImage(file="copy.png")

    output_box = tk.Entry(output_frame, font=("Arial", 14), justify="center")
    output_box.pack(side="left", fill="x", expand=True)

    btn_copy = tk.Button(output_frame, image=copy_icon, command=copy_to_clipboard)
    btn_copy.image = copy_icon  # evita que Tkinter la borre
    btn_copy.pack(side="left", padx=5)

    btn_exit = tk.Button(window, text="Avsluta", command=window.destroy)
    btn_exit.pack(pady=5)

    window.mainloop()

# Startar programmet genom att anropa main-funktionen när skriptet körs direkt

if __name__ == "__main__":
    main()