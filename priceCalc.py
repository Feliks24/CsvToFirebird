import pandas as pd

########################
##########INPUT#########
#where does it start
x = 1
y = 1
#where does it end
last_x = 1
last_y = 1
#dimension 0,x,y,2
dim = "0"

file ="NewProdPriceCalc.csv"
table ="tablename"


#current component name
name = "SURCHARGE_1"
variant = "A"

########################

#definition of row names of table
dim0 = "(id,name, variant, calc_value)"
dimx = "(id,name, x, variant, calc_value)"
dimy = "(id,name, y, variant, calc_value)"
dim2 = "(id,name, x, y, variant, calc_value)"


def num_form(x):
    return str(x).replace(",",".")



def extract_table(start_id,dim,x,y,last_x,last_y,name,variant,file=file,table=table):
    object_id = start_id
    n_rows = last_y - y + 1

    #read cv with file name, separator ;, no header, and extract
    #one table based on the coordinates on the input
    #this means the table even if the starting coordinates are not 0,
    #the new table will start with 0,0 since every entry outside the
    #scope is disregarded
    df = pd.read_csv(
            file, 
            sep=';', 
            header=None,
            skiprows=y,
            usecols=list(range(x,last_x+1)),
            nrows=n_rows)

    #print(df)

    if(dim == "0"):
        #this is a single entry, just add it into the string
        print(f"INSERT INTO {table}"+dim0+f" VALUES({object_id},\'{name}\', \'{variant}\', {num_form(df.iloc[0,0])});")
        object_id=object_id+1
    if(dim == "x"):
        #there is only a x-axis with a header, make into 1 array and cycle through it once
        for x_val,value in zip(df.loc[0], df.loc[1]):
            print(f"INSERT INTO {table}" + dimx + f" VALUES({object_id},\'{name}\', {x_val}, \'{variant}\', {num_form(value)});") 
            object_id=object_id+1
    if(dim == "y"):
        #same as prevoius except that we transpose it first since it's easier to opperate on rows
        df = df.T
        for x_val,value in zip(df.iloc[0], df.iloc[1]):
            print(f"INSERT INTO {table}" + dimy + f" VALUES({object_id},\'{name}\', {x_val}, \'{variant}\', {num_form(value)});") 
            object_id=object_id+1
    if(dim == "2"):
        #similar to 2 previous ones except we add another loop for the y-dimension
        #for one entires row we add another array that has repeatedly the y value of this row
        for y_index in range(1,n_rows):
            for x_val,y_val,value in zip(df.iloc[0][1:], [df.iloc[y_index,0]]*(last_x-x), df.iloc[y_index][1:]):
                print(f"INSERT INTO {table}" + dim2 + f" VALUES({object_id},\'{name}\', {x_val}, {y_val}, \'{variant}\', {num_form(value)});")
                object_id=object_id+1
    return object_id


if __name__ == "__main__":
    extract_table(0,dim, x, y, last_x, last_y, name, variant)
