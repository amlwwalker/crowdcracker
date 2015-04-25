
cat testnewpasswords | while IFS=" " read encrypted password
do
	# echo $encrypted $password
    echo "encrypted='$encrypted' password='$password'"
    UUID=$(uuidgen)
    echo "saving to: $UUID"
    cat cred | grep $encrypted > $UUID.pass
done
