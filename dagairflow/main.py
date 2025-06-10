from flask import Flask, request, jsonify, render_template_string
import json
from datetime import datetime
from db_utils import insert_alert_data, get_info,get_info_failed,get_info_success
from html_template import html_template,html_templateTest
app = Flask(__name__)

def append_to_file(filename, content):
    """Функция для дописывания данных в файл с разделителем"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"\n\nРазделение\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(content)
        f.write("\n")  # Добавляем перенос строки в конце

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    if request.method == 'POST':
        # Получаем данные из запроса
        datapost = request.get_json()
        for data in datapost:
            name=data.get("name")
            startTime=data.get("startTime")
            stopTime=data.get("stopTime")
            TimeCalculation=data.get("TimeCalculation")
            Status=data.get("Status")
            #логирую для разработки
            pretty_data = json.dumps(data, indent=4, ensure_ascii=False)
            print(pretty_data)
            print("\nА здесь разделение между логами\n")
            append_to_file('data.txt', str(data)) #запись в файл до json
            append_to_file('pretty_data.txt', pretty_data) #после json
            print("Начинаю добавлять информацию в таблицу \n")
            insert_alert_data(name,startTime,stopTime,TimeCalculation,Status)

        return jsonify({"message": "Webhook received successfully"}), 200
    else:
        return jsonify({"error": "Произошла ошибка 405"}), 405


@app.route('/getdag', methods=['GET'])
def show_dag_info():
    # Получаем параметр фильтра из URL
    filter_type = request.args.get('filter', 'all')
    # Выбираем соответствующую функцию для получения данных
    if filter_type == 'success':
        data = get_info_success()
        #data_test = [('ЕвгенийСакцесс', '22.04'), ('ИванСакцес', '23.03'), ('ОлегСакцес', '12.05')]
    elif filter_type == 'failed':
        data = get_info_failed()
        #data_test = [('ИванФайлед', '22.04'), ('ИванФайлед', '23.03'), ('ОлегФайлдер', '12.05')]
    else:
        data_test = [('Евгений', '22.04'), ('Иван', '23.03'), ('Олег', '12.05')]
        data = get_info()
    return render_template_string(html_templateTest, data=data)
    # # Получаем данные из базы данных
    # #data = get_info()
    # data_test = [('Евгений', '22.04'), ('Иван', '23.03'), ('Олег', '12.05')] #для тестов
    # print(data_test)
    # return render_template_string(html_template, data=data_test)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)