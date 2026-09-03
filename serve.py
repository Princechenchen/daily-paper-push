"""本地看板服务器：在 python -m http.server 基础上为所有响应追加 no-cache 头，
防止浏览器缓存旧版看板页面或数据文件（历史面板滚动修复依赖最新 HTML）。

用法：python serve.py [端口]   （默认 8765）
"""
import http.server
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, format, *args):
        pass  # 静默访问日志


class ThreadingTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    with ThreadingTCPServer(("127.0.0.1", PORT), NoCacheHandler) as httpd:
        print(f"Serving on http://127.0.0.1:{PORT} (Cache-Control: no-cache)")
        httpd.serve_forever()
