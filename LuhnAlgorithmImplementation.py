def verify_card_number(card_number):
    # Initialize sum of odd and even digits
    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    # Reverse the card number for easier iteration
    card_number_reversed = card_number[::-1]

    # Extract odd digits and calculate their sum
    odd_digits = card_number_reversed[::2]
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Extract even digits, double them, and calculate their sum
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        # If the doubled digit is greater than or equal to 10, adjust it
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    # Calculate total sum
    total = sum_of_odd_digits + sum_of_even_digits
    
    # Check if the total sum is divisible by 10
    return total % 10 == 0

def main():
    #Define the card number and remove any hyphens or spaces
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    #Verify the card number and print the result
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

#Call the main function to execute the program
main()
