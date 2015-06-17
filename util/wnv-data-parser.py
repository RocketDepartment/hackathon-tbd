import csv
import pprint
import json

data_2006 = {}
data_2007 = {}
data_2008 = {}
data_2009 = {}
data_2010 = {}
data_2011 = {}
data_2012 = {}
data_2013 = {}
data_2014 = {}

data_sets = {
	"2006" : data_2006,
	"2007" : data_2007,
	"2008" : data_2008,
	"2009" : data_2009,
	"2010" : data_2010,
	"2011" : data_2011,
	"2012" : data_2012,
	"2013" : data_2013,
	"2014" : data_2014
}

def main():

	filename = raw_input("Please enter the data file name: ")

	with open(filename, 'rb') as csvfile:
		reader = csv.reader(csvfile)

		for row in reader:

			# grab data from the csv
			year = row[0]
			week = int(row[1])
			county = row[2]
			cases = int(row[3])

			# find the correct years data set
			if year in data_sets.keys():

				data_set = data_sets[year]

				# find out which quarter the case happened in
				if week > 0 and week <= 13:
					quarter = " Q1"
				elif week > 13 and week <= 26:
					quarter = " Q2"
				elif week > 26 and week <= 39:
					quarter = " Q3"
				elif week > 39:
					quarter = " Q4"

				key = county + quarter


				if key in data_set.keys():
					# update count of cases
					data_set[key] = data_set[key] + cases
				else:
					# add new county to the data set
					data_set.update( {key : cases} )

	pprint.pprint(data_2006)

	for year in data_sets:

		out_file = open( year + "_data.json","w" )

		my_dict = data_sets[year]
		json.dump(my_dict,out_file, indent=4)                                    

		out_file.close()



if __name__ == "__main__":
	main()