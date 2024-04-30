import sys

def encode_message(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            # Convert to uppercase
            char = char.upper()
            # Apply shift
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encoded_message += shifted_char
    
    return encoded_message

def main(shift):
    for line in sys.stdin:
        # Convert the message to all uppercase
        message = line.strip().upper()
        # Encode the message
        encoded_message = encode_message(message, shift)
        
        # Print the encoded message in blocks of five letters
        block_count = 0
        for i in range(0, len(encoded_message), 5):
            if block_count == 10:
                print()
                block_count = 0
            print(encoded_message[i:i+5], end=" ")
            block_count += 1
        print()


if __name__ == "__main__":
    shift_amount = int(sys.argv[1])
    main(shift_amount)
