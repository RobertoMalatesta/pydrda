##############################################################################
#The MIT License (MIT)
#
#Copyright (c) 2016 Hajime Nakagami
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
##############################################################################

EXCSAT = 0x1041
SYNCCTL = 0x1055
SYNCRSY = 0x1069
ACCSEC = 0x106D
SECCHK = 0x106E
SYNCLOG = 0x106F
ACCRDB = 0x2001
BGNBND = 0x2002
BNDSQLSTT = 0x2004
CLSQRY = 0x2005
CNTQRY = 0x2006
DRPPKG = 0x2007
DSCSQLSTT = 0x2008
ENDBND = 0x2009
EXCSQLIMM = 0x200A
EXCSQLSTT = 0x200B
EXCSQLSET = 0x2014
OPNQRY = 0x200C
PRPSQLSTT = 0x200D
RDBCMM = 0x200E
RDBRLLBCK = 0x200F
REBIND = 0x2010
DSCRDBTBL = 0x2012
SQLDTA = 0x2412
SQLDTARD = 0x2413
SQLSTT = 0x2414
SQLATTR = 0x2450
SQLSTTVRB = 0x2419
QRYDSC = 0x241A
QRYDTA = 0x241B
SQLRSLRD = 0x240E
SQLCINRD = 0x240B
ACCSECRD = 0x14AC
AGENT = 0x1403
CODPNT = 0x000C
CODPNTDR = 0x0064
CSTMBCS = 0x2435
CCSIDDBC = 0x119D
CCSIDMBC = 0x119E
CCSIDMGR = 0x14CC
UNICODEMGR = 0x1C08
CCSIDSBC = 0x119C
CMNAPPC = 0x1444
CMNSYNCPT = 0x147C
CMNTCPIP = 0x1474
XAMGR = 0x1C01
CRRTKN = 0x2135
TRGDFTRT = 0x213B
DICTIONARY = 0x1458
DEPERRCD = 0x119B
DSCERRCD = 0x2101
EXCSATRD = 0x1443
EXTNAM = 0x115E
FIXROWPRC = 0x2418
FRCFIXROW = 0x2410
LMTBLKPRC = 0x2417
MGRLVLLS = 0x1404
MGRLVLN = 0x1473
MONITOR = 0x1900
MONITORRD = 0x1C00
NEWPASSWORD = 0x11DE
PASSWORD = 0x11A1
PKGDFTCST = 0x2125
PKGID = 0x2109
MAXBLKEXT = 0x2141
MAXRSLCNT = 0x2140
RSLSETFLG = 0x2142
RDBCMTOK = 0x2105
PKGNAMCT = 0x2112
PKGSNLST = 0x2139
PRCCNVCD = 0x113F
PRDID = 0x112E
OUTOVR = 0x2415
OUTOVROPT = 0x2147
PKGCNSTKN = 0x210D
PRDDTA = 0x2104
QRYINSID = 0x215B
QRYBLKCTL = 0x2132
QRYBLKSZ = 0x2114
QRYPRCTYP = 0x2102
QRYCLSIMP = 0x215D
QRYCLSRLS = 0x215E
QRYOPTVAL = 0x215F
NBRROW = 0x213A
OUTEXP = 0x2111
PRCNAM = 0x2138
QRYATTUPD = 0x2150
RDB = 0x240F
RDBACCCL = 0x210F
RDBALWUPD = 0x211A
QRYRELSCR = 0x213C
QRYSCRORN = 0x2152
QRYROWNBR = 0x213D
QRYROWSNS = 0x2153
QRYRFRTBL = 0x213E
QRYATTSCR = 0x2149
QRYATTSNS = 0x2157
QRYBLKRST = 0x2154
QRYROWSET = 0x2156
QRYRTNDTA = 0x2155
RDBINTTKN = 0x2103
RDBNAM = 0x2110
RDBCOLID = 0x2108
RSCNAM = 0x112D
RSCTYP = 0x111F
RSNCOD = 0x1127
RSYNCMGR = 0x14C1
RTNSQLDA = 0x2116
TYPSQLDA = 0x2146
SECCHKCD = 0x11A4
SECMEC = 0x11A2
SECMGR = 0x1440
SECMGRNM = 0x1196
SECTKN = 0x11DC
RTNEXTDTA = 0x2148
RTNEXTROW = 0x1
RTNEXTALL = 0x2
SPVNAM = 0x115D
SQLAM = 0x2407
SQLCARD = 0x2408
SQLCSRHLD = 0x211F
SQLDARD = 0x2411
SRVCLSNM = 0x1147
SRVDGN = 0x1153
SRVLST = 0x244E
SRVNAM = 0x116D
SRVRLSLV = 0x115A
STTDECDEL = 0x2121
STTSTRDEL = 0x2120
SUPERVISOR = 0x143C
SVCERRNO = 0x11B4
SVRCOD = 0x1149
SYNCPTMGR = 0x14C0
SYNERRCD = 0x114A
TYPDEFNAM = 0x002F
TYPDEFOVR = 0x0035
UOWDSP = 0x2115
USRID = 0x11A0
VRSNAM = 0x1144
PKGNAMCSN = 0x2113
DIAGLVL = 0x2160
DSCINVRM = 0x220A
CMDATHRM = 0x121C
CMDCHKRM = 0x1254
CMDNSPRM = 0x1250
AGNPRMRM = 0x1232
BGNBNDRM = 0x2208
ABNUOWRM = 0x220D
ACCRDBRM = 0x2201
CMDCMPRM = 0x124B
MGRLVLRM = 0x1210
MGRDEPRM = 0x1218
ENDUOWRM = 0x220C
OBJNSPRM = 0x1253
PRCCNVRM = 0x1245
PRMNSPRM = 0x1251
PKGBNARM = 0x2206
PKGBPARM = 0x2209
QRYNOPRM = 0x2202
QRYPOPRM = 0x220F
RDBACCRM = 0x2207
SECCHKRM = 0x1219
RDBAFLRM = 0x221A
RDBATHRM = 0x22CB
RDBNACRM = 0x2204
RDBNFNRM = 0x2211
RDBUPDRM = 0x2218
RSCLMTRM = 0x1233
SYNTAXRM = 0x124C
TRGNSPRM = 0x125F
VALNSPRM = 0x1252
SQLERRRM = 0x2213
OPNQRYRM = 0x2205
ENDQRYRM = 0x220B
DTAMCHRM = 0x220E
OPNQFLRM = 0x2212
RSLSETRM = 0x2219
CMDVLTRM = 0x221D
CMMRQSRM = 0x2225
EXTDTA = 0x146C
FDODSC = 0x0010
FDODTA = 0x147A
FDODSCOFF = 0x2118
FDOPRMOFF = 0x212B
FDOTRPOFF = 0x212A
PBSD = 0xC000
PBSD_ISO = 0xC001
PBSD_SCHEMA = 0xC002
RLSCONV = 0x119F
SYNCCRD = 0x1248
XARETVAL = 0x1904
TIMEOUT = 0x1907
FORGET = 0x1186
SYNCTYPE = 0x1187
XID = 0x1801
XAFLAGS = 0x1903
RSYNCTYP = 0x11EA
SYNCRRD = 0x126D
PRPHRCLST = 0x1905
XIDCNT = 0x1906
