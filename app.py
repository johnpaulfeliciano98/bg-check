from flask import Flask, render_template, request

app = Flask(__name__)


def adjust_insulin_infusion(current_bg, previous_bg, current_infusion_rate):
    # Define Tables A and B
    table_A = {(0.1, 2): 0.3, (2.1, 4): 0.5, (4.1, 7): 1, (7.1, 10): 2, (10, float('inf')): 3}
    table_B = {(0.1, 2): 0.5, (2.1, 4): 1, (4.1, 7): 2,
               (7.1, 10): 3, (10, float('inf')): 4}

    def lookup_table(infusion_rate, table):
        for key, value in table.items():
            if key[0] <= infusion_rate <= key[1]:
                return value
        return 0

    # Calculate the change in BG
    bg_change = current_bg - previous_bg
    new_infusion = current_infusion_rate

    # Determine infusion adjustment based on the table conditions
    if 70 <= current_bg <= 79:
        return f"Current BG is between 70 and 79 mg/dL. Hold infusion for 1 hour. Recheck BG in 1 hour and if BG is greater than 120 mg/dL, restart drip and decrease infusion by (B). Refer to table."

    elif 80 <= current_bg <= 139:
        if bg_change < -40:
            return f"Current BG is between 80 and 139 mg/dL. BG change is less than -40 mg/dL.\nHold infusion for 30 minutes. Recheck BG in 30 minutes and if BG is greater than 120 mg/dL, restart drip and decrease infusion by (B). Refer to table."
        elif -40 <= bg_change <= -21:
            new_infusion -= lookup_table(current_infusion_rate, table_B)
            return f"Current BG is between 80 and 139 mg/dL. BG change is between -40 and -21 mg/dL. Decreased infusion rate by (B). New infusion rate: <b>{new_infusion}</b>."
        elif -20 <= bg_change <= 0:
            new_infusion -= lookup_table(current_infusion_rate, table_A)
            return f"Current BG is between 80 and 139 mg/dL. BG change is between -20 and 0 mg/dL. Decreased infusion rate by (A). New infusion rate: <b>{new_infusion}</b>."
        elif 0 < bg_change:
            return f"Current BG is between 80 and 139 mg/dL. BG change is greater than 0 mg/dL. <b>No change in infusion rate</b>."

    elif 140 <= current_bg <= 180:
        if bg_change < -40:
            return f"Current BG is between 140 and 180 mg/dL. BG change is less than -40 mg/dL.\nHold infusion for 30 minutes. Recheck BG in 30 minutes and if BG is greater than 120 mg/dL, restart drip and decrease infusion by (B). Refer to table."
        elif -40 <= bg_change <= -21:
            new_infusion -= lookup_table(current_infusion_rate, table_A)
            return f"Current BG is between 140 and 180 mg/dL. BG change is between -40 and -21 mg/dL. Decreasing infusion rate by (A). New infusion rate: <b>{new_infusion}</b>."
        elif -20 <= bg_change <= 20:
            return f"Current BG is between 140 and 180 mg/dL. BG change is between -20 and 20 mg/dL. <b>No change in infusion rate</b>."
        elif 20 < bg_change:
            new_infusion += lookup_table(current_infusion_rate, table_A)
            return f"Current BG is between 140 and 180 mg/dL. BG change is greater than 20 mg/dL. Increasing infusion rate by (A). New infusion rate: <b>{new_infusion}</b>."

    elif 181 <= current_bg <= 220:
        if bg_change < -80:
            return f"Current BG is between 181 and 220 mg/dL. BG change is less than -80 mg/dL. Hold infusion for 30 minutes. Recheck BG in 30 minutes and if BG is greater than 120 mg/dL, restart drip and decrease infusion by (B). Refer to table."
        elif -80 <= bg_change < -40:
            new_infusion -= lookup_table(current_infusion_rate, table_A)
            return f"Current BG is between 181 and 220 mg/dL. BG change is between -80 and -40 mg/dL. Decreasing infusion rate by (A). New infusion rate: <b>{new_infusion}</b>"
        elif -40 <= bg_change <= -21:
            return f"Current BG is between 181 and 220 mg/dL. BG change is between -40 and -21 mg/dL. <b>No change in infusion rate.</b>"
        elif -20 <= bg_change <= 0:
            new_infusion += lookup_table(current_infusion_rate, table_A)
            return f"Current BG is between 181 and 220 mg/dL. BG change is between -20 and 0 mg/dL. Increasing infusion rate by (A). New infusion rate: <b>{new_infusion}</b>"
        elif 1 <= bg_change <= 40:
            new_infusion += lookup_table(current_infusion_rate, table_A)
            return f"Current BG is between 181 and 220 mg/dL. BG change is between 1 and 40 mg/dL. Increasing infusion rate by (A). New infusion rate: <b>{new_infusion}</b>"
        elif 40 < bg_change:
            new_infusion += lookup_table(current_infusion_rate, table_B)
            return f"Current BG is between 181 and 220 mg/dL. BG change is greater than 40 mg/dL. Increasing infusion rate by (B). New infusion rate: <b>{new_infusion}</b>"

    elif 221 <= current_bg <= 250:
        if bg_change > 0:
            bolus = lookup_table(current_infusion_rate, table_A)
            new_infusion += lookup_table(current_infusion_rate, table_B)
            return f"Current BG is between 221 and 250 mg/dL. BG change is greater than 0 mg/dL. Bolus by (A). Increasing infusion rate by (B). Bolus: <b>{bolus}</b>. New infusion rate: <b>{new_infusion}</b>"
        elif -20 <= bg_change <= 0:
            new_infusion += lookup_table(current_infusion_rate, table_A)
            return f"Current BG is between 221 and 250 mg/dL. BG change is between -20 and 0 mg/dL. Increasing infusion rate by (A). New infusion rate: <b>{new_infusion}</b>"
        elif -80 <= bg_change <= -21:
            return f"Current BG is between 221 and 250 mg/dL. BG change is between -80 and -21 mg/dL. <b>No change in infusion rate.</b>"
        elif -120 <= bg_change <= -81:
            new_infusion -= lookup_table(current_infusion_rate, table_B)
            return f"Current BG is between 221 and 250 mg/dL. BG change is between -120 and -81 mg/dL. Decreasing infusion rate by (B). New infusion rate: <b>{new_infusion}</b>"
        elif bg_change < -120:
            return f"Current BG is between 221 and 250 mg/dL. BG change is less than -120 mg/dL. Hold infusion for 30 minutes. Recheck BG in 30 minutes and if BG is greater than 120 mg/dL, restart drip and decrease infusion by (B). Refer to table."

    elif current_bg > 250:
        if bg_change > 0:
            bolus = lookup_table(current_infusion_rate, table_B)
            new_infusion += lookup_table(current_infusion_rate, table_B)
            return f"Current BG is greater than 250 mg/dL. BG change is greater than 0 mg/dL. Bolus by (B). Increasing infusion rate by (B). Bolus: <b>{bolus}</b>. New infusion rate: <b>{new_infusion}</b>"
        elif -20 <= bg_change <= 0:
            new_infusion += lookup_table(current_infusion_rate, table_B)
            return f"Current BG is greater than 250 mg/dL. BG change is between -20 and 0 mg/dL. Increasing infusion rate by (B). New infusion rate: <b>{new_infusion}</b>"
        elif -80 <= bg_change <= -21:
            return f"Current BG is greater than 250 mg/dL. BG change is between -80 and -21 mg/dL. <b>No change in infusion rate.</b>"
        elif -120 <= bg_change <= -81:
            new_infusion -= lookup_table(current_infusion_rate, table_A)
            return f"Current BG is greater than 250 mg/dL. BG change is between -120 and -81 mg/dL. Decreasing infusion rate by (A). New infusion rate: <b>{new_infusion}</b>"
        elif bg_change < -120:
            return f"Current BG is greater than 250 mg/dL. BG change is less than -120 mg/dL. Hold infusion for 30 minutes. Recheck BG in 30 minutes and if BG is greater than 120 mg/dL, restart drip and decrease infusion by (B). Refer to table."

    # Return the final adjusted infusion rate
    return f"Adjusted infusion rate: <b>{new_infusion}</b>"


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Get the form data
        current_bg = float(request.form['current_bg'])
        previous_bg = float(request.form['previous_bg'])
        current_infusion_rate = float(request.form['current_infusion_rate'])

        # Calculate the BG change
        bg_change = current_bg - previous_bg

        # Call the function with the form data
        result = adjust_insulin_infusion(
            current_bg, previous_bg, current_infusion_rate)

        # Include the input values and BG change in the result with line breaks
        result = (f"Input values:\n"
                  f"Current BG = {current_bg} mg/dL\n"
                  f"Previous BG = {previous_bg} mg/dL\n"
                  f"BG Change = {bg_change} mg/dL\n"
                  f"Current Infusion Rate = {current_infusion_rate} units/hour\n\n"
                  f"{result}")

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
