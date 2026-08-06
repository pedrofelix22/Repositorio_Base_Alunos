from flask import Flask, jsonify

app = Flask (__name__)

@app.get("/")
def inicio():
    return "Hello, world"

@app.get("/sobre")
def sobre():
    return jsonify( {
        "statrus ":"online",
        "mensagem":"citio do picapal amarelo"
})

@app.get("/api/status")
def status():
    return "aoooba"


app.run(debug=True)

