import csv
import pprint

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
			county = row[1]
			cases = int(row[2])

			# find the correct years data set
			if year in data_sets.keys():

				data_set = data_sets[year]

				if county in data_set.keys():
					# update count of cases
					data_set[county] = data_set[county] + cases
				else:
					# add new county to the data set
					data_set.update( {county : cases} )

	pprint.pprint(data_2006)


if __name__ == "__main__":
	main()