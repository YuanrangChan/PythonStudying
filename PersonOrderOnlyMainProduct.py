#coding=utf-8
import cx_Oracle
import requests
from time import *
import random

def FourteenTime(a):
	if a==8:
		return strftime('%Y%m%d%H%M%S',localtime(time()))[0:8]
	elif a==12:
		return strftime('%Y%m%d%H%M%S',localtime(time()))[0:12]
	elif a==14:
		return strftime('%Y%m%d%H%M%S',localtime(time()))

def OprSeq(FourteenTime):
	o='4311BIP2B958'
	p=FourteenTime(14)
	q=str(random.randint(000000,999999))
	OprSeq=o+p+q
	return OprSeq
#print OprSeq(FourteenTime)

db=cx_Oracle.connect('pboss/pboss#2016@192.168.xxx.xxx/xxx')
cur=db.cursor()
'''
cur.execute("select to_char(iotnumber),provcode,status from (select a.iotnumber,a.provcode,a.status from rs_iot_number a  where a.provcode='431'and a.iotnumber like '106481875%'  AND a.status ='USABLE')")
iotnumber = cur.fetchall()

cur.execute("select to_char(imsi),iccid,k,opc from (select a.imsi,a.iccid,a.k,a.opc from rs_card_info a where a.provcode='431' and a.IMSI like '%46004%' AND a.status ='USABLE' and a.msisdnsection like '%106481875%')")
carddata  = cur.fetchall()
'''
cur.execute("select to_char(iotnumber),provcode,status from (select a.iotnumber,a.provcode,a.status from rs_iot_number a  where a.provcode='431'and a.iotnumber like '106474500%'  AND a.status ='USABLE')")
iotnumber = cur.fetchall()

cur.execute("select to_char(imsi),iccid,k,opc from (select a.imsi,a.iccid,a.k,a.opc from rs_card_info a where a.provcode='431' and a.IMSI like '%46004%' AND a.status ='USABLE' and a.msisdnsection like '%106474500%')")
carddata  = cur.fetchall()

def xmlheader(FourteenTime):
    xml_request='''<?xml version="1.0" encoding="UTF-8"?>
<InterBOSS>
    <Version>0100</Version>
    <TestFlag>0</TestFlag>
    <BIPType>
        <BIPCode>BIP2B958</BIPCode>
        <ActivityCode>T2140958</ActivityCode>
        <ActionCode>0</ActionCode>
    </BIPType>
    <RoutingInfo>
        <OrigDomain>BOSS</OrigDomain>
        <RouteType>00</RouteType>
        <Routing>
            <HomeDomain>PBSS</HomeDomain>
            <RouteValue>997</RouteValue>
        </Routing>
    </RoutingInfo>
    <TransInfo>
        <SessionID>2017070511031010</SessionID>
        <TransIDO>2017070511031010</TransIDO>
        <TransIDOTime>%s</TransIDOTime>
	</TransInfo>
	<SNReserve> 
		<TransIDC>2017070511031010</TransIDC>
		<ConvID>2017070511031010</ConvID>
		<CutOffDay>%s</CutOffDay>
		<OSNTime>%s</OSNTime>
		<OSNDUNS>4310</OSNDUNS>
		<HSNDUNS>9970</HSNDUNS>
		<MsgSender>4311</MsgSender>
		<MsgReceiver>0600</MsgReceiver>
		<Priority>90</Priority>
		<ServiceLevel>55</ServiceLevel>
		<SvcContType>01</SvcContType>
	</SNReserve>  
</InterBOSS>'''%(FourteenTime(14),FourteenTime(8),FourteenTime(14))
    return xml_request

	
	
