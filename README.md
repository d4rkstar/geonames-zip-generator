# Geonames Zip Generator

Generates countries zip files from allCountries.zip

Sometimes it happens that the geonames.org zip code download service [is not available](https://github.com/OCA/partner-contact/issues/826).

By retrieving the allCountries.zip file from the network, it is possible to regenerate all the individual country zips using the attached extract.py script.

Clone the repository, replace the allCountries.zip file and run the command:

`python extract.py`

In the "countries" directory you will find the zip files.

If, like me, you use odoo and the [base_location_geonames_import](https://apps.odoo.com/apps/modules/12.0/base_location_geonames_import) module, you can use the zip obtained by placing the files on your webserver (or using the webserver integrated in python) and modifying the system parameter "geonames.url" in this way:

`https://domain/subpath /% s.zip`

where domain = your domain
subpath = any subpath

# Disclaimer
All data are from Geonames: http://www.geonames.org/
