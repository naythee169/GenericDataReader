from flask import render_template_string
import matplotlib
matplotlib.use("Agg")  # Use a non-interactive backend
import matplotlib.pyplot as plt
import io
import base64
from collections import Counter

def generate_bar_chart(data):
    # Count records by file_type
    file_types = [record.get("file_type", "unknown") for record in data]
    counts = Counter(file_types)

    # Create bar chart
    plt.figure(figsize=(6,4))
    plt.bar(counts.keys(), counts.values(), color="skyblue")
    plt.xlabel("File Type")
    plt.ylabel("Record Count")
    plt.title("Records per File Type")

    # Save to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    encoded = base64.b64encode(buf.getvalue()).decode("utf-8")
    plt.close()
    return encoded

def render_dashboard(data):
    # Generate HTML for a simple dashboard that shows a table and bar chart
    chart = generate_bar_chart(data)
    table_rows = ""
    for record in data:
        row = "<tr>"
        for key, value in record.items():
            row += f"<td>{value}</td>"
        row += "</tr>"
        table_rows += row

    html = f"""
    <html>
    <head>
      <title>Data Dashboard</title>
      <style>
        table, th, td {{
          border: 1px solid black;
          border-collapse: collapse;
          padding: 5px;
        }}
      </style>
    </head>
    <body>
      <h1>Unified Data Dashboard</h1>
      <h2>Data Table</h2>
      <table>
        <tr>
          {"".join(f"<th>{key}</th>" for key in data[0].keys()) if data else "<th>No Data</th>"}
        </tr>
        {table_rows}
      </table>
      <h2>Bar Chart</h2>
      <img src="data:image/png;base64,{chart}" alt="Bar Chart"/>
    </body>
    </html>
    """
    return html