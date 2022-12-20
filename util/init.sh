# USAGE:
# $ . ./util/init.sh
# (Use a source to allow last cd, otherwise the CD in only for the child process)
. ./util/.env

DAY=${1:-$(date '+%-d')}
YEAR=${2:-$(date '+%Y')}

echo '##########################################'
echo "#      ADVENT OF CODE DAY $DAY             #"
echo '##########################################'

mkdir "$YEAR/$DAY" && touch $YEAR/$DAY/sample.txt && cp ./util/main.py $YEAR/$DAY/main.py
wget --quiet --header "Cookie: session=$AOC_SESSION_COOKIE" "https://adventofcode.com/$YEAR/day/$DAY/input" -O $YEAR/$DAY/input.txt

cd $YEAR/$DAY