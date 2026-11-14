from flask import Flask
import pymysql
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "sae502-mariadb")
DB_NAME = os.getenv("DB_NAME", "centralis_db")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


@app.route("/")
def accueil():
    try:
        connexion = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        connexion.close()

        return """
        <h1>Centralis</h1>
        <p>Application Flask opérationnelle.</p>
        <p>Connexion à MariaDB : OK</p>
        """

    except Exception as erreur:
        return f"""
        <h1>Centralis</h1>
        <p>Application Flask opérationnelle.</p>
        <p>Connexion à MariaDB : ERREUR</p>
        <p>{erreur}</p>
        """, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
