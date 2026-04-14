# Importerar nödvändiga bibliotek

import tkinter as tk # Importerar tkinter för att skapa GUI:t
import secrets # Importerar secrets för att generera säkra lösenord
import string # Importerar string för att få tillgång till bokstäver och siffror som kan användas i lösenordet

# Funktion för att generera ett enkelt lösenord

def generate_simple_password():
    characters = string.ascii_letters + string.digits # Inkluderar både stora och små bokstäver samt siffror   
    size = 12
    return ''.join(secrets.choice(characters) for _ in range(size)) # Genererar ett lösenord med 12 tecken bestående av bokstäver och siffror

# Funktion för att generera lösenord och visa det i output-boxen

def generate_and_display():
    password = generate_simple_password() # Anropar funktionen för att generera ett lösenord
    output_box.delete(0, tk.END) # Tar bort eventuellt innehåll i output-boxen
    output_box.insert(0, password) # Visar det genererade lösenordet i output-boxen

# Huvudfunktionen som skapar GUI:t

def main():
    global output_box # Deklarerar output_box som global så att den kan användas i generate_and_display-funktionen

    window = tk.Tk() # Skapar huvudfönstret för GUI:t
    window.title("Lösenord Generator")
    window.geometry("400x200")

    title = tk.Label(window, text="Lösenord Generator", font=("Arial", 16)) # Skapar en label-widget som fungerar som titel för fönstret
    title.pack(pady=10) # Packar titel-labelen i fönstret med vertikal padding

    btn_generate = tk.Button(window, text="Generera Lösenord", command=generate_and_display) # Skapar en knapp som när den klickas på, anropar funktionen generate_and_display för att generera och visa lösenordet
    btn_generate.pack(pady=5) # Packar knappen i fönstret med lite vertikal padding

    output_box = tk.Entry(window, font=("Arial", 14), justify="center") # Skapar en entry-widget för att visa det genererade lösenordet
    output_box.pack(pady=10, fill="x", padx=20) # Packar entry-widgeten i fönstret med vertikal padding, horisontell fyllning och horisontell padding

    btn_exit = tk.Button(window, text="Avsluta", command=window.destroy) # Skapar en knapp som när den klickas på, stänger fönstret
    btn_exit.pack(pady=5)  # Packar avsluta-knappen i fönstret med lite vertikal padding

    window.mainloop()

# Kör huvudfunktionen när skriptet körs

if __name__ == "__main__":
    main()