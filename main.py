import webview
import os
import sys

class api:
    def destroy(self):
        window.destroy()
        sys.exit()

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), "index.html"), 'r') as file:
        html = file.read()

    window = webview.create_window('phoenixthrush', html=html, js_api=api, width=1000, height=500, frameless=True, resizable=True, shadow=True)
    webview.start()