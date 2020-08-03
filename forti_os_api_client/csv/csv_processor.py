import csv


# Import CSV file into a list
def read_csv(src_path):
    row_list = []

    with open(src_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = 0
        for row in reader:
            row_list.append(row)
            # print(row)
            rows += 1
    return row_list


# Write a CSV from a list
def write_csv(row_list, out_csv_path):
    with open(out_csv_path, mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in row_list:
            writer.writerow(row)


# Pass a list to be processed
# Pass the output file path
# Pass a list of column names to be written to
# Pass a function that will process the data and the row_list's column name that will be the input for the function
# The output of the function will be written to the column_names' rows,
# The function's output list size should be equal to the column_names list size or an error will be thrown
def write_csv_with_function(row_list, out_csv_path, col_output_names, func, col_input_names):
    with open(out_csv_path, mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        if len(col_output_names) == len(func(get_row_value(col_input_names, row_list[0]))):
            for row in row_list:
                if row_list.index(row) != 0:
                    func_output = func(get_row_value(col_input_names, row))
                    count = 0
                    for name in col_output_names:
                        row[name] = func_output[count]
                        count = count + 1
                    writer.writerow(row.values())
                else:
                    writer.writerow(row)
        else:
            print("column_names list size does not equal func_output list size")


# Return row value
def get_row_value(input_list, row):
    output_list = []
    if isinstance(input_list, list):
        for obj in input_list:
            output_list.append(row.get(obj))
        return output_list

    return row.get(input_list)
