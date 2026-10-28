"""Loopback-only teaching server, not a production payment/tax service."""

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json

from . import reference, replacement


def make_server(implementation="replacement", port=8765):
    if implementation not in {"reference", "replacement"}:
        raise ValueError("unknown implementation")
    calculate = reference.quote if implementation == "reference" else replacement.quote

    class Handler(BaseHTTPRequestHandler):
        server_version = "UnfiredLab/0.2"

        def setup(self):
            super().setup()
            self.connection.settimeout(5)

        def log_message(self, *args):
            pass

        def respond(self, status, value):
            body = json.dumps(value, ensure_ascii=False, allow_nan=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            self.respond(200, {"status": "ok"}) if self.path == "/health" else self.respond(404, {"error": "not_found"})

        def do_POST(self):
            if self.path != "/v1/quote":
                return self.respond(404, {"error": "not_found"})
            try:
                length = int(self.headers.get("Content-Length", "-1"))
                if length > 65536:
                    return self.respond(413, {"error": "request_too_large"})
                if length < 0:
                    return self.respond(400, {"error": "invalid_request"})
                payload = json.loads(self.rfile.read(length).decode("utf-8"))
            except (ValueError, UnicodeError, OSError):
                return self.respond(400, {"error": "invalid_request"})
            status, response = calculate(payload)
            self.respond(status, response)

    return ThreadingHTTPServer(("127.0.0.1", port), Handler)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--implementation", choices=("reference", "replacement"), default="replacement")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    if not 0 <= args.port <= 65535:
        parser.error("port must be between 0 and 65535")
    with make_server(args.implementation, args.port) as server:
        print(f"{args.implementation} lab listening on http://127.0.0.1:{server.server_port}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
