from flask import Flask, render_template
from apimercadopago import gerar_link_pagamento

app = Flask(__name__)

@app.route("/")
def index():
    link_iniciar_pagamento = gerar_link_pagamento()
    return render_template("index.html", link_pagamento = gerar_link_pagamento)

@app.route("/compracerta")
def compra_certa():
    return render_template("compracerta.html")

@app.route("/compraerrada")
def compra_errada():
    return render_template("compraerrada.html")

if __name__ == "__main__":
    app.run()