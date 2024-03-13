from currency_converter import CurrencyConverter
 
def main():
    print("This is a currency converter")
    print("You can use these currency ('INR','USD','EUR','GBP','CAD','CNY','RUB','AUD')")

    amount=float(input("Enter the amount you want convert:"))

    curr_currency=input("Enter the currency which you have:")
    want_currency=input("Enter the currency you want to have:")

    c=CurrencyConverter()

    converted_amount=c.convert(amount,curr_currency,want_currency)

    print(f"The {amount} {curr_currency} in {want_currency} is :{converted_amount}")


main()