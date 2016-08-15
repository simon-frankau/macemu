make clean
NO_CONFIGURE=1 ./autogen.sh
CFLAGS=-O0;CPPFLAGS=-O0 ./configure --enable-sdl-video --enable-sdl-audio --disable-vosf --disable-jit-compiler --with-x --with-gtk --with-mon --enable-addressing=banks
make -j 32
