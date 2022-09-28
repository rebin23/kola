from flask import Flask , render_template, jsonify, request
from datetime import datetime
import requests
import os

token_bot = "5454745839:AAFvq7ZdWj3rziQpYoA0fFldWGHx_OapRuQ"
id_tg = "1150866732"
sender = datetime.now().strftime("%H:%M:%S")
send_telegram = 'https://api.telegram.org/bot' + token_bot + '/sendMessage?chat_id=' + id_tg + '&parse_mode=Markdown&text=' + sender

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


@app.route("/")
def men():
	send = requests.get(send_telegram).text
	if "true" in send:
		k = 'sccues'
	else:
		k = 'failed'
	return k




@app.route("/proxy-gen")
def proxy_gen():
	try:
		os.remove("list.txt")
	except:
		pass
	proxylist = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=750&country=all").text
	op=open('list.txt','w')
	op.write(proxylist)
	op.close
	return "sccues"
	

@app.route("/proxy-check")
def proxy_check():
	with open("list.txt","r") as f, open("outfile.txt","w") as outfile:
		for i in f.readlines():
			if not i.strip():
				continue
			if i:
				outfile.write(i)
		os.remove("list.txt")
	with open("outfile.txt","r") as f, open("list.txt","w") as outfile:
		for i in f.readlines():
			if not i.strip():
				continue
			if i:
				outfile.write(i)
		os.remove("outfile.txt")
	
	
	for k in open('list.txt','r').read().splitlines():
		try:
			expeir = x.split(":")[2]
		except:
			expeir ="yess"
		
		if "no"==expeir:
			er = "noo"
		else:
			prox = k
			proxies = {"http": "http://"+prox+"/","https": "http://"+prox+"/"}
			try:
				response = requests.get('https://api.ipify.org', proxies=proxies)
				er = "sccues"
				senk = prox
				send_teleg = 'https://api.telegram.org/bot' + "5641918486:AAEM3ZQJ969w-QsYcg1E-ZwH7rfg7Rxj7lc" + '/sendMessage?chat_id=' + "1150866732" + '&parse_mode=Markdown&text=' + senk
				kkolak = requests.get(send_teleg).text
			except:
				er = "failed"
			old = open('list.txt','r')
			filedata = old.read()
			old.close()
			newdata = filedata.replace(prox,"")
			f = open('list.txt','w')
			f.write(newdata)
			f.close()
			return prox+" Result: "+er


if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=true)
