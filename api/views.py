from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health(request):
    """Simple health check used by tests and by the deploy stage."""
    return Response({"status": "ok"})


@api_view(["GET"])
def greeting(request):
    """Returns a greeting. Optional ?name=... query parameter."""
    name = request.query_params.get("name", "CSC325")
    return Response({"message": f"Hello, {name}!"})

@api_view(["GET"])
def about(request):
    return Response({"course": "CSC325", "student": "Chris Gonzalez"})
