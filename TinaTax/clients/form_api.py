BASE_URL="https://www.tinataxresolution.com/"
class Form:
    def __init__(self, session):
        self.session = session
    def post_form(self,payload):
        return self.session.post(f"{BASE_URL}/api/contact", json=payload, timeout=10)
