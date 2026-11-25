import http.server
import socketserver
import urllib.parse

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        
        # Fix: List er vitor theke value niye tarpor capitalize kora holo
        site_list = query_params.get("site", ["Website"])
        site_name = site_list[0].capitalize() if site_list else "Website"
        
        key_name = site_name.lower()
        encoded_site = urllib.parse.quote(site_name)

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        # Website onujayi unique styling (Color & Branding)
        styles = {
            "facebook": {"bg": "#f0f2f5", "primary": "#1877f2", "btn_sec": "#42b72a", "card_bg": "#ffffff", "text": "#1c1e21"},
            "instagram": {"bg": "#fafafa", "primary": "#e1306c", "btn_sec": "#0095f6", "card_bg": "#ffffff", "text": "#262626"},
            "github": {"bg": "#0d1117", "primary": "#238636", "btn_sec": "#1f6feb", "card_bg": "#161b22", "text": "#c9d1d9"},
            "twitter": {"bg": "#000000", "primary": "#1d9bf0", "btn_sec": "#ffffff", "card_bg": "#16181c", "text": "#e7e9ea"},
            "google": {"bg": "#ffffff", "primary": "#1a73e8", "btn_sec": "#1a73e8", "card_bg": "#ffffff", "text": "#202124"},
        }

        theme = styles.get(key_name, {"bg": "#f0f2f5", "primary": "#2563eb", "btn_sec": "#16a34a", "card_bg": "#ffffff", "text": "#1f2937"})

        common_css = f"""
            body {{
                background-color: {theme['bg']};
                font-family: Helvetica, Arial, sans-serif;
                color: {theme['text']};
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
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
                color: {theme['primary']};
                font-size: 38px;
                font-weight: bold;
                margin-bottom: 20px;
                letter-spacing: -1px;
                text-transform: capitalize;
            }}
            .login-card {{
                background: {theme['card_bg']};
                padding: 24px;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
                width: 100%;
                box-sizing: border-box;
                text-align: center;
                border: 1px solid rgba(128, 128, 128, 0.2);
            }}
            h3 {{ margin-top: 0; font-size: 20px; }}
            p.sub-text {{ font-size: 14px; opacity: 0.8; margin-bottom: 15px; }}
            input {{
                width: 100%;
                padding: 14px 16px;
                margin: 8px 0;
                border: 1px solid rgba(128, 128, 128, 0.4);
                border-radius: 6px;
                font-size: 16px;
                box-sizing: border-box;
                outline: none;
                background: transparent;
                color: {theme['text']};
            }}
            input:focus {{ border-color: {theme['primary']}; box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2); }}
            .login-btn {{
                background-color: {theme['primary']};
                border: none;
                border-radius: 6px;
                color: #fff;
                font-size: 17px;
                font-weight: bold;
                line-height: 44px;
                padding: 0 16px;
                width: 100%;
                cursor: pointer;
                margin-top: 10px;
            }}
            .forgot-pass {{
                color: {theme['primary']};
                font-size: 14px;
                text-decoration: none;
                display: block;
                margin: 15px 0;
            }}
            .forgot-pass:hover {{ text-decoration: underline; }}
            hr {{ border: none; border-bottom: 1px solid rgba(128, 128, 128, 0.2); margin: 20px 0; }}
            .create-btn {{
                display: inline-block;
                background-color: {theme['btn_sec']};
                border: none;
                border-radius: 6px;
                color: #fff;
                font-size: 16px;
                font-weight: bold;
                padding: 12px 20px;
                text-decoration: none;
                cursor: pointer;
                width: 100%;
                box-sizing: border-box;
            }}
            .back-link {{
                margin-top: 20px;
                font-size: 13px;
                opacity: 0.7;
                text-decoration: none;
            }}
            .dev-footer {{
                margin-top: 15px;
                font-size: 12px;
                opacity: 0.6;
            }}
        """

        # 1. Login Page (/login)
        if parsed_url.path == "/login":
            html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{site_name} • Log In</title>
                <style>{common_css}</style>
            </head>
            <body>
                <div class="container">
                    <div class="logo">{site_name}</div>
                    <div class="login-card">
                        <form onsubmit="event.preventDefault(); alert('Demo Login Submitted for {site_name}!');">
                            <input type="text" placeholder="Phone number, username, or email" required>
                            <input type="password" placeholder="Password" required>
                            <button type="submit" class="login-btn">Log In</button>
                        </form>
                        <a href="/forgot?site={encoded_site}" class="forgot-pass">Forgot password?</a>
                        <hr>
                        <a href="/register?site={encoded_site}" class="create-btn">Create new account</a>
                    </div>
                    <a href="/" class="back-link">← Back to Generator Home</a>
                    <div class="dev-footer">Developed by <b>samiul14</b> (Wsamiul)</div>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode("utf-8"))
            return

        # 2. Forgot Password Page (/forgot)
        if parsed_url.path == "/forgot":
            html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Reset Password | {site_name}</title>
                <style>{common_css}</style>
            </head>
            <body>
                <div class="container">
                    <div class="logo">{site_name}</div>
                    <div class="login-card">
                        <h3>Trouble logging in?</h3>
                        <p class="sub-text">Enter your email, phone, or username and we'll send you a link to get back into your account.</p>
                        <form onsubmit="event.preventDefault(); alert('Password reset link sent for {site_name}!');">
                            <input type="text" placeholder="Email, Phone, or Username" required>
                            <button type="submit" class="login-btn">Send Login Link</button>
                        </form>
                        <hr>
                        <a href="/login?site={encoded_site}" class="forgot-pass">← Back to Log In</a>
                    </div>
                    <div class="dev-footer">Developed by <b>samiul14</b> (Wsamiul)</div>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode("utf-8"))
            return

        # 3. Register Page (/register)
        if parsed_url.path == "/register":
            html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Sign Up • {site_name}</title>
                <style>{common_css}</style>
            </head>
            <body>
                <div class="container">
                    <div class="logo">{site_name}</div>
                    <div class="login-card">
                        <h3>Sign up to see photos and videos from your friends.</h3>
                        <form onsubmit="event.preventDefault(); alert('Account registered successfully on {site_name}!');">
                            <input type="text" placeholder="Mobile Number or Email" required>
                            <input type="text" placeholder="Full Name" required>
                            <input type="text" placeholder="Username" required>
                            <input type="password" placeholder="Password" required>
                            <button type="submit" class="create-btn" style="margin-top: 10px;">Sign Up</button>
                        </form>
                        <hr>
                        <a href="/login?site={encoded_site}" class="forgot-pass">Have an account? Log in</a>
                    </div>
                    <div class="dev-footer">Developed by <b>samiul14</b> (Wsamiul)</div>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode("utf-8"))
            return

        # 4. Main Home Page (Link Generator)
        html_content = """
        <html>
        <head>
            <title>Dynamic Site Cloner - Wsamiul</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { font-family: Arial; padding: 20px; background: #121212; color: #fff; text-align: center; }
                .card { background: #1e1e1e; padding: 25px; border-radius: 10px; display: inline-block; margin-top: 40px; width: 90%; max-width: 400px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }
                input { padding: 12px; width: 90%; border-radius: 5px; border: 1px solid #444; background: #2a2a2a; color: #fff; margin-top: 15px; font-size: 16px; }
                button { padding: 12px 20px; background: #2563eb; color: white; border: none; border-radius: 5px; cursor: pointer; margin-top: 15px; font-size: 16px; width: 95%; font-weight: bold; }
                .result { margin-top: 25px; word-break: break-all; background: #262626; padding: 15px; border-radius: 8px; }
                .open-btn { display: inline-block; padding: 12px 20px; background: #16a34a; color: white; text-decoration: none; border-radius: 5px; margin-top: 12px; font-weight: bold; }
                .dev-tag { margin-top: 20px; font-size: 13px; color: #38bdf8; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="card">
                <h2>Dynamic Login Cloner</h2>
                <form method="GET">
                    <input type="text" name="name" placeholder="Website Name (e.g. Instagram, GitHub)" required><br>
                    <button type="submit">Generate Site Link</button>
                </form>
        """

        if "name" in query_params:
            raw_name = query_params["name"][0].strip()
            encoded_name = urllib.parse.quote(raw_name)
            final_link = f"http://localhost:{PORT}/login?site={encoded_name}"

            html_content += f"""
                <div class="result">
                    <p style="color: #4ade80; margin: 0 0 8px 0;"><b>Link Ready for "{raw_name}":</b></p>
                    <small style="color: #bbb;">{final_link}</small><br>
                    <a href="{final_link}" target="_blank" class="open-btn">🚀 Open Cloned Page</a>
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
