import math

def get_dimension(prompt):
    """Get the dimension from the user, defaulting to 0 if they press enter."""
    try:
        value = input(prompt).strip()
        return float(value) if value else 0.0
    except ValueError:
        print("Invalid input. Please enter a number or press Enter to default to 0.")
        return get_dimension(prompt)

def main():
    # Constants
    FERTILIZER_COVERAGE = 2000  # square feet per bag
    FERTILIZER_COST = 27.00    # dollars per bag
    TECHNICIAN_COVERAGE = 2500  # square feet per hour
    TECHNICIAN_RATE = 20.00    # dollars per hour
    NITROGEN_PER_BAG = 1.0     # pounds
    POTASSIUM_PER_BAG = 0.125  # pounds

    # Get dimensions for each lawn section
    print("Enter the dimensions of each lawn section (in feet). Press Enter to default to 0 for missing sections.")
    front_length = get_dimension("Front length: ")
    front_width = get_dimension("Front width: ")
    rear_length = get_dimension("Rear length: ")
    rear_width = get_dimension("Rear width: ")
    left_length = get_dimension("Left side length: ")
    left_width = get_dimension("Left side width: ")
    right_length = get_dimension("Right side length: ")
    right_width = get_dimension("Right side width: ")

    # Calculate areas
    front_area = front_length * front_width
    rear_area = rear_length * rear_width
    left_area = left_length * left_width
    right_area = right_length * right_width
    total_area = front_area + rear_area + left_area + right_area

    # Calculate fertilizer requirements
    bags_needed = math.ceil(total_area / FERTILIZER_COVERAGE)
    fertilizer_cost = bags_needed * FERTILIZER_COST

    # Calculate labor requirements
    hours_needed = math.ceil(total_area / TECHNICIAN_COVERAGE)
    labor_cost = hours_needed * TECHNICIAN_RATE

    # Total cost
    total_cost = fertilizer_cost + labor_cost

    # Calculate environmental impact
    nitrogen_applied = bags_needed * NITROGEN_PER_BAG
    potassium_applied = bags_needed * POTASSIUM_PER_BAG

    # Print results
    print("\n--- Fertilizer Application Summary ---")
    print(f"Total Area: {total_area:.0f} square feet")
    print(f"Fertilizer Bags Needed: {bags_needed}")
    print(f"Cost of Fertilizer: ${fertilizer_cost:.2f}")
    print(f"Labor Hours Needed: {hours_needed}")
    print(f"Cost of Labor: ${labor_cost:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Nitrogen Applied: {nitrogen_applied:.3f} pounds")
    print(f"Potassium Applied: {potassium_applied:.3f} pounds")

# Run the program
if __name__ == "__main__":
    main()
