import csv

# with open('log_file.csv') as File:
#     reader = csv.reader(File, delimiter=',', quotechar=',',
#                         quoting=csv.QUOTE_MINIMAL)


def write_values(title, url, date, status):

    row = [title, url, date, status]
    with open('/Users/baker/Code/Python/gmail_instapaper/log_file.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)

    csvFile.close()
