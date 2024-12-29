from flask import Flask
import random

app = Flask(__name__)
facts_list = ['Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.','Интересно кто сьел мой бигмак?','Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.','Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.']
random_name = ['Это я сьел бигмак','Твой друг украл у тебя деньги,накажи его','Качмен идет за тобой','Лол','Брух']
passw = ['0','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','a','s','d','q','w','e','r','r','t','y','u','i','o','p','f','g','h','j','k','l','z','x','c','v','b','n','m']
def gen_pass():
    rand_pass = ''.join(random.choice(passw) for _ in range(10))
    return rand_pass
    
@app.route("/")
def facts():
    return f'<h1>{random.choice(facts_list)}</h1><a href=/secret_page>НЕ ПЕРЕХОДИ</a>'

@app.route("/random")
def random_page():
    return f'<h1>{random.choice(random_name)}</h1>'

@app.route('/secret_page')
def secret():
        return f'<h1>{gen_pass()}</h1>'
    
if __name__ == "__main__":
    app.run(debug=True)