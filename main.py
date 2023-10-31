import streamlit as st
from flask import Flask, render_template
from streamlit import caching

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def main():
    st.title("Streamlit-Flask Integration")
    st.write("Dies ist eine Streamlit-Anwendung, die eine Flask-Route anzeigt.")
    st.write("Besuche die Flask-Route auf /flask-route")

    # Embed Flask route in Streamlit
    with st.echo():
        from streamlit import caching
        caching.clear_cache()
        from flask import Flask
        app = Flask(__name__)

        @app.route('/flask-route')
        def flask_route():
            return "Das ist die Flask-Route"

        if __name__ == '__main__':
            app.run(port=8501)

if __name__ == '__main__':
    main()
