from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate future date
    future_date = datetime.now() + timedelta(days=days_to_add)
    
    # Format future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    # Print the future date
    print(f"Future date: {formatted_future_date}")

# Main function to run the script
if __name__ == "__main__":
    display_current_datetime()  # Display current date and time first
    print()  # Add an empty line for clarity
    calculate_future_date()  # Then prompt for the number of days and calculate future date

