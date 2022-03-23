import wget
import ssl
import os
from sh import gunzip

# Ignore ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Define the local filename to save data
local_file = 'title.basics.tsv.gz'
os.system("rm -rf " + local_file)
os.system("rm -rf title.basics.tsv")

# Define the remote file to retrieve
remote_url = 'https://datasets.imdbws.com/title.basics.tsv.gz'
# Make http request for remote file data
print("Downloading dataset '" + local_file + "' from " + remote_url)
wget.download(remote_url)

# Extract Archive
print("\nExtracting Archive.")
gunzip(local_file)
