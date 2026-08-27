'''QNO 1:Student Result Processing System(3 Marks)

You are working as a Python developer for a training institute. The institute maintains student marks in a file named students.txt.

Your task is to develop a Student Result Processing System that reads student records from the file,
validates the data, calculates the result, and generates separate files for valid results and errors.

Input File: students.txt

The file contains student records in the following format:

Student_ID,Student_Name,Subject,Marks

The actual file contains:

101,Ajay,Python,85
102,Rahul,Python,78
103,Priya,Python,92
104,Amit,Python,abc
105,Neha,Python,88
106,Rohit,Python
107,Simran,Python,95
108,Karan,Python,105
109,Anita,Python,35
110,Vikas,Python,65

NOTE:
Some records intentionally contain invalid data:

104,Amit,Python,abc → Marks are not numeric.
106,Rohit,Python → Marks are missing.
108,Karan,Python,105 → Marks are outside the valid range of 0–100.

Your program must not terminate when it encounters an invalid record.

It should skip the invalid record, store the error in an error file, and continue processing the remaining records.

Requirements
1. Read the Input File

Read student records from students.txt using Python file handling.

Process the file line by line.

2. Validate Student Records

For every record, validate:

Student ID must be present.
Student Name must be present.
Subject must be present.
Marks must be present.
Marks must be numeric.
Marks must be between 0 and 100.
3. Calculate Result

Based on marks, assign the following result:

Marks Result
90–100 Excellent
75–89 Very Good
60–74 Good
40–59 Pass
0–39 Fail
4. Generate result.txt

For every valid student record, write:

Student ID - Name - Subject - Marks - Result

Expected output:

101 - Ajay - Python - 85 - Very Good
102 - Rahul - Python - 78 - Very Good
103 - Priya - Python - 92 - Excellent
105 - Neha - Python - 88 - Very Good
107 - Simran - Python - 95 - Excellent
109 - Anita - Python - 35 - Fail
110 - Vikas - Python - 65 - Good

5. Generate error_log.txt

For every invalid record, write the original record along with the reason for the error.

Expected output:

Error: 104,Amit,Python,abc -> Marks must be numeric
Error: 106,Rohit,Python -> Marks are missing
Error: 108,Karan,Python,105 -> Marks must be between 0 and 100

6. Error Handling

Your program should handle different types of invalid situations appropriately.

Important: If one student's record is invalid, the program must continue processing the remaining records instead of terminating.

For example:

104 → Invalid → Continue
105 → Valid → Process
106 → Invalid → Continue
107 → Valid → Process
7. Additional Requirement

If the input file is not available, display an appropriate error message instead of terminating the program.

Expected Final Output

After successful execution, display:

Student result processing completed successfully.

Valid records have been written to result.txt
Invalid records have been written to error_log.txt

The following files should be generated:

project/
│
├── student_result.py
├── students.txt
├── result.txt
└── error_log.txt
'''


try: 
    file = open("students.txt","r")

    for line in file:
        data = line.strip().split(",")
        print(data)

        if len(data) != 4:
            print("Marks are missing")
            continue

        try:
            marks = int(data[3])
        except ValueError:
            print("Marks must be numeric")
            continue

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100")
            continue

    file.close() 

except FileNotFoundError:
    print("students.txt file not found")
