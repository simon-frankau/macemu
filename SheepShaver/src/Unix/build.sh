make clean
NO_CONFIGURE=1 ./autogen.sh
./configure --enable-sdl-video --enable-sdl-audio --disable-vosf --disable-jit-compiler --with-x --with-gtk
make -j 32
