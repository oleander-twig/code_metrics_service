from flask import Flask, request, render_template
from clickhouse_driver import Client
from sender import create_task


client = Client(host='localhost')
app = Flask(__name__)

@app.get("/start/<repo_name>")
def get_repo(repo_name):

    if repo_name != "":

      # check if this repo in db 
        res = client.execute('SELECT %(repo_name)s FROM repos', {'repo_name':repo_name})
        if res:
            
            print(res)
            # serch metrics
            pass
        else: 

            # put repo  in message queue 
            create_task(repo_name)
            pass
        
        return render_template('hello.html', repo_name=repo_name)
    else:
        error = 'Empty query!'
        return render_template('hello.html', error=error), 404


@app.post("/metrics/<repo_name>")
def export_metrics(repo_name):
    # get metrics by repo_name
    return render_template('hello.html')