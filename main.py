import os
from flask import Flask, jsonify, send_from_directory
from google.cloud import bigquery

app = Flask(__name__, static_folder="static")
TABLE = os.getenv("BQ_TABLE", "datastory-analytic-mis.pop_coverage_poc.vw_store_planning")
client = bigquery.Client()

@app.get("/api/data")
def data():
    sql = f"""
      SELECT month_no, month_name, region_id, region_name,
             ucinfo_population, dopa_registered_population,
             latent_population, target_store_count
      FROM `{TABLE}`
      ORDER BY month_no, region_id
    """
    rows = [dict(r) for r in client.query(sql).result()]
    return jsonify(rows)

@app.get("/")
def index():
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
