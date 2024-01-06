def my_func():
    import csv
    from collections import Counter

    with open("Crimes.csv", "r", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)

        primary_type_col_idx = header.index("Primary Type")
        date_col_idx = header.index("Date")

        count_crimes_by_type = Counter(
            row[primary_type_col_idx]
            for row in reader
            if row[date_col_idx][6:10] == "2015"
        )

        print(max(count_crimes_by_type, key=count_crimes_by_type.get))

    #     for row in reader:
    #         try:
    #             dt = row[date_col_idx]
    #             if dt[6:10] == "2015":
    #                 crime_type = row[primary_type_col_idx]
    #                 crime_types_count[crime_type] = crime_types_count.get(crime_type, 0) + 1
    #         except ValueError:
    #             continue
    # return max(crime_types_count, key=crime_types_count.get)


import timeit

execution_time = timeit.timeit(my_func, number=10)
print(f"Execution time: {execution_time} seconds")
