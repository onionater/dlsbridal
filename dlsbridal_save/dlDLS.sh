mysql -uaskerry -ppassword -e "select * from DLSPHOTO" aesbehave | sed 's/\t/","/g;s/^/"/;s/$/"/' > dlsphotos.csv
mysql -uaskerry -ppassword -e "select * from DLSMSG" aesbehave | sed 's/\t/","/g;s/^/"/;s/$/"/' > dlsmsgs.csv
mysql -uaskerry -ppassword -e "select * from DLSRSVP" aesbehave | sed 's/\t/","/g;s/^/"/;s/$/"/' > dlsrsvps.csv
mysql -uaskerry -ppassword -e "select * from DLSRECIPE" aesbehave | sed 's/\t/","/g;s/^/"/;s/$/"/' > dlsrecipes.csv


