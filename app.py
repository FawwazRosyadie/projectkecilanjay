from flask import Flask, request, jsonify
from weightlifting import calculate_load_percentage, calculate_total, calculate_sinclair, plate_load, print_plates

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    pr = data.get('pr')
    load = data.get('load')
    sn = data.get('sn')
    cj = data.get('cj')
    body_weight = data.get('bodyWeight')

    train_pct = calculate_load_percentage(pr, load)
    total_lift = calculate_total(sn, cj)
    sinclair = calculate_sinclair(body_weight) * total_lift
    plate_needed = plate_load(load, 20)  # Assuming BAR weight is 20 kg

    return jsonify({
        'trainPct': train_pct,
        'totalLift': total_lift,
        'sinclair': sinclair,
        'plateNeeded': plate_needed
    })

if __name__ == '__main__':
    app.run(debug=True)
