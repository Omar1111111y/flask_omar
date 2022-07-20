from flask import Flask, jsonify, request

#########################

app = Flask(__name__)

incomes = {'name':'Omar_Style','age': 18}


@app.route('/api/omar')
def get_incomes():
  return jsonify(incomes)
if __name__ == "__main__":
	app.run()


##########################

