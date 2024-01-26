import streamlit as st

def parse_measurement(measurement):
    """ Parses a measurement string (feet and inches) and returns total inches. """
    if '"' in measurement:
        measurement = measurement.replace('"', '')

    parts = measurement.split("'")
    feet = 0
    inches = 0

    if len(parts) == 2:
        feet = float(parts[0]) if parts[0] else 0
        inches = int(parts[1]) if parts[1] else 0
    elif "'" in measurement:
        feet = float(parts[0]) if parts[0] else 0
    else:
        try:
            feet = float(measurement)
        except ValueError:
            return 0  # Return 0 if the input is not a valid number

    return int(feet * 12 + inches)

def calculate_total_measurements(input_str):
    """ Calculates the total of measurements input in the format '2+3'4"+5'6"'. """
    try:
        measurements = input_str.split('+')
        total_inches = sum(parse_measurement(m.strip()) for m in measurements)
        feet = total_inches // 12
        inches = total_inches % 12
        return f"{feet}'{inches}\""
    except Exception as e:
        return "Error in calculation"

# Streamlit UI components
st.title('Kitchen Cabinet Calculator')

#image_path = 'CalculatorApp.png'  # Replace with your image path or URL
#st.image(image_path, caption='Kitchen Cabinet Example')

## Display an image with a specified width
image_path = 'CalculatorApp.png'  # Image path or URL
st.image(image_path, caption='Kitchen Cabinet Example', width=300)  # Set the width as needed

features = ['Upper Cabinets', 'Lower Cabinets', 'Countertop', 'Backsplash', 'Full Cabinets']
user_inputs = {feature: st.text_input(f"Enter measurements for {feature} (e.g., 2+3'4\"+5'6\"): ") for feature in features}

if st.button('Calculate'):
    st.subheader("Total Linear Feet and Inches for each feature:")
    for feature, input_str in user_inputs.items():
        total = calculate_total_measurements(input_str)
        st.text(f"{feature}: {total}")

# Optional: Any additional functionality or components you want to add

