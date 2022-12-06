. ./util/.env

DAY=${1:-$(date '+%-d')}
YEAR=${1:-$(date '+%Y')}

echo '##########################################'
echo "#      ADVENT OF CODE DAY $DAY             #"
echo '##########################################'

mkdir "$YEAR/$DAY" && touch $YEAR/$DAY/sample.txt && cp ./util/main.py $YEAR/$DAY/main.py
wget --header "Cookie: session=$AOC_SESSION_COOKIE" "https://adventofcode.com/$YEAR/day/$DAY/input" -O $YEAR/$DAY/input.txt

cd $YEAR/$DAY/