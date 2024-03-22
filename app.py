from flask import Flask, request, render_template

app = Flask(__name__)



# Calculadora
def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    else:
        return x / y

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    resultado = None
    if request.method == 'POST':
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        operacao = request.form.get('operacao')
        
        if operacao == 'adicionar':
            resultado = adicionar(num1, num2)
        elif operacao == 'subtrair':
            resultado = subtrair(num1, num2)
        elif operacao == 'multiplicar':
            resultado = multiplicar(num1, num2)
        elif operacao == 'dividir':
            resultado = dividir(num1, num2)
            
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)