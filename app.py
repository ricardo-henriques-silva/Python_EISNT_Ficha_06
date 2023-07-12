from flask import Flask, render_template, request, redirect, url_for, flash
from forms import AvancarForm, RespostaForm, MensagemForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredo'

respostas_correctas = 'lisboa'
mensagens = []

@app.route("/", methods=['GET', 'POST'])
def home(): # alterar código seguinte
    form_avancar = AvancarForm()
    if form_avancar.validate_on_submit():
        if True:
            return redirect(url_for('desafios'))
    return render_template('home.html', form=form_avancar)

@app.route("/desafios", methods=['GET', 'POST'])
def desafios():
    #respostas_form=[] # inicialização da lista com as respostas do utilizador
    respostas_form = RespostaForm() # Obter as respostas enviadas pelo formulário
    if respostas_form.validate_on_submit():
        # Verificar se as respostas estão corretas
        if respostas_form.resposta.data == respostas_correctas:
            return redirect(url_for('final'))
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')
    return render_template('desafios.html', form=respostas_form)

@app.route("/final", methods=['GET', 'POST'])
def mensagem(): # alterar código seguinte
    form = MensagemForm() #Inicia o form
    if form.validate_on_submit():
        mensagem = form.mensagem.data 
        mensagens.append(mensagem) # adiciona a nova mensagem à lista de mensagens
        flash(f'Mensagem recebida: {mensagem}') # Print da mensagem
        flash(f'Mensagem enviada com sucesso! Já existem {len(mensagens)} mensagem(s).', 'success')
    return render_template('final.html', form=form)
   
#@app.route("/mensagens")
#def ver_mensagens():
#    return render_template('mensagens.html', mensagens=mensagens)

if __name__ == "__main__":
    app.run()