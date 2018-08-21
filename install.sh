#!/bin/sh
if [ ! -f "/opt/wordgen/wordgen.py" ]; then
sudo mkdir /opt/wordgen
cp wordgen.py /opt/wordgen
/bin/cat <<EOM > /usr/bin/wordgen
#!/bin/sh
python /opt/wordgen/wordgen.py
EOM
sudo chmod 777 /usr/bin/wordgen
sudo chmod 777 /opt/wordgen/wordgen.py
echo installation compeleted
echo you can run the programm with typing wordgen
else
echo The programm have been already installed
fi
