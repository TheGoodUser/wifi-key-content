import subprocess as sb

html = r'''<!DOCTYPE html>
<html>
<head>
	<title>wi-fi passwords</title>
	<link rel="icon" type="image/x-icon" href="https://photos.google.com/share/AF1QipM72EgfTnVhACkEqt96_rVolDTjfWYssSvy3g1-uZeNsXHusHmriXovgsOAVRhrlQ/photo/AF1QipO1tZgOVXxx8grO5Ll7vw-T9gvI4Bt5XejIiC0c?key=UC0zNHhjVEVOMkZFVUw4VDB4RjM0aU5yUVpnTVFR">


	<style type="text/css">
	@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300&family=Source+Code+Pro:wght@300&display=swap');
	@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&family=Roboto+Mono:wght@300&family=Source+Code+Pro:wght@300&display=swap');

		body{
			background-color: rgb(15, 50, 50);
		}

		#head{
			font-family: Roboto Mono;
			font-weight: bold;
			text-align: center;
			font-size: 70px;
			padding-left: 4px;
			background-color: rgb(240, 250, 250);
			padding: 10px;
			margin: 40px;
			border-radius: 4rem;
		}

		#host{
			font-family: Roboto Mono;
			text-align: center;
			font-size: 40px;
		}

		th, td{
			border-collapse: collapse;
			margin-left: 3rem;
			margin-right: 3rem;
			
		}

		td{
			padding: 20px;
			font-size: 30px;
		}

		th{
			font-family: Poppins;
			background-color: rgb(32, 40, 50);
			color: white;
			padding-right: 10rem;
			padding-left: 1rem;
			font-size: 50px;
		}

		table{
			border-collapse: collapse;
		}

		tr{
			background-color: rgb(36, 46, 56);
			color: white;
			padding: auto;
			font-family: Roboto Mono;
		}

		tr:nth-child(odd){
			background-color: rgb(44, 56, 68);
		}

		#main-data{
			background-color: rgb(90, 60, 80);
			padding-bottom: 4rem;
			border-radius: 3rem;
		}

		#end{
			font-family: Seoge Point;
			font-size: 30px;
			padding-top: 30rem;
			color: white;
		}

		#end a{
			text-decoration: none;
		}

	</style>
</head>
<body>
	<p id="head">WiFi Key-Content</p>
	<br>
	<br>
	<br>

	<p id="host"><span style="color: white;">host-name : </span><span style="color: rgb(255, 153, 153); background-color: rgb(49, 61, 71); padding: 10px;"><u>The_User</u></span></p>
	
	<div id="main-data">
		<br><br><br><br><br>
		<table align="center">
			<caption style="font-size: 30px; color: gold; margin: 2rem;"><i>TheGoodUser</i></caption>
			<tr>
				<th>Profiles</th>
				<th>Key Content</th>
			</tr>
			table_data
		</table>
	</div>

	<p id="end">This page is designed by <a href="https://www.github.com/TheGoodUser/"><span style="color: orange;">TheGoodUser.</span></a></p>
</body>
</html>'''

a = sb.check_output("netsh wlan show profile", shell=True).decode("utf-8").splitlines()
body = ""
_1_ = {}

for f in range(9, len(a)):
    try:
        p = sb.check_output(f'netsh wlan show profile "{a[f][27:]}" key=clear', shell=True).decode("utf-8").splitlines()
        for m in range(32, len(p)-9, 2):
            _1_[a[f][27:]] = p[m][29:]
    except:
        pass
for f,j in _1_.items():
    body += f"""<tr><td>{f}</td><td>{j}</td></tr>"""

html = html.replace("table_data", body)
html = html.replace("The_User", sb.check_output("hostname", shell=True).decode("utf-8"))
with open("index.html", "a") as f:
	f.write(html)



sb.check_output("start index.html", shell=True)


print("Task accomplished sucessfully.")

