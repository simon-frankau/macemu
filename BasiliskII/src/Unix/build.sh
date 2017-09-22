make clean
NO_CONFIGURE=1 ./autogen.sh
./configure --enable-addressing=banks --with-gtk=no --with-esd=no
make -j 32
