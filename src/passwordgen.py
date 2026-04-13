# main.py
import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("400x200")

    label = tk.Label(window, text="Password Generator", font=("Arial", 16))
    label.pack(pady=20)

    btn_generate = tk.Button(window, text="Generate Password")
    btn_generate.pack(pady=5)

    btn_exit = tk.Button(window, text="Exit", command=window.destroy)
    btn_exit.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    main()