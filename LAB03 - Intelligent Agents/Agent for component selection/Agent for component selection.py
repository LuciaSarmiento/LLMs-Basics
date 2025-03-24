from flask import Flask, render_template, request
import ollama
import ast
import pandas as pd

app = Flask(__name__)

# Load data from the Excel file
excel_file = "Components.xlsx"
df_components = pd.read_excel(excel_file, sheet_name="Components")
df_prices = pd.read_excel(excel_file, sheet_name="Prices")

# List available components in the database
available_components = df_components["Component"].str.lower().tolist()

# Extract and filter valid components from the text
def extract_valid_components(text):
    messages = [{'role': 'user', 'content':
        f"From the following text, identify the mentioned components and "
        f"organize them into two categories: 'Mechanical' and 'Electronic'. "
        f"Only consider the following valid components: {available_components}. "
        f"Return the result as a Python dictionary with this structure without adding any other words or phrases: "
        f"{{'Mechanical': [], 'Electronic': []}}.\n\nText: {text}\n\nDictionary:",
    }]
    
    response = ollama.chat(model='llama3.1:latest', messages=messages)
    dictionary = ast.literal_eval(response['message']['content'])
    # Filter only components that exist in the database
    filtered_dictionary = {
        category: [comp for comp in list if comp.lower() in available_components]
        for category, list in dictionary.items()
    }
    
    return filtered_dictionary

# Select recommended models and get prices
def select_models(component_dictionary):
    selection = {}
    for category, component_list in component_dictionary.items():
        selection[category] = []
        for component in component_list:
            rows = df_components[df_components["Component"].str.lower() == component.lower()]
            if not rows.empty:
                # Take the first match
                row = rows.iloc[0]
                available_models = [row[f"Model {i}"] for i in range(1, 4) if pd.notna(row[f"Model {i}"])]
                if available_models:
                    # Choose the first available model
                    best_model = available_models[0]
                    price = df_prices.loc[df_prices["Model"] == best_model, "Price (USD)"].values
                    if price:
                        selection[category].append({"Component": component,"Model": best_model,"Price (USD)": price[0]})
    
    return selection

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_text = request.form["description"]
        # Extract and select components
        dictionary = extract_valid_components(user_text)
        selection = select_models(dictionary)
        
        return render_template("result.html", selection=selection, description=user_text)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)