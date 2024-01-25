
#ifndef __COMPRO_H__
#define __COMPRO_H__

#if defined(linux) || defined(__LYNX) || defined(__unix) || defined(_AIX)|| defined(__mips__)
#define _stdcall
#define __stdcall
#include <stdbool.h>
#define BOOL	bool
#endif

#ifndef BOOL
typedef int		BOOL;
#endif 

#ifdef __cplusplus
extern "C"
{
#endif

//===============================================
/*---------- Common Functions--------*/
//===============================================
int _stdcall lc_init(int port,long baud); 
int _stdcall lc_init_ex(int comType, char* szPathName,long baud);
int _stdcall lc_exit(int icdev);
int _stdcall lc_chooseCommuniDevcieAddr(unsigned int devAddr);
//ASC to HEX
int  _stdcall asc_hex(unsigned char *strasc,unsigned char *strhex,int length);
//HEX to ASC
int  _stdcall hex_asc(unsigned char *strhex,unsigned char *strasc,int length);
int _stdcall lc_commonTransferInfo(unsigned char* pBuf_in, int* len_in, unsigned char* pBuf_out, int* len_out);
int _stdcall lc_getFlashUserMemSize(int icdev, unsigned int* pSize);
int _stdcall lc_getver(int icdev,unsigned char *buff);
int _stdcall lc_GetDevSN(int icdev, unsigned char* pbuf, int* rlen);
int _stdcall lc_srd_flash(int icdev,int offset,int length,
								   unsigned char *rec_buffer);
int _stdcall lc_swr_flash(int icdev,int offset,int length,
								   unsigned char* buffer);
int _stdcall lc_devReboot(int icdev);
int _stdcall lc_setAddress(int icdev, unsigned int addr);
int _stdcall lc_getAddress(int icdev, unsigned int* pAddr);
int _stdcall lc_setBaudRate(int icdev,int baud);
int _stdcall lc_SetDevPassword(int icdev,unsigned char pwdAddr, unsigned char pwdLen, unsigned char *pPwd);
int _stdcall lc_crypt(int icdev,unsigned char fEn_De, unsigned char algorithm,
	unsigned int srcLen, unsigned char *pSrc_in, unsigned char* pIv_in,
	unsigned char* pDest_out, unsigned int* pDestLen_out);


int _stdcall lc_setReadOnlyPara(int icdev,unsigned char* pPara,int paraLen);
int _stdcall lc_getReadOnlyPara(int icdev, unsigned char* pPara_out, int* paraLen_out);
int _stdcall lc_setAppendData(int icdev, unsigned char* para_in, unsigned char paraLen);
int _stdcall lc_getAppendData(int icdev, unsigned char* pPara_out, unsigned char* pLen_out);
int _stdcall lc_getOutDataSequence(int icdev, unsigned char* pPara_out, unsigned char* pLen_out);
int _stdcall lc_setOutDataSequence(int icdev, unsigned char* para_in, unsigned char paraLen);
//0->Read/Write, 1->Read only
int _stdcall lc_setReaderMode(int icdev, unsigned char mode);
int _stdcall lc_getReaderMode(int icdev, unsigned char* mode);
int _stdcall lc_set_identifyResponsePara(int icdev, unsigned char* pParaIn, unsigned char paraLen);
int _stdcall lc_get_identifyResponsePara(int icdev, unsigned char* pParaOut, unsigned char* pParaLen);
int _stdcall lc_set_AutoReportDataType(int icdev, unsigned char type,unsigned short outputPort);
int _stdcall lc_get_AutoReportDataType(int icdev, unsigned char* type_out, unsigned short* pOutputPort);
int _stdcall lc_getAutoReturnedData(int icdev, unsigned char* pRData, unsigned int* pRLen);
//===============================================
/*---------- device Functions--------*/
//===============================================
int _stdcall lc_beep(int icdev,unsigned int _Msec);
int _stdcall lc_led(int icdev, int iLED, int on_off);

int _stdcall lc_getBTMAC(int icdev, unsigned char* pMAC);//MAC contain 6 bytes
int _stdcall lc_setBTName(int icdev, char* szName);
int _stdcall lc_getBTName(int icdev, char* pszName);
int _stdcall lc_getPower(int icdev, unsigned char* pPowerPercent);
int _stdcall lc_setShutdownTimer(int icdev, int time);
int _stdcall lc_shutDown(int icdev);

//// expend functions
int _stdcall lc_setTestState(int icdev, unsigned char newSt);

//===============================================
/*----------RFID  Functions--------*/
//===============================================
int _stdcall lc_setANT(int icdev, unsigned char status);
int _stdcall lc_selectANT(int icdev, unsigned int iANT);
int _stdcall lc_rfReset(int icdev, unsigned int time);
int _stdcall lc_getRF_TXConductance(int icdev, unsigned char protocol,  unsigned char* pRegVal);
int _stdcall lc_setRF_TXConductance(int icdev, unsigned char protocol, unsigned char regVal);
int _stdcall lc_card(int icdev,unsigned char _Mode,unsigned char *_Snr, unsigned char* _outSnrSize, unsigned int* pTag, unsigned char* pSak);
int _stdcall lc_requestAndIdentifyTypeA(int icdev,unsigned char _Mode,unsigned char *_Snr, unsigned char* _outSnrSize, 
	unsigned char* pfTagType, unsigned char* pfCompliant14443_4);
int _stdcall lc_authentication(int icdev, unsigned char _Mode, unsigned char sector,unsigned char* pKey);
int _stdcall lc_read(int icdev,unsigned char _Adr,unsigned char *_Data);
int _stdcall lc_read_convenient(int icdev, unsigned char blkAddr, unsigned char keyMode,unsigned char* pKey, unsigned char* pData_out);
int _stdcall lc_write(int icdev,unsigned char _Adr,unsigned char *_Data);
int _stdcall lc_write_convenient(int icdev, unsigned char blkAddr,unsigned char keyMode, unsigned char* pKey, unsigned char* pData_in);
int _stdcall lc_updateKey(int icdev, unsigned char secNr, unsigned char* pNewKeyA, unsigned char* pNewCtrlW, unsigned char* pNewKeyB);
int _stdcall lc_halt(int icdev);
int _stdcall lc_initval(int icdev,unsigned char _Adr,unsigned long _Value);
int _stdcall lc_increment(int icdev,unsigned char _Adr,unsigned long _Value);
int _stdcall lc_readval(int icdev,unsigned char _Adr,unsigned long *_Value);
int _stdcall lc_decrement(int icdev,unsigned char _Adr,unsigned long _Value);
int _stdcall lc_restore(int icdev,unsigned char _fromAdr, unsigned char _toAdr);
int _stdcall lc_readTag(int icdev,unsigned char _Adr,unsigned char *_Data);
int _stdcall lc_writeTag(int icdev,unsigned char _Adr,unsigned char *_Data);
int _stdcall lc_tag_authenPwd(int icdev, unsigned char* pKey_in);
//Para:
//tagType: Tag type, 1-ntag213, 2-ntag215, 3-ntag216
//pPwd: Password, 4 bytes
//protectType: 1-write only, 2-read&write
//protectStartAddr: The address of page start been protect
//maxErrorVerify: The max time verify invalid password continuly,0-Ever(No limit)
//lockConfigAfterSet: Wheather lock configure after setting,TRUE:yes, FALSE:no
int _stdcall lc_tag_setPwd(int icdev, unsigned char tagType,
	unsigned char* pPwd_in,
	unsigned char  protectType,
	unsigned char protectStartAddr,
	unsigned char maxErrorVerify,
	BOOL	lockConfigAfterSet);

/***************
 * Function: Convert card SN to a password
 * Para:
 * pKey: In, the key for cipher, must be 16 bytes
 * cardSN: In,the card number data for cipher
 * snSize: The size of card number data (Bytes)
 * acKeySize: In, the length of pass want return
 * pPass: Out, the returned result
 ***************/
int _stdcall _cardNumberToAccessPass (unsigned char* pKey, unsigned char* pCardSN, int snSize,
	int acKeySize, unsigned char* pPass);

//Utrlight-C
int _stdcall lc_ultralt_C_authen(int icdev, unsigned char* key);
int _stdcall lc_ultralt_C_setSafePage(int icdev, int ipage, BOOL readSec);
int _stdcall lc_ultralt_C_changePwd(int icdev, unsigned char* keyold,
									unsigned char* keynew);
int _stdcall lc_ultralt_C_lockPage(int icdev, int flag);

int __stdcall
lc_pro_reset
(
 int ICDev,//Handle of device
 unsigned char *rlen,//The length of reset information
 unsigned char * rbuff//Reset information
 );

int __stdcall
lc_pro_commandlink
(
 int ICDev,//Handle of device
 unsigned int slen,//The length of data to send
 unsigned char * sbuff,//Data to send
 unsigned int *rlen,//The length of data received
 unsigned char * rbuff,//The data received
 unsigned char tt,//Time for wait when transfering(Unit:10ms)
 unsigned char FG//Section length when transfering(Small than 64)
 );
int _stdcall lc_rawExchange(int icdev,unsigned char slen,unsigned char * sbuff,unsigned char *rrlen,unsigned char * rbuff);
/* getMode: 0-Once every time each card,1-Can read many times one card */
int _stdcall lc_getPBOC_PAN(int icdev, unsigned char slot, unsigned char getMode, char* pPAN);
int _stdcall lc_readSSC(int icdev, unsigned char slot, char* pSSC_Info_out);

