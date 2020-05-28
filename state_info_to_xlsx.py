import json 
import xlsxwriter

# Opening JSON file 
f = open('state_info.json',) 

data = json.load(f) 

# Create an new Excel file and add a worksheet.
with xlsxwriter.Workbook('demo.xlsx') as workbook:

    # Add worksheet
    worksheet = workbook.add_worksheet()

    # Write headers
    worksheet.write(0, 0, 'State')
    worksheet.write(0, 1, 'Name')
    worksheet.write(0, 2, 'Designation')
    worksheet.write(0, 3, 'Functional Area')
    worksheet.write(0, 4, 'Email')
    worksheet.write(0, 5, 'Mobile')
    worksheet.write(0, 6, 'Date of Joining')
    worksheet.write(0, 7, 'Present Status')

    # Write dict data
    start = 1
    for i, (state, state_dict) in enumerate(data.items(), start=1):
        if state == "TELANGANA":
            continue
        else:
            for j, (no, person_dict) in enumerate(state_dict.items(), start=start):
                worksheet.write(j,0,state)
                worksheet.write(j,1,person_dict["Name"])
                worksheet.write(j,2,person_dict["Designation"])
                worksheet.write(j,3,person_dict["Functional Area"])
                worksheet.write(j,4,person_dict["Email"])
                worksheet.write(j,5,person_dict["Mobile"])
                worksheet.write(j,6,person_dict["Date of Joining"])
                worksheet.write(j,7,person_dict["Present Status"])
            start = start + int(no)

