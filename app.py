from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'super-secret-key-for-bmi-history' # Required for session

def calculate_bmi(weight, height_cm):
    try:
        height_m = float(height_cm) / 100
        weight_kg = float(weight)
        bmi = weight_kg / (height_m ** 2)
    except (ValueError, ZeroDivisionError):
        return None, None, None
    
    if bmi < 18.5:
        category = "體重過輕 (Underweight)"
        color = "text-blue-500"
    elif 18.5 <= bmi < 25:
        category = "正常範圍 (Normal weight)"
        color = "text-green-500"
    elif 25 <= bmi < 30:
        category = "過重 (Overweight)"
        color = "text-yellow-500"
    else:
        category = "肥胖 (Obese)"
        color = "text-red-500"
        
    return round(bmi, 2), category, color

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    
    if request.method == 'POST':
        weight = request.form.get('weight')
        height = request.form.get('height')
        bmi, category, color = calculate_bmi(weight, height)
        
        if bmi:
            result = {'bmi': bmi, 'category': category, 'color': color}
            # Save to session history
            if 'history' not in session:
                session['history'] = []
            
            # Append new result to history (keep last 5)
            session['history'].insert(0, {
                'bmi': bmi, 
                'category': category, 
                'color': color,
                'weight': weight,
                'height': height
            })
            session['history'] = session['history'][:5]
        else:
            result = {'error': '請輸入正確的數字！'}
            
    return render_template('index.html', result=result, history=session.get('history', []))

@app.route('/clear')
def clear_history():
    session.pop('history', None)
    return render_template('index.html') # In a real app, we'd redirect

if __name__ == '__main__':
    app.run(debug=True, port=5000)
