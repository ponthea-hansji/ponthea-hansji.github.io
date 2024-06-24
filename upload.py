import cgi
import pandas as pd

# Parse form data
form = cgi.FieldStorage()

# Get uploaded file
file = form['csvfile']

# Check if the file was uploaded
if file.filename:
    # Save the file
    filename = './uploads/' + file.filename
    with open(filename, 'wb') as f:
        f.write(file.file.read())

    # Process the CSV file (example processing)
    df = pd.read_csv(filename)
    # Example processing: Sum of 'Requested Rooms '
    grouped_df = df.groupby('Date')['Requested Rooms '].sum()

    # Save processed data to a new CSV file
    processed_filename = './processed_data.csv'
    grouped_df.to_csv(processed_filename, header=True)

    # Print success message
    print("Content-Type: text/html")
    print()
    print("<html><body>")
    print("<h2>File uploaded and processed successfully!</h2>")
    print(f"<p>Processed data saved as <a href='{processed_filename}' download>processed_data.csv</a></p>")
    print("</body></html>")
else:
    print("Content-Type: text/html")
    print()
    print("<html><body>")
    print("<h2>Error: No file uploaded.</h2>")
    print("</body></html>")
