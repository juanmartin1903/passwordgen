# Bibliotek som används för att skapa det grafiska gränssnittet, generera säkra lösenord och hantera strängar

import tkinter as tk # Bibliotek för att skapa grafiska användargränssnitt
import secrets # Bibliotek för att generera säkra slumpmässiga tal, används här för att skapa lösenord
import string # Bibliotek som innehåller olika strängkonstanter, används här för att få tillgång till bokstäver och siffror

from tkinter import ttk # Importerar ttk-modulen från tkinter för att använda mer avancerade widgets, även om den inte används i det här skriptet

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
    password = generate_simple_password()
    output_box.delete(0, tk.END)
    output_box.insert(0, password)

    strength, color, score = evaluate_strength(password)

    # Actualizar texto
    strength_label.config(text=f"Styrka: {strength}", fg=color)

    # Actualizar barra (máximo 40)
    strength_bar["value"] = score
    strength_bar["maximum"] = 40

    # Cambiar color de la barra
    style = ttk.Style()
    style.theme_use("default")

    if strength == "Svagt":
        style.configure("red.Horizontal.TProgressbar", troughcolor="#ddd", background="red")
        strength_bar.config(style="red.Horizontal.TProgressbar")

    elif strength == "Medel":
        style.configure("orange.Horizontal.TProgressbar", troughcolor="#ddd", background="orange")
        strength_bar.config(style="orange.Horizontal.TProgressbar")

    else:
        style.configure("green.Horizontal.TProgressbar", troughcolor="#ddd", background="green")
        strength_bar.config(style="green.Horizontal.TProgressbar")

def copy_to_clipboard():
    password = output_box.get()
    if password.strip() != "":
        window.clipboard_clear()
        window.clipboard_append(password)

# Klass för att skapa verktygstips (tooltips) som visas när användaren hovrar över en widget, i det här fallet används den för att visa en tooltip

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        widget.bind("<Enter>", self.show_tooltip)
        widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        if self.tip_window is not None:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20

        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")

        label = tk.Label(
            tw,
            text=self.text,
            background="#ffffe0",
            relief="solid",
            borderwidth=1,
            font=("Arial", 10)
        )
        label.pack(ipadx=5, ipady=3)

    def hide_tooltip(self, event=None):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None


def evaluate_strength(password):
    score = 0

    # Longitud
    score += min(len(password), 20)

    # Variedad de caracteres
    if any(c.islower() for c in password):
        score += 5
    if any(c.isupper() for c in password):
        score += 5
    if any(c.isdigit() for c in password):
        score += 5
    if any(c in string.punctuation for c in password):
        score += 5

    # Determinar nivel
    if score < 15:
        return "Svagt", "red", score
    elif score < 30:
        return "Medel", "orange", score
    else:
        return "Starkt", "green", score

# Huvudfunktionen som skapar det grafiska gränssnittet och hanterar användarinteraktionen

def main():
    global output_box, scale_1, window, copy_icon
    global checkbutton_var, checkbutton_var2, checkbutton_var3, checkbutton_var4    

# Skapar huvudfönstret för applikationen, sätter titel och storlek, och lägger till olika widgets (etiketter, skala, knappar och inmatningsfält) för att skapa användargränssnittet

    window = tk.Tk()
    window.title("Lösenord Generator")
    window.geometry("400x500")
    window.resizable(False, False)
    window.attributes("-toolwindow", True)
    window.configure(highlightthickness=2, highlightbackground="#555")

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

    # Skapar tooltips för varje checkbox för att ge användaren mer information om vad varje alternativ innebär
    
    Tooltip(chk1, "Inkluderar konsonanter (b, c, d, f...)")
    Tooltip(chk2, "Inkluderar vokaler (a, e, i, o, u, å, ä, ö)")
    Tooltip(chk3, "Inkluderar siffror (0–9)")
    Tooltip(chk4, "Inkluderar specialtecken (!@#$% osv.)")
    
    scale_label = tk.Label(window, text="Välj Lösenordslängd:", font=("Arial", 12))
    scale_label.pack(pady=5)

    scale_1 = tk.Scale(window, from_=8, to=20, orient=tk.HORIZONTAL)
    scale_1.pack(pady=5)

    btn_generate = tk.Button(window, text="Generera Lösenord", command=generate_and_display)
    btn_generate.pack(pady=5)

    # Frame para colocar entry + botón en la misma fila
    output_frame = tk.Frame(window)
    output_frame.pack(pady=10, padx=20, fill="x")   

    global strength_label, strength_bar

    strength_label = tk.Label(window, text="Styrka: -", font=("Arial", 12))
    strength_label.pack(pady=5)

    strength_bar = ttk.Progressbar(window, length=250, mode="determinate")
    strength_bar.pack(pady=5)

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