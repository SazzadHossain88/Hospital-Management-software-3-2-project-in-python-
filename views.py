from django.shortcuts import render,render_to_response
from django.template import Context,loader,RequestContext
from django.http import HttpResponse
from django.db import connection
def index(request):
	
	return render_to_response('home.html',RequestContext(request,{}))

def mylogin(request):
	return render_to_response('login.html',RequestContext(request,{}))

def myhistory(request):
	
	return render_to_response('history.html',RequestContext(request,{}))
def myuseroutpatient(request):
	
	return render_to_response('useroutpatient.html',RequestContext(request,{}))	
def mymsgdg(request):
	
	return render_to_response('msgdg.html',RequestContext(request,{}))

def myonlineappoint(request):
	
	return render_to_response('onlineappoint.html',RequestContext(request,{}))
def myhealthqueries(request):
	
	return render_to_response('healthqueries.html',RequestContext(request,{}))
def myambulance(request):
	
	return render_to_response('ambulance.html',RequestContext(request,{}))

def myhealth(request):
	
	return render_to_response('health.html',RequestContext(request,{}))

def mycomplement(request):
	
	return render_to_response('complement.html',RequestContext(request,{}))
def mypharmacyservice(request):
	
	return render_to_response('pharmacyservice.html',RequestContext(request,{}))
def mycontactus(request):
	
	return render_to_response('contactus.html',RequestContext(request,{}))
def myccu(request):
	
	return render_to_response('ccu.html',RequestContext(request,{}))
def mydeptlocation(request):
	
	return render_to_response('deptlocation.html',RequestContext(request,{}))
def mydiagtest(request):
	
	return render_to_response('diagtest.html',RequestContext(request,{}))
def mypublisharticle(request):
	
	return render_to_response('publisharticle.html',RequestContext(request,{}))
def myjournal(request):
	
	return render_to_response('journal.html',RequestContext(request,{}))
def mydeptdetails(request):
	if 'depttype' in request.POST:
		DeptName=request.POST['depttype']
		cur=connection.cursor()
		quer="Select Did,DName,Age,Address,Email,MobileNo from Doctor where DeptName = '{0}'".format(DeptName)
		cur.execute(quer)
		userlist=cur.fetchall()
			
		return render_to_response('deptdetails.html',{'datas':userlist},RequestContext(request,{}))
	return render_to_response('deptdetails.html',RequestContext(request,{}))	
def myfinddoctors(request):
	
	return render_to_response('finddoctors.html',RequestContext(request,{}))

	
def afterlogin(request):
	username=request.POST['username']
	password=request.POST['password']
	Type=request.POST['Type']
	cur=connection.cursor()
	quer="Select Username,Password,Type from User"
	cur.execute(quer)
	userlist=cur.fetchall()
	
	
	for user in userlist:
		if username==user[0] and password==user[1] and Type==user[2] and Type=="Receptionist":
			con=connection.cursor()
			con.execute("Select Pid,PName,Age,Gender,BloodGroup,MaritalStatus,Occupation,Dateofbirth,Address,Email,MobileNo,test,bill,appoinment from Patient")
			userlist=con.fetchall()
			return render_to_response('reception.html',{'datas':userlist},RequestContext(request,{}))
			
		elif username==user[0] and password==user[1] and Type==user[2] and Type=="Doctor":
			con=connection.cursor()
			con.execute("Select Did ,DName,DeptName,Age,BloodGroup,Dateofbirth,Address,Email,MobileNo,Gender from Doctor where DName = '{0}'".format(username))
			userlist=con.fetchall()
			return render_to_response('doctorprofile.html',{'datas':userlist},RequestContext(request,{}))

		elif username==user[0] and password==user[1] and Type==user[2] and Type=="Pharmacy_Staff":
			con=connection.cursor()
			con.execute("Select Mid ,MName,Mtype,PriceUnit,MfgDate,ExpDate,Quantity from Medicine")
			userlist=con.fetchall()
			return render_to_response('medicinestore.html',{'datas':userlist},RequestContext(request,{}))
		elif  username==user[0] and password==user[1] and Type==user[2] and Type=="Lab_Doctor":
			con=connection.cursor()
			con.execute("Select Testid ,TestName, Amount, TestDate, Pid from Test")
			userlist=con.fetchall()
			return render_to_response('lab.html',{'datas':userlist},RequestContext(request,{}))
		elif  username==user[0] and password==user[1] and Type==user[2] and Type=="Admin":
	
			return render_to_response('adminhome.html',RequestContext(request,{}))

	
	return render_to_response('login.html',RequestContext(request,{}))

