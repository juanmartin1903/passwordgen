# Importerar nödvändiga bibliotek

import tkinter as tk
import secrets
import string

# Funktion för att generera ett enkelt lösenord

def generate_simple_password():
    characters = string.ascii_letters + string.digits
    size = 12
    return ''.join(secrets.choice(characters) for _ in range(size))

# Funktion för att generera lösenord och visa det i output-boxen

def generate_and_display():
    password = generate_simple_password()
    output_box.delete(0, tk.END)
    output_box.insert(0, password)

# Huvudfunktionen som skapar GUI:t

def main():
    global output_box

    window = tk.Tk()
    window.title("Lösenord Generator")
    window.geometry("400x200")

    title = tk.Label(window, text="Lösenord Generator", font=("Arial", 16))
    title.pack(pady=10)

    btn_generate = tk.Button(window, text="Generera Lösenord", command=generate_and_display)
    btn_generate.pack(pady=5)

    output_box = tk.Entry(window, font=("Arial", 14), justify="center")
    output_box.pack(pady=10, fill="x", padx=20)

    btn_exit = tk.Button(window, text="Avsluta", command=window.destroy)
    btn_exit.pack(pady=5)

    window.mainloop()

# Kör huvudfunktionen när skriptet körs

if __name__ == "__main__":
    main()