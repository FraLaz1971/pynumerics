#!/usr/bin/env bash

clean(){
    rm -f selection.txt F.txt C.txt f2c_out.txt c2f_out.txt
}

convert(){
    declare -i val
    eval val=$1
    case "$val" in 
    1)
        echo "executing C2F" >/dev/stderr
        kdialog --title "C2F" --inputbox "Input temperature in Celsius deg." > C.txt
        cat C.txt | python3 c2f.py > c2f_out.txt
        kdialog --textbox c2f_out.txt
    ;;
    2)
        echo "executing F2C" >/dev/stderr
        kdialog --title "F2C" --inputbox "Input temperature in Fahrenheit deg." > F.txt
        cat F.txt | python3 f2c.py > f2c_out.txt
        kdialog --textbox f2c_out.txt
    ;;
    3)
        echo "Quitting.Bye."
        clean
        exit 0
    ;;
    *)
         echo "unknown selection">/dev/stderr
     ;;
    esac
}


    if !  test -f splash.txt
    then
        echo "tconv.py: python3 program" > splash.txt
        echo "to convert temperature" >> splash.txt
        echo "from celsius to fahrenheit" >> splash.txt
        echo "degrees and viceversa" >> splash.txt
    fi
    kdialog --textbox splash.txt
while :
do
    kdialog --checklist "Select your choice:" \
    1 "Celsius to fahrenheit" off \
    2 "Fahrenheit to Celsius" off \
    3 "Close the app" off  > selection.txt
    convert $(cat selection.txt )
done
