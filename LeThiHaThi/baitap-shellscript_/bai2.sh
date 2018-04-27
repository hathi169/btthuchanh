#!/bin/bash
read -p "Nhap ho: " ho
read -p "Nhap ten: " ten
a="Le"
b="Thi"
if [ $ho = $a ] && [ $ten = $b ]
then 
	echo "trung khop"
else
	echo "khong trung khop"
fi
