from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
from datetime import datetime
from gri_glossary import GRI_GLOSSARY

app = Flask(__name__)

# Store data in JSON files for simplicity
DATA_DIR = 'data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    # Load existing reports
    reports = []
    if os.path.exists(f'{DATA_DIR}/reports.json'):
        with open(f'{DATA_DIR}/reports.json', 'r') as f:
            reports = json.load(f)
    return render_template('dashboard.html', reports=reports)

@app.route('/new-report')
def new_report():
    return render_template('new_report.html')

@app.route('/organization-setup')
def organization_setup():
    return render_template('organization_setup.html')

@app.route('/guidance')
def guidance():
    return render_template('guidance.html')

@app.route('/api/save-organization', methods=['POST'])
def save_organization():
    data = request.json
    data['created_at'] = datetime.now().isoformat()
    
    with open(f'{DATA_DIR}/organization.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    return jsonify({'success': True, 'message': 'Organization details saved successfully'})

@app.route('/api/get-organization')
def get_organization():
    if os.path.exists(f'{DATA_DIR}/organization.json'):
        with open(f'{DATA_DIR}/organization.json', 'r') as f:
            return jsonify(json.load(f))
    return jsonify({})

@app.route('/api/glossary/<term>')
def get_glossary_term(term):
    definition = GRI_GLOSSARY.get(term.lower())
    if definition:
        return jsonify({'term': term, 'definition': definition})
    return jsonify({'error': 'Term not found'}), 404

@app.route('/api/save-report', methods=['POST'])
def save_report():
    data = request.json
    data['id'] = datetime.now().strftime('%Y%m%d_%H%M%S')
    data['created_at'] = datetime.now().isoformat()
    
    # Load existing reports
    reports = []
    if os.path.exists(f'{DATA_DIR}/reports.json'):
        with open(f'{DATA_DIR}/reports.json', 'r') as f:
            reports = json.load(f)
    
    reports.append(data)
    
    with open(f'{DATA_DIR}/reports.json', 'w') as f:
        json.dump(reports, f, indent=2)
    
    return jsonify({'success': True, 'report_id': data['id']})

@app.route('/report/<report_id>')
def view_report(report_id):
    if os.path.exists(f'{DATA_DIR}/reports.json'):
        with open(f'{DATA_DIR}/reports.json', 'r') as f:
            reports = json.load(f)
            for report in reports:
                if report['id'] == report_id:
                    return render_template('view_report.html', report=report)
    return "Report not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)