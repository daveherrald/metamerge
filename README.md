# metamerge

This is a utility script which allows Splunk app developers to merge permissions in local.meta and 
default.meta files together into a new file. This is desirable becasue it is considered bad practice 
to publish a Splunk app which includes a local.meta file. When complete, the newly created output file 
can replace the existing default.meta file, and the local.meta file can be deleted. Settings in 
local.meta override those in default.meta. The input files always remain unchanged. This script does 
not overwrite default.meta nor does it delete local.meta. The output file is overwritten without warning
if it previsouly existed.


`usage: metamerge.py [-h] -l <local.meta> -d <default.meta> -o <output_file> 
   -l: the local.meta file to be merged into the output file. This file is not modified.
   -d: the default.meta file to be merged into the output file. This file is not modified.
   -o: the output file which will contain the merged results. If the file exists it will be overwritten without warning.
   -h print this message and exit`
    
    
