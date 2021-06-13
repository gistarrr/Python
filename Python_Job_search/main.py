from flask import Flask, request, render_template, redirect, send_file
import scrapper
import exporter

db={}
app = Flask("DayThirteen")

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/search")
def jobs():
  searchingBy = request.args.get('term').lower()
  fromDb = db.get(searchingBy)
  if fromDb:
    jobs = fromDb
  else :
    try :
      jobs = scrapper.get_jobs(searchingBy)
      db[searchingBy]=jobs
    except:
      return redirect("/")

  return render_template('search.html', searchingBy = searchingBy, reNumber = len(jobs), jobs=jobs)

@app.route("/export")
def export():
  searchingBy = request.args.get('term')
  try : 
    jobs = db[searchingBy]
    if not jobs:
      raise Exception()
    exporter.save_to_file(searchingBy, jobs)
    return send_file(f"{searchingBy}.csv", mimetype='text/csv',as_attachment=True, attachment_filename=f"{searchingBy}.csv")
  except:
    return redirect("/")
  

app.run(host='0.0.0.0')