import os
import pandas as pd

def create_file_if_not_exists(filename):if not os.path.exists(filename):open(filename,'w').close()
def write_to_file(filename,data):f=open(filename,'w');f.write(data);f.close()
def append_to_file(filename,data_to_add):f=open(filename,'a');f.write(data_to_add);f.close()
def read_file(filename):with open(filename,'r')as file:return file.read()
def count_lines_in_file(filename):with open(filename,'r' )as f:return len(f.readlines())
def get_longest_line(filename):with open(filename,'r')as file:return max(file,key=len)
def add_column_to_csv(filename,columnName,columnValues):df=pd.read_csv(filename);df[columnName]=columnValues;df.to_csv(filename,index=False )
def get_avg_age(filename):df=pd.read_csv(filename);return df['Age'].mean()
def get_profession_count(filename):df=pd.read_csv(filename);return df['Profession'].value_counts()

if __name__=='__main__':
    filename="testfile.csv";create_file_if_not_exists( filename);write_to_file(filename,"Name,Age\nAlice,25\nBob,30\n" )
    append_to_file(filename,"Charlie,35\nDaisy,40\nEve,28\nFrank,31\n")
    print("Content of file:\n" + read_file(filename))
    totalLines = count_lines_in_file(filename)
    print(f'Total lines: {totalLines}')
    longestLine = get_longest_line(filename).strip()
    print('Longest line:',longestLine)
    professions = ['Engineer'  ,'Doctor','Lawyer','Chef'   ,'Artist','Engineer'    ]
    add_column_to_csv(filename,"Profession",professions)
    print(read_file(filename))
    averageAge = get_avg_age(  filename)
    print(f'Average Age: {averageAge}')
    professionCount = get_profession_count(filename )
    print("Profession counts:\n",professionCount )
    append_to_file(filename,f'\nGinny,29,Doctor'  )
    updated_df = pd.read_csv(filename)
    updated_df = updated_df[updated_df['Age'] > 30]
    print('People older than 30:\n', updated_df)
    group_by_profession = updated_df.groupby('Profession').mean()
    print("Average age per profession for people older than 30:\n",group_by_profession['Age'])
