# CsvToFirebird
extract tables from csv file and print as PSQL statement

Input assumes a csv file with at least one table. Define coorindates of top left corner and bottom right as x,y, last_x, last_y.

The program allows to read tables in either 0, x, y and 2 dimensions; x and y dimensions means a 1 dimensional table in either x or y direction.

Define a name for the inserted item as well as a variant(this is case specific and can be edited out).

Define how an entry should look for a given dimension; as default there is id, name, variant and value(called calc_value because of "value" being a common keyword).

x and y are defined based on the dimension, for instance a table with only a x dimensions will not have y values.

The function allows to give the entries id's based on a starting id; this can be manually used but in example.py there is an example how you could run 
multiple table from one file with a continuous id without manually having to define it for every table.
