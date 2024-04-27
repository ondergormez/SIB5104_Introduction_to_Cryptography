

class Digest:
    """Digest class"""

    @staticmethod
    def calculate_digest(message):
        text = ""
        ascii_code = ""
        for char in message:
            text += char + "   "
            ascii_code += str(ord(char)) + "  "

        print(f"Text: \t\t {text}")
        print(f"ASCII code: \t {ascii_code}")
        print()

        digest = 0
        for char in message:
            old_digest = digest
            digest ^= ord(char)
            print(f"{old_digest} xor {ord(char)} = {digest}")

        print()
        print(f"Digest of the '{message}' is: {digest}")
        return digest
