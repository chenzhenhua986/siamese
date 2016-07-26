echo -n > list1
echo -n > list2
for i in /l/vision/v5/chen478/siamese/chip-images/*;do
  for j in /l/vision/v5/chen478/siamese/chip-images/*;do
    label=0
    if [ $(echo $i| cut -d'/' -f 8|cut -d'.' -f 1) -le 10 ]; then
	label=1
    else
	label=0
    fi
    echo $i $label >> list1
    if [ $(echo $j| cut -d'/' -f 8|cut -d'.' -f 1) -le 10 ]; then
        label=1
    else
        label=0
    fi
    echo $j $label  >> list2
#      echo $i $(echo $i| cut -d'/' -f 8|cut -d'.' -f 1) >> list1.txt
#      echo $j $(echo $j| cut -d'/' -f 8|cut -d'.' -f 1) >> list2.txt
  done
done

# split data set into traing set and testing set
split -l 195 list1
mv xaa tr1
mv xab test1
split -l 195 list2
mv xaa tr2
mv xab test2

# shuflle training set
cat tr1 | shuf >> train1
cat tr2 | shuf >> train2

rm -f list1
rm -f list2
rm -f tr1
rm -f tr2

