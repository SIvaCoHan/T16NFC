#! /usr/bin/env python3.10
# -*- coding: utf8 -*-


import ctypes

dll = ctypes.cdll.LoadLibrary('./vendor/comPro.win64.dll')


def lc_init(port: int, baud: int):
    return dll.lc_init(port, baud)


def lc_init_ex(com_type: int, sz_path_name: str, baud: int):
    p1 = ctypes.c_char_p(sz_path_name.encode('utf8'))
    return dll.lc_init_ex(com_type, p1, baud)


def lc_exit(device: int):
    return dll.lc_exit(device)


def lc_choose_communication_device_addr(dev_addr: int):
    return dll.lc_chooseCommuniDevcieAddr(dev_addr)


def asc_hex(str_asc: str, length: int):
    p1 = ctypes.c_char_p(str_asc.encode('utf8'))
    p2 = ctypes.create_string_buffer(length)
    dll.asc_hex(p1, p2, length)
    return p2.value.decode('utf8')


def hex_asc(str_hex: str, length: int):
    p1 = ctypes.c_char_p(str_hex.encode('utf8'))
    p2 = ctypes.create_string_buffer(length * 2)
    dll.hex_asc(p1, p2, length)
    return p2.value.decode('utf8')


def lc_commonTransferInfo(p_buf_in: str):
    p1 = ctypes.c_char_p(p_buf_in.encode('utf8'))
    p2 = ctypes.byref(ctypes.c_int(len(p_buf_in.encode('utf8'))))
    p3 = ctypes.create_string_buffer(24)  # FIXME p3 的参数给的非常任意, 需要重新验证
    p4 = ctypes.byref(ctypes.c_int())
    dll.lc_commonTransferInfo(p1, p2, p3, p4)
    ret_data = p3.value.decode('utf8')
    return ret_data


# def lc_getFlashUserMemSize(int icdev, unsigned int* pSize);
# def lc_getver(int icdev,unsigned char *buff);
# def lc_GetDevSN(int icdev, unsigned char* pbuf, int* rlen);

# def lc_beep(device: int, msec: int):
#     dll.lc_beep(device, msec)
