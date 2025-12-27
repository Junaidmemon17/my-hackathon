class PersonalDiary:
    def __init__(self):
        self.is_authenticated = False

    def login(self):
        user = input("Enter your username: ")
        pwd = input("Enter your password: ")

        with open("login.txt", "r") as f:
            creds = f.read().split()

        if len(creds) >= 2 and user == creds[0] and pwd == creds[1]:
            self.is_authenticated = True
            print("Login successful! Welcome back.")
        else:
            print("Login failed! Check username or password.")

    def encrypt_text(self, message):
        encrypted = ""
        for char in message:
            encrypted += chr(ord(char) + 1)  # simple shift cipher
        return encrypted

    def decrypt_text(self, message):
        decrypted = ""
        for char in message:
            decrypted += chr(ord(char) - 1)
        return decrypted

    def add_entry(self):
        entry = input("Write your diary entry: ")
        encrypted_entry = self.encrypt_text(entry)

        with open("diary.txt", "a") as f:
            f.write(encrypted_entry + "\n")

        print("Your entry has been saved securely.")

    def view_entries(self):
        try:
            with open("diary.txt", "r") as f:
                for line in f:
                    print(self.decrypt_text(line.strip()))
        except FileNotFoundError:
            print("No diary entries found.")


# -------- Main Program --------
if __name__ == "__main__":
    diary_app = PersonalDiary()
    diary_app.login()

    if diary_app.is_authenticated:
        diary_app.add_entry()
        print("\nYour Diary Entries:")
        diary_app.view_entries()
