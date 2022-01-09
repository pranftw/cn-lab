#Script for renaming files with starting with cs228 or cs_228

for f in *
do
	if [[ "$(echo -n "$f" | cut -d "_" -f 1)" == "cs228" ]]
	then
		mv "$f" "$(echo -n "$f" | cut -d "_" -f 2-)"
	elif [[ $(echo -n "$f" | cut -d "_" -f 1-2) == "cs_228" ]]
	then
		mv "$f" "$(echo -n "$f" | cut -d "_" -f 3-)"
	fi
done
