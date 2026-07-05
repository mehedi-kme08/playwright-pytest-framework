from playwright.sync_api import APIRequestContext, Playwright
import pytest


BASE_URL = "https://jsonplaceholder.typicode.com/"


@pytest.fixture(scope="session")
def api(playwright: Playwright):
    context = playwright.request.new_context(base_url=BASE_URL)
    yield context
    context.dispose()


def test_get_posts_list(api: APIRequestContext):
    response = api.get("posts")

    assert response.ok
    posts = response.json()
    assert len(posts) == 100
    for post in posts[:5]:
        assert "id" in post
        assert "title" in post
        assert "userId" in post


def test_get_single_post(api: APIRequestContext):
    response = api.get("posts/1")

    assert response.status == 200
    post = response.json()
    assert post["id"] == 1
    assert len(post["title"]) > 0


def test_post_not_found(api: APIRequestContext):
    response = api.get("posts/9999")

    assert response.status == 404
    # Verify it's a real "not found" — body should be empty JSON
    assert response.json() == {}


def test_create_post(api: APIRequestContext):
    payload = {"title": "test automation", "body": "playwright api test", "userId": 1}
    response = api.post("posts", data=payload)

    assert response.status == 201
    body = response.json()
    assert body["title"] == "test automation"
    assert "id" in body


def test_update_post(api: APIRequestContext):
    payload = {"id": 1, "title": "updated title", "body": "updated", "userId": 1}
    response = api.put("posts/1", data=payload)

    assert response.status == 200
    assert response.json()["title"] == "updated title"


def test_delete_post(api: APIRequestContext):
    response = api.delete("posts/1")

    assert response.status == 200