def afterreception(request):
	if 'save_button' in request.POST:
		patientID=request.POST['PID']
		patientName=request.POST['PName']
		poccupation=request.POST['Occupation']
		Age=request.POST['Age']
		Gender=request.POST['Gender']
		Address=request.POST['Address']
		Mobile=request.POST['Mobile']
		Bloodgr=request.POST['Blood_group']
		Mstatus="married"
		Bdate=request.POST['DOB']
		email=request.POST['Email']
		test=13456
		bill=1000
		appoint=12
		#print(patientName)
		cur=connection.cursor()
		quer="Insert into Patient values({0},'{1}',{2},'{3}','{4}','{5}','{6}','{7}','{8}','{9}',{10},{11},{12},{13})".format(patientID,patientName,Age,Gender,Bloodgr,Mstatus,poccupation,Bdate,Address,email,Mobile,test,bill,appoint)
		#quer="Insert into Patient values({0})".format(patientID)
		cur.execute(quer)
		con=connection.cursor()
		con.execute("Select Pid ,PName,Age,Gender,BloodGroup,MaritalStatus,Occupation,Dateofbirth,Address,Email,MobileNo,test,bill,appoinment from Patient")
		userlist=con.fetchall()
		return render_to_response('reception.html',{'datas':userlist},RequestContext(request,{}))
		
	if 'search_button' in request.POST:
		searchname=request.POST['PID_search']
		cur=connection.cursor()
		quer="Select Pid ,PName,Age,Gender,BloodGroup,MaritalStatus,Occupation,Dateofbirth,Address,Email,MobileNo,test,bill,appoinment from Patient where PName = '{0}'".format(searchname)
		cur.execute(quer)
		user=cur.fetchall()
		print(user)
		return render_to_response('reception.html',{'datas':user},RequestContext(request,{}))
	if 'delete_button' in request.POST:
		searchname=request.POST['delete']
		cur=connection.cursor()
		quer="Delete from Patient where Pid = {0}".format(searchname)
		cur.execute(quer)
		con=connection.cursor()
		con.execute("Select Pid ,PName,Age,Gender,BloodGroup,MaritalStatus,Occupation,Dateofbirth,Address,Email,MobileNo,test,bill,appoinment from Patient")
		userlist=con.fetchall()
		return render_to_response('reception.html',{'datas':userlist},RequestContext(request,{}))
	if 'clear_button' in request.POST:
		con=connection.cursor()
		con.execute("Select Pid ,PName,Age,Gender,BloodGroup,MaritalStatus,Occupation,Dateofbirth,Address,Email,MobileNo,test,bill,appoinment from Patient")
		userlist=con.fetchall()
		return render_to_response('reception.html',{'datas':userlist},RequestContext(request,{}))
	con=connection.cursor()
	con.execute("Select Pid,PName,Age,Gender,BloodGroup,MaritalStatus,Occupation,Dateofbirth,Address,Email,MobileNo,test,bill,appoinment from Patient")
	userlist=con.fetchall()
	return render_to_response('reception.html',{'datas':userlist},RequestContext(request,{}))

