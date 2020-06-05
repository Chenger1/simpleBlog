from blog_app import app


@app.route('/')
def main():
    return 'Response'