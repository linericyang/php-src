# phpver=php-8.1.0
phpver=php74
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 7 && \
sudo    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 7 && \
    git checkout $phpver
    ./buildconf --force && \
    ./configure  --enable-opcache --enable-fpm --with-mysqli --with-pdo-mysql --enable-pcntl && \
    EXTRA_CFLAGS="-g" LDFLAGS="-Wl,--emit-relocs,-znow" make -j && \
sudo    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 9 && \
sudo    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 9
