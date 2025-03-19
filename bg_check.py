def adjust_insulin_infusion():
    # Prompt user for inputs
    current_bg = float(input("Enter current BG (mg/dL): "))
    previous_bg = float(input("Enter previous BG (mg/dL): "))
    current_infusion_rate = float(input("Enter current infusion rate (units/hour): "))
    print()
    print(f"Current BG: {current_bg} mg/dL")
    print(f"Previous BG: {previous_bg} mg/dL")
    print(f"Current Infusion Rate: {current_infusion_rate} units/hour")
    print()

    # Define Tables A and B
    table_A = {(0.1, 2): 0.3, (2.1, 4): 0.5, (4.1, 7): 1, (7.1, 10): 2, (10, float('inf')): 3}
    table_B = {(0.1, 2): 0.5, (2.1, 4): 1, (4.1, 7): 2, (7.1, 10): 3, (10, float('inf')): 4}

    def lookup_table(infusion_rate, table):
        for key, value in table.items():
            if key[0] <= infusion_rate <= key[1]:
                return value
        return 0

    # Calculate the change in BG
    bg_change = current_bg - previous_bg
    print(f"Change in BG: {bg_change} mg/dL")

    # Initialize new_infusion variable
    new_infusion = current_infusion_rate

    # Determine infusion adjustment based on the table conditions
    if 70 <= current_bg <= 79:
        print("BG is between 70 and 79 mg/dL. Holding infusion for 1 hour.")
        return "Hold infusion for 1 hour. Recheck BG in 1 hour."

    elif 80 <= current_bg <= 139:
        print("BG is between 80 and 139 mg/dL.")
        if bg_change < -40:
            print("BG change is less than -40 mg/dL. Holding infusion for 30 minutes.")
            return "Hold infusion for 30 minutes. Recheck BG in 30 minutes."
        elif -40 <= bg_change <= -21:
            print("BG change is between -40 and -21 mg/dL. Decreasing infusion rate by (B).")
            new_infusion -= lookup_table(current_infusion_rate, table_B)
        elif -20 <= bg_change <= 0:
            print("BG change is between -20 and 0 mg/dL. Decreasing infusion rate by (A).")
            new_infusion -= lookup_table(current_infusion_rate, table_A)
        elif 0 < bg_change:
            print("BG is increasing. No change in infusion rate.")
            return "No change in infusion rate."

    elif 140 <= current_bg <= 180:
        print("BG is between 140 and 180 mg/dL.")
        if bg_change < -40:
            print("BG change is less than -40 mg/dL. Holding infusion for 30 minutes.")
            return "Hold infusion for 30 minutes. Recheck BG in 30 minutes."
        elif -40 <= bg_change <= -21:
            print("BG change is between -40 and -21 mg/dL. Decreasing infusion rate by (A).")
            new_infusion -= lookup_table(current_infusion_rate, table_A)
        elif -20 <= bg_change <= 20:
            print("BG change is between -20 and 20 mg/dL. No change in infusion rate.")
            return "No change in infusion rate."
        elif 20 < bg_change:
            print("BG change is greater than 20 mg/dL. Increasing infusion rate by (A).")
            new_infusion += lookup_table(current_infusion_rate, table_A)

    elif 181 <= current_bg <= 220:
        print("BG is between 181 and 220 mg/dL.")
        if bg_change < -80:
            print("BG change is less than -80 mg/dL. Holding infusion for 30 minutes.")
            return "Hold infusion for 30 minutes. Recheck BG in 30 minutes."
        elif -80 <= bg_change < -40:
            print("BG change is between -80 and -40 mg/dL. Decreasing infusion rate by (A).")
            new_infusion -= lookup_table(current_infusion_rate, table_A)
        elif -40 <= bg_change <= -21:
            print("BG change is between -40 and -21 mg/dL. No change in infusion rate.")
            return "No change in infusion rate"
        elif -20 <= bg_change <= 0:
            print("BG change is between -20 and 0 mg/dL. Increasing infusion rate by (A).")
            new_infusion += lookup_table(current_infusion_rate, table_A)
        elif 1 <= bg_change <= 40:
            print("BG change is between 1 and 40 mg/dL. Increasing infusion rate by (A).")
            new_infusion += lookup_table(current_infusion_rate, table_A)
        elif 40 < bg_change:
            print("BG change is greater than 40 mg/dL. Increasing infusion rate by (B).")
            new_infusion += lookup_table(current_infusion_rate, table_B)

    elif 221 <= current_bg <= 250:
        print("BG is between 221 and 250 mg/dL.")
        if bg_change > 0:
            print("BG change is greater than 0 mg/dL. Bolusing by (A) and increasing infusion rate by (B).")
            new_infusion += lookup_table(current_infusion_rate, table_B)
            return f"Bolus by (A). New infusion rate: {new_infusion}"
        elif -20 <= bg_change <= 0:
            print("BG change is between -20 and 0 mg/dL. Increasing infusion rate by (A).")
            new_infusion += lookup_table(current_infusion_rate, table_A)
        elif -80 <= bg_change <= -21:
            print("BG change is between -80 and -21 mg/dL. No change in infusion rate.")
            return f"No change in infusion rate. New infusion rate: {new_infusion}"
        elif -120 <= bg_change <= -81:
            print("BG change is between -120 and -81 mg/dL. Decreasing infusion rate by (B).")
            new_infusion -= lookup_table(current_infusion_rate, table_B)
        elif bg_change < -120:
            print("BG change is less than -120 mg/dL. Holding infusion for 30 minutes.")
            return "Hold infusion for 30 minutes. Recheck BG in 30 minutes."

    elif current_bg > 250:
        print("BG is greater than 250 mg/dL.")
        if bg_change > 0:
            print("BG change is greater than 0 mg/dL. Bolusing by (B) and increasing infusion rate by (B).")
            new_infusion += lookup_table(current_infusion_rate, table_B)
            return f"Bolus by (B). New infusion rate: {new_infusion}"
        if -20 <= bg_change <= 0:
            print("BG change is between -20 and 0 mg/dL. Increasing infusion rate by (B).")
            new_infusion += lookup_table(current_infusion_rate, table_B)
        elif -80 <= bg_change <= -21:
            print("BG change is between -80 and -21 mg/dL. No change in infusion rate.")
            return f"No change in infusion rate. New infusion rate: {new_infusion}"
        elif -120 <= bg_change <= -81:
            print("BG change is between -120 and -81 mg/dL. Decreasing infusion rate by (A).")
            new_infusion -= lookup_table(current_infusion_rate, table_A)
        elif bg_change < -120:
            print("BG change is less than -120 mg/dL. Holding infusion for 30 minutes.")
            return "Hold infusion for 30 minutes. Recheck BG in 30 minutes."

    print()
    print()
    return f"Adjusted infusion rate: {new_infusion} units/hour"

# Testing the function (You can call this function to interactively test)
print(adjust_insulin_infusion())
