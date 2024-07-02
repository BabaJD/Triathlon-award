# Triathlon Award Calculator

## Description

This Python script calculates the total duration of a triathlon (swim, cycle, and run) and determines the corresponding award a participant receives based on their performance.

**Key Features:**

* **Input Gathering:** Prompts the user to enter the duration (in minutes) for each leg of the triathlon (swim, cycle, run).
* **Total Calculation:** Sums up the durations to calculate the total triathlon time.
* **Award Determination:** Uses conditional logic (if-elif-else) to determine the appropriate award based on the total duration.
* **Output:** Displays the total duration and the awarded prize or a message of encouragement for future attempts.

## Purpose

This script is useful for triathlon organizers or participants:

* **Organizers:** Quickly and accurately determine the awards for each participant based on official rules.
* **Participants:** Calculate their potential award to gauge their performance relative to the award criteria.

## Usage

1. **Run the script:** Execute the Python script from your terminal or IDE.

2. **Input Durations:** Enter the duration for each leg of the triathlon in minutes when prompted.

3. **View Results:** The script will display the total duration and the corresponding award:

   * Total duration <= 100 minutes: Provincial colours
   * 101 minutes <= Total duration <= 105 minutes: Provincial half colours
   * 106 minutes <= Total duration <= 110 minutes: Provincial scroll
   * Total duration > 110 minutes: No award, encouragement message

## Customization (Optional)

You can tailor this script for specific events:

* **Award Criteria:** Modify the time ranges and corresponding awards to match your event's rules.
* **Additional Awards:** Introduce more award categories for different performance levels.
* **Data Storage:** Save participant data (name, times, awards) to a file or database.

## Code Overview

* **Input:** Uses `input()` to get the duration of each leg from the user.
* **Calculation:** Employs `sum()` for efficient addition of durations.
* **Conditionals:** Applies `if`, `elif`, and `else` statements to determine the correct award based on the `Total_duration`.


## Credits

* **Author:** Babajide Abraham Alamu
