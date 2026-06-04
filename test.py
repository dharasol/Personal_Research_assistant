from dotenv import load_dotenv
load_dotenv()

# Patch at the httpx level - intercepts ALL HTTP requests
import httpx
_orig_send = httpx.Client.send
def _patched_send(self, request, *args, **kwargs):
    import json
    if b"cache_breakpoint" in request.content or b"cache_control" in request.content:
        body = json.loads(request.content)
        # Strip from messages
        for msg in body.get("messages", []):
            msg.pop("cache_breakpoint", None)
            msg.pop("cache_control", None)
            if isinstance(msg.get("content"), list):
                msg["content"] = [
                    {k: v for k, v in b.items() if k not in ("cache_breakpoint", "cache_control")}
                    for b in msg["content"]
                ]
        # Rebuild request
        new_content = json.dumps(body).encode()
        request = request.stream.__self__  # rebuild
        import httpx
        request = httpx.Request(
            method=request.method,
            url=request.url,
            headers=request.headers,
            content=new_content,
        )
    return _orig_send(self, request, *args, **kwargs)
httpx.Client.send = _patched_send

from crew import research_crew
research_crew.kickoff(inputs={"topic": "AI Agents"})