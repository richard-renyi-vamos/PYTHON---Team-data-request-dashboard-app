from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Store team data in a dictionary
team_data = {}

@app.route('/')
def dashboard():
    """
    Display the dashboard with all team data.
    """
    return render_template('dashboard.html', teams=team_data)

@app.route('/submit_data/<team_id>', methods=['POST'])
def submit_data(team_id):
    """
    Endpoint for teams to submit their data.
    :param team_id: The ID of the team submitting data.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Save the team's data
    team_data[team_id] = data
    return jsonify({"message": f"Data received from Team {team_id}"}), 200

if __name__ == '__main__':
    app.run(debug=True)
