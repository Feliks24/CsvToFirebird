
from priceCalc import extract_table

#function in put is in order of
#dim, x, y, last_x, last_y, name, variant
#optional variables are file and table

table_data = [["2", 1, 1, 16, 16, "Item_name_1", "1"],
              ["2", 17, 17, 30, 30, "Item_name_2", "2"]]


#print(table_data)

#starting id
object_id = 1

for dim, x, y, last_x, last_y, name, variant in table_data:
    object_id = extract_table(object_id,dim,x,y,last_x,last_y,name,variant,table="MY_TABLE", file="my_file.csv")
