import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}
    with open (filename,"rt") as file:
        line_reader = csv.reader(file)
        next(line_reader)
        for line in line_reader: 
            key = line[key_column_index]
            dictionary[key] = line
    return dictionary

def main ():
    print ("All products")
    products_dict = read_dictionary("products.csv",0)
    
    print (products_dict) 

    print ("Requested Items")
    with open ("request.csv","rt") as file:
        line_reader = csv.reader(file)
        next(line_reader)
        for line in line_reader: 
            name = products_dict[line[0]][1]

            quantity = line[1]
            price = products_dict[line[0]][2]

            print (f"{name}: {quantity} @ {price}")


    

if __name__ == "__main__":
    main()