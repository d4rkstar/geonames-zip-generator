import zipfile
import os

def ensure_dir(file_path):
	if not os.path.exists(file_path):
		os.makedirs(file_path)

def writeAndZipFile(country, data):
	baseFname = country + '.txt'
	fname = 'countries/' + baseFname
	# remove if exists
	if os.path.exists(fname):
		os.remove(fname)

	f = open(fname, 'w')
	f.write(data)
	f.close()

	with zipfile.ZipFile('countries/' + country + '.zip', 'w') as zip:
		zip.write(fname, baseFname)
	# cleanup
	if os.path.exists(fname):
		os.remove(fname)

def main():
	fname = 'allCountries'
	txtFile = fname + '.txt'
	zipFile = fname + '.zip'
	print 'Creating directory countries'
	ensure_dir('countries')
	print 'Extracting file ' + zipFile
	with zipfile.ZipFile(zipFile, 'r') as zip_ref:
		zip_ref.extractall(".")
		print 'Reading ' + txtFile
		
		with open(txtFile) as f:
		    lines = [line.rstrip() for line in f]

		    countries = {}
		    for line in lines:
		    	data = line.split('\t')	    	
		    	if not data[0] in countries:
		    		countries[data[0]] = []

		    	countries[data[0]].append(line)


		    for country in countries:    	
		    	data = '\n'.join(countries[country])
		    	print 'Writing country ' + country
		    	writeAndZipFile(country, data)

		print 'Cleanup ' + txtFile
		if os.path.exists(txtFile):
			os.remove(txtFile)    	

if __name__ == '__main__':
	main()