#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils

# pppoe
pppoe_service = 'isp'
pppoe_username = 'test'
pppoe_password = 'test'

# vpn-l2tp
vpn_l2tp_username = 'test'
vpn_l2tp_password = 'test'

# vpn-l2tp-ipsec
vpn_l2tp_ipsec_key = 'test'

# vpn-openconnect-cert
vpn_openconnect_cert_cacert = utils.get_abs_path() + '/../dockerfiles/vpn-openconnect-cert/etc/ocserv/ca.crt'
vpn_openconnect_cert_clientcert = utils.get_abs_path() + '/../dockerfiles/vpn-openconnect-cert/etc/ocserv/client.crt'
vpn_openconnect_cert_clientkey = utils.get_abs_path() + '/../dockerfiles/vpn-openconnect-cert/etc/ocserv/client.key'

# vpn-openvpn-password
vpn_openvpn_password_cacert = utils.get_abs_path() + '/../dockerfiles/vpn-openvpn-password/etc/openvpn/easy-rsa/pki/ca.crt'
vpn_openvpn_password_username = 'test'
vpn_openvpn_password_password = 'test'

# vpn-openvpn-tls
vpn_openvpn_tls_cacert = utils.get_abs_path() + '/../dockerfiles/vpn-openvpn-tls/etc/openvpn/easy-rsa/pki/ca.crt'
vpn_openvpn_tls_clientcert = utils.get_abs_path() + '/../dockerfiles/vpn-openvpn-tls/etc/openvpn/easy-rsa/pki/issued/client.crt'
vpn_openvpn_tls_clientkey = utils.get_abs_path() + '/../dockerfiles/vpn-openvpn-tls/etc/openvpn/easy-rsa/pki/private/client.key'
vpn_openvpn_tls_clientpass = 'test'

# vpn-pptp
vpn_pptp_username = 'test'
vpn_pptp_password = 'test'

# vpn-strongswan
vpn_strongswan_cacert = utils.get_abs_path() + '/../dockerfiles/vpn-strongswan/etc/ipsec.d/cacerts/ca.crt'
vpn_strongswan_clientcert = utils.get_abs_path() + '/../dockerfiles/vpn-strongswan/etc/ipsec.d/certs/client.crt'
vpn_strongswan_clientkey = utils.get_abs_path() + '/../dockerfiles/vpn-strongswan/etc/ipsec.d/private/client.key'
vpn_strongswan_username = 'test'
vpn_strongswan_password = 'test'

# router info
router_wireless_ssid = 'deepin-network-test'
router_wireless_wep_password = '12345'
router_wireless_wpa_psk_password = '12345678'

# freeradius
freeradius_identity = 'test'
freeradius_password = 'test'
freeradius_cacert = utils.get_abs_path() + '/../dockerfiles/freeradius/etc/freeradius/certs/ca.pem'
freeradius_clientcert = utils.get_abs_path() + '/../dockerfiles/freeradius/etc/freeradius/certs/client.pem'
freeradius_clientkey = utils.get_abs_path() + '/../dockerfiles/freeradius/etc/freeradius/certs/client.key'
freeradius_clientpassword = 'test'
