for (( i = 0; $i <= 2; i = $i + 1 )); do

	if [[ $i -le 1 ]]; then

		if [[ $i == 0 ]]; then
			file=mystery_img1.txt
			var="5db9862819edb16f9ac0f3b1c406e79d"

		elif [[ $i == 1 ]]; then
			file=mystery_img2.txt
			var="b091a841da98ca516635f4dfea1dbaf5"
		fi

		checksum_file=$(md5sum $file | awk '{print $1;}')
		echo "checksum: ${checksum_file}"
		echo "checksum original: ${var}"

		if [[ "$checksum_file" == "$var" ]]; then
			img_str=$(cat $file)
			file=Archivo$i
			echo "$img_str" | base64 -d > ${file}.jpg
			echo "imagen decodificada"
		else
			echo "Error"
		fi

	fi

	if [[ $i == 2 ]]; then
		file=hola_mundo.c
		var=543762badfd317820ff70624fe8a9a11

		checksum_file=$(md5sum -b $file | awk '{print $1}')
		echo "checksum: ${checksum_file}"
		echo "checksum original: ${var}"

		if [[ "$checksum_file" == "$var" ]]; then
			echo hola_mundo.c | base64 $file > "hola_mundo_encriptado"
			echo "Archivo codificado"
		else
			echo "Error"
		fi
	fi
	echo
done

mkdir "Archivos Nuevos"
mv hola_mundo_encriptado "Archivos Nuevos"
mv Archivo0.jpg "Archivos Nuevos"
mv Archivo1.jpg "Archivos Nuevos"
