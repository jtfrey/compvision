ls -l /mnt/data27/wisser/drmaize/image_data/e${1}/microimages/reconstructed/HS/ 2> err.log | grep -e "e${1}${2}w[A-D][1-6]x[0-9]\{2\}_[0-9]\{10\}rf[0-9]\{3\}.ome.tif" | tr -s ' ' | cut -d ' ' -f3,9,5 | sort -k 2 > file2
ls -l /mnt/data27/wisser/drmaize/image_data/e${1}/microimages/reconstructed/HS/ 2> err.log | grep -e "e${1}${2}w[A-D][1-6]x[0-9]\{2\}_[0-9]\{10\}rl[0-9]\{3\}.ome.tif" | tr -s ' ' | cut -d ' ' -f5 | sort > file1
join -1 1 -2 2 file1 file2 | sort -k 3

