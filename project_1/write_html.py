# write-html.py
import webbrowser

f = open('Homepage','w')

message = """ <html>
<head></head>
<body><p>This is Jennifer's homepage</p></body>
</html>"""

f.write(message)
f.close()

filename = 'file:///Users/caigen100/百度云同步盘/PythonPractice/project%201/Homepage'
webbrowser.open_new_tab(filename)