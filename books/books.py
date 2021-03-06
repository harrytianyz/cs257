# Kevin Chen and Harry Tian
import csv
import argparse

# function that reads the content of books.csv
def read_csv():
  dict_authors = {}  # dictionary with authors as keys and list of titles as values
  dict_years = {} # dictionary with years as keys and list of titles as values
  titles = [] # list of all book titles

  with open('books.csv', newline='') as csvfile:
      temp = csv.reader(csvfile)
      for row in temp:
          # populate dict_authors
          if not row[2] in dict_authors:
              dict_authors[row[2]] = [row[0]]
          else:
              dict_authors[row[2]].append(row[0])

          # populate dict_years
          if not row[1] in dict_years:
              dict_years[row[1]] = [row[0]]
          else:
              dict_years[row[1]].append(row[0])

          # populate titles
          if row[0] not in titles:
            titles.append(row[0])

  return titles, dict_authors, dict_years

# set up arguments for argparse
def get_parsed_arguments():
  parser = argparse.ArgumentParser(description='Searching through books.csv.')
  parser.add_argument("function", help = "enter [b] or [book] to search books by title, [a] or [author] to search books by authors, [y] or [year]")
  parser.add_argument("search_string", help = "the string you want to search for")
  parsed_arguments = parser.parse_args()
  return parsed_arguments

# search books by title
def get_book_info(search_string, function):
  output = []
  titles, dict_authors, dict_years = read_csv()
  
  # search for titles
  if function == "book" or function == "b":
    for title in titles:
      if search_string.lower() in title.lower():
        output.append(title)

  # search books by author
  elif function == "author" or function == "a":
    for author in dict_authors:
      if search_string.lower() in author.lower():
        output.append(author + ": ")
        output.append(dict_authors[author])
  
  # search books by years
  elif function == "year" or function == "y":
    temp = search_string.split('-')
    year1 = temp[0]
    year2 = temp[1]
    
    # swaps years if year1 is bigger
    tempYear = year1
    if year1 > year2:
      year1 = year2
      year2 = tempYear
    
    for year in dict_years:
      if int(year) >= int(year1) and int(year) <= int(year2):
        output.append(dict_years[year])
    output = [item for sublist in output for item in sublist]

  else:
    print("wrong function name entered, use -h to see accepted function names")
    quit()

  return output

def main():
  arguments = get_parsed_arguments() # get arguments
  output = get_book_info(arguments.search_string, arguments.function) # get output based on arguments
  if output: #print output if found
    for item in output:
      print(item)
  else:
    print("We couldn't find results that match your selection")

if __name__ == '__main__':
    main()
