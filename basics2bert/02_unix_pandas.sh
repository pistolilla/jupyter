# manual
man head

# 10. Output N lines from the beginning
head -3 "group_pinfo.csv"

# 11. Number of records
tail -n +2 group_binfo.csv | count
tail -n +2 group_binfo.csv | wc -l

# 12: Combine two files (inner join) by using ID (first column) as a key
# -t: delimiter (default: space)
# -j: column (default: 1st)
join -t, -j 1 "group_pinfo.csv" "group_binfo.csv"

# 13: Convert commas to spaces.
cat group_binfo.csv | sed 's/,/ /g'

# 14: Column Extraction. Save the "group_pbinfo.csv" with only the name column extracted from each line as col1.txt
# -d: delimiter
# -f: column
cat group_pinfo.csv | cut -d , -f 2

# 15: Insert the following record between the lines of ID=1 and ID=2 in "group_pbinfo.csv":
# 6, Toshi, 54, Male, Vocal, Cooking
brew install gnu-sed
cat group_pinfo.csv | gsed '2 a 6,Toshi,54,Male,Vocal,Cooking'

# 16: Split the file in two.
SIZE=$(cat group_pinfo.csv | wc -l)
cat group_pinfo.csv | split -l $(($SIZE / 2))

# 17: Find the type of string (set of different strings) in the "role" column
tail -n +2 group_binfo.csv | cut -d , -f 2 | uniq
# 19. Find the frequency of occurrence of elements in a particular column and arrange them in order of frequency of occurrence
tail -n +2 group_binfo.csv | cut -d , -f 2 | uniq -c | sort -r

# 18. Output the result of sorting only the record rows except the header row of "group_pinfo.csv" into the descending order of numbers in the [age] column
# Please display all rows of the output.
tail -n +2 group_pinfo.csv | sort -t , -k3 -r


