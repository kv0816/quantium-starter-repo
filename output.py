import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./formatted_data.csv"

# Open the output file
with open(OUTPUT_FILE_PATH, "w", newline="") as output_file:
    writer = csv.writer(output_file)

    # Add CSV header
    header = ["sales", "date", "region"]
    writer.writerow(header)

    # Check if data directory exists
    if not os.path.exists(DATA_DIRECTORY):
        print(f"Error: Data directory {DATA_DIRECTORY} not found!")
    else:
        # Iterate through all files in the data directory
        for file_name in os.listdir(DATA_DIRECTORY):
            file_path = os.path.join(DATA_DIRECTORY, file_name)

            print(f"Processing file: {file_name}")  # Debugging step

            # Open the CSV file for reading
            with open(file_path, "r") as input_file:
                reader = csv.reader(input_file)

                # Iterate through each row in the CSV file
                row_index = 0
                for input_row in reader:
                    # Skip header row
                    if row_index > 0:
                        # Collect data from row
                        product = input_row[0]
                        raw_price = input_row[1]
                        quantity = input_row[2]
                        transaction_date = input_row[3]
                        region = input_row[4]

                        # Check if it's a "pink morsel"
                        if product == "pink morsel":
                            # Process price correctly (remove $ sign)
                            try:
                                price = float(raw_price.replace("$", ""))
                                sale = price * int(quantity)

                                # Write the row to output file
                                output_row = [sale, transaction_date, region]
                                writer.writerow(output_row)

                                print(f"✅ Processed row: {output_row}")  # Debugging step
                            except ValueError as e:
                                print(f"⚠️ Skipping row due to error: {input_row} - {e}")
                    row_index += 1

print(f"✅ Data processing complete. Check {OUTPUT_FILE_PATH}")







