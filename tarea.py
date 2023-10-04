from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                bytes(
                    "<html><head><title>https://pythonbasics.org</title></head>"
                    f"<p>Request: {self.path}</p>"
                    "<body><p>Este es un curso de python.</p></body></html>",
                    "utf-8",
                )
            )
        elif self.path == "/test":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                bytes(
                    "<html><head><title>https://pythonbasics.org</title></head>"
                    f"<p>Request: {self.path}</p>"
                    "<body><p>This is a test page.</p></body></html>",
                    "utf-8",
                )
            )

        elif self.path == "/users":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                bytes(
                    "<html><head><title>https://pythonbasics.org</title></head>"
                    f"<p>Request: {self.path}</p>"
                    "<body><p>Users de la pagina del curso de python</p></body></html>",
                    "utf-8",
                )
            )

        elif self.path == "/albums":
            response = requests.get("https://jsonplaceholder.typicode.com/albums")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            album_urls = ""
            for album in response.json():
                album_urls += f"<p>{album}</p>"
            self.wfile.write(
                bytes(
                    "<html><head><title>https://pythonbasics.org</title></head>"
                    f"<p>Request: {self.path}</p>"
                    f"<body><p>{response.json()[1]}</p></body></html>",
                    "utf-8",
                )
            )

        
        elif self.path == "/photos":
            response = requests.get("https://jsonplaceholder.typicode.com/photos")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            photos_urls = ""
            for photo in response.json():
                photos_urls += f"<p>{photo}</p>"
            self.wfile.write(
                bytes(
                    "<html><head><title>https://pythonbasics.org</title></head>"
                    f"<p>Request: {self.path}</p>"
                    f"<body><p>{response.json()[1]}</p></body></html>",
                    "utf-8",
                )
            )

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
