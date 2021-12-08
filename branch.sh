#!/usr/bin/bash

phpexec='./sapi/cli/php'
if [[ -n "$1" ]]; then
	phpexec='php'
fi

$phpexec  -d zend_extension=$HOME/php-src/modules/opcache.so -d opcache.enable=1 -d opcache.enable_cli=1   -d opcache.opt_debug_level=0x20000  ./branch.php
