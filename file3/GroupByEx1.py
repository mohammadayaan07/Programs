#GroupByEx1.py
import pandas as pd
# List of Tuples
empoyees = [
			(11, 'Jack',    44, 'Sydney',19) ,
            (12, 'Riti',    41, 'Delhi' ,   17) ,
            (13, 'Aadi',    46, 'Mumbai',   11) ,
            (14, 'Mohit',   45, 'Delhi' ,   15) ,
            (15, 'Veena',   43, 'Delhi' ,   14) ,
            (16, 'Shaunak', 42, 'Mumbai',   17 ),
            (17, 'Manik',   42, 'Sydney',   14 ),
            (18, 'Vikas',   42, 'Delhi',   11 ),
            (19, 'Samir',   42, 'Mumbai',   15 ),
            (20, 'Shobhit', 40, 'Sydney',   12) ]
# Create a DataFrame object
df = pd.DataFrame(empoyees,columns=['ID', 'Name', 'Age', 'City', 'Experience'])
df = df.set_index('ID')
# Display the DataFrame
print("-"*40)
print(df)
print("-"*40)