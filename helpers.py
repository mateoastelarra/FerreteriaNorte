# Hash function to convert Letters to Numbers (Only one letter)
def letter_to_number(letter):
    if len(letter) == 1:
        return ord(letter.lower()) - 97 


# Function to search a given code in excel file
def search_item(data, column, code):
    for i in range(len(data)):
        if (data.loc[i][column] == code):
            return True
    return False


# Function to search for products availability by code from a given excel file from ferretería NORTE
def filter_products(consumer_data, stock_data, consumer_column, stock_column):
    products_availability = {"available":[], "not available": []}

    for i in range(len(consumer_data)):
        if (search_item(stock_data, stock_column, consumer_data.loc[i][consumer_column])):
            products_availability["available"].append(consumer_data.loc[i][consumer_column])
        else:
            products_availability["not available"].append(consumer_data.loc[i][consumer_column])
    return products_availability

# Function to search a given code in CSV file
def search_item_csv(data, column, code):
    for i in range(len(data)):
        if (data.iloc[i, column] == code):
            return True
    return False


# Function to search for products availability by code from a given excel CSV from ferretería NORTE
def filter_products_csv(consumer_data, stock_data, consumer_column, stock_column):
    products_availability = {"available":[], "not available": []}

    for i in range(len(consumer_data)):
        if (search_item(stock_data, stock_column, consumer_data.iloc[i, consumer_column])):
            products_availability["available"].append(consumer_data.iloc[i, consumer_column])
        else:
            products_availability["not available"].append(consumer_data.iloc[i, consumer_column])
    return products_availability