def xmlbody(FourteenTime):
    xml_request='''<?xml version="1.0" encoding="UTF-8"?>
<InterBOSS>
  <SvcCont><![CDATA[<?xml version="1.0" encoding="UTF-8"?>
		<PersonOrderInfoRequest>
		<PersonInfo>
				<OprSeq>%s</OprSeq>
				<OprTime>%s</OprTime>
				<OprCode>01</OprCode>
			    <ApplyChannel>02</ApplyChannel>
				<ProdID>I00010100001</ProdID>
				<ProdInstID>9431%s01</ProdInstID>
				<SubsID>9431%s01</SubsID>  
				<ProdInstEffTime>%s</ProdInstEffTime> 
				<ProdInstExpTime>20251231235959</ProdInstExpTime>
				          	<ProdInfo>
				               <ProdID>I00010100001</ProdID>
				               <PkgProdID></PkgProdID>
				               <ProdInstID>9431%s01</ProdInstID>
				               <SubsID>9431%s01</SubsID>
					           <ProdInstEffTime>%s</ProdInstEffTime> 
				               <ProdInstExpTime>20251231235959</ProdInstExpTime> 
				               <OperType>01</OperType> 	
					           <MobNum>%s</MobNum>
					           <CardType>01</CardType>
					           <CardPhysicalType>01</CardPhysicalType>
						       <IMSI>%s</IMSI>
						       <ICCID>%s</ICCID>
						       <kKeyID>%s</kKeyID>
						       <opcKeyID>%s</opcKeyID>
				          </ProdInfo>  
				<ProvinceID>431</ProvinceID>
			    <UserStatus>00</UserStatus>
			    <OpenTime>%s</OpenTime>
				<UseTime>%s</UseTime>
				<UserNum>15773343632</UserNum>
				<Addr></Addr> 
				<Email>653435@qq.com</Email> 
				<PostCode>510660</PostCode>
				<Fax>020-00000000</Fax> 
				<IndustryID>03</IndustryID> 
				<SubsInfo> 
				     <SubsID>9431%s01</SubsID>
				     <ServNumber>%s</ServNumber>
				     <ProdID>I00010100001</ProdID> 
				     <CreateDate>%s</CreateDate> 
				     <StartDate>%s</StartDate> 
				     <InvalidDate>20251231235959</InvalidDate> 
				     <Status>00</Status> 
				</SubsInfo>
				<OtherInfo>
				     <InfoCode>100</InfoCode> 
				     <InfoValue>11</InfoValue>
				</OtherInfo> 
				</PersonInfo>
		</PersonOrderInfoRequest>]]></SvcCont>
</InterBOSS>
'''%(OprSeq(FourteenTime),FourteenTime(14),FourteenTime(12),FourteenTime(12),FourteenTime(14),FourteenTime(12),FourteenTime(12),FourteenTime(14),iotnumber[256][0],carddata[196][0],carddata[196][1],carddata[196][2],carddata[196][3],FourteenTime(14),FourteenTime(14),FourteenTime(12),iotnumber[256][0],FourteenTime(14),FourteenTime(14))
    return xml_request

'''
Oprseq=OprSeq(FourteenTime(14))
print Oprseq
'''
header=xmlheader(FourteenTime)
body=xmlbody(FourteenTime)

requestXml = header+body
#print body

url=u'http://192.168.xxx.xxx:xxxx/huawei-test/http/tsn_boss_call_pboss/send.jsp'
data = {'serviceUrl':'http://192.168.xxx.xxx:xxxx/interface4boss/bossTSNActionServlet','requestHeaderXml': header,'requestBodyXml':body,'responseXml':''}
r = requests.post(url,data=data)
x=r.text.find("<Response>")
y=r.text.find("</Response>")
print(r.text[x:y+11])

a=body.find('<OprSeq>')
b=body.find('</OprSeq>')
#Oprseq=body.find[a:b+9]

#print body[a+8:b]
#Oprseq=body[164:196]
oprseq=body[a+8:b]
print oprseq

#print'*'*50
#print '查询工作流程'

#cur.execute("select nodeid,status,to_char(workflowinstid) from (select a.nodeid,a.status,a.workflowinstid from SP_WORKFLOW_INST_NODE a where workflowinstid in (Select a.workflowinstid from SP_WORKFLOW_INST a where oprseq = oprseq))")
#cur.execute("select a.nodeid,a.status  from SP_WORKFLOW_INST_NODE a where workflowinstid in (Select a.workflowinstid from SP_WORKFLOW_INST a where oprseq = oprseq)")

#nodeidstatus = cur.fetchall()

#print nodeidstatus

#print u'nodeidstatus类型为：' 
#print type(nodeidstatus)
#print nodeidstatus[0],nodeidstatus[1],nodeidstatus[2]
#print nodeidstatus[0],nodeidstatus[1],nodeidstatus[2]

'''
print nodeidstatus[0][0],nodeidstatus[0][1]
print nodeidstatus[1][0],nodeidstatus[1][1]
print nodeidstatus[2][0],nodeidstatus[2][1]
print nodeidstatus[3][0],nodeidstatus[3][1]
print nodeidstatus[4][0],nodeidstatus[4][1]
'''
sleep(30)

print'*'*50
print'查询订单明细'
cur.execute("select a.status from om_opr_order_detail a  where  oprseq = oprseq")

orderdetailstatus = int(cur.fetchone()[0])


print orderdetailstatus

if orderdetailstatus==99:
	print '该笔订单已完成，正常竣工！'
else:
	print '该笔订单未正常竣工，请自行查看原因！'

cur.close()

db.close()
