from django.shortcuts import render
from .forms import FileUploadForm

#now cyber part
import hashlib
#-----------


def handle_uploaded_file(f):
	with open('x','wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

# Create your views here.

def home(request):
	return render(request,'home.html')

def fileprocess(request):
	form = FileUploadForm(request.POST, request.FILES)
	if form.is_valid():
		handle_uploaded_file(request.FILES['file'])

		#Cyber Security Begins
		#Malware Detection Project Starts Here 
		#//------------------------------------------------

		#Global Variable
		global malware_hashes #= list(open('vhash.txt','r').read().split('\n'))
		malware_hashes = list(open('vhash.txt','r').read().split('\n'))
		global virusInfo #= list(open('vrinfo.txt','r').read().split('\n'))
		virusInfo = list(open('vrinfo.txt','r').read().split('\n'))



		#Get Hash of File
		def sha256_hash(filename):
			with open(filename,'rb') as f:
				bytes = f.read()
				sha256hash = hashlib.sha256(bytes).hexdigest()
				f.close()

				print(sha256hash)
			return sha256hash

		#Malware Detection By Hash
		def malware_checker(pathOfFile):
			#global malware_hashes
			#global virusInfo

			hash_malware_check = sha256_hash(pathOfFile)
			counter = 0


			for i in malware_hashes:
				if i == hash_malware_check:
					return virusInfo[counter]

				counter += 1

			return 0

		print(malware_checker('x'))


		res = malware_checker('x')

		



		#//-------------------------------------------------


	return render(request,'result.html',{'res' : res })