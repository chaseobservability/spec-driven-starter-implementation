#!/usr/bin/env python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

TODOS = {}
NEXT_ID = 1


class Handler(BaseHTTPRequestHandler):
    def _json(self, code: int, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/health":
            self._json(200, {"ok": True})
            return
        if path == "/todos":
            self._json(200, list(TODOS.values()))
            return
        if path.startswith("/todos/"):
            todo_id = path.split("/")[-1]
            if todo_id in TODOS:
                self._json(200, TODOS[todo_id])
            else:
                self._json(404, {"error": "not_found"})
            return
        self._json(404, {"error": "not_found"})

    def do_POST(self):
        global NEXT_ID
        path = urlparse(self.path).path
        if path != "/todos":
            self._json(404, {"error": "not_found"})
            return

        length = int(self.headers.get("Content-Length", "0"))
        body = json.loads(self.rfile.read(length) or b"{}")
        title = body.get("title")
        if not isinstance(title, str) or not title.strip():
            self._json(422, {"error": "validation: title"})
            return

        todo_id = str(NEXT_ID)
        NEXT_ID += 1
        todo = {"id": todo_id, "title": title, "completed": False}
        if "dueDate" in body:
            todo["dueDate"] = body["dueDate"]
        TODOS[todo_id] = todo
        self._json(201, todo)

    def log_message(self, *_args):
        return


def main():
    HTTPServer(("127.0.0.1", 38080), Handler).serve_forever()


if __name__ == "__main__":
    main()