def Doctorpage(request):
	if 'save_button' in request.POST:
		docotorID=request.POST['DID']
		doctorname=request.POST['Dname']
		dage=request.POST['Age']
		Gender=request.POST['Gender']
		dept=request.POST['department']
		bloodgroup=request.POST['Bloodgroup']
		special=request.POST['speciality']
		Mobile=request.POST['mobileno']
		Address=request.POST['Address']
		dateofbirth=request.POST['DOB']
		email=request.POST['email']
		cur=connection.cursor()
		quer="Insert into Doctor values({0},'{1}','{2}',{3},'{4}','{5}','{6}','{7}',{8},'{9}')".format(docotorID,doctorname,dept,dage,bloodgroup,dateofbirth,Address,email,Mobile,Gender)
		#quer="Insert into Doctor values({0})".format(docotorID)
		cur.execute(quer)
		con=connection.cursor()
		con.execute("Select Did ,DName,DeptName,Age,BloodGroup,Dateofbirth,Address,Email,MobileNo,Gender from Doctor")
		userlist=con.fetchall()
		return render_to_response('doctor.html',{'datas':userlist},RequestContext(request,{}))
	if 'search_button' in request.POST:
		searchname=request.POST['Dsearch']
		cur=connection.cursor()
		quer="Select Did ,DName,DeptName,Age,BloodGroup,Dateofbirth,Address,Email,MobileNo,Gender from Doctor where DName = '{0}'".format(searchname)
		cur.execute(quer)
		user=cur.fetchall()
		return render_to_response('doctor.html',{'datas':user},RequestContext(request,{}))
    
	if 'clear_button' in request.POST:
		con=connection.cursor()
		con.execute("Select Did ,DName,DeptName,Age,BloodGroup,Dateofbirth,Address,Email,MobileNo,Gender from Doctor")
		userlist=con.fetchall()
		return render_to_response('doctor.html',{'datas':userlist},RequestContext(request,{}))
	if 'delete_button' in request.POST:
		searchname=request.POST['deleteID']
		cur=connection.cursor()
		quer="Delete from Doctor where Did = {0}".format(searchname)
		cur.execute(quer)
		con=connection.cursor()
		con.execute("Select Did ,DName,DeptName,Age,BloodGroup,Dateofbirth,Address,Email,MobileNo,Gender from Doctor")
		userlist=con.fetchall()
		return render_to_response('doctor.html',{'datas':userlist},RequestContext(request,{}))

def medicinestaff(request):
	if 'save_button' in request.POST:
		medicineID=request.POST['MID']
		Medname=request.POST['MName']
		Medtype=request.POST['Type']
		priceunit=request.POST['price_unit']
		mfg_date=request.POST['mfgdate']
		exp_date=request.POST['expdate']
		quant=request.POST['quantity']
		cur=connection.cursor()
		quer="Insert into Medicine values({0},'{1}','{2}','{3}','{4}','{5}',{6})".format(medicineID,Medname,Medtype,priceunit,mfg_date,exp_date,quant)
		#quer="Insert into Doctor values({0})".format(docotorID)
		cur.execute(quer)
		con=connection.cursor()
		con.execute("Select Mid ,MName,Mtype,PriceUnit,MfgDate,ExpDate,Quantity from Medicine")
		userlist=con.fetchall()
		return render_to_response('medicinestore.html',{'datas':userlist},RequestContext(request,{}))
	if 'delete_button' in request.POST:
		deletename=request.POST['deleteID']
		cur=connection.cursor()
		quer="Delete from Medicine where Mid = {0}".format(deletename)
		cur.execute(quer)
		con=connection.cursor()
		con.execute("Select Mid ,MName,MType,PriceUnit,MfgDate,ExpDate,Quantity from Medicine")
		userlist=con.fetchall()
		return render_to_response('medicinestore.html',{'datas':userlist},RequestContext(request,{}))
	if 'search_button' in request.POST:
		searchname=request.POST['medsearch']
		cur=connection.cursor()
		quer="Select Mid ,MName,MType,PriceUnit,MfgDate,ExpDate,Quantity from Medicine where MName = '{0}'".format(searchname)
		cur.execute(quer)
		user=cur.fetchall()
		return render_to_response('medicinestore.html',{'datas':user},RequestContext(request,{}))
	if 'clear_button' in request.POST:
		con=connection.cursor()
		con.execute("Select Mid ,MName,MType,PriceUnit,MfgDate,ExpDate,Quantity from Medicine")
		userlist=con.fetchall()
		return render_to_response('medicinestore.html',{'datas':userlist},RequestContext(request,{}))
	if 'logout_button' in request.POST:
		#return render_to_response('login.html',RequestContext(request,{}))
		return index(request);

def doctorprescription(request):
	return render_to_response('prescription.html',RequestContext(request,{}))
