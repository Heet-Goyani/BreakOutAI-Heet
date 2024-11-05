from get_options_data import get_option_chain

def calculate_margin(options_data):
    """Calculates margin based on open interest in the options chain data."""
    margin = sum(option['put_options']['market_data']['oi'] for option in options_data)
    return margin

def main():
    instrument_key = "NSE_INDEX|Nifty 50"  # Example symbol
    expiry_date = "2024-05-10"             # Example expiry date
    
    # Fetch options data
    options_data = get_option_chain(instrument_key, expiry_date)
    if options_data:
        margin = calculate_margin(options_data)
        print(f"Calculated Margin: {margin}")
    else:
        print("No options data available.")

if __name__ == "__main__":
    main()
