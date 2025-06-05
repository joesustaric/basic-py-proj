import pytest
import threading
import time
import requests
import json
from src.main import Handler
from http.server import HTTPServer
from http import HTTPStatus

class TestServer:
    def teardown_method(self):
        Handler._events = []

    @pytest.fixture(scope="function")
    def server(self):
        test_port = 8081
        server = HTTPServer(('localhost', test_port), Handler)

        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        # Give server time to start
        time.sleep(0.1)

        yield f"http://localhost:{test_port}"

        # Cleanup
        server.shutdown()
        server.server_close()

        time.sleep(0.1)

    def test_hello_world(self, server):
        response = requests.get(f"{server}/hello")
        assert response.status_code == HTTPStatus.OK
        assert response.text == "Hello, World!"

    def test_not_found(self, server):
        response = requests.get(f"{server}/foobar")
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.text == ""

    def test_post_json_event(self, server):
        post_data = {
            "timestamp": "2025-06-05T07:00:00Z",
            "type": "login",
            "user_id": "user-123"
        }
        response = requests.post(
            f"{server}/event",
            data=json.dumps(post_data),
            headers={"Content-Type": "application/json"}
        )

        assert response.status_code == HTTPStatus.OK

    def test_query_all_event_data(self, server):

        post_data_1 = {
            "timestamp": "2025-06-05T07:00:00Z",
            "type": "login",
            "user_id": "user-123"
        }
        post_data_2 = {
            "timestamp": "2025-06-05T07:30:00Z",
            "type": "login",
            "user_id": "user-456"
        }
        requests.post(
            f"{server}/event",
            data=json.dumps(post_data_1),
            headers={"Content-Type": "application/json"}
        )

        requests.post(
            f"{server}/event",
            data=json.dumps(post_data_2),
            headers={"Content-Type": "application/json"}
        )

        response = requests.get(f"{server}/events")

        expected_response = [
            {
                "timestamp": "2025-06-05T07:00:00Z",
                "type": "login",
                "user_id": "user-123"
            },
            {
                "timestamp": "2025-06-05T07:30:00Z",
                "type": "login",
                "user_id": "user-456"
            }
        ]

        assert response.status_code == HTTPStatus.OK
        assert response.json() == expected_response