def inpatient(request):
	if 'admit_button' in request.POST:
		AdmitID=request.POST['AdmitID']
		patientName=request.POST['PName']
		pid=request.POST['PID']
		Roomid=request.POST['Room']
		
		Adate=request.POST['DOA']
		
		print(patientName)
		cur=connection.cursor()
		quer="Insert into Admission values({0},{1},'{2}',{3},'{4}','{5}')".format(AdmitID,pid,patientName,Roomid,Adate,Rdate)
		#quer="Insert into Patient values({0})".format(patientID)
		cur.execute(quer)
		con=connection.cursor()
		con.execute("Select Admitid,Pid ,PName,Roomid,Admitdate,ReleaseDate from Admission")
		userlist=con.fetchall()
		return render_to_response('inpatient.html',{'datas':userlist},RequestContext(request,{}))
	if 'clear_button' in request.POST:
		con=connection.cursor()
		con.execute("Select Admitid,Pid ,PName,Roomid,Admitdate,ReleaseDate from Admission")
		userlist=con.fetchall()
		return render_to_response('inpatient.html',{'datas':userlist},RequestContext(request,{}))
	if 'search_button' in request.POST:
		searchID=request.POST['AID_search']
		cur=connection.cursor()
		quer="Select Admitid,Pid ,PName,Roomid,Admitdate,ReleaseDate from Admission where Admitid = {0}".format(searchID)
		cur.execute(quer)
		user=cur.fetchall()
		return render_to_response('inpatient.html',{'datas':user},RequestContext(request,{}))
	if 'release_button' in request.POST:

		AdmitID=request.POST['AdmitID']
		Rdate=request.POST['DOR']
		
		cur=connection.cursor()
		quer="Update  Admission set ReleaseDate = ('{0}') where Admitid = {1}".format(Rdate,AdmitID)
		cur.execute(quer)
		true=1
		cur.execute("Update  Room set isempty =({0})  where Roomid =(select Roomid from Admission where Admitid = {1})".format(true,AdmitID))
		con=connection.cursor()
		con.execute("Select Admitid,Pid ,PName,Roomid,Admitdate,ReleaseDate from Admission")
		userlist=con.fetchall()
		cur=connection.cursor()
		quer1="SELECT julianday(ReleaseDate) - julianday(Admitdate) from Admission where Admitid = {0}".format(AdmitID)
		cur.execute(quer1);
		dat=cur.fetchall()
		quer2="Select RoomCPD from Room where Roomid = (select Roomid from Admission where Admitid = {0})".format(AdmitID)
		#dat=300
		
		cur.execute(quer2)
		cost=cur.fetchall()
		cur.execute("select Pid from Admission where Admitid = {0}".format(AdmitID))
		Patientid=cur.fetchall()
		quer3="Insert into Bill values({0},{1},{2},'{3}','{4}')".format(request.POST['BID'],Patientid[0][0],dat[0][0]*cost[0][0],request.POST['DOR'],"HOSPITAL")
		cur.execute(quer3)
		return render_to_response('inpatient.html',{'datas':userlist,'data':dat[0][0]*cost[0][0]},RequestContext(request,{}))
	con=connection.cursor()
	con.execute("Select Admitid,Pid ,PName,Roomid,Admitdate,ReleaseDate from Admission")
	userlist=con.fetchall()
	return render_to_response('inpatient.html',{'datas':userlist},RequestContext(request,{}))

		
def labview(request):
	if 'save_button' in request.POST:
		TestID=request.POST['TID']
		Testname=request.POST['TName']
		Date=request.POST['date']
		Amount=request.POST['amount']
		PID=request.POST['PID']
		mobile=request.POST['mobile']
		
		cur=connection.cursor()
		quer="Insert into Test values({0},'{1}','{2}','{3}',{4},'{5}')".format(TestID,Testname,Amount,Date,PID,mobile)
		#quer="Insert into Doctor values({0})".format(docotorID)
		cur.execute(quer)
		con=connection.cursor()
		con.execute("Select Testid ,TestName,Amount,TestDate,Pid,Mobile from Test")
		userlist=con.fetchall()
		return render_to_response('lab.html',{'datas':userlist},RequestContext(request,{}))
	if 'clear_button' in request.POST:
		con=connection.cursor()
		con.execute("Select Testid ,TestName,Amount,TestDate,Pid,Mobile from Test")
		userlist=con.fetchall()
		return render_to_response('lab.html',{'datas':userlist},RequestContext(request,{}))
	if 'delete_button' in request.POST:
		deleteID=request.POST['deleteID']
		con=connection.cursor()
		con.execute("Delete from Test where Testid = {0}".format(deleteID))
		con.execute("Select Testid ,TestName,Amount,TestDate,Pid,Mobile from Test")
		userlist=con.fetchall()
		return render_to_response('lab.html',{'datas':userlist},RequestContext(request,{}))
	if 'search_button' in request.POST:
		searchname=request.POST['searchID']
		cur=connection.cursor()
		quer="Select Testid ,TestName,Amount,TestDate,Pid,Mobile from Test where Testid = '{0}'".format(searchname)
		cur.execute(quer)
		user=cur.fetchall()
		
		return render_to_response('lab.html',{'datas':user},RequestContext(request,{}))
	if 'bill_button' in request.POST:
		bill=request.POST['billID']
		cur=connection.cursor()
		quer1="Select Amount from Test where Testid = '{0}'".format(bill)
		cur.execute(quer1)
		userlist=cur.fetchall()
		return render_to_response('lab.html',{'data':userlist},RequestContext(request,{}))
	return render_to_response('lab.html',RequestContext(request,{}))

