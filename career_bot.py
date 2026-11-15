import pandas as pd
import re
import time

def calculate_tnea(maths, physics, chemistry):
    """Calculates the official Anna University TNEA Cutoff out of 200."""
    return maths + (physics / 2.0) + (chemistry / 2.0)

def predict_seat_chance(user_cutoff, college_cutoff):
    """Determines seat probability based on the difference from previous year cutoffs."""
    diff = user_cutoff - college_cutoff
    if diff >= 2.0:
        return "🟢 High Chance"
    elif -1.5 <= diff < 2.0:
        return "🟡 Moderate (Borderline)"
    else:
        return "🔴 Low Chance (Reach)"

def run_career_counselor():
    csv_file = "anna_university_colleges_2026.csv"
    
    # 1. Load the expanded 134-row dataset
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: '{csv_file}' not found! Place it in the exact same folder as this script.")
        return

    print("=" * 115)
    print("               FUTUREPATH: COMPREHENSIVE CAREER & SEAT PREDICTOR CHATBOT")
    print("=" * 115)

    # 2. Gather Student Information
    name = input("Bot: Hello! I am your Career Counselor. What is your name?\nYou: ").strip()
    print(f"\nBot: Welcome, {name}! Let's explore all engineering, creative, nature, and specialized paths.")
    
    try:
        print("\nBot: Please enter your 12th Standard marks (out of 100):")
        m = float(input("  -> Maths: "))
        p = float(input("  -> Physics: "))
        c = float(input("  -> Chemistry: "))
        
        if not (0 <= m <= 100 and 0 <= p <= 100 and 0 <= c <= 100):
            print("\nBot: Marks must be between 0 and 100. Please restart and try again.")
            return

    except ValueError:
        print("\nBot: Invalid input! Please enter numeric values for your marks.")
        return

    # 3. Calculate Cutoff
    user_cutoff = calculate_tnea(m, p, c)
    print(f"\nBot: Your calculated Anna University (TNEA) Cutoff is: {user_cutoff:.2f} / 200")

    # 4. Interactive Hobby Search Loop
    while True:
        print("\nBot: Enter your hobbies or interests (you can separate multiple with commas, or type 'quit' to exit):")
        print("     Examples: aero, cyber, gaming, animals, cooking, sports, fashion, psychology, law, stocks, photography")
        user_input = input("You: ").lower().strip()

        if user_input in ["quit", "exit", "bye"]:
            print(f"\nBot: Best of luck with your future, {name}! Follow your passion.")
            break

        # Split multiple hobbies and build a regex pattern (e.g., "gaming|cyber")
        keywords = [re.escape(k.strip()) for k in user_input.split(",") if k.strip()]
        if not keywords:
            print("Bot: Please type at least one hobby keyword.")
            continue

        pattern = "|".join(keywords)
        print(f"\nBot: Searching 134 programs across Tamil Nadu for '{user_input}'...")
        time.sleep(0.8)

        # 5. Filter Dataset
        matches = df[df['hobby_tag'].str.contains(pattern, case=False, na=False, regex=True)].copy()

        if matches.empty:
            print(f"\nBot: No exact tag matched '{user_input}'. Showing top recommended programs for your cutoff instead:\n")
            matches = df[df['cutoff_2024'] <= user_cutoff + 3.0].copy()
            if matches.empty:
                matches = df.copy()
        else:
            print(f"\nBot: Found {len(matches)} matching college & course options!\n")

        # 6. Apply Seat Prediction Logic & Sort by Best College (Highest Cutoff)
        matches['Seat_Chance'] = matches['cutoff_2024'].apply(lambda x: predict_seat_chance(user_cutoff, x))
        ranked_results = matches.sort_values(by='cutoff_2024', ascending=False)

        # 7. Display Formatted Results Table
        print("-" * 125)
        print(f"{'College / Institution Name':<44} | {'Course / Branch':<34} | {'City':<13} | {'Cutoff':<6} | {'Seat Chance'}")
        print("-" * 125)
        
        for _, row in ranked_results.head(15).iterrows():
            col_name = (row['college_name'][:41] + '...') if len(row['college_name']) > 44 else row['college_name']
            br_name = (row['branch_name'][:31] + '...') if len(row['branch_name']) > 34 else row['branch_name']
            print(f"{col_name:<44} | {br_name:<34} | {row['city']:<13} | {row['cutoff_2024']:<6.1f} | {row['Seat_Chance']}")
            
        print("-" * 125)

if __name__ == "__main__":
    run_career_counselor()