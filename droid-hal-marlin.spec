# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device marlin
%define vendor google

%define droid_target_aarch64 1

%define vendor_pretty Google
%define device_pretty Pixel XL

%define installable_zip 1

%define straggler_files \
/bugreports\
/cache\
/d\
/dsp\
/product\
/sdcard\
/system_ext\
/verity_key\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