def mydoctorprofile(request):
	if 'see_patient' in request.POST:
		DID=request.POST['DID']
		con=connection.cursor()
		con.execute("Select Did ,DName,DeptName,Age,BloodGroup,Dateofbirth,Address,Email,MobileNo,Gender from Doctor where Did = '{0}'".format(DID))
		userlist1=con.fetchall()
		quer="select Pid,PName,Date,Fee,AdvanceFee from Appoinment where Did = {0}".format(DID)
		con.execute(quer)
		userlist=con.fetchall()
		return render_to_response('doctorprofile.html',{'datas1':userlist,'datas':userlist1},RequestContext(request,{}))
		
def prescription(request):
	if 'add_button' in request.POST:
		Pre_ID=request.POST['PreID']
		PID=request.POST['PID']
		MName=request.POST['MName']
		Quantity=request.POST['quantity']
		Mtype=request.POST['MType']
		con=connection.cursor()
		quer="Insert into PresMed values({0},'{1}','{2}',{3})".format(Pre_ID,MName,Mtype,Quantity)
		con.execute(quer)	
		return render_to_response('prescription.html',{'datas':Pre_ID},RequestContext(request,{}))
	if 'clear_button' in request.POST:
		return render_to_response('prescription.html',RequestContext(request,{}))
	if 'search_button' in request.POST:
		searchname=request.POST['search_ID']
		print(searchname)
		cur=connection.cursor()
		quer="Select P.Did ,P.PreDate,M.MName,M.Mtype,M.Quantity from Prescription P, PresMed M where P.Pid = {0} AND P.Preid = M.Preid".format(searchname)
		cur.execute(quer)
		user=cur.fetchall()
		return render_to_response('prescription.html',{'datas':user},RequestContext(request,{}))
	return render_to_response('prescription.html',RequestContext(request,{}))

def appointments(request):
	if 'appoint_button' in request.POST:
		cur=connection.cursor();
		quer1="Insert into Appoinment(Pid,PName,Did,DName,Date,AdvanceFee) values({0},'{1}',{2},'{3}','{4}',{5})".format(request.POST['PID'],request.POST['PName'],request.POST['DID'],request.POST['DName'],request.POST['DOB'],request.POST['Ad_fee'])
		#quer="Update Appoinment set Pid = {0},PName = '{1}',Did = {2},DName ='{3}',Date = '{4}', AdvanceFee = {5}".format(request.POST['PID'],request.POST['PName'],request.POST['DID'],request.POST['DName'],request.POST['DOB'],request.POST['Ad_fee'])
		cur.execute(quer1)
		return render_to_response('apointment.html',RequestContext(request,{}))
	if 'clear_button' in request.POST:
		return render_to_response('apointment.html',RequestContext(request,{}))
	if 'search_button' in request.POST:
		cur=connection.cursor();
		searchname=request.POST['DID_search']
		quer1="Select Pid,PName,Fee,AdvanceFee,Date from Appoinment where Did = {0}".format(searchname)
		
		cur.execute(quer1)
		datas=cur.fetchall()
		return render_to_response('apointment.html',{'data':datas},RequestContext(request,{}))

	return render_to_response('apointment.html',RequestContext(request,{}))


