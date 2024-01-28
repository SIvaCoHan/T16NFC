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
    # FIXME 这个接口文档没有提到
    return dll.lc_chooseCommuniDevcieAddr(dev_addr)


def asc_hex(str_asc: bytes, length: int):
    p1 = ctypes.c_char_p(str_asc)
    p2 = ctypes.create_string_buffer(1024)
    dll.asc_hex(p1, p2, length)
    return p2.value


def hex_asc(str_hex: bytes, length: int):
    p1 = ctypes.c_char_p(str_hex)
    p2 = ctypes.create_string_buffer(1024)
    dll.hex_asc(p1, p2, length)
    return p2.value


def lc_commonTransferInfo(p_buf_in: str):
    p1 = ctypes.c_char_p(p_buf_in.encode('utf8'))
    p2 = ctypes.byref(ctypes.c_int(len(p_buf_in.encode('utf8'))))
    p3 = ctypes.create_string_buffer(24)  # FIXME p3 的参数给的非常任意, 需要重新验证
    p4 = ctypes.byref(ctypes.c_int())
    dll.lc_commonTransferInfo(p1, p2, p3, p4)
    ret_data = p3.value.decode('utf8')
    return ret_data


def lc_getFlashUserMemSize(device: int):
    pSize = ctypes.c_uint(0)
    p1 = ctypes.byref(pSize)
    dll.lc_getFlashUserMemSize(device, p1)
    return pSize.value


def lc_getver(device: int):
    p3 = ctypes.create_string_buffer(24)  # FIXME p3 的参数给的非常任意, 需要重新验证
    dll.lc_getver(device, p3)
    return p3.value.decode('utf8')


def lc_GetDevSN(device: int):
    p3 = ctypes.create_string_buffer(1024)  # FIXME p3 的参数给的非常任意, 需要重新验证
    _p = ctypes.c_int()
    p4 = ctypes.byref(_p)
    dll.lc_GetDevSN(device, p3, p4)
    ret = hex_asc(p3.raw[:_p.value], _p.value)
    return ret


def lc_srd_flash(device: int, offset: int,length: int, rec_buffer):
    # TODO 不知道rec_buffer 是输入还是输出
    pass


def lc_swr_flash(device: int, offset: int,length: int, rec_buffer):
    # TODO 不知道rec_buffer 是输入还是输出
    pass


def lc_devReboot(device: int):
    return dll.lc_devReboot(device)


def lc_setAddress(device: int, addr: int):
    return dll.lc_setAddress(device, addr)


def lc_getAddress(device: int):
    pAddr = ctypes.c_uint(0)
    dll.lc_getAddress(device, ctypes.byref(pAddr))
    return pAddr.value


def lc_setBaudRate(device: int,baud: int):
    return dll.lc_setBaudRate(device, baud)


def lc_SetDevPassword(device: int, pwdAddr: int, pwdLen: int, pPwd: str):
    return dll.lc_SetDevPassword(device, pwdAddr, pwdLen, ctypes.c_char_p(pPwd.encode('utf8')))


def lc_crypt(device: int, fEn_De: int, algorithm: int, srcLen: int, pSrc_in: str, pIv_in: str):
    pDest_out = ctypes.create_string_buffer(100)
    pDestLen_out = ctypes.c_uint(0)
    dll.pDestLen_out(device, fEn_De, algorithm, srcLen, pSrc_in, pIv_in, pDest_out, ctypes.byref(pDestLen_out))
    return pDest_out.value.decode('utf8')


def lc_setReadOnlyPara(device: int, pPara: str):
    paraLen = len(pPara.encode('utf8'))
    return dll.lc_setReadOnlyPara(device, ctypes.byref(ctypes.c_char_p(pPara.encode('utf8'))), paraLen)


def lc_getReadOnlyPara(device: int):
    pPara = ctypes.create_string_buffer(100)
    pParaLen = ctypes.c_uint(0)
    dll.lc_getReadOnlyPara(device, pPara, ctypes.byref(pParaLen))
    return pPara.value.decode('utf8')


# def lc_setAppendData(int icdev, unsigned char* para_in, unsigned char paraLen);
# def lc_getAppendData(int icdev, unsigned char* pPara_out, unsigned char* pLen_out);
# def lc_getOutDataSequence(int icdev, unsigned char* pPara_out, unsigned char* pLen_out);
# def lc_setOutDataSequence(int icdev, unsigned char* para_in, unsigned char paraLen);
# def lc_setReaderMode(int icdev, unsigned char mode);
# def lc_getReaderMode(int icdev, unsigned char* mode);
# def lc_set_identifyResponsePara(int icdev, unsigned char* pParaIn, unsigned char paraLen);
# def lc_get_identifyResponsePara(int icdev, unsigned char* pParaOut, unsigned char* pParaLen);
# def lc_set_AutoReportDataType(int icdev, unsigned char type,unsigned short outputPort);
# def lc_get_AutoReportDataType(int icdev, unsigned char* type_out, unsigned short* pOutputPort);
# def lc_getAutoReturnedData(int icdev, unsigned char* pRData, unsigned int* pRLen);


def lc_card(device: int, _Mode: int):
    # , _Snr: str, _outSnrSize: str, pTag: int, pSak: str
    _Snr = ctypes.create_string_buffer(1024)
    _outSnrSize = ctypes.c_uint(0)
    pTag = ctypes.c_uint(0)
    pSak = ctypes.create_string_buffer(1024)
    dll.lc_card(device, _Mode, _Snr, ctypes.byref(_outSnrSize), ctypes.byref(pTag), pSak)
    # return hex_asc(_Snr.raw[:_outSnrSize.value], _outSnrSize.value)
    return pTag.value, pSak.raw[:10]

# def lc_requestAndIdentifyTypeA(int icdev,unsigned char _Mode,unsigned char *_Snr, unsigned char* _outSnrSize,
# unsigned char* pfTagType, unsigned char* pfCompliant14443_4);

# int _stdcall lc_authentication(int icdev, unsigned char _Mode, unsigned char sector,unsigned char* pKey);
# int _stdcall lc_read(int icdev,unsigned char _Adr,unsigned char *_Data);
def lc_read_convenient(device: int, blkAddr: int, keyMode: int, pKey: bytes):
    pData_out = ctypes.create_string_buffer(20)
    dll.lc_read_convenient(device, blkAddr, keyMode, ctypes.c_char_p(pKey), pData_out)
    return pData_out.raw

# int _stdcall lc_write(int icdev,unsigned char _Adr,unsigned char *_Data);
def lc_write_convenient(device: int, blkAddr: int,keyMode: int, pKey: bytes, pData_in: bytes):
    d = dll.lc_write_convenient(device, blkAddr, keyMode, ctypes.c_char_p(pKey), ctypes.c_char_p(pData_in))
    return d


# int _stdcall lc_updateKey(int icdev, unsigned char secNr, unsigned char* pNewKeyA, unsigned char* pNewCtrlW, unsigned char* pNewKeyB);

def lc_beep(device: int, msec: int):
    dll.lc_beep(device, msec)
