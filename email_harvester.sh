#!/bin/bash
cd ~
python3 search_result_links.py
cut -f 2 -d '<' searchresultlinks.txt | cut -f 3 -d '/' >> websiteurl.txt
sed 's/www.//g' websiteurl.txt >> website_domain.txt
declare -i FILENAME=0
while read -r LINE; do
	cd /opt/theHarvester 
       sudo python ./theHarvester.py -d "$LINE" -l 20 -b google -f $FILENAME.xml  #you can include other search options for harvester
       ((FILENAME++))
done < ~/website_domain.txt
cd ~
sudo cat /opt/theHarvester  *.xml >> all.xml
xmlstarlet sel -t -v '//email' -n /opt/theHarvester/*.xml > emails.txt
