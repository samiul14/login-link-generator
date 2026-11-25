import http.server
import socketserver
import urllib.parse

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        # Jodi /login request ashe, tahole hubohu original page + developer branding show korbe
        if parsed_url.path == "/login":
            site_name = query_params.get("site", ["Facebook"])[0]
            
            fb_login_html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{site_name} - Log In or Sign Up</title>
                <style>
                    body {{
                        background-color: #f0f2f5;
                        font-family: Helvetica, Arial, sans-serif;
                        color: #1c1e21;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                    }}
                    .container {{
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        width: 100%;
                        max-width: 400px;
                        padding: 20px;
                    }}
                    .logo {{
                        color: #1877f2;
                        font-size: 40px;
                        font-weight: bold;
                        margin-bottom: 20px;
                        letter-spacing: -1px;
                    }}
                    .login-card {{
                        background: #ffffff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1), 0 8px 16px rgba(0, 0, 0, 0.1);
                        width: 100%;
                        box-sizing: border-box;
                        text-align: center;
                    }}
                    input {{
                        width: 100%;
                        padding: 14px 16px;
                        margin: 6px 0;
                        border: 1px solid #dddfe2;
                        border-radius: 6px;
                        font-size: 17px;
                        box-sizing: border-box;
                        outline: none;
                    }}
                    input:focus {{
                        border-color: #1877f2;
                        box-shadow: 0 0 0 2px #e7f3ff;
                    }}
                    .login-btn {{
                        background-color: #1877f2;
                        border: none;
                        border-radius: 6px;
                        color: #fff;
                        font-size: 20px;
                        font-weight: bold;
                        line-height: 48px;
                        padding: 0 16px;
                        width: 100%;
                        cursor: pointer;
                        margin-top: 10px;
                    }}
                    .login-btn:hover {{
                        background-color: #166fe5;
                    }}
                    .forgot-pass {{
                        color: #1877f2;
                        font-size: 14px;
                        text-decoration: none;
                        display: block;
                        margin: 15px 0;
                    }}
                    .forgot-pass:hover {{
                        text-decoration: underline;
                    }}
                    hr {{
                        border: none;
                        border-bottom: 1px solid #dadde1;
                        margin: 20px 0;
                    }}
                    .create-btn {{
                        background-color: #42b72a;
                        border: none;
                        border-radius: 6px;
                        color: #fff;
                        font-size: 17px;
                        font-weight: bold;
                        padding: 12px 16px;
                        cursor: pointer;
                    }}
                    .create-btn:hover {{
                        background-color: #36a420;
                    }}
                    .back-link {{
                        margin-top: 20px;
                        font-size: 13px;
                        color: #65676b;
                        text-decoration: none;
                    }}
                    .dev-footer {{
                        margin-top: 15px;
                        font-size: 12px;
                        color: #888;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="logo">{site_name}</div>
                    <div class="login-card">
                        <form onsubmit="event.preventDefault(); alert('Login details captured/submitted successfully!');">
                            <input type="text" placeholder="Email address or phone number" required>
                            <input type="password" placeholder="Password" required>
                            <button type="submit" class="login-btn">Log In</button>
                        </form>
                        <a href="#" class="forgot-pass">Forgotten password?</a>
                        <hr>
                        <button class="create-btn">Create new account</button>
                    </div>
                    <a href="/" class="back-link">← Back to Generator Home</a>
                    <div class="dev-footer">Developed by <b>samiul14</b> (Wsamiul)</div>
                </div>
            </body>
            </html>
            """
            self.wfile.write(fb_login_html.encode("utf-8"))
            return

        # Main Home Page
        html_content = """
        <html>
        <head>
            <title>Hubohu Page Generator - Wsamiul</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { font-family: Arial; padding: 20px; background: #121212; color: #fff; text-align: center; }
                .card { background: #1e1e1e; padding: 25px; border-radius: 10px; display: inline-block; margin-top: 40px; width: 90%; max-width: 400px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }
                input { padding: 12px; width: 90%; border-radius: 5px; border: 1px solid #444; background: #2a2a2a; color: #fff; margin-top: 15px; font-size: 16px; }
                button { padding: 12px 20px; background: #1877f2; color: white; border: none; border-radius: 5px; cursor: pointer; margin-top: 15px; font-size: 16px; width: 95%; font-weight: bold; }
                .result { margin-top: 25px; word-break: break-all; background: #262626; padding: 15px; border-radius: 8px; }
                .open-btn { display: inline-block; padding: 12px 20px; background: #42b72a; color: white; text-decoration: none; border-radius: 5px; margin-top: 12px; font-weight: bold; }
                .dev-tag { margin-top: 20px; font-size: 13px; color: #38bdf8; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="card">
                <h2>Original Style Link Generator</h2>
                <form method="GET">
                    <input type="text" name="name" placeholder="Website Nam likhun (e.g. Facebook)" required><br>
                    <button type="submit">Generate Hubohu Link</button>
                </form>
        """

        if "name" in query_params:
            raw_name = query_params["name"][0].strip()
            encoded_name = urllib.parse.quote(raw_name)
            final_link = f"http://localhost:{PORT}/login?site={encoded_name}"

            html_content += f"""
                <div class="result">
                    <p style="color: #42b72a; margin: 0 0 8px 0;"><b>Hubohu Link Ready for "{raw_name}":</b></p>
                    <small style="color: #bbb;">{final_link}</small><br>
                    <a href="{final_link}" target="_blank" class="open-btn">🚀 Open Original Look Page</a>
                </div>
            """

        html_content += """
                <div class="dev-tag">Developer: samiul14 (Wsamiul)</div>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode("utf-8"))

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server cholche! Browser-e open korun: http://localhost:{PORT}")
    httpd.serve_forever()
