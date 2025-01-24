from flask import Flask, request, jsonify
from weightligting import *

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json

    try:
        pr = float(data.get('pr'))
        load = float(data.get('load'))
        sn = float(data.get('sn'))
        cj = float(data.get('cj'))
        body_weight = float(data.get('bodyWeight'))

        if pr <= 0 or load <= 0 or sn <= 0 or cj <= 0 or body_weight <= 0:
            return jsonify({'error': 'Inputs must be positive numbers.'}), 400

        train_pct = calculate_load_percentage(pr, load)
        total_lift = calculate_total(sn, cj)
        sinclair = calculate_sinclair(body_weight, total_lift)
        plate_needed = plate_load(load, 20)

        return jsonify({
            'trainPct': train_pct,
            'totalLift': total_lift,
            'sinclair': sinclair,
            'plateNeeded': plate_needed
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
