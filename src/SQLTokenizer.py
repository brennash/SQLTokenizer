import re
import os
import sys
import datetime
import collections
from optparse import OptionParser

class SQLTokenizer:

	def __init__(self):
		self.sqlString = ''

	def run(self, inputFilename):

		sqlText = self.readFile(inputFilename)
		print (sqlText)

	def readFile(self, inputFilename):
		""" readFile reads the SQL input file and 
		returns a string representing the data in the 
		file.

		Args:
		  inputFilename - The input SQL filename

		Returns:
		  A string giving the data in the file
		"""

		sqlText   = ''
		try:
			inputFile = open(inputFilename, 'r')
			for line in inputFile:
				sqlText += line.strip() + ' '
		except Exception as error:
			print(error)
		return sqlText.strip()



def main(argv):
        parser = OptionParser(usage="Usage: SQLTokenizer <SQL-fileame>")
        (options, filename) = parser.parse_args()

	if len(filename) == 1:
		if os.path.exists(filename[0]):
			tokenizer = SQLTokenizer()
			tokenizer.run(filename[0])
		else:
	                parser.print_help()
        	        print '\nYou need to provide an existing input file.'
			exit(1)
	else:
                parser.print_help()
                print '\nYou need to provide an input file.'
                exit(1)

if __name__ == "__main__":
    sys.exit(main(sys.argv))

