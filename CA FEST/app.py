from flask import Flask, request, jsonify, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_files():
    group_file = request.files['groupFile']
    hostel_file = request.files['hostelFile']
    
    # Read CSV files
    group_df = pd.read_csv(group_file)
    hostel_df = pd.read_csv(hostel_file)
    
    # Perform room allocation
    allocation = allocate_rooms(group_df, hostel_df)
    
    # Convert allocation to CSV
    output = io.StringIO()
    allocation.to_csv(output, index=False)
    output.seek(0)
    
    return send_file(output, mimetype='text/csv', attachment_filename='room_allocation.csv', as_attachment=True)

def allocate_rooms(group_df, hostel_df):
    # Initialize result dataframe
    allocation = []

    # Sort hostels by capacity (larger rooms first)
    hostel_df = hostel_df.sort_values(by='Capacity', ascending=False)
    
    # Group by gender
    boys_hostels = hostel_df[hostel_df['Gender'] == 'Boys']
    girls_hostels = hostel_df[hostel_df['Gender'] == 'Girls']
    
    # Sort groups by size (larger groups first)
    group_df = group_df.sort_values(by='Members', ascending=False)

    # Allocate rooms
    for index, group in group_df.iterrows():
        group_id = group['Group ID']
        members = group['Members']
        gender = group['Gender']
        
        # Find suitable hostel rooms
        if gender == 'Boys':
            suitable_hostels = boys_hostels
        else:
            suitable_hostels = girls_hostels
        
        allocated = False
        for i, hostel in suitable_hostels.iterrows():
            if hostel['Capacity'] >= members:
                allocation.append([group_id, hostel['Hostel Name'], hostel['Room Number'], members])
                suitable_hostels.at[i, 'Capacity'] -= members
                allocated = True
                break

        if not allocated:
            # Handle case where no single room can fit the group
            pass
    
    allocation_df = pd.DataFrame(allocation, columns=['Group ID', 'Hostel Name', 'Room Number', 'Members Allocated'])
    return allocation_df

if __name__ == '__main__':
    app.run(debug=True)
