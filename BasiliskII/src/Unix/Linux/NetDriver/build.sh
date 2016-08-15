if [ -z "$1" ]
then
   echo "Passed in user account for changing /dev/sheep_net owner (non root)"
   exit 0
fi
make clean
make
sudo make install
sudo rmmod sheep_net
sudo modprobe sheep_net
sudo chown $1 /dev/sheep_net
