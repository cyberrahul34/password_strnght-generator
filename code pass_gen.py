import string
import secrets
import tkinter as tk


# ==========================================
# 1. PASSWORD STRENGTH CHECKER
# ==========================================

def check_strength(password):

    length = len(password)

    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([
        length >= 8,
        has_lower,
        has_upper,
        has_digit,
        has_symbol
    ])

    if length < 8 or score <= 2:
        strength = "WEAK"

    elif score == 3:
        strength = "MEDIUM"

    else:
        strength = "STRONG"

    return strength, score


# ==========================================
# 2. SECURE PASSWORD GENERATOR
# ==========================================

def generate_password(length=12):

    if length < 8 or length > 256:
        raise ValueError(
            "Password length must be between 8 and 256."
        )

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from every category
    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    all_chars = lowercase + uppercase + digits + symbols

    # Fill the remaining positions
    for _ in range(length - 4):
        password_chars.append(secrets.choice(all_chars))

    # Shuffle the characters
    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)


# ==========================================
# 3. COPY PASSWORD TO CLIPBOARD
# ==========================================

def copy_password(password):

    root = tk.Tk()
    root.withdraw()

    try:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()

    finally:
        root.destroy()


# ==========================================
# 4. DISPLAY PASSWORD STRENGTH
# ==========================================

def display_strength(password):

    strength, score = check_strength(password)

    print("\n========== PASSWORD RESULT ==========")
    print("Password Strength :", strength)
    print("Complexity Score  :", str(score) + "/5")

    if strength == "WEAK":
        print("Security Level    : LOW")
        print("Suggestion        : Use a longer, unique password.")

    elif strength == "MEDIUM":
        print("Security Level    : MODERATE")
        print("Suggestion        : Improve length and character variety.")

    else:
        print("Security Level    : HIGH")
        print("Message           : Passes basic complexity checks.")

    print("=====================================")

    return strength


# ==========================================
# 5. MAIN PROGRAM
# ==========================================

def main():

    while True:

        print("\n" + "=" * 45)
        print("   PASSWORD STRENGTH CHECKER & GENERATOR")
        print("=" * 45)

        print("1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Exit")

        print("=" * 45)

        choice = input("Enter your choice (1-3): ").strip()

        # OPTION 1: CHECK PASSWORD

        if choice == "1":

            password = input("Enter password: ")

            display_strength(password)

        # OPTION 2: GENERATE PASSWORD

        elif choice == "2":

            while True:

                user_input = input(
                    "Enter password length (8-256, default 12): "
                ).strip()

                try:

                    length = int(user_input) if user_input else 12

                    if length < 8 or length > 256:
                        print(
                            "Invalid length! Enter a number "
                            "between 8 and 256."
                        )
                        continue

                    break

                except ValueError:

                    print("Invalid input! Please enter a number.")

            password = generate_password(length)

            print("\n========== GENERATED PASSWORD ==========")
            print("Generated Password:", password)

            display_strength(password)

            # COPY OPTION

            copy_choice = input(
                "\nCopy password to clipboard? (y/n): "
            ).strip().lower()

            if copy_choice == "y":

                try:
                    copy_password(password)
                    print("Password copied successfully!")

                except tk.TclError:
                    print("Clipboard unavailable on this system.")

            elif copy_choice == "n":
                print("Password was not copied.")

            else:
                print("Invalid copy choice. Password was not copied.")

        # OPTION 3: EXIT

        elif choice == "3":

            print("\nThank you for using our security tool!")
            print("Stay safe online!")
            break

        else:

            print("\nInvalid choice! Please select 1, 2, or 3.")


# ==========================================
# 6. RUN THE PROGRAM
# ==========================================

if __name__ == "__main__":
    main()