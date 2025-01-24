from flask import Flask, request, jsonify
from weightligting import *

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        pr = data.get('pr')
        load = data.get('load')
        sn = data.get('sn')
        cj = data.get('cj')
        body_weight = data.get('bodyWeight')

        if None in (pr, load, sn, cj, body_weight):
            return jsonify({"error": "All fields are required."}), 400

        train_pct = calculate_load_percentage(pr, load)
        if isinstance(train_pct, str):
            return jsonify({"error": train_pct}), 400

        total_lift = calculate_total(sn, cj)
        if isinstance(total_lift, str):
            return jsonify({"error": total_lift}), 400

        sinclair = calculate_sinclair(body_weight) * total_lift
        plate_needed = plate_load(load, BAR)

        return jsonify({
            'trainPct': train_pct,
            'totalLift': total_lift,
            'sinclair': sinclair,
            'plateNeeded': plate_needed
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
