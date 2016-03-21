#
# Configuration file for using the XML library in GNOME applications
#
prefix="/usr/local"
exec_prefix="${prefix}"
libdir="${exec_prefix}/lib"
includedir="${prefix}/include"

XMLSEC_LIBDIR="${exec_prefix}/lib"
XMLSEC_INCLUDEDIR=" -D__XMLSEC_FUNCTION__=__FUNCTION__ -DXMLSEC_NO_SIZE_T -DXMLSEC_NO_GOST=1 -DXMLSEC_NO_XKMS=1 -DXMLSEC_DL_LIBLTDL=1 -I${prefix}/include/xmlsec1   -I/usr/local/include/libxml2 -I/usr/local/include -I/usr/local/include -I/usr/local/include/libxml2 -IC:/Opt/msys64/mingw64/include -DXMLSEC_OPENSSL_100=1 -DXMLSEC_CRYPTO_OPENSSL=1 -DXMLSEC_CRYPTO=\\\"openssl\\\""
XMLSEC_LIBS="-L${exec_prefix}/lib -lxmlsec1-openssl -lxmlsec1 -lltdl  -L/usr/local/lib -lxml2 -L/usr/local/lib -lz -L/usr/local/lib -liconv -lws2_32 -L/usr/local/lib -lxslt -lxml2 -lz -liconv -lws2_32 -LC:/Opt/msys64/mingw64/lib -lssl -lcrypto"
MODULE_VERSION="xmlsec-1.2.20-openssl"

