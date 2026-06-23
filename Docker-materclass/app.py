from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome Notice Generator</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #000000, #1a1a1a);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background: #1e1e1e;
            color: white;
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            width: 500px;
            box-shadow: 0 0 25px rgba(255,255,255,0.1);
        }

        h1 {
            color: white;
            margin-bottom: 20px;
        }

        input[type="text"] {
            width: 80%;
            padding: 12px;
            margin: 15px 0;
            border: 1px solid #444;
            border-radius: 8px;
            background: #2b2b2b;
            color: white;
            font-size: 16px;
        }

        input[type="text"]:focus {
            outline: none;
            border-color: #4facfe;
        }

        button {
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            margin: 5px;
        }

        .generate-btn {
            background: #007bff;
        }

        .generate-btn:hover {
            background: #0056b3;
        }

        .reset-btn {
            background: #dc3545;
        }

        .reset-btn:hover {
            background: #b02a37;
        }

        .notice {
            margin-top: 25px;
            padding: 20px;
            border-radius: 10px;
            background: #198754;
            color: white;
            font-size: 20px;
            font-weight: bold;
            border-left: 6px solid #0f5132;
            animation: fadeIn 0.5s ease-in-out;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        p {
            color: #cccccc;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>🎉 Welcome Notice Generator</h1>

    <p>Enter your name and receive a personalized welcome message.</p>

    <form method="POST">
        <input
            type="text"
            name="name"
            placeholder="Enter Your Name"
            required
        >

        <br>

        <button type="submit" class="generate-btn">
            Generate Notice
        </button>

        <button
            type="button"
            class="reset-btn"
            onclick="window.location.href='/'">
            Reset
        </button>
    </form>

    {% if message %}
    <div class="notice">
        {{ message }}
    </div>
    {% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        name = request.form["name"].strip().title()

        message = (
            f"🎊 Welcome {name}! "
            f"We are delighted to have you with us. "
            f"Wishing you success, happiness, and a wonderful journey ahead."
        )

    return render_template_string(HTML, message=message)



if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)